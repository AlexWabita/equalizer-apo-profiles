# Troubleshooting Guide

Complete solutions to common problems when using Equalizer APO and these audio profiles.

## Table of Contents

- [Quick Diagnostics](#quick-diagnostics)
- [Installation Issues](#installation-issues)
- [Audio Problems](#audio-problems)
- [Profile Loading Issues](#profile-loading-issues)
- [Performance Issues](#performance-issues)
- [Advanced Troubleshooting](#advanced-troubleshooting)
- [FAQ](#faq)

## Quick Diagnostics

### Is Equalizer APO Working?

**Quick Test:**
1. Open Configuration Editor
2. Play music
3. Click the "Power" button to toggle EQ on/off
4. Do you hear a difference?
   - **YES** → Working correctly
   - **NO** → See below

### Basic Checklist

Before diving into detailed troubleshooting:

- [ ] Computer restarted after installing Equalizer APO
- [ ] Correct audio device selected during installation
- [ ] Profile file exists in config folder
- [ ] No syntax errors in config.txt
- [ ] Windows volume not muted
- [ ] Speakers/headphones properly connected

## Installation Issues

### Problem: "APO not installed" Message

**Symptoms:**
- Configuration Editor shows "APO not installed" error
- EQ has no effect on audio

**Solutions:**

1. **Reinstall on correct device**
   - Uninstall Equalizer APO
   - Reinstall and carefully select your audio device
   - Common mistake: selecting wrong audio device

2. **Check device compatibility**
   - Some devices don't support APO
   - Try a different audio output
   - External USB DACs usually work well

3. **Restart computer**
   - Always restart after installation
   - Required for APO to initialize

### Problem: No Audio After Installation

**Symptoms:**
- Sound completely stops working
- Windows shows audio device as disabled

**Solutions:**

1. **Uninstall from problematic device**
   - Open Configuration Editor
   - Go to: Troubleshooting Options
   - Select device and uninstall APO
   - Restart computer

2. **Restore default Windows audio**
   - Right-click speaker icon > Sounds
   - Playback tab > Properties
   - Advanced tab > Restore Defaults
   - Restart

3. **Reinstall audio drivers**
   - Device Manager > Sound controllers
   - Right-click device > Uninstall
   - Restart (Windows will reinstall drivers)

### Problem: Can't Find Configuration Editor

**Solutions:**

1. **Search in Start Menu**
   - Press Windows key
   - Type "Configuration Editor"
   - Should appear in results

2. **Navigate manually**
   ```
   C:\Program Files\EqualizerAPO\Editor\Editor.exe
   ```

3. **Create desktop shortcut**
   - Right-click Editor.exe
   - Send to > Desktop (create shortcut)

## Audio Problems

### Problem: Audio Distortion or Clipping

**Symptoms:**
- Crackling, popping, or harsh sounds
- Sound "breaks up" especially at louder volumes
- Bass sounds fuzzy or distorted

**Solutions:**

1. **Increase Preamp (most common fix)**
   - Open your config file
   - Find line: `Preamp: -6 dB`
   - Change to: `Preamp: -8 dB` or `-10 dB`
   - Save and reload

2. **Reduce bass gains**
   - Lower the Gain values for bass frequencies
   - Reduce by 2-3 dB across all bass filters
   - Example: Change `Gain 12 dB` to `Gain 9 dB`

3. **Check Windows volume**
   - Keep Windows volume at 80% or below
   - Use hardware volume control instead

4. **Disable Windows audio enhancements**
   - Right-click speaker icon > Sounds
   - Playback > Properties > Enhancements
   - Check "Disable all enhancements"

### Problem: Not Enough Bass

**Symptoms:**
- Bass sounds weak or thin
- Can't feel the bass impact
- Profile doesn't seem to work

**Solutions:**

1. **Verify subwoofer is connected**
   - Check physical connections
   - Ensure subwoofer is powered on
   - Adjust subwoofer volume knob

2. **Check bass crossover**
   - Some systems have crossover settings
   - Ensure it's set to 80-120 Hz

3. **Use more aggressive profile**
   - Try: Party, Workout, or Hip Hop profiles
   - These have maximum bass emphasis

4. **Increase bass gains manually**
   - Open config file
   - Increase Gain for 30-80 Hz range by 2-3 dB
   - Don't forget to adjust preamp!

### Problem: Muddy or Unclear Sound

**Symptoms:**
- Vocals sound muffled
- Everything blends together
- Lacks clarity and separation

**Solutions:**

1. **Enable room resonance filters**
   - Some profiles have commented-out filters
   - Look for lines starting with `#`
   - Remove `#` from room correction filters around 100-150 Hz

2. **Reduce low-mids**
   - Lower gains in 200-500 Hz range
   - Try reducing by 2-3 dB

3. **Use different profile**
   - Try: Night Mode, Balanced, or Classical
   - These have less bass emphasis

4. **Check speaker placement**
   - Subwoofer in corner = more bass
   - Move away from walls for clearer sound

### Problem: Harsh or Fatiguing Highs

**Symptoms:**
- Treble sounds harsh or sharp
- Cymbals are painful
- Can't listen for long periods

**Solutions:**

1. **Reduce treble gains**
   - Lower Gain for 5000+ Hz frequencies
   - Reduce by 2-4 dB

2. **Use smoother profile**
   - Try: Intimate, Meditation, or Classical
   - These have gentler high frequencies

3. **Check speaker tweeters**
   - Ensure tweeters aren't aimed directly at ears
   - Angle speakers slightly away

## Profile Loading Issues

### Problem: Config File Not Loading

**Symptoms:**
- Profile doesn't take effect
- Configuration Editor shows empty
- Changes don't apply

**Solutions:**

1. **Check file location**
   ```
   ✓ Correct: C:\Program Files\EqualizerAPO\config\config.txt
   ✗ Wrong:   C:\Users\[Name]\Desktop\config.txt
   ```

2. **Verify Include path**
   - If using Include method
   - Check path is correct: `Include: occasions/config_party.txt`
   - No extra spaces or typos

3. **Check for syntax errors**
   - Open config.txt in Notepad
   - Look for typos in filter lines
   - Ensure proper spacing

4. **Reload configuration**
   - Configuration Editor > Click "Reload" button
   - Or restart audio device

### Problem: "File Not Found" Error

**Solutions:**

1. **Verify file exists**
   - Check the exact path in Include statement
   - Make sure file is actually there

2. **Check file extension**
   - File should be `.txt` not `.txt.txt`
   - Windows hides extensions by default
   - View > Show file extensions

3. **Use absolute path**
   ```
   Instead of: Include: config_hiphop.txt
   Try: Include: C:\Program Files\EqualizerAPO\config\config_hiphop.txt
   ```

## Performance Issues

### Problem: Audio Stuttering or Dropouts

**Symptoms:**
- Sound cuts in and out
- Brief moments of silence
- Crackling during playback

**Solutions:**

1. **Increase buffer size**
   - Configuration Editor > Device Options
   - Increase buffer to 10-20ms
   - Apply and test

2. **Close background apps**
   - CPU-intensive programs can cause issues
   - Close unnecessary applications

3. **Update audio drivers**
   - Visit manufacturer's website
   - Download latest drivers
   - Install and restart

### Problem: High CPU Usage

**Solutions:**

1. **Simplify profile**
   - Use fewer filters
   - Combine similar frequency adjustments

2. **Reduce sample rate**
   - Right-click speaker icon > Sounds
   - Playback > Properties > Advanced
   - Try 44100 Hz instead of 192000 Hz

## Advanced Troubleshooting

### Problem: EQ Only Works in Some Apps

**Symptoms:**
- Works in Spotify but not YouTube
- Works in browser but not media player

**Solutions:**

1. **Check application routing**
   - Some apps bypass Windows audio
   - Use "Exclusive Mode" settings

2. **Disable exclusive mode in apps**
   - App settings > Audio output
   - Uncheck "Exclusive mode"

3. **Set as default device**
   - Right-click speaker icon > Sounds
   - Playback > Set as default

### Problem: Settings Reset After Restart

**Solutions:**

1. **Check config.txt permissions**
   - Right-click config.txt
   - Properties > Security
   - Ensure you have write permissions

2. **Run Configuration Editor as Admin**
   - Right-click Editor.exe
   - Run as administrator
   - Make changes and save

### Collecting Diagnostic Information

If problems persist, collect this information for support:

1. **System Information**
   ```
   - Windows version
   - Equalizer APO version
   - Audio device model
   - Speaker/headphone model
   ```

2. **Configuration Files**
   - Copy content of config.txt
   - Note any error messages

3. **Steps to Reproduce**
   - Exact steps that cause the problem
   - When it started
   - What changed recently

## FAQ

### Q: Do I need to restart after every profile change?

**A:** No, just click "Reload" in Configuration Editor or restart your media player.

### Q: Can I use multiple profiles at once?

**A:** No, only one profile can be active. You can combine settings manually though.

### Q: Will this work with Bluetooth speakers?

**A:** Yes, if they're set as your default Windows audio device.

### Q: Is it safe for my speakers?

**A:** Yes, if configured properly. Excessive bass can damage small speakers, so start conservative.

### Q: Why does bass sound different in different rooms?

**A:** Room acoustics affect bass significantly. You may need different settings for different locations.

### Q: Can I use this with a gaming headset?

**A:** Yes! Try reducing bass gains by 3-4 dB from the recommended settings.

### Q: Does this work with Dolby Atmos or DTS?

**A:** It can conflict. Disable those enhancements for best results with Equalizer APO.

### Q: How do I completely uninstall?

**A:** 
1. Control Panel > Programs > Uninstall
2. Select Equalizer APO
3. Follow uninstall wizard
4. Restart computer

## Still Having Issues?

### Community Support

1. **Check GitHub Issues**
   - Search existing issues: https://github.com/AlexWabita/equalizer-apo-profiles/issues
   - Someone may have had the same problem

2. **Create New Issue**
   - Provide system information
   - Include config file content
   - Describe problem in detail

3. **Official Equalizer APO**
   - Documentation: https://sourceforge.net/p/equalizerapo/wiki/Documentation/
   - Forum: https://sourceforge.net/p/equalizerapo/discussion/

### Before Asking for Help

✅ **Do:**
- Search existing solutions first
- Provide complete system information
- Include error messages exactly as shown
- Describe what you've already tried

❌ **Don't:**
- Say "it doesn't work" without details
- Skip basic troubleshooting steps
- Modify multiple things at once

---

**Most problems can be solved by adjusting the Preamp value or reducing bass gains!**