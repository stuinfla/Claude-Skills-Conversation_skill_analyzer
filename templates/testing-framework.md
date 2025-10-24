# Skill Testing Framework

Use this framework to ensure your skill works reliably across different scenarios.

## Testing Philosophy

Good skills are:
1. **Predictable**: Same input → same output
2. **Forgiving**: Handle mistakes gracefully
3. **Fast**: Complete in seconds, not minutes
4. **Clear**: Users know what happened and why

## Test Scenario Template

For each test, document:

```markdown
### Test: [Test Name]

**Category**: [Basic | Advanced | Edge Case | Error Handling]
**Priority**: [Critical | High | Medium | Low]

**Input:**
```
[Exact prompt or command]
```

**Expected Behavior:**
[What should happen]

**Expected Output:**
[What the user should see]

**Actual Result:**
- [ ] Pass
- [ ] Fail (describe what happened)

**Notes:**
[Any observations or improvements needed]
```

## Core Test Categories

### Category 1: Basic Functionality

These tests verify the skill does what it claims to do.

#### Test 1.1: Minimum Viable Input
- **Purpose**: Can the skill work with the simplest possible input?
- **Example**: If skill needs a topic, test with just one word
- **Success**: Skill completes without errors

#### Test 1.2: Standard Use Case
- **Purpose**: Does it handle the most common scenario well?
- **Example**: Test with a typical, realistic input
- **Success**: Output is accurate, complete, and well-formatted

#### Test 1.3: Complex But Valid Input
- **Purpose**: Can it handle sophisticated requests?
- **Example**: Multiple parameters, long inputs, nested requirements
- **Success**: Skill handles complexity without degradation

### Category 2: Edge Cases

These tests find breaking points and unusual scenarios.

#### Test 2.1: Empty/Missing Input
- **Purpose**: What happens if user forgets to provide something?
- **Example**: Trigger skill without required information
- **Success**: Helpful error message, asks for missing info

#### Test 2.2: Extremely Large Input
- **Purpose**: Does it handle volume?
- **Example**: Maximum reasonable data size
- **Success**: Either processes successfully or fails gracefully with guidance

#### Test 2.3: Invalid/Malformed Input
- **Purpose**: Can it detect nonsense?
- **Example**: Wrong data types, impossible requests
- **Success**: Identifies issue and explains what's wrong

#### Test 2.4: Ambiguous Input
- **Purpose**: How does it handle unclear requests?
- **Example**: Vague or multi-interpretable input
- **Success**: Either asks clarifying questions or makes reasonable assumptions

### Category 3: Output Quality

These tests verify the skill produces valuable results.

#### Test 3.1: Formatting Consistency
- **Purpose**: Is output always structured the same way?
- **Example**: Run same test 3 times
- **Success**: Format is consistent across runs

#### Test 3.2: Completeness
- **Purpose**: Does output answer the full question?
- **Example**: Review if all requested elements are present
- **Success**: Nothing important is missing

#### Test 3.3: Scannability
- **Purpose**: Can user quickly find what they need?
- **Example**: Show output to someone unfamiliar
- **Success**: They can extract key info in 10 seconds

#### Test 3.4: Actionability
- **Purpose**: Can user immediately act on the output?
- **Example**: Follow the output as instructions
- **Success**: Next steps are clear and executable

### Category 4: Performance

These tests ensure the skill is efficient.

#### Test 4.1: Response Time
- **Purpose**: Is it fast enough?
- **Example**: Time from trigger to completion
- **Success**: 
  - Simple queries: < 10 seconds
  - Complex queries: < 60 seconds
  - Very complex: < 3 minutes

#### Test 4.2: Tool Efficiency
- **Purpose**: Does it minimize tool calls?
- **Example**: Count number of tool invocations
- **Success**: Uses minimum necessary tools

#### Test 4.3: Resource Usage
- **Purpose**: Does it handle resources well?
- **Example**: Check file sizes, memory usage
- **Success**: No unnecessary bloat

### Category 5: Error Handling

These tests verify graceful failures.

#### Test 5.1: Tool Failure Recovery
- **Purpose**: What if a tool fails?
- **Example**: Simulate tool unavailability
- **Success**: Provides workaround or clear error message

#### Test 5.2: Timeout Handling
- **Purpose**: What if something takes too long?
- **Example**: Test with slow operations
- **Success**: Times out gracefully with partial results

