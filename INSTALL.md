# Installation Guide

## For End Users (Easiest Method)

### Option 1: Direct Upload to Claude (Recommended)

1. **Download the skill**
   - Go to [Releases](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/releases)
   - Download `conversation-skill-analyzer-v2.6.zip`

2. **Install in Claude**
   - Open Claude.ai
   - Upload the ZIP file to Claude
   - Say: "Please install this skill"
   - Claude will extract and place it in the correct location

3. **Verify Installation**
   ```
   List my installed skills
   ```

4. **Use It**
   ```
   Analyze my conversation history and recommend my top 5 skills to build
   ```

---

### Option 2: Manual Installation

1. **Download and extract**
   - Download `conversation-skill-analyzer-v2.6.zip`
   - Extract the ZIP file
   - You'll get a folder like `skill-analyzer-v2.6/`

2. **Rename the folder**
   ```
   conversation-skill-analyzer/
   ```
   (Remove the version number from folder name)

3. **Place in skills directory**
   - The folder should go at:
   ```
   /mnt/skills/user/conversation-skill-analyzer/
   ```

4. **Verify the structure**
   ```
   /mnt/skills/user/conversation-skill-analyzer/
   ├── SKILL.md
   ├── README.md
   ├── CHANGELOG.md
   ├── templates/
   ├── references/
   └── scripts/
   ```

5. **Test it**
   ```
   Analyze my conversation history
   ```

---

## For Developers / Contributors

### Clone the Repository

```bash
git clone https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer.git
cd Claude-Skills-Conversation_skill_analyzer
```

### Development Setup

1. **Make your changes** to SKILL.md, templates, etc.

2. **Test locally**
   - Copy folder to `/mnt/skills/user/conversation-skill-analyzer/`
   - Test with Claude

3. **Submit improvements**
   - Fork the repository
   - Create a feature branch
   - Submit a Pull Request

---

## Distribution Methods

### 1. GitHub Releases (Recommended for Sharing)

**Best for:** Public distribution, versioning, discoverability

**How it works:**
1. Create a new Release on GitHub
2. Attach the ZIP file (`conversation-skill-analyzer-v2.6.zip`)
3. Add release notes from CHANGELOG.md
4. Users download from Releases page

**Advantages:**
- ✅ Version tracking
- ✅ Release notes
- ✅ Easy to find and download
- ✅ GitHub handles hosting
- ✅ Users get updates via new releases

**Share with:**
- Direct link: `https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/releases`
- Or in Claude: "Install skill from github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer"

---

### 2. Claude Skills Marketplace (Future)

When Anthropic launches an official skills marketplace:
- Submit via their official process
- Users can install with one click
- Automatic updates
- Discovery features

**For now:** GitHub Releases is the de facto standard

---

### 3. Direct ZIP Distribution

**Best for:** Sharing with specific people

Simply share the ZIP file:
- Via email, Slack, Discord
- Cloud storage (Dropbox, Google Drive)
- File sharing services

Users upload to Claude and say "Install this skill"

---

## Best Practices for Sharing

### 1. Use GitHub Releases

This is currently the best way:

```bash
# Create a release on GitHub
1. Go to repository → Releases → Draft a new release
2. Tag: v2.6.0
3. Title: "v2.6.0 - User-Adaptive Analysis"
4. Description: Copy from CHANGELOG.md
5. Attach: conversation-skill-analyzer-v2.6.zip
6. Publish release
```

### 2. Clear Documentation

Ensure these files are up-to-date:
- **README.md** - Quick overview and quick start
- **SKILL.md** - Complete documentation for Claude
- **CHANGELOG.md** - Version history
- **INSTALLATION.md** - This file!

### 3. Semantic Versioning

Follow [semver](https://semver.org/):
- **Major (3.0.0)**: Breaking changes
- **Minor (2.7.0)**: New features, backward compatible
- **Patch (2.6.1)**: Bug fixes

### 4. Keep It Simple

Users should be able to:
1. Download ZIP
2. Upload to Claude
3. Say "Install this skill"
4. Start using it

---

## Troubleshooting

### "Skill not found"

Make sure the folder is named exactly:
```
conversation-skill-analyzer/
```
(no version numbers, no extra text)

### "Skill not working"

Verify structure:
```
conversation-skill-analyzer/
└── SKILL.md  ← This file must exist at the root
```

### "Permission denied"

If manually installing, ensure you have write access to:
```
/mnt/skills/user/
```

---

## Requirements

- Claude Pro or Team account (skills feature)
- Minimum 20-30 conversations for meaningful analysis
- Chat memory enabled (recommended)

---

## Support

- **Issues**: [GitHub Issues](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/issues)
- **Discussions**: [GitHub Discussions](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/discussions)
- **Updates**: Watch the repository for new releases

---

## Quick Reference

**Install via upload:**
```
Upload ZIP → "Install this skill"
```

**Use the skill:**
```
Analyze my conversation history and recommend my top 5 skills to build
```

**Check version:**
```
What version of conversation-skill-analyzer do I have?
```

**Update:**
1. Download latest release
2. Upload to Claude
3. Say "Update the conversation-skill-analyzer skill"
