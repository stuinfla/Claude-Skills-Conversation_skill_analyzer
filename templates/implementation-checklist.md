# Skill Implementation Checklist

Use this checklist to build your skill from concept to launch.

## Phase 1: Planning (30-60 minutes)

### Define the Problem
- [ ] Write down the specific problem this skill solves
- [ ] Identify 3-5 concrete use cases
- [ ] Define success criteria: What does "working well" look like?
- [ ] List what the skill should NOT do (boundaries)

### Research Existing Solutions
- [ ] Check if similar skills exist in the examples folder
- [ ] Search Claude's available tools that might help
- [ ] Identify any reference documentation needed
- [ ] Note any APIs or external services required

### Design the User Experience
- [ ] Write the simplest possible prompt that should trigger this skill
- [ ] Design the output format (markdown, table, artifact, etc.)
- [ ] Sketch the conversation flow
- [ ] Identify any required user inputs

## Phase 2: Core Implementation (2-4 hours)

### Create Basic Structure
- [ ] Copy starter-skill-template.md to your skill folder
- [ ] Fill in name and description (iterate on this!)
- [ ] Write the "When to Use" section with specific triggers
- [ ] Create Quick Start prompts

### Build Core Functionality
- [ ] Identify which tools/commands are needed
- [ ] Write the main skill instructions
- [ ] Document the step-by-step process
- [ ] Create any required scripts or reference files

### Add Examples
- [ ] Write 2-3 concrete examples with inputs and outputs
- [ ] Include a simple case
- [ ] Include a complex case
- [ ] Include an edge case

## Phase 3: Enhancement (1-2 hours)

### Add Advanced Features
- [ ] Identify optional parameters or modes
- [ ] Document advanced usage patterns
- [ ] Add customization options
- [ ] Create fallback behaviors

### Polish Documentation
- [ ] Review and tighten description (under 200 chars)
- [ ] Add tips for best results
- [ ] Document limitations honestly
- [ ] Add troubleshooting section

### Create References (if needed)
- [ ] Add methodology documentation
- [ ] Include example templates
- [ ] Link to external resources
- [ ] Add technical specifications

## Phase 4: Testing (30-60 minutes)

### Basic Functionality Tests
- [ ] Test with the simplest possible input
- [ ] Test with a complex, realistic input
- [ ] Test with missing/invalid inputs
- [ ] Test with edge cases

### User Experience Tests
- [ ] Is the output format clear and scannable?
- [ ] Are error messages helpful?
- [ ] Can someone use this without reading full docs?
- [ ] Does it handle ambiguous requests gracefully?

### Performance Tests
- [ ] Does it complete in reasonable time?
- [ ] Does it handle large inputs?
- [ ] Are there any timeout issues?
- [ ] Does it use tools efficiently?

## Phase 5: Launch Prep (15-30 minutes)

### Final Polish
- [ ] Proofread all documentation
- [ ] Verify all examples work
- [ ] Check that Quick Start prompts are copy-pasteable
- [ ] Ensure consistent formatting

### Metadata
- [ ] Version number (start with 1.0)
- [ ] Creation date
- [ ] Update SKILL.md frontmatter
- [ ] Add any tags or categories

### Deployment
- [ ] Move to /mnt/skills/user/[skill-name]/
- [ ] Test skill in fresh conversation
- [ ] Verify Claude can find and use it
- [ ] Create a demo conversation showing key features

## Phase 6: Iteration (Ongoing)

### Collect Feedback
- [ ] Use the skill yourself for 1 week
- [ ] Note any friction points
- [ ] Track which features get used most
- [ ] Identify missing capabilities

### Improve Based on Usage
- [ ] Update examples with real usage patterns
- [ ] Refine prompts based on what works
- [ ] Add shortcuts for common operations
- [ ] Document new use cases discovered

### Version Updates
- [ ] Document changes in version history
- [ ] Increment version number
- [ ] Share improvements with community (optional)

---

## Quality Checklist

A 9/10+ skill should have:
- ✅ **Crystal clear value prop**: User knows instantly what it does
- ✅ **Zero-friction start**: Copy-paste prompts that work immediately
- ✅ **Concrete examples**: Real inputs and outputs, not theoretical
- ✅ **Honest limitations**: What it can't do
- ✅ **Polished output**: Clean, scannable, professional formatting
- ✅ **Error handling**: Graceful failures with helpful messages
- ✅ **Documentation**: Complete but not overwhelming
- ✅ **Tested edge cases**: Doesn't break on weird inputs

## Time Budget Guide

**Quick Skill (4-6 hours total)**:
- Simple, focused functionality
- Minimal custom logic
- Uses existing Claude tools
- Example: Template library, prompt generator

**Medium Skill (8-12 hours total)**:
- Multi-step workflow
- Some custom scripts/references
- Combines multiple tools
- Example: Research synthesizer, document processor

**Complex Skill (20+ hours total)**:
- Advanced logic and decision trees
- Custom code execution
- External API integration
- Example: Development environment automator, data pipeline

---

**Pro Tip**: Don't try to build everything at once. Ship a minimal v1.0 that solves ONE problem really well, then iterate based on real usage.
