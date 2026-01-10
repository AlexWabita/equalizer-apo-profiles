# Equalizer APO Professional Audio Profiles

A comprehensive collection of 28+ professionally tuned Equalizer APO configurations optimized for indoor subwoofer systems. Transform your audio experience with profiles designed for every occasion and music genre.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Equalizer APO](https://img.shields.io/badge/Equalizer%20APO-Compatible-blue)](https://sourceforge.net/projects/equalizerapo/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

## 🎵 Features

- **28 Pre-configured Profiles** - Professionally tuned for different scenarios
- **Occasion-Based** - 14 profiles for different environments and moods
- **Genre-Specific** - 14 profiles optimized for music genres
- **Indoor Subwoofer Optimized** - Designed specifically for dedicated subwoofer systems
- **Easy Switching** - Multiple methods to quickly change between profiles
- **Fully Documented** - Detailed comments explaining each setting

## 📋 Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Profile Categories](#profile-categories)
- [Usage Guide](#usage-guide)
- [Configuration Details](#configuration-details)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## 🔧 Requirements

- **Equalizer APO** v1.2 or higher ([Download here](https://sourceforge.net/projects/equalizerapo/))
- **Windows** 7/8/10/11
- **Audio System**: Indoor subwoofer + satellite speakers (recommended)
  - Can be adapted for headphones or other speaker configurations

## 📥 Installation

### Quick Install

1. Install [Equalizer APO](https://sourceforge.net/projects/equalizerapo/)
2. Clone or download this repository:
   ```bash
   git clone https://github.com/AlexWabita/equalizer-apo-profiles.git
   ```
3. Copy desired profile files to your Equalizer APO config folder:
   ```
   C:\Program Files\EqualizerAPO\config\
   ```
4. Choose your switching method (see [Usage Guide](#usage-guide))

### Manual Installation

1. Download individual profile files from the repository
2. Navigate to `C:\Program Files\EqualizerAPO\config\`
3. Copy the profile files you want to use
4. Rename your chosen profile to `config.txt` or use the Include method

## 🎯 Profile Categories

### Occasion-Based Profiles (14)

| Profile | Use Case | Bass Level | Best For |
|---------|----------|------------|----------|
| **Party** | Gatherings, celebrations | Maximum | Dancing, high energy events |
| **Night** | Late night listening | Low | Quiet hours, no disturbance |
| **Intimate** | Private moments | Deep/Smooth | Romantic settings |
| **Romantic** | Dates, dinners | Moderate | Background music, conversation |
| **Movie** | Films, TV shows | High/Impactful | Home theater, immersive viewing |
| **Morning** | Wake up, breakfast | Moderate/Bright | Energizing start to day |
| **Balanced** | All-day listening | Natural | Work, general music |
| **Worship** | Church, praise | Clear/Uplifting | Spiritual gatherings |
| **Meditation** | Yoga, mindfulness | Deep/Subtle | Relaxation, centering |
| **Workout** | Gym, exercise | Maximum | High-intensity training |
| **Prayer** | Spiritual rituals | Minimal/Clear | Contemplation, focus |
| **Coffee Shop** | Cafes, lounges | Warm/Background | Conversation spaces |
| **Retail** | Stores, shops | Engaging | Shopping environments |
| **Hotel** | Upscale venues | Sophisticated | Professional atmospheres |

### Genre-Based Profiles (14)

| Genre | Key Features | Signature Sound |
|-------|--------------|-----------------|
| **Hip Hop** | Deep bass, punchy beats | Sub-bass emphasis, clear vocals |
| **R&B** | Smooth, warm, soulful | Balanced warmth, vocal clarity |
| **Pop** | Bright, catchy | Energetic highs, balanced bass |
| **Reggae** | Deep bass, laid-back | Heavy low-end, relaxed mids |
| **Riddim** | Massive sub-bass | Extreme sub frequencies |
| **Trap** | Heavy 808s | Modern bass, crisp hi-hats |
| **Gospel** | Clear vocals, uplifting | Powerful mids, inspiring highs |
| **Dancehall** | Energetic rhythms | Caribbean bass, bright presence |
| **Rock** | Punchy mids | Guitar clarity, drum impact |
| **Techno** | Electronic precision | Clean bass, detailed highs |
| **Rap** | Vocal focus | Clear lyrics, strong foundation |
| **Classical** | Natural dynamics | Wide range, authentic timbre |
| **House** | Four-on-floor groove | Rhythmic bass, danceable |
| **EDM** | Festival energy | Maximum impact, exciting |

## 🎮 Usage Guide

### Method 1: Simple Copy (Beginner-Friendly)

1. Choose your desired profile (e.g., `config_hiphop.txt`)
2. Copy its entire content
3. Paste into `C:\Program Files\EqualizerAPO\config\config.txt`
4. Save and restart audio or reload in Equalizer APO

### Method 2: Include System (Recommended)

1. Copy all profile files to config folder
2. Create/edit `config.txt` with a single line:
   ```
   Include: config_hiphop.txt
   ```
3. To switch profiles, just change the filename:
   ```
   Include: config_party.txt
   ```
4. Save and reload

### Method 3: Multi-Profile Setup (Advanced)

Keep all profiles accessible with comments:

```
# Uncomment the profile you want to use:

# OCCASIONS
# Include: config_party.txt
# Include: config_night.txt
Include: config_balanced.txt
# Include: config_workout.txt

# GENRES
# Include: config_hiphop.txt
# Include: config_rock.txt
# Include: config_edm.txt
```

Simply remove the `#` from your desired profile and add `#` to others.

## ⚙️ Configuration Details

### Understanding the Settings

Each profile uses parametric EQ filters with three key parameters:

- **Fc (Frequency)**: The center frequency being adjusted
- **Gain**: How much boost (+) or cut (-) in decibels
- **Q**: The width of the frequency range affected (higher Q = narrower)

### Frequency Ranges

- **Sub-Bass (20-60 Hz)**: Felt more than heard, creates physical impact
- **Bass (60-250 Hz)**: Adds body and warmth
- **Midrange (250-2000 Hz)**: Vocals and most instruments
- **Presence (2-5 kHz)**: Clarity and detail
- **Treble (5-16 kHz)**: Sparkle and air

### Preamp Values

Each profile includes a Preamp setting (e.g., `Preamp: -6 dB`) to prevent clipping. If you experience distortion:
- Increase the negative value (e.g., from `-6 dB` to `-8 dB`)
- Or reduce individual filter gains

## 🎨 Customization

### Adapting for Different Systems

**For Headphones:**
- Reduce all bass gains by 3-4 dB
- Increase preamp by -2 dB

**For Small Speakers (No Subwoofer):**
- Reduce sub-bass (20-60 Hz) gains significantly
- Focus on mid-bass (80-200 Hz) instead

**For Large Venue Systems:**
- Can increase bass gains by 2-3 dB
- Adjust preamp accordingly

### Creating Custom Profiles

1. Start with the `config_balanced.txt` as a base
2. Adjust specific frequencies to taste
3. Save as `config_custom.txt`
4. Test and iterate

### Fine-Tuning Tips

- Adjust in small increments (1-2 dB at a time)
- Test with familiar music
- Use high-quality audio sources
- Trust your ears, not just numbers

## 🔍 Troubleshooting

### Audio Distortion or Clipping
**Solution**: Increase preamp value (more negative)
```
Preamp: -8 dB  # Change from -6 dB
```

### Not Enough Bass
**Solution**: 
1. Check your subwoofer is properly connected
2. Verify subwoofer volume level
3. Increase bass filter gains by 2-3 dB

### Too Much Bass / Muddy Sound
**Solution**:
1. Enable room resonance filters (uncomment in profiles)
2. Reduce bass gains by 2-3 dB
3. Try the Night Mode or Balanced profiles

### Profiles Not Loading
**Solution**:
1. Verify file is saved as `.txt` not `.txt.txt`
2. Check file is in correct directory
3. Ensure no syntax errors in config.txt
4. Restart Equalizer APO service

### Changes Not Taking Effect
**Solution**:
1. Open Equalizer APO Configuration Editor
2. Click "Reload" or restart audio device
3. Verify correct output device is selected

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Issues
- Use the [GitHub Issues](https://github.com/AlexWabita/equalizer-apo-profiles/issues) page
- Provide details: profile used, audio system, problem description
- Include your Equalizer APO version

### Submitting Profiles
1. Fork the repository
2. Create a new profile following the naming convention: `config_[name].txt`
3. Add detailed comments explaining the profile's purpose
4. Test thoroughly on your system
5. Submit a Pull Request with description

### Suggesting Improvements
- Open an issue with enhancement tag
- Describe the improvement clearly
- Explain the use case or benefit

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### What This Means
- ✅ Free to use personally and commercially
- ✅ Modify and distribute
- ✅ Private use
- ❌ No warranty or liability
- ℹ️ Must include original license

## 👨‍💻 Author

**Alex Wabita**
- GitHub: [@AlexWabita](https://github.com/AlexWabita)
- Repository: [equalizer-apo-profiles](https://github.com/AlexWabita/equalizer-apo-profiles)

## 🙏 Acknowledgments

- [Equalizer APO](https://sourceforge.net/projects/equalizerapo/) by jthedering
- Audio engineering community for EQ principles
- All contributors and users providing feedback

## 📊 Project Stats

- **Total Profiles**: 28+
- **Categories**: 2 (Occasions + Genres)
- **Optimization**: Indoor Subwoofer Systems
- **Compatibility**: Windows 7/8/10/11

## 🔄 Changelog

### Version 1.0.0 (2025-01-10)
- Initial release
- 14 occasion-based profiles
- 14 genre-based profiles
- Complete documentation
- MIT License

## 📞 Support

Need help? Here's how to get support:

1. **Documentation**: Read this README thoroughly
2. **Issues**: Check [existing issues](https://github.com/AlexWabita/equalizer-apo-profiles/issues)
3. **New Issue**: Create a detailed issue report
4. **Community**: Engage with other users in Discussions

## 🌟 Star This Repo

If you find these profiles useful, please consider:
- ⭐ Starring the repository
- 🔀 Forking for your own use
- 📢 Sharing with others
- 🤝 Contributing improvements

---

**Made with ❤️ for audiophiles and music lovers everywhere**