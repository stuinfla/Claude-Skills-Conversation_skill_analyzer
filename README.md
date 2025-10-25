# Conversation Skill Analyzer

> Analyzes up to 150 conversations using **streaming analytics**—no context overflow, clear progress, professional results.

[![Version](https://img.shields.io/badge/version-4.2.0-blue.svg)](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/releases)
[![Platform](https://img.shields.io/badge/platform-Claude%20AI-blue.svg)](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## What It Does

This skill uses **streaming statistical aggregation** to analyze your conversation history:

1. ⚡ **Fetches** up to 150 conversations (adaptive to your history)
2. 🔍 **Extracts** keywords and patterns from titles in real-time
3. 📊 **Aggregates** statistics (frequency, recency, categories)
4. 🗑️ **Discards** raw data immediately (keeps only ~5-10KB statistics)
5. 🎯 **Generates** personalized skill recommendations
6. 📱 **Displays** interactive React dashboard

**Complete workflow:** Stream → Analyze → Recommend → **BUILD**

**Key Features:**
- **⚡ Streaming analytics** - Processes 150+ conversations without context overflow
- **🎯 Adaptive fetch** - Automatically adjusts to your conversation count
- **💬 Clear progress** - Professional messaging: "Examined 20... 40... 60..."
- **🚀 Fast** - Completes in 20-30 seconds
- **📊 React dashboard** - Professional visualization with evidence
- **🎨 Claude-native** - Uses recent_chats tool

---

## 🚀 Quick Start

### Installation
1. Download [conversation-skill-analyzer-v4.2.0.zip](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/releases/latest/download/conversation-skill-analyzer-v4.2.0.zip)
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

## 🎉 What's New in v4.2.0

### ⚡ Streaming Analytics Engine
**The game-changer:** Now analyzes up to 150 conversations using streaming statistical aggregation.

**What Changed:**
- **Streaming aggregation** - Processes conversations in batches, keeps only statistics (~5-10KB)
- **Adaptive fetch** - Automatically handles 20 to 150+ conversations based on your history
- **Clear progress** - Professional messaging: "Examined 20... 40... 60..." (no confusing jumps)
- **Context-safe** - Statistics only, raw data discarded immediately
- **Fast completion** - 20-30 seconds for 150 conversations

**User Experience Improvements:**
- 💬 **Clear communication** - "I'll analyze your conversation history..." opening
- 📊 **Smooth progress** - Progressive counts, no confusing batch numbers
- ✅ **Professional finish** - "Analysis complete! Found patterns across X conversations"
- 🎯 **Better recommendations** - Frequency + recency + category analysis

**Technical Innovation:**
- Memory footprint: ~5-10KB (vs 200KB+ for raw data)
- Can process unlimited conversations without context overflow
- Keyword extraction from titles only
- Real-time statistical aggregation
- Pattern detection from compact statistics

## Previous Updates

**v4.1.0** - Context Fix
- Reduced to 60 conversations (metadata only)
- Fixed context overflow issue

**v4.0.1** - Platform Clarity
- Removed false ChatGPT compatibility claims

**v4.0.0** - Initial Release
- Attempted 160-conversation fetch (had context issues)

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

### 1. Analyze (20-30 seconds)
- Fetches up to 150 conversations (adaptive to your history)
- Discovers YOUR actual work domain
- Identifies repeated patterns and pain points
- Progress tracking: "Examined 20... 40... 60... 140..."

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

- **Analysis time**: ~20-30 seconds
- **Conversations analyzed**: Up to 150 (adaptive batches of 20)
- **Memory footprint**: ~5-10KB statistics (vs 200KB+ raw data)
- **Data extracted**: Keyword patterns from titles (not full content)
- **Privacy**: Lightweight statistical analysis only
- **Pattern detection**: Frequency + recency scoring with category inference
- **Output**: Interactive React dashboard with Tailwind CSS
- **Context usage**: Streaming aggregation - guaranteed completion within limits
- **Native tool**: Uses Claude's `recent_chats` API

---

## 🎓 Version History

**v4.2.0** (Current) - Streaming Analytics Release
- ⚡ **BREAKTHROUGH**: Streaming statistical aggregation handles 150+ conversations
- 🎯 **Adaptive fetch**: Automatically adjusts to user's conversation count (20-150+)
- 💬 **Clear UX**: Professional progress messaging, no confusing batch numbers
- 📊 **Memory efficient**: ~5-10KB statistics vs 200KB+ raw data (45x reduction)
- ⚡ **Fast**: Completes in 20-30 seconds
- ✅ **Context-safe**: Guaranteed completion within limits

**v4.1.0** - Context Fix (Temporary Solution)
- ⚡ Reduced 160 → 60 conversations to prevent context overflow
- ⚡ Metadata-only analysis (titles/timestamps)
- ⚡ Fast completion (~10-15 seconds)
- ✅ Lightweight pattern detection

**v4.0.1** - Platform Clarity Patch
- Removed false ChatGPT compatibility claims
- Claude-only with accurate capability description

**v4.0.0** - Initial Production Release (Had Context Issues)
- Attempted 160-conversation fetch (caused context overflow)
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
