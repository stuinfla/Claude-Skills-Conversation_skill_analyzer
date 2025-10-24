# Conversation Skill Analyzer

> Analyzes your Claude conversation history to discover automation opportunities, then **helps you BUILD those skills immediately**.

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## What It Does

This Claude skill:
1. 🔍 **Analyzes** YOUR conversation patterns to discover automation opportunities
2. 🎯 **Recommends** your top 5 skills to build (personalized to YOUR work)
3. 🚀 **Builds** those skills with you via skill-creator integration

**Complete workflow:** Analyze → Recommend → **BUILD**

**Key Feature:** Works for teachers, doctors, lawyers, marketers, developers, consultants, researchers - anyone who uses Claude.

## Quick Start

### Installation

**Upload to Claude (Easiest)**
1. Download [latest release](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/releases) ZIP
2. Upload to Claude.ai
3. Say: `Install this skill`

### Usage

```
Analyze my conversation history and recommend my top 5 skills to build
```

Claude will analyze and show you a dashboard with recommendations.

### Build a Skill

```
Build skill #1
```

Claude will immediately start building that skill using skill-creator, with all the context pre-filled!

## Features

### v3.0 - Optimized Data Fetching ⭐
- **Efficient conversation fetching**: 40 per call, 160 total target
- **Better pattern detection**: Fixed target ensures reliable analysis
- **Faster processing**: 4 calls minimum (40 × 4 = 160)
- **Progress visibility**: Shows "40... 80... 120... 160..."

### v2.7 - Build Integration
- **"Build This Skill" buttons now work!**
- Say "Build skill #1" to immediately create that skill
- Claude calls skill-creator with pre-populated context
- Complete workflow: analyze → recommend → build

### v2.6 - Proper Data Fetching
- Fetches 150-250+ conversations for reliable patterns
- Smart scope recommendations

### v2.5 - User-Adaptive
- No hardcoded assumptions
- Discovers YOUR domain automatically

## Complete Workflow

1. **Analyze** - `Analyze my conversations`
   - Fetches 150-250+ conversations
   - Discovers YOUR patterns and domain
   
2. **Review** - Dashboard appears
   - See your top 5 personalized skills
   - Evidence from your conversations
   - Time savings estimates

3. **Build** - `Build skill #1`
   - Claude calls skill-creator
   - Pre-fills all context
   - Guides you through building

## Version History

**v3.0.0** (Current) ⭐
- Optimized data fetching: 40 per call, 160 total
- Efficient pattern analysis
- Progress visibility during fetch

**v2.7.0**
- Build buttons now functional
- Skill-creator integration
- Complete analyze → build workflow

**v2.6.0**
- Fetches 150-250+ conversations
- Proper data volume

**v2.5.0**
- User-adaptive, no assumptions
- Works for everyone

[Full changelog](CHANGELOG.md)

## Example Output

**The recommendations are completely personalized to YOU:**

### For a Teacher:
```
#1 [VERY HIGH]
Lesson Plan Generator
Transform curriculum standards into weekly plans
Time Saved: 8-12 hrs/week
[Build This Skill →]
```

### For a Developer:
```
#1 [VERY HIGH]
Environment Setup Automator
One-command dev environment configuration
Time Saved: 15-20 hrs/month
[Build This Skill →]
```

### For a Marketing Professional:
```
#1 [VERY HIGH]
Campaign Report Generator
Transform analytics into client-ready reports
Time Saved: 8-12 hrs/week
[Build This Skill →]
```

**Your results will be different** - based on YOUR conversations!

## Why Use This?

### For Individuals
- 🎯 **Save time**: Discover which automations provide biggest impact
- 💰 **Prioritize**: Know what to build first based on evidence
- 🔍 **Understand yourself**: See your workflow patterns objectively
- 🚀 **Take action**: Each recommendation has a "Build This" button

### For Teams
- 📊 **Identify common needs**: See what skills would help the team
- 🤝 **Share solutions**: Build skills that benefit multiple people
- 📈 **Measure impact**: Track time savings and productivity gains
- 🎓 **Onboarding**: Help new members build relevant skills

## Technical Details

- **Minimum conversations**: 20-30 (but 150-250 is ideal)
- **Processing time**: ~30-45 seconds
- **Memory**: Uses chat memory if enabled (recommended)
- **Privacy**: Analyzes conversation titles/summaries, not full content
- **Output**: Interactive React dashboard with collapsible sections

## Documentation

- 📖 [SKILL.md](SKILL.md) - Complete skill documentation
- 🚀 [INSTALL.md](INSTALL.md) - Installation guide
- 📝 [CHANGELOG.md](CHANGELOG.md) - Version history
- 📋 [templates/](templates/) - Starter templates for building skills

## Requirements

- Claude Pro or Team account (skills feature required)
- Minimum 20-30 conversations for meaningful analysis
- Chat memory enabled (recommended, not required)

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Version History

**v2.6.0**
- Fixed: Now fetches 150-250+ conversations for proper analysis
- Added: Explicit data volume requirements
- Improved: Pattern detection reliability

**v2.5.0**
- User-adaptive: No hardcoded profession assumptions
- Discovers domain from conversations
- Works for everyone

**v2.4.0**
- Simplified dashboard with build buttons
- Removed complex ROI calculations
- Single-page view

[Full changelog](CHANGELOG.md)

## Support

- 🐛 **Bug reports**: [GitHub Issues](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/discussions)
- 📧 **Contact**: Open an issue

## License

MIT License - See [LICENSE](LICENSE) for details

## Author

Created by Stuart Kerr ([@stuinfla](https://github.com/stuinfla))

Built with Claude to help people discover their productivity goldmines.

---

## Star This Repo ⭐

If this skill helps you discover valuable automations, please star the repo to help others find it!

## Share Your Results 🎉

Found some great skill recommendations? Share your experience in [Discussions](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/discussions)!
