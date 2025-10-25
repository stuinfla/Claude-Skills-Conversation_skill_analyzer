---
name: conversation-skill-analyzer
description: Analyzes your Claude conversation history to discover which custom skills would save you the most time, make you the most money, or eliminate your biggest frustrations. Returns a data-driven, prioritized roadmap of your top 5 skill-building opportunities with ROI estimates and evidence from your actual usage patterns.
---

# Conversation Skill Analyzer v4.1

**Claude AI Only** | **⚡ Context-Efficient** | **✅ Quality Verified**

Identifies high-value automation opportunities by analyzing YOUR Claude conversation patterns efficiently without maxing out context window.

---

## ⚡ CRITICAL: Context-Efficient Design

**Problem**: Previous versions tried to fetch 160 conversations, maxing out context before delivering results

**Solution**: Fetch only 60 conversations, extract metadata only (titles/timestamps), analyze patterns efficiently

**Result**: Fast analysis that completes within context limits and delivers actionable recommendations

---

## Quick Start

```
Analyze my conversation history and recommend my top 5 skills to build
```

---

## 📥 Phase 1: Context-Efficient Data Collection

### MANDATORY PROTOCOL (60 Conversations Max)

**FETCH ONLY 60 CONVERSATIONS - Extract Metadata Only**:

```javascript
// ===== CALL 1: Fetch first 20 (tool maximum) =====
const batch1 = await recent_chats({n: 20});
console.log("✓ Batch 1: 20 conversations");

// Extract ONLY titles and timestamps (ignore full content)
const metadata1 = batch1.map(c => ({
  title: c.name || c.uuid.substring(0, 8),
  created: c.created_at,
  updated: c.updated_at
}));

// ===== CALL 2: Fetch next 20 =====
const lastTimestamp1 = batch1[batch1.length - 1].updated_at;
const batch2 = await recent_chats({n: 20, before: lastTimestamp1});
console.log("✓ Batch 2: 40 conversations total");

const metadata2 = batch2.map(c => ({
  title: c.name || c.uuid.substring(0, 8),
  created: c.created_at,
  updated: c.updated_at
}));

// ===== CALL 3: Fetch final 20 =====
const lastTimestamp2 = batch2[batch2.length - 1].updated_at;
const batch3 = await recent_chats({n: 20, before: lastTimestamp2});
console.log("✓ Batch 3: 60 conversations total");

const metadata3 = batch3.map(c => ({
  title: c.name || c.uuid.substring(0, 8),
  created: c.created_at,
  updated: c.updated_at
}));

// ===== COMBINE METADATA ONLY =====
const allMetadata = [...metadata1, ...metadata2, ...metadata3];
console.log(`✓ Collected ${allMetadata.length} conversation titles for analysis`);

// ===== IMMEDIATE PATTERN ANALYSIS =====
// Analyze titles for keywords, domains, patterns
// NO full conversation content loaded - just metadata
console.log("✓ Starting pattern analysis on titles...");
```

**CRITICAL EFFICIENCY REQUIREMENTS**:
- ✅ MUST use `n: 20` (actual tool limit)
- ✅ MUST make exactly 3 calls (60 conversations total)
- ✅ MUST extract ONLY metadata (titles, timestamps)
- ✅ MUST discard full conversation content immediately
- ✅ MUST show progress: "20... 40... 60..."
- ✅ MUST proceed to analysis immediately after metadata extraction
- ❌ DO NOT fetch more than 60 conversations
- ❌ DO NOT store full conversation objects

---

## 🔍 Phase 2: Lightweight Pattern Analysis

**ANALYZE METADATA ONLY - NO FULL CONTENT**:

1. **Extract Keywords from Titles**:
   - Common themes: "API", "deployment", "analysis", "document", etc.
   - Technical domains: "React", "Python", "database", "AWS", etc.
   - Task types: "debugging", "optimization", "automation", etc.

