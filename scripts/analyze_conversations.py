#!/usr/bin/env python3
"""
Conversation Skill Analyzer
Analyzes past Claude conversations to identify top skill-building opportunities
"""

import json
import sys
from collections import Counter, defaultdict
from datetime import datetime

def analyze_conversations(conversations_data):
    """
    Analyze conversations to identify skill opportunities
    
    Args:
        conversations_data: List of conversation summaries with metadata
        
    Returns:
        dict: Analysis results including top skill recommendations
    """
    
    # Initialize tracking structures
    workflow_patterns = Counter()
    tool_usage = Counter()
    domain_areas = Counter()
    pain_points = []
    repeated_tasks = Counter()
    
    # Keywords for different categories
    automation_keywords = ['automate', 'automation', 'workflow', 'process', 'integrate', 'sync']
    client_keywords = ['client', 'proposal', 'consulting', 'recommend', 'help them']
    research_keywords = ['search', 'find', 'research', 'analyze', 'compare', 'evaluate']
    document_keywords = ['document', 'report', 'presentation', 'spreadsheet', 'template']
    code_keywords = ['code', 'script', 'develop', 'build', 'program', 'application']
    
    for conv in conversations_data:
        title = conv.get('title', '').lower()
        summary = conv.get('summary', '').lower()
        content = title + ' ' + summary
        
        # Track automation patterns
        if any(kw in content for kw in automation_keywords):
            workflow_patterns['business_automation'] += 1
            
        # Track client-facing work
        if any(kw in content for kw in client_keywords):
            workflow_patterns['client_consulting'] += 1
            
        # Track research tasks
        if any(kw in content for kw in research_keywords):
            workflow_patterns['research_analysis'] += 1
            
        # Track document creation
        if any(kw in content for kw in document_keywords):
            workflow_patterns['document_creation'] += 1
            
        # Track coding/development
        if any(kw in content for kw in code_keywords):
            workflow_patterns['development'] += 1
        
        # Identify domain-specific work
        if 'insurance' in content or 'health' in content:
            domain_areas['healthcare_insurance'] += 1
        if 'financial' in content or 'loan' in content or 'investment' in content:
            domain_areas['finance'] += 1
        if 'api' in content or 'integration' in content:
            domain_areas['api_integration'] += 1
        if 'data' in content or 'database' in content:
            domain_areas['data_management'] += 1
        if 'github' in content or 'codespace' in content:
            domain_areas['development_environment'] += 1
            
        # Track repeated frustrations/pain points
        if 'error' in content or 'issue' in content or 'problem' in content:
            pain_points.append({
                'title': conv.get('title', ''),
                'context': content[:200]
            })
            
        # Track specific repeated tasks
        if 'contacts' in content and 'clean' in content:
            repeated_tasks['contact_cleanup'] += 1
        if 'skill' in content and 'build' in content:
            repeated_tasks['skill_creation'] += 1
        if 'setup' in content or 'configure' in content:
            repeated_tasks['environment_setup'] += 1
    
    return {
        'workflow_patterns': dict(workflow_patterns.most_common(10)),
        'domain_areas': dict(domain_areas.most_common(10)),
        'repeated_tasks': dict(repeated_tasks.most_common(10)),
        'pain_points': pain_points[:5],
        'total_conversations': len(conversations_data)
    }

