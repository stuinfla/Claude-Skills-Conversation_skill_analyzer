# Conversation Skill Analyzer

> Analyzes your Claude conversation history to discover automation opportunities, then **helps you BUILD those skills with quality verification**.

[![Version](https://img.shields.io/badge/version-4.0.1-blue.svg)](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/releases)
[![Platform](https://img.shields.io/badge/platform-Claude%20AI-blue.svg)](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## What It Does

This skill:
1. 🔍 **Analyzes** YOUR Claude conversation patterns
2. 🎯 **Recommends** your top 5 skills to build (personalized to YOUR work)
3. ✅ **Builds** those skills with quality verification

**Complete workflow:** Analyze → Recommend → Build → **VERIFY**

**Key Features:**
- **✅ Fixed 60-chat bug** - Now reliably fetches 160 conversations
- **📊 Complete React dashboard** - Actual JSX code included
- **🔧 Quality verification** - 12-point checklist ensures professional results
- **🎯 Claude-native** - Uses recent_chats tool for direct conversation access

---

## 🚀 Quick Start

### Installation
1. Download [conversation-skill-analyzer-v4.0.1.zip](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/releases/latest/download/conversation-skill-analyzer-v4.0.1.zip)
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

## 🎉 What's New in v4.0.1

### 🔧 Platform Clarity
- **Removed false ChatGPT compatibility claims**
- ChatGPT doesn't have native conversation history API
- Skill is Claude-only, using `recent_chats` tool
- Honest and accurate capability description

## Previous Updates (v4.0.0)

### 🔧 Critical Bug Fix
- **Problem**: Only 60 conversations fetched (instead of 160)
- **Root Cause**: Tool defaulting to n=20, stopping after 3 calls
- **Solution**: Mandatory execution protocol with explicit `n: 40` syntax
- **Result**: 100% reliable 160-conversation fetch

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

- **Analysis time**: ~30-45 seconds
- **Privacy**: Analyzes metadata only, not full content
- **Pattern detection**: Frequency, recency, domain clustering
- **Output**: Interactive React dashboard with Tailwind CSS
- **Quality**: 12-point verification checklist
- **Native tool**: Uses Claude's `recent_chats` API

---

## 🎓 Version History

**v4.0.1** (Current) - Platform Clarity Patch
- ✅ Removed false ChatGPT compatibility claims
- ✅ Claude-only with accurate capability description
- ✅ Honest platform requirements

**v4.0.0** - Complete Production Release
- ✅ Fixed 60-chat bug with mandatory execution protocol
- ✅ Complete React dashboard code (JSX + Tailwind)
- ✅ Integrated quality verification (12-point checklist)
- ✅ Clean single version (no v3/v4 mixing)

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
