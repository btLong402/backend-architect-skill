#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Backend Architect Skill Search - CLI for backend architecture knowledge base
Usage: python search.py "<query>" [--domain <domain>] [--stack <stack>] [--max-results 3]
       python search.py "<query>" --architecture-system [-p "Project Name"]
       python search.py "<query>" --architecture-system --persist [-p "Project Name"] [--service "payment"]

Domains: architecture, database, security, product, language, api, naming, error, platform, backend-reasoning
Stacks: go, python, node, java, dotnet, rust

Architecture System Generation (NEW):
  --architecture-system    Generate complete backend architecture recommendation
  --persist                Save to architecture-system/MASTER.md
  --service                Create service-specific override file
"""

import sys
import io

# Fix UnicodeEncodeError on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import argparse
from core import CSV_CONFIG, AVAILABLE_STACKS, AVAILABLE_DOMAINS, MAX_RESULTS, search, search_stack
from architecture_system import generate_architecture_system, persist_architecture_system


def format_output(result):
    """Format results for AI consumption (token-optimized)"""
    if "error" in result:
        return f"Error: {result['error']}"

    output = []
    if result.get("stack"):
        output.append(f"## Backend Architect Stack Guidelines")
        output.append(f"**Stack:** {result['stack']} | **Query:** {result['query']}")
    else:
        output.append(f"## Backend Architect Search Results")
        output.append(f"**Domain:** {result['domain']} | **Query:** {result['query']}")
    output.append(f"**Source:** {result['file']} | **Found:** {result['count']} results\n")

    for i, row in enumerate(result['results'], 1):
        output.append(f"### Result {i}")
        for key, value in row.items():
            value_str = str(value)
            if len(value_str) > 400:
                value_str = value_str[:400] + "..."
            output.append(f"- **{key}:** {value_str}")
        output.append("")

    return "\n".join(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backend Architect Skill Search")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--domain", "-d", choices=AVAILABLE_DOMAINS, help="Search domain")
    parser.add_argument("--stack", "-s", choices=AVAILABLE_STACKS, help="Stack-specific search")
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS, help="Max results (default: 3)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    # Architecture system generation
    parser.add_argument("--architecture-system", "-as", action="store_true",
                        help="Generate complete backend architecture recommendation")
    parser.add_argument("--project-name", "-p", type=str, default=None,
                        help="Project name for architecture system output")
    parser.add_argument("--format", "-f", choices=["ascii", "markdown"],
                        default="ascii", help="Output format for architecture system")
    
    # Persistence (Master + Overrides pattern)
    parser.add_argument("--persist", action="store_true",
                        help="Save architecture system to architecture-system/MASTER.md")
    parser.add_argument("--service", type=str, default=None,
                        help="Create service-specific override file in architecture-system/services/")
    parser.add_argument("--output-dir", "-o", type=str, default=None,
                        help="Output directory for persisted files")

    args = parser.parse_args()

    # Architecture system takes priority
    if args.architecture_system:
        result = generate_architecture_system(
            args.query,
            args.project_name,
            args.format,
            persist=args.persist,
            service=args.service,
            output_dir=args.output_dir
        )
        print(result)
        
        # Print persistence confirmation
        if args.persist:
            project_slug = args.project_name.lower().replace(' ', '-') if args.project_name else "default"
            print("\n" + "=" * 60)
            print(f"✅ Architecture system persisted to architecture-system/{project_slug}/")
            print(f"   📄 architecture-system/{project_slug}/MASTER.md (Global Source of Truth)")
            if args.service:
                service_filename = args.service.lower().replace(' ', '-')
                print(f"   📄 architecture-system/{project_slug}/services/{service_filename}.md (Service Overrides)")
            print("")
            print(f"📖 Usage: When building a service, check architecture-system/{project_slug}/services/[service].md first.")
            print(f"   If exists, its rules override MASTER.md. Otherwise, use MASTER.md.")
            print("=" * 60)
    
    # Stack search
    elif args.stack:
        result = search_stack(args.query, args.stack, args.max_results)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
    
    # Domain search
    else:
        result = search(args.query, args.domain, args.max_results)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