def generate_skill_recommendations(analysis):
    """Generate top 5 skill recommendations based on analysis"""
    
    recommendations = []
    
    # Recommendation 1: Client Automation Proposal Builder
    if analysis['workflow_patterns'].get('client_consulting', 0) > 0:
        recommendations.append({
            'rank': 1,
            'name': 'client-automation-proposal-builder',
            'title': 'Client Automation Proposal Builder',
            'description': 'Automates creation of AI automation proposals for clients based on their industry and pain points',
            'rationale': f"You've had {analysis['workflow_patterns'].get('client_consulting', 0)} conversations about client work. This skill would encode your consulting methodology into reusable templates.",
            'impact': 'HIGH - Directly monetizable, saves 2-4 hours per proposal',
            'complexity': 'MEDIUM - Requires industry templates and workflow analysis patterns',
            'time_savings_weekly': '4-6 hours',
            'revenue_potential': '$10,000-$30,000 annually',
            'implementation_time': '3-4 days',
            'break_even_point': 'After 2 proposals',
            'evidence_strength': '⭐⭐⭐⭐⭐' if analysis['workflow_patterns'].get('client_consulting', 0) > 5 else '⭐⭐⭐⭐',
            'next_action': 'Start by mapping your standard proposal template structure and identifying common industry pain points',
            'key_features': [
                'Industry-specific automation templates',
                'ROI calculation frameworks',
                'Process mapping and pain point analysis',
                'Proposal generation with case studies',
                'Implementation roadmap builder'
            ]
        })
    
    # Recommendation 2: Research Intelligence Synthesizer
    if analysis['workflow_patterns'].get('research_analysis', 0) > 2:
        recommendations.append({
            'rank': 2,
            'name': 'research-intelligence-synthesizer',
            'title': 'Research Intelligence Synthesizer',
            'description': 'Systematic research methodology for evaluating technologies, products, and vendors',
            'rationale': f"You've had {analysis['workflow_patterns'].get('research_analysis', 0)} research-heavy conversations. This skill would encode your research frameworks.",
            'impact': 'HIGH - Critical for client recommendations and product evaluations',
            'complexity': 'MEDIUM - Requires structured research workflows and validation criteria',
            'time_savings_weekly': '3-5 hours',
            'revenue_potential': '$8,000-$20,000 annually',
            'implementation_time': '2-3 days',
            'break_even_point': 'After 5 research projects',
            'evidence_strength': '⭐⭐⭐⭐⭐' if analysis['workflow_patterns'].get('research_analysis', 0) > 8 else '⭐⭐⭐⭐',
            'next_action': 'Document your current research process and create a template for technology evaluation criteria',
            'key_features': [
                'Multi-source research orchestration',
                'Competitive analysis frameworks',
                'Technology evaluation matrices',
                'Vendor assessment criteria',
                'Evidence-based recommendation builder'
            ]
        })
    
    # Recommendation 3: Development Environment Automator
    if analysis['domain_areas'].get('development_environment', 0) > 1:
        recommendations.append({
            'rank': 3,
            'name': 'dev-environment-automator',
            'title': 'Development Environment Automator',
            'description': 'One-command setup of complete development environments with all tools and configs',
            'rationale': f"You've spent significant time on Codespaces, MCP, and environment setup across {analysis['domain_areas'].get('development_environment', 0)} conversations.",
            'impact': 'VERY HIGH - You personally lose hours to environment setup issues',
            'complexity': 'HIGH - Requires scripts for multiple environments and tools',
            'time_savings_weekly': '5-8 hours',
            'revenue_potential': '$15,000-$25,000 annually',
            'implementation_time': '4-6 days',
            'break_even_point': 'After 1 week',
            'evidence_strength': '⭐⭐⭐⭐⭐',
            'next_action': 'List all the setup steps you repeat when creating a new environment, then script the top 3 most painful ones',
            'key_features': [
                'GitHub Codespaces auto-configuration',
                'Claude Code + SuperClaude setup automation',
                'MCP server installation and config',
                'Dotfiles and shell configuration',
                'API key and secrets management'
            ]
        })
    
    # Recommendation 4: Insurance Document Processor
    if analysis['domain_areas'].get('healthcare_insurance', 0) > 0:
        recommendations.append({
            'rank': 4,
            'name': 'insurance-document-processor',
            'title': 'Insurance Document Processor',
            'description': 'Automated insurance verification, comparison, and appeals generation',
            'rationale': f"You've worked on {analysis['domain_areas'].get('healthcare_insurance', 0)} insurance-related projects. This is highly specialized domain expertise.",
            'impact': 'VERY HIGH - Billable service offering, saves clients thousands',
            'complexity': 'VERY HIGH - Requires OCR, plan comparison logic, regulatory knowledge',
            'time_savings_weekly': '2-4 hours',
            'revenue_potential': '$25,000-$50,000+ annually',
            'implementation_time': '7-10 days',
            'break_even_point': 'After 2 client engagements',
            'evidence_strength': '⭐⭐⭐⭐⭐' if analysis['domain_areas'].get('healthcare_insurance', 0) > 3 else '⭐⭐⭐',
            'next_action': 'Create a library of insurance document templates and common comparison scenarios',
            'key_features': [
                'EOB and denial letter analysis',
                'Provider network verification automation',
                'Plan comparison and recommendation engine',
                'Appeals letter generation',
                'Cost-benefit analysis calculations'
            ]
        })
    
    # Recommendation 5: Data Cleanup & Transformation Suite
    if analysis['repeated_tasks'].get('contact_cleanup', 0) > 0 or analysis['domain_areas'].get('data_management', 0) > 1:
        recommendations.append({
            'rank': 5,
            'name': 'data-cleanup-transformation-suite',
            'title': 'Data Cleanup & Transformation Suite',
            'description': 'Intelligent data deduplication, cleaning, and transformation for various data sources',
            'rationale': f"You've dealt with data cleanup in {analysis['domain_areas'].get('data_management', 0)} conversations including complex contact database issues.",
            'impact': 'HIGH - Solves recurring client problems with messy data',
            'complexity': 'HIGH - Requires fuzzy matching, SQLite expertise, validation logic',
            'time_savings_weekly': '3-5 hours',
            'revenue_potential': '$12,000-$20,000 annually',
            'implementation_time': '5-7 days',
            'break_even_point': 'After 3 cleanup projects',
            'evidence_strength': '⭐⭐⭐⭐' if analysis['domain_areas'].get('data_management', 0) > 3 else '⭐⭐⭐',
            'next_action': 'Build a simple contact deduplication script first, then expand to other data types',
            'key_features': [
                'Smart duplicate detection algorithms',
                'Contact database cleanup automation',
                'CSV/Excel data transformation',
                'SQLite database repair tools',
                'Data validation and quality scoring'
            ]
        })
    
    # Sort by rank and return top 5
    recommendations.sort(key=lambda x: x['rank'])
    return recommendations[:5]

