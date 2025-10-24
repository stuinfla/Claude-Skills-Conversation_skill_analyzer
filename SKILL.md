---
name: conversation-skill-analyzer
description: Analyzes your Claude conversation history to discover which custom skills would save you the most time, make you the most money, or eliminate your biggest frustrations. Returns a data-driven, prioritized roadmap of your top 5 skill-building opportunities with ROI estimates and evidence from your actual usage patterns.
---

# Conversation Skill Analyzer v3.1

**🚨 CRITICAL FETCH REQUIREMENT 🚨**
- **Pull 40 conversations per call** using `n=40` parameter in recent_chats
- **Target: 160 conversations** or all available chats (whichever is fewer)
- **This requires 4 calls minimum** to reach 160 (40 × 4 = 160)
- **Show progress**: "Fetching... 40... 80... 120... 160..."
- **NEVER STOP before reaching 160 or exhausting all chats**

Identifies high-value automation opportunities by analyzing YOUR conversation patterns, then helps you BUILD those skills immediately.

## Quick Start

```
Analyze my conversation history and recommend my top 5 skills to build
```

Claude will:
1. Count your conversations and show usage timeline
2. Recommend optimal analysis scope (typically last 3 months)
3. Analyze patterns with rolling commentary
4. Create interactive dashboard with your top 5 priorities
5. Ask if any are from completed projects
6. Refine recommendations based on your feedback
7. **When you're ready:** Help you build any skill by saying "Build skill #1"

## When to Use

- Planning your skill development roadmap
- Identifying highest-ROI automation opportunities
- Understanding your workflow patterns objectively
- Finding billable service opportunities to package
- Justifying time investment in skill building

## How It Works

### Analysis Workflow

**CRITICAL: User-Adaptive Analysis**

This skill must be **completely personalized** to whoever runs it. Do NOT make assumptions about the user's profession, industry, or use case.

**Before analyzing:**
1. Check user's memory and preferences for context about their work
2. Infer profession/domain from actual conversation patterns
3. Detect their unique workflows and pain points
4. Never assume they are an AI consultant, developer, or any specific role
5. Let the conversations reveal what they actually do

**Phase 1: Discovery (10-15 seconds)**
- **Counts total conversations properly** using multiple `recent_chats` calls
- Shows clear stats: "X total conversations found"
- **DETERMINES FETCH STRATEGY:**
  - **Pull 40 conversations per call** using `n=40` in recent_chats
  - **Target: 160 conversations total** or all available chats (whichever is fewer)
  - **If user has < 160 total conversations**: Fetch ALL of them
  - **If user has 160+ total conversations**: Fetch exactly 160 conversations
- **MANDATORY**: Continue calling `recent_chats` with `n=40` and pagination (using `before` parameter) until you reach 160 or exhaust all chats
- **Minimum 4 calls required** to reach 160 (40 × 4 = 160)
- User can see progress: "Fetching conversations... 40... 80... 120... 160..."
- **DO NOT PROCEED** to Phase 2 until you have fetched 160 conversations or all available chats.

**Phase 2: Pattern Analysis (15-25 seconds)**
- **STEP 1**: Count total conversations retrieved so far
- **STEP 2**: If less than 160, CONTINUE FETCHING with recent_chats using `n=40` and the `before` parameter from the last conversation's timestamp
- **STEP 3**: Repeat Step 2 until you have 160 conversations OR all available chats (4+ calls to recent_chats with n=40)
- **STEP 4**: Only after fetching sufficient conversations (160 or all available), begin analysis
- **Discovers the user's actual work domain** by analyzing conversation topics (don't assume!)
- **Identifies THEIR unique workflow categories** and repeated tasks
- **Detects THEIR specific domain expertise** and pain points from conversation content
- Calculates impact based on frequency and recency
- Shows rolling commentary with discovered patterns: "Analyzing... found patterns in [discovered categories]..."

**Phase 3: Interactive Dashboard**
- Creates single-page React artifact
- Shows summary stats at top
- Lists top 5 skills as cards
- Each card has **functional** "Build This Skill" button
- Opens automatically on right side

**Phase 4: Refinement**
- Asks: "Are any from completed projects?"
- You can deselect 1-2 recommendations
- Claude updates the dashboard with revised list
- No tabs, no complexity - just clean list of priorities

**Phase 5: Skill Building (NEW)**
- **When user clicks "Build This Skill" button:**
  1. User says: "Build skill #1" (or clicks the button)
  2. Claude extracts the skill context and requirements
  3. Claude calls the skill-creator skill with full context
  4. Skill-creator guides user through building the actual skill
- **Alternative**: Claude provides ready-to-use prompt that user can execute

### Smart Scope Recommendation

**SIMPLE RULE:**
- **Target: 160 conversations** using `n=40` per call (4 calls minimum)
- **< 160 total conversations**: Fetch ALL of them
- **160+ total conversations**: Fetch exactly 160 most recent

