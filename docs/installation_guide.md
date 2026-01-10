# Installation Guide

Complete step-by-step guide to install and configure Equalizer APO with these professional audio profiles.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Step 1: Install Equalizer APO](#step-1-install-equalizer-apo)
- [Step 2: Download Profiles](#step-2-download-profiles)
- [Step 3: Install Profiles](#step-3-install-profiles)
- [Step 4: Configure and Test](#step-4-configure-and-test)
- [Platform-Specific Notes](#platform-specific-notes)
- [Verification](#verification)
- [Next Steps](#next-steps)

## Prerequisites

### System Requirements
- **Operating System**: Windows 7, 8, 10, or 11 (32-bit or 64-bit)
- **Audio System**: Any Windows-compatible audio device
- **Recommended**: Indoor subwoofer + satellite speaker system
- **Disk Space**: ~50 MB for Equalizer APO + profiles

### What You'll Need
- Administrator access to your computer
- Active internet connection for download
- About 15-20 minutes of time

## Step 1: Install Equalizer APO

### Download Equalizer APO

1. **Visit the official download page**
   - Go to: https://sourceforge.net/projects/equalizerapo/
   - Click the green "Download" button

2. **Wait for download to complete**
   - File name: `EqualizerAPO64-[version].exe` (64-bit)
   - Or: `EqualizerAPO-[version].exe` (32-bit)
   - Size: ~5-10 MB

### Run the Installer

1. **Locate the downloaded file**
   - Usually in your Downloads folder
   - Double-click to run

2. **User Account Control prompt**
   - Click "Yes" to allow the installer to make changes

3. **Welcome screen**
   - Click "Next"

4. **License agreement**
   - Read the license
   - Click "I Agree"

5. **Select installation directory** (Default is fine)
   - Default: `C:\Program Files\EqualizerAPO\`
   - Click "Next"

6. **Select audio devices** - IMPORTANT STEP!
   - You'll see a list of all your audio devices
   - **Check the box** next to your main audio output device
   - Common names: "Speakers", "Realtek HD Audio", "NVIDIA High Definition Audio"
   - You can select multiple devices if needed
   - Click "Next"

   ```
   ┌─────────────────────────────────────────┐
   │ Select devices to install APO on:       │
   ├─────────────────────────────────────────┤
   │ ☑ Speakers (Realtek HD Audio)          │
   │ ☐ Headphones (Realtek HD Audio)        │
   │ ☐ Digital Output (Realtek HD Audio)    │
   │ ☐ NVIDIA High Definition Audio         │
   └─────────────────────────────────────────┘
   ```

7. **Installation**
   - Click "Install"
   - Wait for installation to complete (1-2 minutes)

8. **Completion**
   - **IMPORTANT**: You'll be prompted to restart your computer
   - Click "Finish" and **restart immediately**
   - Equalizer APO only works after restart!

### Verify Installation

After restart:

1. Open File Explorer
2. Navigate to: `C:\Program Files\EqualizerAPO\`
3. You should see these folders:
   - `config\`
   - `Editor\`
   - Various DLL files

## Step 2: Download Profiles

### Option A: Download from GitHub (Recommended)

1. **Visit the repository**
   - Go to: https://github.com/AlexWabita/equalizer-apo-profiles

2. **Download the repository**
   - Click the green "Code" button
   - Select "Download ZIP"
   - Save to your Downloads folder

3. **Extract the ZIP file**
   - Right-click the downloaded ZIP
   - Select "Extract All..."
   - Choose a location (e.g., Downloads)
   - Click "Extract"

### Option B: Clone with Git

If you have Git installed:

```bash
git clone https://github.com/AlexWabita/equalizer-apo-profiles.git
cd equalizer-apo-profiles
```

## Step 3: Install Profiles

### Copy Profile Files

1. **Navigate to the extracted folder**
   - Open: `equalizer-apo-profiles-main\profiles\`
   - You'll see two folders: `occasions\` and `genres\`

2. **Open Equalizer APO config folder**
   - Open File Explorer
   - Navigate to: `C:\Program Files\EqualizerAPO\config\`

3. **Create organized folders** (Optional but recommended)
   ```
   C:\Program Files\EqualizerAPO\config\
   ├── occasions\
   └── genres\
   ```

4. **Copy all profile files**
   - From: `equalizer-apo-profiles-main\profiles\occasions\*`
   - To: `C:\Program Files\EqualizerAPO\config\occasions\`
   
   - From: `equalizer-apo-profiles-main\profiles\genres\*`
   - To: `C:\Program Files\EqualizerAPO\config\genres\`

### Choose Your Switching Method

#### Method 1: Simple (Beginner)

1. Choose a profile you want (e.g., `config_balanced.txt`)
2. Copy its entire content
3. Open: `C:\Program Files\EqualizerAPO\config\config.txt` in Notepad
4. Paste the content
5. Save and close

#### Method 2: Include System (Recommended)

1. Open: `C:\Program Files\EqualizerAPO\config\config.txt` in Notepad
2. Delete all existing content
3. Add a single line:
   ```
   Include: occasions/config_balanced.txt
   ```
4. Save and close

To switch profiles later, just change the filename in that line!

#### Method 3: Multi-Profile Setup (Advanced)

1. Open: `C:\Program Files\EqualizerAPO\config\config.txt` in Notepad
2. Add all profiles with comments:
   ```
   # Uncomment the one you want to use:
   
   # OCCASIONS
   # Include: occasions/config_party.txt
   # Include: occasions/config_night.txt
   Include: occasions/config_balanced.txt
   # Include: occasions/config_workout.txt
   
   # GENRES
   # Include: genres/config_hiphop.txt
   # Include: genres/config_rock.txt
   ```
3. Remove `#` from the profile you want active
4. Save and close

## Step 4: Configure and Test

### Open Configuration Editor

1. **Launch the editor**
   - Press Windows key
   - Type "Configuration Editor"
   - Click "Configuration Editor" (Equalizer APO)
   
   OR
   
   - Navigate to: `C:\Program Files\EqualizerAPO\Editor\`
   - Double-click `Editor.exe`

2. **Check your device is selected**
   - Top of the window shows selected device
   - Should match the device you selected during installation

3. **Reload configuration**
   - Click the "Reload" button or press Ctrl+R
   - This applies your chosen profile

### Test Your Audio

1. **Play some music**
   - Use your favorite music player
   - Choose a song you know well
   - Start at moderate volume (50%)

2. **Listen for improvements**
   - More powerful bass
   - Clearer vocals
   - Better overall balance

3. **Adjust if needed**
   - If too much bass: Try Night Mode or Balanced
   - If distortion: See troubleshooting guide
   - Switch profiles to find your favorite

## Platform-Specific Notes

### Windows 11
- All features work normally
- New Settings app location: Settings > System > Sound > Advanced
- May need to disable audio enhancements in Windows settings

### Windows 10
- Fully compatible
- Ensure Windows audio enhancements are disabled for best results
- Right-click speaker icon > Sounds > Playback > Properties > Enhancements > Disable all

### Windows 7/8
- Fully compatible
- May need to manually restart audio service after profile changes
- Services.msc > Windows Audio > Restart

### For Laptops
- Built-in speakers may have limited bass response
- Reduce bass gains if distortion occurs
- Consider using Night Mode or Balanced profiles

### For External DACs/Sound Cards
- Ensure Equalizer APO is installed on the correct device
- May need to select "USB Audio Device" or specific DAC name
- Some DACs have their own EQ - disable it to avoid conflicts

## Verification

### Check Installation is Working

1. **Open Configuration Editor**
2. **Look for visual EQ curve**
   - Should see frequency response graph
   - Peaks and valleys showing the EQ adjustments

3. **Test with and without**
   - Play music
   - In Configuration Editor, click "Power" button to disable
   - Notice the difference
   - Enable again

### Common Signs It's Working

✅ **Working correctly:**
- More powerful bass
- Clearer sound overall
- No distortion at normal volumes
- Frequency graph visible in editor

❌ **Not working:**
- No change in sound
- "APO not installed" message
- Empty configuration editor
- Sound cuts out completely

## Next Steps

### After Installation

1. **Explore different profiles**
   - Try various occasion and genre profiles
   - Find what works best for your music taste

2. **Fine-tune settings**
   - Read the [Customization Guide](customization-guide.md)
   - Adjust individual frequencies to taste

3. **Learn about frequencies**
   - Read the [Frequency Guide](frequency-guide.md)
   - Understand what each range does

4. **Join the community**
   - Star the GitHub repository
   - Report any issues or suggestions
   - Share your custom profiles

### Recommended Reading

- [Troubleshooting Guide](troubleshooting.md) - Fix common problems
- [Customization Guide](customization-guide.md) - Modify profiles
- [Frequency Guide](frequency-guide.md) - Understand EQ basics

## Getting Help

If you encounter issues:

1. Check the [Troubleshooting Guide](troubleshooting.md)
2. Review GitHub Issues for similar problems
3. Create a new issue with details about your system
4. Join community discussions

---

**Congratulations! You've successfully installed Equalizer APO with professional profiles!** 🎉

Enjoy your enhanced audio experience!