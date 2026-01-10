#!/usr/bin/env python3
"""
Equalizer APO Profile Validator
================================
Validates EQ profile files for syntax errors and common issues

Usage:
    python validate_profile.py config_yourprofile.txt
    python validate_profile.py --all   (validates all profiles in current directory)

Requirements:
    Python 3.6+
"""

import re
import sys
import os
from pathlib import Path
from typing import List, Tuple, Dict

class ProfileValidator:
    """Validates Equalizer APO configuration files"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
        
    def validate_file(self, filepath: str) -> bool:
        """
        Validate a single profile file
        Returns True if valid, False if errors found
        """
        self.errors = []
        self.warnings = []
        self.info = []
        
        if not os.path.exists(filepath):
            self.errors.append(f"File not found: {filepath}")
            return False
            
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        # Run validation checks
        self._check_preamp(lines)
        self._check_filters(lines)
        self._check_frequency_coverage(lines)
        self._check_gain_levels(lines)
        self._check_syntax(lines)
        
        return len(self.errors) == 0
        
    def _check_preamp(self, lines: List[str]):
        """Check if preamp is present and reasonable"""
        preamp_found = False
        preamp_value = None
        
        for line_num, line in enumerate(lines, 1):
            if line.strip().startswith('Preamp:'):
                preamp_found = True
                match = re.search(r'Preamp:\s*([-+]?\d+\.?\d*)\s*dB', line)
                if match:
                    preamp_value = float(match.group(1))
                    
                    if preamp_value > 0:
                        self.warnings.append(
                            f"Line {line_num}: Positive preamp ({preamp_value} dB) may cause clipping"
                        )
                    elif preamp_value < -15:
                        self.warnings.append(
                            f"Line {line_num}: Very low preamp ({preamp_value} dB) - may be too quiet"
                        )
                break
                
        if not preamp_found:
            self.warnings.append("No Preamp found - may cause clipping with boosted frequencies")
        else:
            self.info.append(f"Preamp: {preamp_value} dB")
            
    def _check_filters(self, lines: List[str]):
        """Check filter syntax and parameters"""
        filter_count = 0
        
        for line_num, line in enumerate(lines, 1):
            if 'Filter:' in line and 'ON' in line:
                filter_count += 1
                
                # Check for PK (parametric) filters
                if 'PK' in line:
                    # Extract frequency
                    freq_match = re.search(r'Fc\s+(\d+\.?\d*)\s*Hz', line)
                    if freq_match:
                        freq = float(freq_match.group(1))
                        if freq < 20 or freq > 20000:
                            self.warnings.append(
                                f"Line {line_num}: Frequency {freq} Hz outside audible range (20-20000 Hz)"
                            )
                    else:
                        self.errors.append(f"Line {line_num}: Missing or invalid frequency")
                        
                    # Extract gain
                    gain_match = re.search(r'Gain\s+([-+]?\d+\.?\d*)\s*dB', line)
                    if gain_match:
                        gain = float(gain_match.group(1))
                        if abs(gain) > 20:
                            self.warnings.append(
                                f"Line {line_num}: Very high gain ({gain} dB) - may cause distortion"
                            )
                    else:
                        self.errors.append(f"Line {line_num}: Missing or invalid gain")
                        
                    # Extract Q
                    q_match = re.search(r'Q\s+(\d+\.?\d*)', line)
                    if q_match:
                        q = float(q_match.group(1))
                        if q > 10:
                            self.warnings.append(
                                f"Line {line_num}: Very high Q value ({q}) - very narrow filter"
                            )
                    else:
                        self.errors.append(f"Line {line_num}: Missing or invalid Q value")
                        
        self.info.append(f"Total filters: {filter_count}")
        
        if filter_count == 0:
            self.warnings.append("No filters found in profile")
        elif filter_count > 50:
            self.warnings.append(f"{filter_count} filters may impact performance")
            
    def _check_frequency_coverage(self, lines: List[str]):
        """Check if important frequency ranges are covered"""
        frequencies = []
        
        for line in lines:
            freq_match = re.search(r'Fc\s+(\d+\.?\d*)\s*Hz', line)
            if freq_match:
                frequencies.append(float(freq_match.group(1)))
                
        if frequencies:
            frequencies.sort()
            
            # Check coverage
            has_sub_bass = any(f < 60 for f in frequencies)
            has_bass = any(60 <= f < 250 for f in frequencies)
            has_mids = any(250 <= f < 2000 for f in frequencies)
            has_highs = any(f >= 5000 for f in frequencies)
            
            if not has_sub_bass:
                self.info.append("No sub-bass (<60 Hz) adjustments")
            if not has_bass:
                self.warnings.append("No bass (60-250 Hz) adjustments")
            if not has_mids:
                self.warnings.append("No midrange (250-2000 Hz) adjustments")
            if not has_highs:
                self.info.append("No high frequency (>5000 Hz) adjustments")
                
            self.info.append(f"Frequency range: {min(frequencies):.0f} Hz - {max(frequencies):.0f} Hz")
            
    def _check_gain_levels(self, lines: List[str]):
        """Check for excessive gain that might cause clipping"""
        total_positive_gain = 0
        max_gain = 0
        
        for line in lines:
            gain_match = re.search(r'Gain\s+([-+]?\d+\.?\d*)\s*dB', line)
            if gain_match:
                gain = float(gain_match.group(1))
                if gain > 0:
                    total_positive_gain += gain
                if abs(gain) > abs(max_gain):
                    max_gain = gain
                    
        if total_positive_gain > 50:
            self.warnings.append(
                f"High total positive gain ({total_positive_gain:.1f} dB) - ensure preamp compensates"
            )
            
        self.info.append(f"Maximum gain: {max_gain:+.1f} dB")
        
    def _check_syntax(self, lines: List[str]):
        """Check for common syntax errors"""
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
                
            # Check for common typos
            if 'Filter:' in line:
                if 'ON' not in line and 'OFF' not in line:
                    self.errors.append(f"Line {line_num}: Filter missing ON/OFF state")
                    
                if 'PK' in line or 'LS' in line or 'HS' in line:
                    required = ['Fc', 'Gain', 'Q'] if 'PK' in line else ['Fc', 'Gain']
                    for param in required:
                        if param not in line:
                            self.errors.append(f"Line {line_num}: Missing {param} parameter")
                            
    def print_report(self, filepath: str):
        """Print validation report"""
        print(f"\n{'='*70}")
        print(f"Validation Report: {os.path.basename(filepath)}")
        print(f"{'='*70}")
        
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"   {error}")
                
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"   {warning}")
                
        if self.info:
            print(f"\nℹ️  INFO:")
            for info in self.info:
                print(f"   {info}")
                
        if not self.errors and not self.warnings:
            print("\n✅ Profile looks good!")
        elif not self.errors:
            print("\n✅ No critical errors found (warnings are advisory)")
        else:
            print(f"\n❌ Found {len(self.errors)} error(s) that should be fixed")
            
        print(f"{'='*70}\n")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python validate_profile.py <profile_file.txt>")
        print("       python validate_profile.py --all")
        sys.exit(1)
        
    validator = ProfileValidator()
    
    if sys.argv[1] == '--all':
        # Validate all .txt files in current directory
        txt_files = list(Path('.').glob('config_*.txt'))
        if not txt_files:
            print("No config_*.txt files found in current directory")
            sys.exit(1)
            
        results = {}
        for filepath in txt_files:
            is_valid = validator.validate_file(str(filepath))
            results[filepath.name] = (is_valid, len(validator.errors), len(validator.warnings))
            validator.print_report(str(filepath))
            
        # Summary
        print(f"\n{'='*70}")
        print("SUMMARY")
        print(f"{'='*70}")
        for filename, (is_valid, errors, warnings) in results.items():
            status = "✅" if is_valid else "❌"
            print(f"{status} {filename:40} Errors: {errors:2}  Warnings: {warnings:2}")
        print(f"{'='*70}\n")
        
    else:
        # Validate single file
        filepath = sys.argv[1]
        is_valid = validator.validate_file(filepath)
        validator.print_report(filepath)
        
        sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()