**Why 160 is optimal:**
- Enough patterns to detect repeated workflows (minimum 100 needed)
- Recent enough to reflect current priorities (not old completed work)
- Fast enough to analyze in 30-45 seconds
- Achievable with just 4 calls at 40 conversations per call

**Implementation:**
- Call `recent_chats` with `n=40` repeatedly (NOT n=20)
- Use `before` parameter with the oldest conversation's timestamp for pagination
- Continue until 160 reached: 4 calls minimum (40 × 4 = 160)
- Show progress to user so they know it's working: "40... 80... 120... 160..."
- Stop at 160 or when all conversations exhausted

**Why 160 conversations:**
- Pattern detection needs volume (160 provides excellent reliability)
- 4 calls at 40 each = efficient data gathering
- More conversations = better evidence for recommendations
- Reduces false positives from one-off projects
- Shows true frequency and recency patterns
- Sweet spot between coverage and analysis speed

**Time-based approach:** "Last 3-6 months" naturally filters old completed work while capturing current priorities. The goal is recent, relevant, and SUFFICIENT data.

### Communication Style

Claude provides:
- **Visual timeline**: Bar charts showing conversation distribution
- **Transparent numbers**: "X total, analyzing Y from last Z months"
- **Rolling commentary**: Updates at each step so you know what's happening
- **Professional tone**: Confidence-inspiring, consultative approach
- **Clear recommendations**: Specific timeframes and alternatives

## Dashboard Output

Interactive React artifact with clean, action-focused design:

**Header Section**
- "Your Skill Dashboard"
- Analysis summary: "Analysis of X conversations • [Usage Pattern]"
- Simple summary cards (optional):
  - Skills to Build: 5
  - Time Saved/Month: X hrs

**Your Top 5 Skills to Build** (Single scrollable view)

