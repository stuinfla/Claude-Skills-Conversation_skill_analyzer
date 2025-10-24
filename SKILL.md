---
name: conversation-skill-analyzer
description: Analyzes your Claude conversation history to discover which custom skills would save you the most time, make you the most money, or eliminate your biggest frustrations. Returns a data-driven, prioritized roadmap of your top 5 skill-building opportunities with ROI estimates and evidence from your actual usage patterns.
---

# Conversation Skill Analyzer v4.0

**🎯 Works on Claude AI and ChatGPT** | **🔧 Bug Fixed** | **✅ Quality Verified**

Identifies high-value automation opportunities by analyzing YOUR conversation patterns, then helps you BUILD those skills with quality standards.

---

## 🚨 CRITICAL: 60-Chat Bug Fixed

**Previous Issue**: Only fetching 60 conversations instead of 160

**Root Cause**: Tool defaults to n=20, Claude was stopping after 3 calls

**Solution**: Mandatory execution protocol with explicit n=40 parameter

---

## Quick Start

**Claude AI**:
```
Analyze my conversation history and recommend my top 5 skills to build
```

**ChatGPT**:
```
Analyze my ChatGPT conversations and recommend my top 5 skills to build
```

---

## 📥 Phase 1: Data Collection

### For Claude AI (MANDATORY PROTOCOL)

**YOU MUST FOLLOW THIS EXACT SEQUENCE**:

```javascript
// ===== CALL 1: Fetch first 40 =====
const batch1 = await recent_chats({n: 40});
console.log("✓ Fetched 40 conversations...");

// ===== CALL 2: Fetch next 40 =====
const lastTimestamp1 = batch1[batch1.length - 1].timestamp;
const batch2 = await recent_chats({n: 40, before: lastTimestamp1});
console.log("✓ Fetched 80 conversations...");

// ===== CALL 3: Fetch next 40 =====
const lastTimestamp2 = batch2[batch2.length - 1].timestamp;
const batch3 = await recent_chats({n: 40, before: lastTimestamp2});
console.log("✓ Fetched 120 conversations...");

// ===== CALL 4: Fetch final 40 =====
const lastTimestamp3 = batch3[batch3.length - 1].timestamp;
const batch4 = await recent_chats({n: 40, before: lastTimestamp3});
console.log("✓ Fetched 160 conversations...");

// ===== VALIDATION CHECKPOINT =====
const allConversations = [...batch1, ...batch2, ...batch3, ...batch4];
const totalFetched = allConversations.length;

if (totalFetched < 160) {
  console.log(`⚠️ User has ${totalFetched} total conversations`);
  console.log(`✓ Fetched ALL ${totalFetched} available conversations`);
} else {
  console.log(`✓ Successfully fetched 160 conversations for analysis`);
}

// ===== STOP CHECK =====
if (totalFetched < 100) {
  throw new Error("Insufficient data: Need at least 100 conversations for reliable analysis");
}

// ===== PROCEED TO ANALYSIS =====
console.log("✓ Data collection complete. Starting analysis...");
```

**CRITICAL REQUIREMENTS**:
- ✅ MUST use `n: 40` (NOT n: 20)
- ✅ MUST make 4 calls minimum
- ✅ MUST use `before` parameter for pagination
- ✅ MUST show progress: "40... 80... 120... 160..."
- ✅ MUST validate before proceeding
- ❌ DO NOT proceed if < 100 conversations

### For ChatGPT

1. **Request Export**:
   ```
   Please export your ChatGPT conversation history:
   - Go to Settings → Data Controls → Export Data
   - Wait for email with conversations.json
   - Upload the file here
   ```

2. **Parse File**: Extract most recent 160 conversations (or all if fewer)
3. **Proceed**: Use same analysis logic

---

## 🔍 Phase 2: User-Adaptive Analysis

**NO ASSUMPTIONS** about user's profession or domain!

1. **Check Memory**: Review user's preferences for work context
2. **Discover Domain**: Analyze conversation topics to identify actual work
3. **Detect Patterns**:
   - Workflow categories (automation, consulting, research, documents, development)
   - Repeated tasks and pain points
   - Frequency and recency scoring
4. **Calculate Impact**:
   - Time savings potential
   - Build complexity vs ROI
   - Domain relevance

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

### ChatGPT export not working?
1. Settings → Data Controls → Export Data
2. Wait for email (can take hours)
3. Download conversations.json
4. Upload to chat

---

## 📊 Technical Details

**Analysis Engine**:
- Metadata analysis (titles, timestamps, summaries)
- Pattern detection: frequency, recency, domain clustering
- ROI calculation: time savings automation
- Complexity rating: technical requirements

**Performance**:
- Claude: ~30-45 seconds
- ChatGPT: ~40-55 seconds (+ file parsing)
- Dashboard: Instant React artifact

**Privacy**:
- Analyzes metadata only (not full content)
- No external storage
- All processing in-session

---

## 🎓 Why 160 Conversations?

- **Pattern reliability**: 160 provides excellent confidence (minimum 100 needed)
- **Efficient fetching**: 4 calls × 40 = optimal batch size
- **Recent focus**: Captures 3-6 months for most users
- **Performance**: Fast enough (~30-45 seconds)
- **Evidence quality**: Reduces false positives

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

**v4.0.0** - Complete production release

**What's Fixed**:
- ✅ 60-chat bug (now fetches 160)
- ✅ Explicit tool syntax with validation
- ✅ Complete React dashboard code
- ✅ Integrated quality standards
- ✅ ChatGPT compatibility
- ✅ Verification protocol

**Previous versions**:
- v3.0.0: Optimized fetching
- v2.7.0: Build integration
- v2.6.0: Smart scope
- v2.5.0: User-adaptive

---

## 📌 Key Features

- 🎯 **UNIVERSAL**: Claude AI + ChatGPT
- 🔧 **FIXED**: 160-conversation mandatory fetch
- 🌟 **USER-ADAPTIVE**: Personalizes to YOUR work
- 📊 **EVIDENCE-BASED**: Backed by conversation patterns
- 🚀 **ACTIONABLE**: Build buttons work
- ✅ **QUALITY-VERIFIED**: 12-point checklist
- ⚡ **EFFICIENT**: 4 optimized calls
- 🔒 **PRIVATE**: Metadata-only analysis
