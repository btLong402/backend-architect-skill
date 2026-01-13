#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Backend Architect Skill Search - CLI for backend architecture knowledge base
Usage: python search.py "<query>" [--domain <domain>] [--stack <stack>] [--max-results 3]

Domains: architecture, database, security, product, language, api, naming, error, platform
Stacks: go, python, node, java, dotnet, rust
"""

import sys
import io

# Fix UnicodeEncodeError on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import argparse
from core import CSV_CONFIG, AVAILABLE_STACKS, AVAILABLE_DOMAINS, MAX_RESULTS, search, search_stack


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

    args = parser.parse_args()

    # Stack search takes priority
    if args.stack:
        result = search_stack(args.query, args.stack, args.max_results)
    else:
        result = search(args.query, args.domain, args.max_results)

    if args.json:
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_output(result))