2. **Pattern Detection** (from title keywords only):
   - Repeated task categories (development, analysis, documentation)
   - Technology patterns (frameworks, tools, platforms)
   - Workflow patterns (recurring automations, common queries)

3. **Frequency Scoring**:
   - Count keyword appearances across 60 titles
   - Recent activity (last 20 conversations weighted higher)
   - Consistency (appearing in multiple batches)

4. **Domain Inference** (from title patterns):
   - Primary work domain (development, consulting, research, etc.)
   - Technology stack (languages, frameworks, tools)
   - Common pain points (repeated debugging, documentation, etc.)

5. **Skill Opportunities** (lightweight calculation):
   - High-frequency patterns = automation opportunities
   - Repeated technical queries = knowledge gap to fill
   - Manual workflows = skill-building targets

**KEEP IT FAST**: All analysis from 60 titles only, no deep content review

---

## 📊 Phase 3: Interactive Dashboard

**Create React Artifact** using this complete code:

```jsx
import React, { useState } from 'react';

const SkillDashboard = () => {
  const [skills] = useState([
    {
      id: 1,
      name: "[Skill Name from Analysis]",
      description: "[One-line description]",
      impact: "VERY HIGH",
      timeSaved: "[X hrs/week or month]",
      buildTime: "[Y-Z hours]",
      breakEven: "[N days/weeks]",
      evidence: "[X conversations about Y topics]"
    },
    // ... skills 2-5 populated from analysis
  ]);

  const handleBuildSkill = (skillId) => {
    console.log(`Building skill #${skillId}...`);
    // Trigger Phase 5: Skill Building
  };

  const impactColors = {
    "VERY HIGH": "bg-green-100 text-green-800 border-green-300",
    "HIGH": "bg-blue-100 text-blue-800 border-blue-300",
    "MEDIUM": "bg-yellow-100 text-yellow-800 border-yellow-300"
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      {/* Header */}
      <div className="max-w-4xl mx-auto mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">
          Your Skill Dashboard
        </h1>
        <p className="text-gray-600">
          Analysis of [X] conversations • [Usage Pattern]
        </p>
      </div>

      {/* Summary Stats */}
      <div className="max-w-4xl mx-auto grid grid-cols-2 gap-4 mb-8">
        <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
          <div className="text-2xl font-bold text-gray-900">{skills.length}</div>
          <div className="text-sm text-gray-600">Skills to Build</div>
        </div>
        <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
          <div className="text-2xl font-bold text-gray-900">[Total hrs]</div>
          <div className="text-sm text-gray-600">Time Saved/Month</div>
        </div>
      </div>

      {/* Top 5 Skills */}
      <div className="max-w-4xl mx-auto space-y-4">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">
          Your Top 5 Skills to Build
        </h2>

        {skills.map((skill) => (
          <div
            key={skill.id}
            className="bg-white rounded-lg shadow-sm border border-gray-200 p-6"
          >
            {/* Rank and Impact Badges */}
            <div className="flex justify-between items-start mb-3">
              <span className="inline-flex items-center justify-center w-8 h-8 rounded-full bg-blue-600 text-white font-bold text-sm">
                #{skill.id}
              </span>
              <span className={`px-3 py-1 rounded-full text-xs font-semibold border ${impactColors[skill.impact]}`}>
                {skill.impact} IMPACT
              </span>
            </div>

            {/* Skill Name and Description */}
            <h3 className="text-xl font-bold text-gray-900 mb-2">
              {skill.name}
            </h3>
            <p className="text-gray-600 mb-4">
              {skill.description}
            </p>

            {/* Metrics */}
            <div className="grid grid-cols-3 gap-4 mb-4 text-sm">
              <div>
                <div className="text-gray-500">Time Saved</div>
                <div className="font-semibold text-gray-900">{skill.timeSaved}</div>
              </div>
              <div>
                <div className="text-gray-500">Build Time</div>
                <div className="font-semibold text-gray-900">{skill.buildTime}</div>
              </div>
              <div>
                <div className="text-gray-500">Break-Even</div>
                <div className="font-semibold text-gray-900">{skill.breakEven}</div>
              </div>
            </div>

            {/* Evidence */}
            <p className="text-xs text-gray-500 mb-4">
              📊 Evidence: {skill.evidence}
            </p>

            {/* Build Button */}
            <button
              onClick={() => handleBuildSkill(skill.id)}
              className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-4 rounded-lg transition-colors duration-200"
            >
              Build This Skill →
            </button>
          </div>
        ))}
      </div>

      {/* Footer Note */}
      <div className="max-w-4xl mx-auto mt-8 text-center text-sm text-gray-500">
        <p>Click "Build This Skill" to start creating any of these skills</p>
      </div>
    </div>
  );
};

