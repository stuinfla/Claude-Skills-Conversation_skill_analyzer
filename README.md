# Conversation Skill Analyzer

> Analyzes your Claude conversation history to discover automation opportunities **efficiently without maxing out context**.

[![Version](https://img.shields.io/badge/version-4.1.0-blue.svg)](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/releases)
[![Platform](https://img.shields.io/badge/platform-Claude%20AI-blue.svg)](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## What It Does

This skill:
1. ⚡ **Fetches** 60 recent conversations (metadata only)
2. 🔍 **Analyzes** conversation title patterns
3. 🎯 **Recommends** your top 5 personalized skill-building opportunities
4. 📊 **Displays** interactive React dashboard with actionable insights

**Complete workflow:** Fetch → Analyze → Recommend → **BUILD**

**Key Features:**
- **⚡ Context-efficient** - Fetches only 60 conversations, completes within limits
- **🎯 Metadata analysis** - Analyzes titles/timestamps only (not full content)
- **🚀 Fast completion** - Finishes in ~10-15 seconds
- **📊 React dashboard** - Professional visualization of recommendations
- **🎨 Claude-native** - Uses recent_chats tool for conversation access

---

## 🚀 Quick Start

### Installation
1. Download [conversation-skill-analyzer-v4.1.0.zip](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/releases/latest/download/conversation-skill-analyzer-v4.1.0.zip)
2. Go to [Claude Settings > Skills](https://claude.ai/settings/skills)
3. Upload the ZIP file
4. Say: `Install this skill`

### Usage

```
Analyze my conversation history and recommend my top 5 skills to build
```

### Build a Skill

```
Build skill #1
```

Claude will start building with quality standards enforced!

---

## 🎉 What's New in v4.1.0

### ⚡ CRITICAL: Context Window Fix
- **Problem**: Previous versions fetched 160 conversations, maxing out context before delivering results
- **Root Cause**: Trying to load too much conversation data into context window
- **Solution**: Fetch only 60 conversations, extract metadata only (titles/timestamps)
- **Result**: Fast, efficient analysis that completes within context limits (~10-15 seconds)

### Key Changes
- ⚡ Reduced from 160 → 60 conversations
- 🎯 Metadata-only analysis (titles/timestamps, not full content)
- 🚀 Completes in ~10-15 seconds (was timing out before)
- ✅ Lightweight pattern detection from conversation titles
- 📊 Still generates full React dashboard with personalized recommendations

## Previous Updates

**v4.0.1** - Platform Clarity
- Removed false ChatGPT compatibility claims
- Claude-only with honest capability description

**v4.0.0** - Production Release (had context issues)
- Attempted 160-conversation fetch (caused context overflow)

### 📊 Complete React Dashboard
- Actual JSX code included (not just instructions)
- Tailwind CSS styling
- Mobile-responsive design
- Functional "Build This Skill" buttons

### ✅ Quality Verification System
- 12-point checklist for every skill built
- Mandatory verification before marking complete
- Ensures no TODOs, proper testing, error handling
- Professional documentation standards

---

## 📈 Complete Workflow

### 1. Analyze (30-45 seconds)
- Fetches 160 conversations (or all available)
- Discovers YOUR actual work domain
- Identifies repeated patterns and pain points
- Progress tracking: "40... 80... 120... 160..."

### 2. Review Dashboard
- React artifact displays automatically
- See top 5 personalized skills
- Evidence from YOUR conversations
- Time savings estimates
- Build complexity ratings

### 3. Build a Skill
- Click "Build This Skill" or say "Build skill #1"
- Quality standards automatically enforced
- Skill-creator guides implementation
- Pre-filled context from analysis

### 4. Verify Quality
- 12-point checklist runs automatically
- Must pass 10/12 to ship
- Tests documented and passing
- No TODOs or placeholders allowed

---

## 💡 Example Output

**Your results are completely personalized!**

### For a Developer:
```
#1 [VERY HIGH IMPACT]
Dev Environment Automator
One-command setup with all tools
Time Saved: 20-25 hrs/month | Build: 8-12 hrs | Break-Even: 1.5 weeks
[Build This Skill →]
```

### For a Teacher:
```
#1 [VERY HIGH IMPACT]
Lesson Plan Generator
Transform curriculum standards into weekly plans
Time Saved: 8-12 hrs/week | Build: 6-10 hrs | Break-Even: 1 week
[Build This Skill →]
```

### For a Consultant:
```
#1 [VERY HIGH IMPACT]
Proposal Accelerator
Research → proposal in 2-3 hours
Time Saved: 40-50 hrs/month | Build: 12-16 hrs | Break-Even: 3 days
[Build This Skill →]
```

---

## 🎯 Why Use This?

### For Individuals
- **Data-driven**: See which automations provide biggest ROI
- **Personalized**: Based on YOUR conversations, not generic templates
- **Quality-verified**: Every skill meets professional standards
- **Time-saving**: Eliminates guesswork in automation planning

### For Teams
- **Identify common needs**: Find skills benefiting multiple people
- **Share solutions**: Build once, use across team
- **Measure impact**: Track time savings and productivity gains
- **Quality standards**: Consistent professional output

---

## 📚 Documentation

- **[SKILL.md](SKILL.md)** - Complete skill documentation with React code
- **[CHANGELOG.md](CHANGELOG.md)** - Detailed version history
- **[INSTALL.md](INSTALL.md)** - Installation guide
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines
- **[templates/](templates/)** - Starter templates for skill building

---

## 🔧 Requirements

- Claude Pro, Team, or Enterprise (Skills feature required)
- Minimum 20-30 conversations (100+ ideal)
- Chat memory enabled (recommended)

---

## 📊 Technical Details

- **Analysis time**: ~10-15 seconds
- **Conversations fetched**: 60 (3 calls × 20 each)
- **Data extracted**: Titles and timestamps only (not full content)
- **Privacy**: Lightweight metadata analysis only
- **Pattern detection**: Keyword frequency from titles
- **Output**: Interactive React dashboard with Tailwind CSS
- **Context usage**: Efficient, completes within limits
- **Native tool**: Uses Claude's `recent_chats` API

---

## 🎓 Version History

**v4.1.0** (Current) - Context-Efficient Release
- ⚡ CRITICAL FIX: Reduced 160 → 60 conversations to prevent context overflow
- ⚡ Metadata-only analysis (titles/timestamps)
- ⚡ Fast completion (~10-15 seconds)
- ✅ Lightweight pattern detection
- ✅ React dashboard generation

**v4.0.1** - Platform Clarity Patch
- Removed false ChatGPT compatibility claims
- Claude-only with accurate capability description

**v4.0.0** - Production Release
- Attempted 160-conversation fetch (caused context issues)
- Complete React dashboard code (JSX + Tailwind)
- Quality verification checklist

**v3.0.0** - Optimized Data Fetching
- Efficient fetching: 40 per call, 160 total target
- Better pattern detection
- Progress visibility

**v2.7.0** - Build Integration
- "Build This Skill" buttons functional
- Skill-creator integration
- Complete analyze → build workflow

[Full changelog](CHANGELOG.md)

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 🐛 Support

- **Bug reports**: [GitHub Issues](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/issues)
- **Questions**: [GitHub Discussions](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/discussions)
- **Contact**: Open an issue

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

---

## 👤 Author

Created by Stuart Kerr ([@stuinfla](https://github.com/stuinfla))

Built with Claude to help people discover their productivity goldmines.

---

## ⭐ Star This Repo

If this skill helps you discover valuable automations, please star the repo!

## 🎉 Share Your Results

Found great recommendations? Share in [Discussions](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/discussions)!
