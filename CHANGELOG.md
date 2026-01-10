# Changelog

All notable changes to the Equalizer APO Professional Audio Profiles project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Additional genre profiles (Jazz, Blues, Metal, Ambient)
- Headphone-specific profile variants
- Outdoor speaker configurations
- Auto-switching scripts for different times of day
- Profile comparison tool

## [1.0.0] - 2025-01-10

### Added - Initial Release

#### Occasion-Based Profiles (14)
- `config_party.txt` - Maximum energy for parties and gatherings
- `config_night.txt` - Low volume, neighbor-friendly night listening
- `config_intimate.txt` - Warm, enveloping sound for private moments
- `config_romantic.txt` - Natural, emotional sound for romantic settings
- `config_movie.txt` - Cinematic bass and clear dialogue for films
- `config_morning.txt` - Bright, energizing sound to start the day
- `config_balanced.txt` - Natural, all-day listening profile
- `config_worship.txt` - Clear, uplifting sound for spiritual music
- `config_meditation.txt` - Calm, centering profile for mindfulness
- `config_workout.txt` - High energy, motivating sound for exercise
- `config_prayer.txt` - Focused, contemplative atmosphere for prayer
- `config_coffeeshop.txt` - Pleasant background ambiance for cafes
- `config_retail.txt` - Engaging, upbeat sound for shopping environments
- `config_hotel.txt` - Sophisticated, refined sound for upscale venues

#### Genre-Based Profiles (14)
- `config_hiphop.txt` - Deep bass and punchy beats
- `config_rnb.txt` - Smooth, warm, soulful sound
- `config_pop.txt` - Bright, catchy, radio-friendly sound
- `config_reggae.txt` - Deep bass with laid-back groove
- `config_riddim.txt` - Massive sub-bass for riddim music
- `config_trap.txt` - Heavy 808s and modern trap sound
- `config_gospel.txt` - Uplifting vocals and powerful presence
- `config_dancehall.txt` - Energetic Caribbean rhythms
- `config_rock.txt` - Punchy mids and guitar clarity
- `config_techno.txt` - Deep bass with electronic precision
- `config_rap.txt` - Vocal-focused with strong bass foundation
- `config_classical.txt` - Natural, wide dynamic range
- `config_house.txt` - Four-on-floor groove for house music
- `config_edm.txt` - Maximum energy for festival sound

#### Documentation
- Comprehensive README.md with installation and usage guides
- CONTRIBUTING.md with contribution guidelines
- LICENSE file (MIT License)
- CHANGELOG.md for version tracking
- Inline comments in all profile files explaining settings

#### Features
- Multiple switching methods (simple, include, multi-profile)
- Optimized for indoor subwoofer systems
- Detailed frequency range coverage (20 Hz - 16 kHz)
- Preamp settings to prevent clipping
- Customization guidelines for different audio systems

### Technical Details
- All profiles tested on indoor subwoofer configurations
- Frequency optimization based on audio engineering principles
- Q values chosen for natural, musical sound
- Gain adjustments balanced to prevent distortion

---

## Version Guidelines

### Types of Changes
- **Added** - New features or profiles
- **Changed** - Changes to existing functionality
- **Deprecated** - Features that will be removed in future
- **Removed** - Removed features
- **Fixed** - Bug fixes
- **Security** - Security-related changes

### Version Numbers
- **Major (X.0.0)** - Breaking changes, complete restructure
- **Minor (1.X.0)** - New profiles or features, backward compatible
- **Patch (1.0.X)** - Bug fixes, documentation updates

---

## How to Contribute to Changelog

When submitting a PR, please add your changes under the `[Unreleased]` section:

```markdown
## [Unreleased]

### Added
- New config_jazz.txt profile for jazz music

### Fixed
- Corrected distortion issue in config_party.txt
```

The maintainer will move these to the appropriate version section upon release.