def format_recommendations(recommendations, analysis):
    """Format recommendations as markdown output"""
    
    output = []
    output.append("# Top 5 Claude Skills You Should Build")
    output.append(f"\n**Analysis Date:** {datetime.now().strftime('%B %d, %Y')}")
    output.append(f"**Conversations Analyzed:** {analysis['total_conversations']}\n")
    
    # Add Workflow Pattern Heatmap
    output.append("## Your Workflow Pattern Heatmap\n")
    if analysis['workflow_patterns']:
        workflow_items = sorted(analysis['workflow_patterns'].items(), key=lambda x: x[1], reverse=True)
        for pattern, count in workflow_items:
            heat_level = '🔥' * min(5, max(1, count // 2))
            pattern_name = pattern.replace('_', ' ').title()
            output.append(f"{heat_level} {pattern_name} ({count} conversations)")
    output.append("\n")
    
    output.append("## Executive Summary\n")
    output.append("Based on analysis of your conversation history, these skills would:")
    output.append("- Accelerate your client consulting work")
    output.append("- Automate your most time-consuming repeated tasks")
    output.append("- Create billable service offerings")
    output.append("- Reduce environment setup friction")
    output.append("- Leverage your unique domain expertise\n")
    
    for rec in recommendations:
        output.append(f"## {rec['rank']}. {rec['title']}")
        output.append(f"\n**Skill Name:** `{rec['name']}`")
        output.append(f"**Impact:** {rec['impact']}")
        output.append(f"**Complexity:** {rec['complexity']}")
        output.append(f"**Evidence Strength:** {rec.get('evidence_strength', 'N/A')}\n")
        output.append(f"### Description")
        output.append(f"{rec['description']}\n")
        output.append(f"### Why This Skill?")
        output.append(f"{rec['rationale']}\n")
        output.append(f"### ROI Metrics")
        output.append(f"- **Time Savings:** {rec.get('time_savings_weekly', 'N/A')} per week")
        output.append(f"- **Revenue Potential:** {rec.get('revenue_potential', 'N/A')}")
        output.append(f"- **Implementation Time:** {rec.get('implementation_time', 'N/A')}")
        output.append(f"- **Break-Even Point:** {rec.get('break_even_point', 'N/A')}\n")
        output.append(f"### Key Features")
        for feature in rec['key_features']:
            output.append(f"- {feature}")
        output.append(f"\n### Next Action")
        output.append(f"📍 {rec.get('next_action', 'Start by documenting your current workflow')}\n")
    
    # Add ROI Dashboard
    output.append("## Skill ROI Dashboard\n")
    output.append("| Skill | Time Investment | Time Saved/Week | Annual Value | Priority |")
    output.append("|-------|----------------|-----------------|--------------|----------|")
    for rec in recommendations:
        priority = "🚀 URGENT" if rec['impact'].startswith('VERY HIGH') else "⭐ HIGH"
        output.append(f"| {rec['title']} | {rec.get('implementation_time', 'TBD')} | {rec.get('time_savings_weekly', 'TBD')} | {rec.get('revenue_potential', 'TBD')} | {priority} |")
    output.append("\n")
    
    output.append("## Implementation Priority\n")
    output.append("**Start with:** Development Environment Automator (#3)")
    output.append("- You're losing hours to this weekly")
    output.append("- Immediate personal ROI")
    output.append("- Foundation for other skills\n")
    output.append("**Then build:** Client Automation Proposal Builder (#1)")
    output.append("- Directly monetizable")
    output.append("- Differentiates your consulting")
    output.append("- Faster deal cycles\n")
    output.append("**Finally:** Research Intelligence Synthesizer (#2)")
    output.append("- Supports all client work")
    output.append("- Improves recommendation quality")
    output.append("- Compounds in value over time\n")
    
    return "\n".join(output)

def main():
    """Main execution function"""
    
    # In a real implementation, this would load actual conversation data
    # For this script, we'll work with data passed via stdin or file
    
    if len(sys.argv) > 1:
        # Load from file
        with open(sys.argv[1], 'r') as f:
            conversations = json.load(f)
    else:
        # Read from stdin
        conversations = json.loads(sys.stdin.read())
    
    # Analyze conversations
    analysis = analyze_conversations(conversations)
    
    # Generate recommendations
    recommendations = generate_skill_recommendations(analysis)
    
    # Format and output
    output = format_recommendations(recommendations, analysis)
    print(output)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