export default SkillDashboard;
```

**Usage**: Populate the `skills` array with actual analysis results, then render the component as a Claude artifact.

---

## 🔄 Phase 4: Refinement

**Ask user**: "Are any of these from completed projects?"

- User can deselect 1-2 recommendations
- System promotes next priorities from analysis
- Updates dashboard with revised list

---

## 🛠️ Phase 5: Skill Building with Quality Verification

When user says "Build skill #1":

### Step 1: Extract Context

```javascript
const skillContext = {
  name: skills[0].name,
  description: skills[0].description,
  userDomain: discoveredDomain, // from Phase 2
  evidence: {
    conversationCount: X,
    patternFrequency: "daily/weekly/monthly",
    painPoints: ["specific pain 1", "pain 2"]
  },
  expectedImpact: {
    timeSaved: skills[0].timeSaved,
    useFrequency: "daily/weekly"
  },
  buildComplexity: "low/medium/high"
};
```

### Step 2: Call Skill-Creator with Quality Standards

```
Build a new skill called "[Name]" using skill-creator framework.

MANDATORY QUALITY STANDARDS:
✅ Complete implementation (no TODOs)
✅ 3+ test scenarios with pass/fail criteria
✅ Error handling for invalid inputs
✅ Professional documentation with examples
✅ Scannable output formatting

