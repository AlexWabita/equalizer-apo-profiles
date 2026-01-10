# Contributing to Equalizer APO Professional Audio Profiles

First off, thank you for considering contributing to this project! 🎵

This document provides guidelines for contributing to the Equalizer APO Profiles repository. Following these guidelines helps maintain quality and makes the contribution process smooth for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Profile Contribution Guidelines](#profile-contribution-guidelines)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of experience level, background, or identity.

### Expected Behavior

- Be respectful and constructive in communication
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Trolling or insulting remarks
- Publishing others' private information
- Any conduct that would be inappropriate in a professional setting

## How Can I Contribute?

### 1. Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

**Good Bug Report Includes:**
- Clear, descriptive title
- Detailed steps to reproduce
- Expected vs actual behavior
- Your system information:
  - Equalizer APO version
  - Windows version
  - Audio hardware (speakers/headphones/subwoofer)
  - Profile being used
- Screenshots if applicable

**Example:**
```markdown
**Title**: Config_party.txt causes distortion on certain tracks

**Description**: 
When using config_party.txt with bass-heavy tracks, I experience 
distortion even at moderate volume levels.

**Steps to Reproduce**:
1. Load config_party.txt
2. Play [specific song/genre]
3. Set volume to 50%

**Expected**: Clean, powerful bass
**Actual**: Distorted, clipping sound

**System**:
- Equalizer APO v1.3
- Windows 11 Pro
- Logitech Z906 5.1 system with subwoofer
```

### 2. Suggesting New Profiles

We welcome suggestions for new profiles! Consider:

**Occasion-Based Profiles:**
- Study/Focus Mode
- Gaming (FPS, RPG, etc.)
- Podcast/Audiobook
- ASMR
- Nature Sounds
- White Noise

**Genre-Based Profiles:**
- Jazz
- Blues
- Country
- Metal
- Ambient
- Lo-fi
- K-Pop
- Afrobeats

**Submit Suggestions:**
1. Open an issue with "Profile Request" label
2. Describe the use case
3. Explain what sonic characteristics you envision
4. Provide example tracks if possible

### 3. Contributing New Profiles

#### Profile Requirements

✅ **Must Have:**
- Clear purpose and use case
- Optimized for indoor subwoofer systems
- Appropriate preamp setting to prevent clipping
- Detailed inline comments explaining choices
- Tested on actual hardware
- Follows naming convention: `config_[name].txt`

✅ **Should Include:**
- Frequency range coverage (20 Hz - 16 kHz recommended)
- Q values appropriate for the effect
- Gain adjustments that make sense for the genre/occasion

❌ **Avoid:**
- Extreme settings that could damage speakers
- Untested configurations
- Profiles identical to existing ones
- Settings without comments

#### Profile Template

```
# ================================================================
# [PROFILE NAME] - [Short Description]
# ================================================================
# Purpose: [Detailed explanation of use case]
# Focus: [Key sonic characteristics]
# Optimized for: [Speaker type/situation]
# Save as: config_[name].txt
# ================================================================

# PRE-AMPLIFICATION
# [Explain why this preamp value]
Preamp: -X dB

# ================================================================
# [FREQUENCY RANGE] ([XX-XX Hz])
# ================================================================
# [Explain the goal for this frequency range]

Filter: ON PK Fc XX Hz Gain X dB Q X.X
# ... more filters

# ================================================================
# USAGE NOTES
# ================================================================
# - [Important tip 1]
# - [Important tip 2]
# ================================================================
```

### 4. Improving Documentation

Documentation improvements are always welcome:
- Fix typos or unclear instructions
- Add helpful examples
- Improve formatting
- Translate to other languages
- Add troubleshooting tips

## Pull Request Process

### Before Submitting

1. **Test Thoroughly**: Verify your profile works as intended
2. **Check Existing Issues**: Ensure you're not duplicating work
3. **Follow Guidelines**: Adhere to style and naming conventions
4. **Update Documentation**: Add your profile to relevant docs

### Submission Steps

1. **Fork the Repository**
   ```bash
   git clone https://github.com/AlexWabita/equalizer-apo-profiles.git
   cd equalizer-apo-profiles
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/new-profile-name
   ```

3. **Make Your Changes**
   - Add your profile file(s)
   - Update README.md if adding new profile
   - Add entry to CHANGELOG.md

4. **Commit with Clear Message**
   ```bash
   git add .
   git commit -m "Add [Profile Name] for [Use Case]"
   ```

5. **Push to Your Fork**
   ```bash
   git push origin feature/new-profile-name
   ```

6. **Open Pull Request**
   - Provide clear description
   - Reference any related issues
   - Include testing notes

### Pull Request Template

```markdown
## Description
[Clear description of what this PR does]

## Type of Change
- [ ] New profile (occasion-based)
- [ ] New profile (genre-based)
- [ ] Bug fix
- [ ] Documentation improvement
- [ ] Enhancement to existing profile

## Profile Details (if applicable)
- **Name**: config_[name].txt
- **Category**: [Occasion/Genre]
- **Use Case**: [Detailed explanation]

## Testing
- [ ] Tested on actual hardware
- [ ] No distortion at normal volumes
- [ ] Preamp prevents clipping
- [ ] Comments are clear and helpful

## Hardware Tested On
- Speakers/Headphones: [Model]
- Subwoofer: [Yes/No, Model if applicable]
- Equalizer APO Version: [Version]
- Windows Version: [Version]

## Checklist
- [ ] Follows naming convention
- [ ] Includes detailed comments
- [ ] Updated README.md (if needed)
- [ ] Tested thoroughly
- [ ] No duplicate of existing profile
```

## Style Guidelines

### File Naming

- Use lowercase with underscores: `config_profile_name.txt`
- Be descriptive but concise: `config_jazz.txt` not `config_j.txt`
- Avoid special characters or spaces

### Comment Style

```
# ================================================================
# SECTION HEADERS - ALL CAPS, CLEAR SEPARATORS
# ================================================================

# Subsection explanations - Sentence case
# Provide context for why settings are chosen

Filter: ON PK Fc 50 Hz Gain 10 dB Q 0.9  # Inline comments for specific notes
```

### Frequency Organization

Always organize filters from lowest to highest frequency:
```
Filter: ON PK Fc 30 Hz ...   # Correct order
Filter: ON PK Fc 50 Hz ...
Filter: ON PK Fc 80 Hz ...
```

### Preamp Guidelines

- Always include preamp
- Set conservatively to prevent clipping
- Higher bass boost = more negative preamp
- Typical range: -2 dB to -8 dB

### Q Value Best Practices

- **Q 0.7-1.0**: Wide, natural boost/cut
- **Q 1.0-1.5**: Moderate width
- **Q 1.5-3.0**: Narrow, surgical adjustments
- Use wider Q for musical adjustments
- Use narrower Q for problem frequency fixes

## Attribution

If your contribution is based on or inspired by existing work:
- Credit the original source in comments
- Explain what you modified
- Ensure you have rights to contribute

## Questions?

Don't hesitate to ask! You can:
- Open an issue with the "question" label
- Start a discussion in GitHub Discussions
- Reference this guide in your questions

## Recognition

Contributors will be:
- Listed in the project README
- Credited in release notes
- Appreciated by the community! 🎉

---

**Thank you for contributing to making audio experiences better for everyone!** 🎵