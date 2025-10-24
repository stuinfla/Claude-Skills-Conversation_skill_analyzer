# Analysis Methodology Reference

This document explains how the Conversation Skill Analyzer evaluates conversation patterns and generates recommendations.

## Pattern Recognition Categories

### Workflow Patterns

The analyzer identifies five primary workflow categories:

1. **Business Automation** (Keywords: automate, automation, workflow, process, integrate, sync)
   - Indicates repeated manual processes that could be automated
   - High frequency suggests systematic workflow optimization opportunities
   - Monetization potential: Package as consulting service

2. **Client Consulting** (Keywords: client, proposal, consulting, recommend, help them)
   - Shows client-facing work that could be templated
   - Frequency indicates consulting volume and proposal needs
   - Monetization potential: Proposal automation tools

3. **Research & Analysis** (Keywords: search, find, research, analyze, compare, evaluate)
   - Reveals systematic research methodologies
   - Pattern frequency suggests need for research frameworks
   - Value: Improves recommendation quality and speed

4. **Document Creation** (Keywords: document, report, presentation, spreadsheet, template)
   - Shows document generation workload
   - High frequency indicates template/automation opportunities
   - Quick win potential: Template libraries

5. **Development** (Keywords: code, script, develop, build, program, application)
   - Reveals coding and development work
   - Environment setup pain points emerge from this pattern
   - Value: Development workflow optimization

### Domain Areas

The analyzer tracks expertise concentration in:

- **Healthcare & Insurance**: Medical, insurance, benefits, healthcare
- **Finance**: Financial services, loans, investments, banking
- **API Integration**: Technical integrations, API work, systems
- **Data Management**: Database work, data cleanup, ETL
- **Development Environment**: Setup, configuration, tooling

### Pain Point Detection

Identifies friction through:
- Error mentions (implementation struggles)
- Issue keywords (problematic workflows)
- Problem patterns (recurring challenges)
- Frustration indicators (repeated attempts)

### Repeated Task Tracking

Monitors frequency of:
- Specific named tasks (e.g., "contact cleanup")
- Configuration activities (environment setup)
- Creation activities (skill building, document creation)

## Recommendation Scoring

### Impact Assessment

**VERY HIGH Impact**:
- Saves 5+ hours weekly
- Directly monetizable as service offering
- Solves critical personal pain point
- Benefits multiple client engagements

**HIGH Impact**:
- Saves 2-4 hours weekly
- Improves work quality significantly
- Applicable across multiple domains
- Creates competitive differentiation

**MEDIUM Impact**:
- Saves 1-2 hours weekly
- Focused on specific domain
- Improves efficiency incrementally
- Nice-to-have improvement

### Complexity Rating

**VERY HIGH Complexity**:
- Requires multiple specialized technologies
- Needs extensive domain knowledge
- Involves complex integration points
- Significant testing requirements
- Example: Insurance document processor with OCR, NLP, regulatory rules

**HIGH Complexity**:
- Multiple technology components
- Some specialized expertise needed
- Several integration points
- Moderate testing needs
- Example: Data cleanup suite with fuzzy matching, SQLite, validation

**MEDIUM Complexity**:
- Standard technology stack
- Well-understood domain
- Limited integration needs
- Standard testing approaches
- Example: Proposal template builder with document generation

**LOW Complexity**:
- Simple technology requirements
- Common patterns and approaches
- Minimal integration
- Straightforward testing
- Example: Markdown template library

## Priority Algorithm

Skills are prioritized by:

1. **Immediate Pain Relief**: Skills solving active frustrations
2. **Monetization Potential**: Billable service opportunities
3. **Frequency of Use**: How often the skill would be used
4. **Strategic Value**: Long-term compounding benefits
5. **Implementation Feasibility**: Effort vs. benefit ratio

### Quick Wins

Skills that are:
- Medium complexity or lower
- Very high or high impact
- Solve personal pain points
- Can be built in 1-2 days

### Strategic Investments

Skills that are:
- High complexity
- Very high impact
- Create competitive moats
- Compound in value over time
- May take 1-2 weeks to build

## Evidence Thresholds

Recommendations require:
- Minimum 2 conversations in category (shows pattern)
- At least 1 pain point indicator (shows need)
- Clear workflow definition (skill is actionable)
- Distinct value proposition (not redundant)

## Recommendation Template

Each recommendation includes:

1. **Skill Name**: Descriptive, hyphenated identifier
2. **Title**: Human-readable name
3. **Description**: One-sentence value proposition
4. **Rationale**: Evidence from conversation analysis
5. **Impact Rating**: VERY HIGH, HIGH, or MEDIUM
6. **Complexity Rating**: Based on implementation requirements
7. **Key Features**: 5-7 core capabilities to implement
8. **Evidence Metrics**: Specific conversation counts and patterns

## Update Frequency

Re-run analysis:
- After 20+ new conversations
- When shifting to new domain area
- Quarterly for ongoing skill roadmap planning
- When questioning skill investment priorities

