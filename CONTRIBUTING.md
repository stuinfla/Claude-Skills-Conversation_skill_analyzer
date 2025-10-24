# Contributing to Conversation Skill Analyzer

Thank you for your interest in contributing! This guide will help you get started.

## Ways to Contribute

### 1. Report Bugs
- Check [existing issues](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/issues) first
- Provide clear description of the problem
- Include steps to reproduce
- Share your Claude version and skill version

### 2. Suggest Features
- Open a [GitHub Discussion](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/discussions)
- Explain the use case
- Describe the expected behavior
- Share why this would be valuable

### 3. Improve Documentation
- Fix typos or unclear instructions
- Add examples for different professions
- Translate documentation (if multilingual support added)
- Improve installation guides

### 4. Submit Code Changes
- Fork the repository
- Create a feature branch
- Make your changes
- Test thoroughly
- Submit a Pull Request

## Development Setup

### Prerequisites
- Access to Claude Pro or Team (for testing)
- Basic understanding of:
  - Markdown (for SKILL.md documentation)
  - React/JSX (if modifying dashboard output)
  - Git workflow

### Local Development

1. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Claude-Skills-Conversation_skill_analyzer.git
   cd Claude-Skills-Conversation_skill_analyzer
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make changes**
   - Edit SKILL.md for workflow changes
   - Update templates/ for starter templates
   - Modify references/ for methodology docs

4. **Test locally**
   - Copy folder to `/mnt/skills/user/conversation-skill-analyzer/`
   - Test with Claude by running the skill
   - Verify all features work as expected

5. **Update documentation**
   - Update CHANGELOG.md with your changes
   - Update README.md if needed
   - Add examples if relevant

6. **Commit changes**
   ```bash
   git add .
   git commit -m "feat: Add description of your feature"
   ```

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create Pull Request**
   - Go to GitHub and create PR
   - Describe what you changed and why
   - Reference any related issues

## Commit Message Format

Follow conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Formatting changes
- `refactor:` Code refactoring
- `test:` Adding tests
- `chore:` Maintenance tasks

Examples:
```
feat: Add support for custom timeframe selection
fix: Correct conversation counting logic
docs: Improve installation instructions
```

## Key Files

### For Workflow Changes
- **SKILL.md** - Main skill documentation (Claude reads this)
  - Defines how Claude should analyze conversations
  - Specifies output format
  - Contains workflow instructions

### For Output Changes
- **SKILL.md** → Dashboard Output section
  - Describes what the artifact should look like
  - React component structure
  - Design principles

### For Templates
- **templates/** directory
  - Starter skill templates
  - Implementation checklists
  - Testing frameworks

### For Reference
- **references/** directory
  - Methodology explanations
  - Interactive workflow guides

## Testing Guidelines

### Manual Testing Checklist

Before submitting a PR, test:

1. **Installation**
   - [ ] Skill installs correctly via upload
   - [ ] All files present in correct structure

2. **Conversation Counting**
   - [ ] Counts conversations accurately
   - [ ] Shows visual timeline
   - [ ] Classifies usage pattern correctly

3. **Analysis**
   - [ ] Fetches recommended conversation count
   - [ ] Discovers user's domain (don't hardcode!)
   - [ ] Identifies unique patterns
   - [ ] Shows rolling commentary

4. **Dashboard**
   - [ ] Artifact displays automatically
   - [ ] Shows top 5 skills
   - [ ] "Build This Skill" buttons work
   - [ ] Design is clean and professional

5. **Refinement**
   - [ ] Asks about completed projects
   - [ ] Can deselect recommendations
   - [ ] Updates dashboard correctly

### Test with Different User Types

Try to test with conversations from different domains:
- Technical (development, IT)
- Professional (consulting, sales, marketing)
- Creative (writing, design)
- Academic (research, teaching)

## Code Style

### Markdown (SKILL.md, README.md)
- Use clear headers (##, ###)
- Keep lines under 100 characters when possible
- Use code blocks for examples
- Use bold for emphasis, not ALL CAPS
- Include emoji sparingly for visual scanning

### Documentation
- Write in second person ("you") when addressing users
- Use first person ("I", "Claude") in SKILL.md workflow
- Be concise but complete
- Include examples where helpful

## Pull Request Process

1. **Before submitting:**
   - [ ] Test thoroughly
   - [ ] Update CHANGELOG.md
   - [ ] Update version number if needed
   - [ ] Update documentation

2. **PR Description should include:**
   - What changed
   - Why the change was needed
   - How to test the change
   - Any breaking changes
   - Screenshots (if UI changes)

3. **Review process:**
   - Maintainer will review your PR
   - May request changes
   - Once approved, will be merged
   - Will be included in next release

## Versioning

We use [Semantic Versioning](https://semver.org/):

- **Major (3.0.0)**: Breaking changes that affect existing users
- **Minor (2.7.0)**: New features, backward compatible
- **Patch (2.6.1)**: Bug fixes, small improvements

## Questions?

- Open a [Discussion](https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer/discussions)
- Comment on related issues
- Reach out to maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make this skill better for everyone! 🎉