#### Test 5.3: Data Validation
- **Purpose**: Does it catch bad data before processing?
- **Example**: Feed in data that looks right but is wrong
- **Success**: Validates and rejects with explanation

## Test Execution Checklist

Before marking your skill as "ready to use":

### Pre-Launch Testing
- [ ] All Critical priority tests pass
- [ ] All High priority tests pass
- [ ] At least 75% of Medium priority tests pass
- [ ] Documented any Low priority test failures with workarounds

### User Experience Testing
- [ ] Fresh user can use skill with Quick Start prompt only
- [ ] Error messages are helpful (tested with someone else)
- [ ] Output format is professional and clear
- [ ] Examples in SKILL.md actually work

### Edge Case Coverage
- [ ] Tested with no input
- [ ] Tested with minimal input
- [ ] Tested with maximum input
- [ ] Tested with invalid input
- [ ] Tested with ambiguous input

### Documentation Verification
- [ ] Quick Start prompts are copy-pasteable
- [ ] All examples have been actually executed
- [ ] Limitations section lists real limitations found in testing
- [ ] Troubleshooting addresses actual issues encountered

## Sample Test Suite

Here's a complete test suite for a hypothetical "research-synthesizer" skill:

### Test Suite: Research Synthesizer v1.0

#### Test RS-1: Basic Research Query (CRITICAL)
**Input:**
```
Research and synthesize information about MCP servers
```
**Expected**: 3-5 sources, summary, key findings
**Result**: ✅ Pass - Returned 4 sources with comprehensive summary

#### Test RS-2: Multi-Topic Research (HIGH)
**Input:**
```
Compare MCP servers vs traditional APIs for enterprise integration
```
**Expected**: Comparative analysis with pros/cons
**Result**: ✅ Pass - Clear comparison table generated

#### Test RS-3: Empty Query (CRITICAL)
**Input:**
```
Research and synthesize information
```
**Expected**: Asks what topic to research
**Result**: ✅ Pass - Politely requested topic specification

#### Test RS-4: Maximum Depth Research (MEDIUM)
**Input:**
```
Deep dive research on MCP servers including technical architecture, use cases, vendor landscape, and future trends
```
**Expected**: Comprehensive multi-section report
**Result**: ✅ Pass - Generated 8-section report, took 45 seconds

#### Test RS-5: Obscure Topic (HIGH)
**Input:**
```
Research [extremely niche technical topic]
```
**Expected**: Either finds info or clearly states limitations
**Result**: ✅ Pass - Found limited info, noted gaps in knowledge

#### Test RS-6: Response Time (MEDIUM)
**Input**: Standard research query
**Expected**: < 30 seconds for basic query
**Result**: ✅ Pass - Completed in 18 seconds

## Iteration Testing

After initial launch, test weekly for:

### Week 1: Real-World Usage
- [ ] Track which features get used most
- [ ] Note any user confusion patterns
- [ ] Identify missing capabilities users request

### Month 1: Stability
- [ ] Re-run all critical tests
- [ ] Check if any edge cases emerged
- [ ] Verify performance hasn't degraded

### Quarter 1: Enhancement
- [ ] Test new features added
- [ ] Verify backward compatibility
- [ ] Update test suite with new scenarios

## Quality Metrics

Aim for:
- **Critical tests**: 100% pass rate
- **High priority tests**: 95%+ pass rate
- **Medium priority tests**: 80%+ pass rate
- **User satisfaction**: 4.5/5+ (gather feedback)
- **Repeat usage**: If you use it weekly, it's valuable

---

## Red Flags That Need Fixing

Stop and improve if you see:
- ❌ Users have to read the full docs to use it
- ❌ Output format is inconsistent
- ❌ More than 30% of uses require follow-up clarification
- ❌ You built it but don't use it yourself
- ❌ Fails on reasonable inputs
- ❌ Error messages are confusing or unhelpful

## Green Lights for Launch

Ship when you have:
- ✅ Quick Start prompt works every time
- ✅ Common use case completes in < 30 seconds
- ✅ Error messages help users fix issues
- ✅ You've used it successfully 5+ times yourself
- ✅ Output is immediately actionable
- ✅ Edge cases fail gracefully with helpful guidance

---

**Remember**: You can't test everything. Focus on critical paths first, then expand. Ship, learn, iterate.