Each skill displayed as a clean, professional card:
- **Rank badge** (#1, #2, #3) in top-left corner
- **Impact badge** (VERY HIGH/HIGH/MEDIUM) in top-right corner
- **Skill name** (large, bold, clear)
- **One-line description** explaining what it does
- **Key information row:**
  - Time Saved: "20-25 hrs/month" or "10-15 hrs/proposal"
  - Build Time: "8-12 hours" or "12-16 hours"
  - Break-Even: "1.5 weeks" or "3 days"
- **"Build This Skill →" button** (prominent, full-width, action-blue)
  - **CRITICAL**: Button must be functional and trigger skill creation
  - When clicked, button should initiate the skill-creator workflow
  - Pass the skill details to skill-creator for immediate building

### Making the Button Functional

**When user clicks "Build This Skill":**

1. **Extract skill context** from the card that was clicked:
   - Skill name
   - Description
   - User's work domain
   - Evidence from conversations
   - Time saved estimate

2. **Call the skill-creator skill** with this prompt:
   ```
   Build a new skill called "[Skill Name]" that does: [Description]
   
   Context from conversation analysis:
   - User's domain: [discovered domain]
   - Purpose: [what it automates]
   - Evidence: Found in [X] conversations about [topics]
   - Expected impact: Saves [time] per [period]
   
   Please create this skill now using the skill-creator framework.
   ```

3. **Alternatively, provide clickable prompt** that user can execute:
   - Instead of automatic trigger, show a copyable prompt
   - User can paste it to start building
   - Or display instructions: "To build this skill, say: 'Build the [Name] skill using skill-creator'"

**Implementation Approach:**

The button should either:
- **Option A**: Directly invoke skill-creator (preferred)
- **Option B**: Display a pre-filled prompt for user to execute
- **Option C**: Copy prompt to clipboard on click

Choose based on what's technically feasible in the artifact environment.

**Design Principles:**
- Single-page scrollable view (no tabs)
- **Action-focused**: Big, clear "Build" buttons
- **Less financial detail**: Removed annual value calculations
- **Simple time metrics**: Hours saved, not dollar amounts
- **Quick to scan**: Clean cards, good spacing
- **Professional design**: Modern, not over-designed
- Clean white/gray backgrounds, blue accents
- Mobile-friendly responsive layout

## Example Output

**Note:** Examples vary completely based on who runs the skill. These are just samples showing different user types:

### Example A: Developer
```
Your Skill Dashboard
Analysis of 120 conversations • Active User

#1 [VERY HIGH]
Environment Setup Automator
One-command dev environment with all tools configured
Time Saved: 15-20 hrs/month | Build: 6-8 hours | Break-Even: 2 weeks
[ Build This Skill → ]
```

### Example B: Marketing Professional
```
#1 [VERY HIGH]
Campaign Report Generator
Transform analytics into client-ready reports in minutes
Time Saved: 8-12 hrs/week | Build: 10-14 hours | Break-Even: 1 week
[ Build This Skill → ]
```

### Example C: Researcher
```
#1 [VERY HIGH]
Literature Review Synthesizer
Automated literature analysis and citation management
Time Saved: 20-25 hrs/month | Build: 12-16 hours | Break-Even: 3 weeks
[ Build This Skill → ]
```

### Example D: Sales Professional
```
#1 [VERY HIGH]  
Proposal Accelerator
Transform discovery calls into proposals in 30 minutes
Time Saved: 10-15 hrs/proposal | Build: 8-12 hours | Break-Even: 3 days
[ Build This Skill → ]
```

**Your results will be completely different** based on YOUR actual conversation patterns!

## Advanced Options

**Specific timeframe:**
```
Analyze my last [month/6 months/year] of conversations
```

**Specific count:**
```
Analyze my last 150 conversations
```

**All conversations:**
```
Analyze all my conversations regardless of count
```

**Domain focus:**
```
Analyze my [finance/healthcare/development/consulting] conversations
```

**Gap analysis:**
```
I have skills for X, Y, Z. What am I missing?
```

## Memory Integration

For best results, ensure chat memory is enabled:
1. Profile icon (bottom left) → Settings → Profile
2. Toggle "Chat memory" to ON

Why? Helps Claude distinguish ongoing priorities from completed work, avoiding recommendations for temporary projects.

## Interactive Refinement

After seeing recommendations:

**You:** "#3 was a one-time client project that's done"

**Claude:** Removes #3, promotes next priority from analysis, shows revised complete list

This ensures recommendations align with your current focus, not past work.

## Building the Skills

**When user wants to build a skill:**

### Option 1: Direct Request (Recommended)
**User says:** "Build skill #1" or "Build the [Skill Name] skill"

**Claude should:**
1. Extract the skill details from the analysis
2. Create a comprehensive prompt for skill-creator:
   ```
   Build a new skill called "[Skill Name]" using the skill-creator framework.
   
   Purpose: [Description]
   Domain: [User's domain discovered from analysis]
   Use case: [What it automates]
   Evidence: Found in [X] conversations about [specific topics]
   Expected impact: Saves [time estimate] per [period]
   
   Specific requirements based on user's workflows:
   - [Requirement 1 from conversation patterns]
   - [Requirement 2 from conversation patterns]
   - [Requirement 3 from conversation patterns]
   
   Please guide me through building this skill now.
   ```
3. Pass this to skill-creator skill
4. Let skill-creator guide the building process

### Option 2: Button Click in Artifact
If the artifact button is clicked, Claude should detect this and automatically trigger Option 1 above.

### Option 3: Provide Ready Prompt
If the user asks "How do I build this?", provide them with a complete, ready-to-use prompt:

**Claude says:**
"To build the [Skill Name] skill, copy and paste this prompt:

```
Build a new skill called "[Skill Name]" using skill-creator.

Purpose: [Full description with context]
Based on my conversation patterns as a [domain], I need this to [specific use case].

Please create:
- SKILL.md with complete documentation
- Templates for [specific templates needed]
- Examples from my [domain] work

Let's build it step by step.
```"

## Implementation Support

Each recommendation includes:
- **Evidence**: Specific conversation count and patterns
- **Impact rating**: VERY HIGH/HIGH/MEDIUM based on frequency and scope
- **Complexity**: Low/Medium/High based on technical requirements
- **Next action**: Specific first step to start building
- **Template link**: Starter skill template in templates/ folder

## Technical Notes

- Analyzes conversation titles and summaries (not full content)
- Requires minimum 20-30 conversations for meaningful patterns
- Processing time: ~30-45 seconds total (including dashboard creation)
- Artifact displays automatically on right side
- Pattern detection uses frequency, recency, and domain clustering
- ROI calculations based on typical automation time savings
- Complexity ratings factor technical expertise and resource requirements

## Output Format

Single React JSX artifact with:
- Embedded analysis data (no external files)
- State management for tab switching
- Tailwind CSS styling (no external stylesheets)
- Self-contained, interactive component
- Instant display in Claude's artifact panel

## Notes

- **⚠️ FETCH REQUIREMENT**: Pull 40 conversations per call (n=40), minimum 4 calls to reach 160
- **Target: 160 conversations** for optimal pattern detection (or all available if fewer)
- **🌟 COMPLETELY USER-ADAPTIVE**: Analyzes YOUR conversations to discover YOUR patterns - never assumes your profession or domain
- **Personalized recommendations**: Skills are based on what YOU actually do, not generic templates
- **Domain discovery**: Automatically detects your work area from conversation content
- **No assumptions**: Doesn't presume you're a developer, consultant, or any specific role
- **Smart adaptive**: Automatically adjusts scope based on your usage level
- **Transparent**: Always shows what's being analyzed and why
- **User control**: Can override any recommendation or timeframe
- **Interactive**: Clean dashboard with action buttons
- **Refinable**: Deselect irrelevant items, get revised priorities
- **Professional**: Consultative tone, visual polish, clear metrics
- **Fast**: Complete analysis in under 1 minute
- **Actionable**: Each recommendation includes specific next steps
- **Evidence-based**: All suggestions backed by YOUR actual conversation patterns
- **No dependencies**: Works out of the box

## Version

3.0.0 - Major optimization: 40 conversations per call, 160 total target for efficient pattern analysis