Purpose: [Description]
Domain: [User's domain]
Use case: [What it automates]
Evidence: [X] conversations about [topics]
Expected impact: Saves [time] per [period]

VERIFICATION CHECKLIST (must pass 10/12):
[ ] Solves stated problem completely
[ ] Works with valid input on first try
[ ] Handles errors gracefully
[ ] Documentation has copy-paste examples
[ ] 3+ test scenarios included
[ ] No TODOs or placeholders
[ ] Professional output formatting
[ ] Completes in < 60 seconds
[ ] Clear limitations stated
[ ] User can understand without explanation
[ ] No confusing jargon
[ ] Appropriate tool usage

Build this skill now with these quality standards enforced.
```

### Step 3: Verification Protocol

After skill-creator completes:

```
## Skill Verification Results

### Documentation Quality (4 checks)
- [✅/❌] SKILL.md exists and complete
- [✅/❌] Description clear (<200 chars)
- [✅/❌] Quick Start has copy-paste example
- [✅/❌] Limitations stated honestly

### Functional Quality (5 checks)
- [✅/❌] Test 1 (basic): PASS
- [✅/❌] Test 2 (edge case): PASS
- [✅/❌] Test 3 (error handling): PASS
- [✅/❌] Completes in < 60 seconds
- [✅/❌] No TODOs or placeholders

### User Experience (3 checks)
- [✅/❌] Output is scannable
- [✅/❌] Professional formatting
- [✅/❌] Helpful error messages

**Overall Score**: X / 12

**Result**: ✅ PASS (≥10) or ❌ FAIL (<10)

**If FAIL**: [List what needs fixing before marking complete]
```

### Step 4: Fix or Ship

- **If verification passes**: Skill is ready to use
- **If verification fails**: Fix issues and re-verify
- **User acceptance**: User tests with real data before finalizing

---

## 🎯 Quality Standards

Every skill built MUST meet:

1. **Completeness**: Solves problem fully, no TODOs
2. **Testing**: 3+ scenarios documented and passing
3. **Error Handling**: Detects and explains problems
4. **Documentation**: Clear, with examples
5. **UX**: Scannable output, professional tone
6. **Performance**: < 60 seconds execution

**Quality Gates**:
- Planning: Requirements clear before building
- Implementation: No TODOs during development
- Verification: 10/12 checklist items pass

---

## 📝 Examples (User-Adaptive)

Your results will be **completely personalized**!

### Developer
```
#1 [VERY HIGH IMPACT]
Dev Environment Automator
One-command setup with all tools
Time Saved: 20-25 hrs/month
[Build This Skill →]
```

### Teacher
```
#1 [VERY HIGH IMPACT]
Lesson Plan Generator
Standards → weekly plans
Time Saved: 8-12 hrs/week
[Build This Skill →]
```

### Consultant
```
#1 [VERY HIGH IMPACT]
Proposal Accelerator
Research → proposal in 2-3 hrs
Time Saved: 40-50 hrs/month
[Build This Skill →]
```

---

## 🔧 Advanced Usage

### Custom Count
```
Analyze my last 200 conversations
```

### Domain-Specific
```
Analyze my [finance/healthcare/development] conversations
```

### Gap Analysis
```
I have skills for X, Y, Z. What am I missing?
```

---

## ❓ Troubleshooting

### Only fetching 60 conversations?
**Fix**: Verify using `n: 40` in ALL 4 calls (not n: 20)

### No recommendations?
**Requirements**:
- Minimum 20-30 conversations
- Some repeated patterns
- Conversation titles/summaries available

---

## 📊 Technical Details

**Analysis Engine**:
- Metadata analysis (titles, timestamps, summaries)
- Pattern detection: frequency, recency, domain clustering
- ROI calculation: time savings automation
- Complexity rating: technical requirements

**Performance**:
- Analysis time: ~30-45 seconds
- Dashboard: Instant React artifact

**Privacy**:
- Analyzes metadata only (not full content)
- No external storage
- All processing in-session

---

## 🎓 Why Only 60 Conversations?

- **Context Efficiency**: Prevents maxing out context window before delivering results
- **Metadata Analysis**: Titles alone provide sufficient pattern detection
- **Fast Performance**: Completes in ~10-15 seconds
- **Recent Focus**: Last 60 conversations capture current work patterns
- **Quality**: Lightweight analysis still produces actionable recommendations

---

## 📦 Memory Integration

**Recommended: Enable chat memory**
1. Profile icon → Settings → Profile
2. Toggle "Chat memory" ON

**Why?**
- Distinguishes ongoing vs completed work
- Avoids temporary project recommendations
- Better personalization

---

## 🏷️ Version

**v4.1.0** - Context-Efficient Release

**Critical Fix**:
- ⚡ **Context window issue SOLVED**: Fetch only 60 conversations (not 160)
- ⚡ **Metadata-only analysis**: Extract titles/timestamps only, discard full content
- ⚡ **Fast completion**: Analysis finishes in ~10-15 seconds within context limits
- ✅ Lightweight pattern detection from titles
- ✅ Complete React dashboard generation

**Previous versions**:
- v4.0.1: Platform clarity (removed ChatGPT)
- v4.0.0: 160-conversation fetch (caused context issues)
- v3.0.0: Optimized fetching

---

## 📌 Key Features

- ⚡ **CONTEXT-EFFICIENT**: Fetches only 60 conversations, completes within limits
- 🎯 **METADATA-ONLY**: Analyzes titles/timestamps, not full content
- 🚀 **FAST**: Completes in ~10-15 seconds
- 🌟 **USER-ADAPTIVE**: Personalizes to YOUR work from title patterns
- 📊 **EVIDENCE-BASED**: Backed by conversation keyword analysis
- ✅ **QUALITY-VERIFIED**: Professional recommendations
- 🔒 **PRIVATE**: Lightweight metadata analysis only
- 🎨 **CLAUDE-NATIVE**: Uses recent_chats tool
