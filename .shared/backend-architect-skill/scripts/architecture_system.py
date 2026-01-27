#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Backend Architect System Generator - Aggregates search results and applies reasoning
to generate comprehensive backend architecture recommendations.

Usage:
    from architecture_system import generate_architecture_system
    result = generate_architecture_system("e-commerce platform", "MyProject")
    
    # With persistence (Master + Overrides pattern)
    result = generate_architecture_system("e-commerce platform", "MyProject", persist=True)
    result = generate_architecture_system("e-commerce platform", "MyProject", persist=True, service="payment")
"""

import csv
import json
import os
from datetime import datetime
from pathlib import Path
from core import search, DATA_DIR


# ============ CONFIGURATION ============
REASONING_FILE = "backend-reasoning.csv"

SEARCH_CONFIG = {
    "product": {"max_results": 1},
    "architecture": {"max_results": 3},
    "database": {"max_results": 3},
    "api": {"max_results": 2},
    "security": {"max_results": 3},
    "platform": {"max_results": 2}
}


# ============ ARCHITECTURE SYSTEM GENERATOR ============
class ArchitectureSystemGenerator:
    """Generates backend architecture recommendations from aggregated searches."""

    def __init__(self):
        self.reasoning_data = self._load_reasoning()

    def _load_reasoning(self) -> list:
        """Load reasoning rules from CSV."""
        filepath = DATA_DIR / REASONING_FILE
        if not filepath.exists():
            return []
        with open(filepath, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def _multi_domain_search(self, query: str, arch_priority: list = None) -> dict:
        """Execute searches across multiple domains."""
        results = {}
        for domain, config in SEARCH_CONFIG.items():
            if domain == "architecture" and arch_priority:
                priority_query = " ".join(arch_priority[:2]) if arch_priority else query
                combined_query = f"{query} {priority_query}"
                results[domain] = search(combined_query, domain, config["max_results"])
            else:
                results[domain] = search(query, domain, config["max_results"])
        return results

    def _find_reasoning_rule(self, category: str) -> dict:
        """Find matching reasoning rule for a product category."""
        category_lower = category.lower()

        # Try exact match first
        for rule in self.reasoning_data:
            if rule.get("Product_Category", "").lower() == category_lower:
                return rule

        # Try partial match
        for rule in self.reasoning_data:
            prod_cat = rule.get("Product_Category", "").lower()
            if prod_cat in category_lower or category_lower in prod_cat:
                return rule

        # Try keyword match
        for rule in self.reasoning_data:
            prod_cat = rule.get("Product_Category", "").lower()
            keywords = prod_cat.replace("/", " ").replace("-", " ").split()
            if any(kw in category_lower for kw in keywords):
                return rule

        return {}

    def _apply_reasoning(self, category: str) -> dict:
        """Apply reasoning rules to get architecture recommendations."""
        rule = self._find_reasoning_rule(category)

        if not rule:
            return {
                "recommended_architecture": "arch_modular_monolith",
                "stack_priority": ["Node", "TypeScript", "Go"],
                "database_priority": ["PostgreSQL", "Redis"],
                "api_pattern": "REST + GraphQL",
                "key_components": "API Gateway | Service Layer | Repository",
                "anti_patterns": "",
                "decision_rules": {},
                "severity": "MEDIUM"
            }

        # Parse decision rules JSON
        decision_rules = {}
        try:
            decision_rules = json.loads(rule.get("Decision_Rules", "{}"))
        except json.JSONDecodeError:
            pass

        return {
            "recommended_architecture": rule.get("Recommended_Architecture", ""),
            "stack_priority": [s.strip() for s in rule.get("Stack_Priority", "").split("+")],
            "database_priority": [d.strip() for d in rule.get("Database_Priority", "").split("+")],
            "api_pattern": rule.get("API_Pattern", ""),
            "key_components": rule.get("Key_Components", ""),
            "anti_patterns": rule.get("Anti_Patterns", ""),
            "decision_rules": decision_rules,
            "severity": rule.get("Severity", "MEDIUM")
        }

    def _extract_results(self, search_result: dict) -> list:
        """Extract results list from search result dict."""
        return search_result.get("results", [])

    def generate(self, query: str, project_name: str = None) -> dict:
        """Generate complete backend architecture recommendation."""
        # Step 1: Search product to get category
        product_result = search(query, "product", 1)
        product_results = product_result.get("results", [])
        category = "General"
        product_info = {}
        if product_results:
            product_info = product_results[0]
            category = product_info.get("name", "General")

        # Step 2: Get reasoning rules for this category
        reasoning = self._apply_reasoning(category)

        # Step 3: Multi-domain search
        search_results = self._multi_domain_search(query)
        search_results["product"] = product_result

        # Step 4: Extract results from each domain
        arch_results = self._extract_results(search_results.get("architecture", {}))
        db_results = self._extract_results(search_results.get("database", {}))
        api_results = self._extract_results(search_results.get("api", {}))
        security_results = self._extract_results(search_results.get("security", {}))
        platform_results = self._extract_results(search_results.get("platform", {}))

        # Get best matches
        best_arch = arch_results[0] if arch_results else {}
        best_db = db_results[0] if db_results else {}
        best_api = api_results[0] if api_results else {}

        return {
            "project_name": project_name or query.upper(),
            "category": category,
            "product_info": {
                "core_entities": product_info.get("core_entities", ""),
                "critical_features": product_info.get("critical_features", ""),
                "data_consistency": product_info.get("data_consistency", ""),
                "performance_bottleneck": product_info.get("performance_bottleneck", ""),
                "standard_2025": product_info.get("2025_standard", "")
            },
            "architecture": {
                "recommended": reasoning.get("recommended_architecture", ""),
                "name": best_arch.get("name", "Modular Monolith"),
                "description": best_arch.get("description", ""),
                "use_case": best_arch.get("use_case", ""),
                "trade_offs": best_arch.get("trade_offs", ""),
                "key_components": reasoning.get("key_components", ""),
                "ref_pattern": best_arch.get("ref_pattern", "")
            },
            "stack": {
                "priority": reasoning.get("stack_priority", []),
                "languages": [r.get("name", "") for r in self._extract_results(search(query, "language", 2))]
            },
            "database": {
                "priority": reasoning.get("database_priority", []),
                "primary": best_db.get("Technology", "PostgreSQL"),
                "category": best_db.get("Category", ""),
                "key_feature": best_db.get("Key Feature 2025", ""),
                "use_case": best_db.get("Use Case Primary", ""),
                "consistency": best_db.get("Consistency Model", "")
            },
            "api": {
                "pattern": reasoning.get("api_pattern", ""),
                "name": best_api.get("Pattern_Name", "REST"),
                "use_case": best_api.get("Primary_Use_Case", ""),
                "transport": best_api.get("Transport_Protocol", ""),
                "data_format": best_api.get("Data_Format", ""),
                "strength": best_api.get("Key_Strength", ""),
                "trend_2025": best_api.get("Trend_2025_Status", "")
            },
            "security": {
                "considerations": [s.get("name", "") for s in security_results[:3]],
                "checklist": [s.get("checklist_item", "") for s in security_results[:3]],
                "tooling": [s.get("tooling_ref", "") for s in security_results[:3]]
            },
            "platform": {
                "tools": [p.get("Tool", "") for p in platform_results[:3]],
                "categories": list(set([p.get("Category", "") for p in platform_results[:3]]))
            },
            "anti_patterns": reasoning.get("anti_patterns", ""),
            "decision_rules": reasoning.get("decision_rules", {}),
            "severity": reasoning.get("severity", "MEDIUM")
        }


# ============ OUTPUT FORMATTERS ============
BOX_WIDTH = 95

def format_ascii_box(arch_system: dict) -> str:
    """Format architecture system as ASCII box."""
    project = arch_system.get("project_name", "PROJECT")
    category = arch_system.get("category", "")
    product_info = arch_system.get("product_info", {})
    architecture = arch_system.get("architecture", {})
    stack = arch_system.get("stack", {})
    database = arch_system.get("database", {})
    api = arch_system.get("api", {})
    security = arch_system.get("security", {})
    platform = arch_system.get("platform", {})
    anti_patterns = arch_system.get("anti_patterns", "")

    def wrap_text(text: str, prefix: str, width: int) -> list:
        """Wrap long text into multiple lines."""
        if not text:
            return []
        words = text.split()
        lines = []
        current_line = prefix
        for word in words:
            if len(current_line) + len(word) + 1 <= width - 2:
                current_line += (" " if current_line != prefix else "") + word
            else:
                if current_line != prefix:
                    lines.append(current_line)
                current_line = prefix + word
        if current_line != prefix:
            lines.append(current_line)
        return lines

    lines = []
    w = BOX_WIDTH - 1

    lines.append("+" + "=" * w + "+")
    lines.append(f"|  TARGET: {project} - BACKEND ARCHITECTURE SYSTEM".ljust(BOX_WIDTH) + "|")
    lines.append(f"|  Category: {category}".ljust(BOX_WIDTH) + "|")
    lines.append("+" + "=" * w + "+")
    lines.append("|" + " " * BOX_WIDTH + "|")

    # Product Info Section
    if product_info.get("core_entities"):
        lines.append("|  DOMAIN MODEL:".ljust(BOX_WIDTH) + "|")
        entities = product_info.get("core_entities", "")[:70]
        lines.append(f"|     Entities: {entities}".ljust(BOX_WIDTH) + "|")
        if product_info.get("critical_features"):
            for line in wrap_text(f"Critical: {product_info.get('critical_features', '')}", "|     ", BOX_WIDTH):
                lines.append(line.ljust(BOX_WIDTH) + "|")
        if product_info.get("data_consistency"):
            lines.append(f"|     Consistency: {product_info.get('data_consistency', '')}".ljust(BOX_WIDTH) + "|")
        if product_info.get("performance_bottleneck"):
            for line in wrap_text(f"Bottleneck: {product_info.get('performance_bottleneck', '')}", "|     ", BOX_WIDTH):
                lines.append(line.ljust(BOX_WIDTH) + "|")
        lines.append("|" + " " * BOX_WIDTH + "|")

    # Architecture Section
    lines.append(f"|  ARCHITECTURE: {architecture.get('name', '')}".ljust(BOX_WIDTH) + "|")
    lines.append(f"|     ID: {architecture.get('recommended', '')}".ljust(BOX_WIDTH) + "|")
    if architecture.get("description"):
        for line in wrap_text(architecture.get("description", "")[:200], "|     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH) + "|")
    if architecture.get("trade_offs"):
        for line in wrap_text(f"Trade-offs: {architecture.get('trade_offs', '')[:150]}", "|     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH) + "|")
    if architecture.get("key_components"):
        lines.append(f"|     Components: {architecture.get('key_components', '')[:60]}".ljust(BOX_WIDTH) + "|")
    if architecture.get("ref_pattern"):
        lines.append(f"|     Patterns: {architecture.get('ref_pattern', '')}".ljust(BOX_WIDTH) + "|")
    lines.append("|" + " " * BOX_WIDTH + "|")

    # Stack Section
    lines.append("|  RECOMMENDED STACK:".ljust(BOX_WIDTH) + "|")
    stack_str = " + ".join(filter(None, stack.get("priority", [])))[:70]
    lines.append(f"|     Primary: {stack_str}".ljust(BOX_WIDTH) + "|")
    if stack.get("languages"):
        langs = ", ".join(filter(None, stack.get("languages", [])))[:60]
        lines.append(f"|     Languages: {langs}".ljust(BOX_WIDTH) + "|")
    lines.append("|" + " " * BOX_WIDTH + "|")

    # Database Section
    lines.append("|  DATABASE STRATEGY:".ljust(BOX_WIDTH) + "|")
    db_priority = " + ".join(filter(None, database.get("priority", [])))[:60]
    lines.append(f"|     Priority: {db_priority}".ljust(BOX_WIDTH) + "|")
    lines.append(f"|     Primary: {database.get('primary', '')} ({database.get('category', '')})".ljust(BOX_WIDTH) + "|")
    if database.get("key_feature"):
        lines.append(f"|     Key Feature: {database.get('key_feature', '')[:60]}".ljust(BOX_WIDTH) + "|")
    if database.get("consistency"):
        lines.append(f"|     Consistency: {database.get('consistency', '')}".ljust(BOX_WIDTH) + "|")
    lines.append("|" + " " * BOX_WIDTH + "|")

    # API Section
    lines.append("|  API PATTERN:".ljust(BOX_WIDTH) + "|")
    lines.append(f"|     Pattern: {api.get('pattern', '')}".ljust(BOX_WIDTH) + "|")
    lines.append(f"|     Primary: {api.get('name', '')} ({api.get('transport', '')})".ljust(BOX_WIDTH) + "|")
    if api.get("strength"):
        lines.append(f"|     Strength: {api.get('strength', '')[:60]}".ljust(BOX_WIDTH) + "|")
    if api.get("trend_2025"):
        lines.append(f"|     2025 Trend: {api.get('trend_2025', '')}".ljust(BOX_WIDTH) + "|")
    lines.append("|" + " " * BOX_WIDTH + "|")

    # Security Section
    if security.get("considerations"):
        lines.append("|  SECURITY CONSIDERATIONS:".ljust(BOX_WIDTH) + "|")
        for i, sec in enumerate(security.get("considerations", [])[:3], 1):
            if sec:
                lines.append(f"|     {i}. {sec[:70]}".ljust(BOX_WIDTH) + "|")
        lines.append("|" + " " * BOX_WIDTH + "|")

    # Platform Section
    if platform.get("tools"):
        lines.append("|  PLATFORM & DEVOPS:".ljust(BOX_WIDTH) + "|")
        tools = ", ".join(filter(None, platform.get("tools", [])))[:70]
        lines.append(f"|     Tools: {tools}".ljust(BOX_WIDTH) + "|")
        lines.append("|" + " " * BOX_WIDTH + "|")

    # Anti-patterns Section
    if anti_patterns:
        lines.append("|  AVOID (Anti-patterns):".ljust(BOX_WIDTH) + "|")
        for line in wrap_text(anti_patterns, "|     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH) + "|")
        lines.append("|" + " " * BOX_WIDTH + "|")

    # 2025 Standard
    if product_info.get("standard_2025"):
        lines.append("|  2025 STANDARD:".ljust(BOX_WIDTH) + "|")
        for line in wrap_text(product_info.get("standard_2025", ""), "|     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH) + "|")
        lines.append("|" + " " * BOX_WIDTH + "|")

    # Pre-Implementation Checklist
    lines.append("|  PRE-IMPLEMENTATION CHECKLIST:".ljust(BOX_WIDTH) + "|")
    checklist = [
        "[ ] Architecture Decision Record (ADR) documented",
        "[ ] Database schema design reviewed",
        "[ ] API contracts defined (OpenAPI/Protobuf)",
        "[ ] Security threat modeling completed",
        "[ ] Observability stack configured (Logs/Metrics/Traces)",
        "[ ] CI/CD pipeline designed",
        "[ ] Disaster Recovery plan documented",
        "[ ] Load testing scenarios defined"
    ]
    for item in checklist:
        lines.append(f"|     {item}".ljust(BOX_WIDTH) + "|")
    lines.append("|" + " " * BOX_WIDTH + "|")

    lines.append("+" + "=" * w + "+")
    return "\n".join(lines)


def format_markdown(arch_system: dict) -> str:
    """Format architecture system as markdown."""
    project = arch_system.get("project_name", "PROJECT")
    category = arch_system.get("category", "")
    product_info = arch_system.get("product_info", {})
    architecture = arch_system.get("architecture", {})
    stack = arch_system.get("stack", {})
    database = arch_system.get("database", {})
    api = arch_system.get("api", {})
    security = arch_system.get("security", {})
    platform = arch_system.get("platform", {})
    anti_patterns = arch_system.get("anti_patterns", "")

    lines = []
    lines.append(f"# Backend Architecture System: {project}")
    lines.append(f"\n**Category:** {category}")
    lines.append("")

    # Product Info
    if product_info.get("core_entities"):
        lines.append("## Domain Model")
        lines.append(f"- **Core Entities:** {product_info.get('core_entities', '')}")
        lines.append(f"- **Critical Features:** {product_info.get('critical_features', '')}")
        lines.append(f"- **Data Consistency:** {product_info.get('data_consistency', '')}")
        lines.append(f"- **Performance Bottleneck:** {product_info.get('performance_bottleneck', '')}")
        lines.append("")

    # Architecture
    lines.append("## Architecture")
    lines.append(f"- **Recommended:** {architecture.get('name', '')} (`{architecture.get('recommended', '')}`)")
    lines.append(f"- **Description:** {architecture.get('description', '')}")
    lines.append(f"- **Use Case:** {architecture.get('use_case', '')}")
    lines.append(f"- **Key Components:** {architecture.get('key_components', '')}")
    lines.append(f"- **Reference Patterns:** {architecture.get('ref_pattern', '')}")
    lines.append("")

    # Trade-offs
    if architecture.get("trade_offs"):
        lines.append("### Trade-offs")
        lines.append(f"{architecture.get('trade_offs', '')}")
        lines.append("")

    # Stack
    lines.append("## Technology Stack")
    lines.append(f"- **Priority:** {' + '.join(filter(None, stack.get('priority', [])))}")
    lines.append(f"- **Languages:** {', '.join(filter(None, stack.get('languages', [])))}")
    lines.append("")

    # Database
    lines.append("## Database Strategy")
    lines.append(f"| Aspect | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Priority | {' + '.join(filter(None, database.get('priority', [])))} |")
    lines.append(f"| Primary | {database.get('primary', '')} |")
    lines.append(f"| Category | {database.get('category', '')} |")
    lines.append(f"| Consistency | {database.get('consistency', '')} |")
    lines.append(f"| Key Feature | {database.get('key_feature', '')} |")
    lines.append("")

    # API
    lines.append("## API Pattern")
    lines.append(f"- **Pattern:** {api.get('pattern', '')}")
    lines.append(f"- **Primary:** {api.get('name', '')} ({api.get('transport', '')})")
    lines.append(f"- **Strength:** {api.get('strength', '')}")
    lines.append(f"- **2025 Trend:** {api.get('trend_2025', '')}")
    lines.append("")

    # Security
    if security.get("considerations"):
        lines.append("## Security Considerations")
        for sec in filter(None, security.get("considerations", [])):
            lines.append(f"- {sec}")
        lines.append("")

    # Platform
    if platform.get("tools"):
        lines.append("## Platform & DevOps")
        lines.append(f"**Tools:** {', '.join(filter(None, platform.get('tools', [])))}")
        lines.append("")

    # Anti-patterns
    if anti_patterns:
        lines.append("## Anti-Patterns (AVOID)")
        for ap in anti_patterns.split("|"):
            if ap.strip():
                lines.append(f"- ❌ {ap.strip()}")
        lines.append("")

    # 2025 Standard
    if product_info.get("standard_2025"):
        lines.append("## 2025 Standard")
        lines.append(f"> {product_info.get('standard_2025', '')}")
        lines.append("")

    # Checklist
    lines.append("## Pre-Implementation Checklist")
    lines.append("- [ ] Architecture Decision Record (ADR) documented")
    lines.append("- [ ] Database schema design reviewed")
    lines.append("- [ ] API contracts defined (OpenAPI/Protobuf)")
    lines.append("- [ ] Security threat modeling completed")
    lines.append("- [ ] Observability stack configured (Logs/Metrics/Traces)")
    lines.append("- [ ] CI/CD pipeline designed")
    lines.append("- [ ] Disaster Recovery plan documented")
    lines.append("- [ ] Load testing scenarios defined")
    lines.append("")

    return "\n".join(lines)


# ============ MAIN ENTRY POINT ============
def generate_architecture_system(query: str, project_name: str = None, output_format: str = "ascii",
                                  persist: bool = False, service: str = None, output_dir: str = None) -> str:
    """
    Main entry point for architecture system generation.

    Args:
        query: Search query (e.g., "e-commerce platform", "fintech wallet")
        project_name: Optional project name for output header
        output_format: "ascii" (default) or "markdown"
        persist: If True, save to architecture-system/ folder
        service: Optional service name for service-specific override file
        output_dir: Optional output directory

    Returns:
        Formatted architecture system string
    """
    generator = ArchitectureSystemGenerator()
    arch_system = generator.generate(query, project_name)

    # Persist to files if requested
    if persist:
        persist_architecture_system(arch_system, service, output_dir, query)

    if output_format == "markdown":
        return format_markdown(arch_system)
    return format_ascii_box(arch_system)


# ============ PERSISTENCE FUNCTIONS ============
def persist_architecture_system(arch_system: dict, service: str = None, output_dir: str = None, 
                                 service_query: str = None) -> dict:
    """
    Persist architecture system to architecture-system/<project>/ folder.
    
    Args:
        arch_system: The generated architecture system dictionary
        service: Optional service name for service-specific override file
        output_dir: Optional output directory
        service_query: Optional query for intelligent service override
    
    Returns:
        dict with created file paths and status
    """
    base_dir = Path(output_dir) if output_dir else Path.cwd()
    
    project_name = arch_system.get("project_name", "default")
    project_slug = project_name.lower().replace(' ', '-')
    
    arch_system_dir = base_dir / "architecture-system" / project_slug
    services_dir = arch_system_dir / "services"
    
    created_files = []
    
    # Create directories
    arch_system_dir.mkdir(parents=True, exist_ok=True)
    services_dir.mkdir(parents=True, exist_ok=True)
    
    master_file = arch_system_dir / "MASTER.md"
    
    # Generate and write MASTER.md
    master_content = format_master_md(arch_system)
    with open(master_file, 'w', encoding='utf-8') as f:
        f.write(master_content)
    created_files.append(str(master_file))
    
    # If service is specified, create service override file
    if service:
        service_file = services_dir / f"{service.lower().replace(' ', '-')}.md"
        service_content = format_service_override_md(arch_system, service, service_query)
        with open(service_file, 'w', encoding='utf-8') as f:
            f.write(service_content)
        created_files.append(str(service_file))
    
    return {
        "status": "success",
        "architecture_system_dir": str(arch_system_dir),
        "created_files": created_files
    }


def format_master_md(arch_system: dict) -> str:
    """Format architecture system as MASTER.md with hierarchical override logic."""
    project = arch_system.get("project_name", "PROJECT")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    lines = []
    
    lines.append("# Architecture System Master File")
    lines.append("")
    lines.append("> **LOGIC:** When building a specific service, first check `architecture-system/services/[service-name].md`.")
    lines.append("> If that file exists, its rules **override** this Master file.")
    lines.append("> If not, strictly follow the rules below.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"**Project:** {project}")
    lines.append(f"**Generated:** {timestamp}")
    lines.append(f"**Category:** {arch_system.get('category', 'General')}")
    lines.append("")
    
    # Include full markdown content
    lines.append(format_markdown(arch_system))
    
    return "\n".join(lines)


def format_service_override_md(arch_system: dict, service_name: str, service_query: str = None) -> str:
    """Format a service-specific override file."""
    project = arch_system.get("project_name", "PROJECT")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    service_title = service_name.replace("-", " ").replace("_", " ").title()
    
    lines = []
    
    lines.append(f"# {service_title} Service Overrides")
    lines.append("")
    lines.append(f"> **PROJECT:** {project}")
    lines.append(f"> **Generated:** {timestamp}")
    lines.append("")
    lines.append("> ⚠️ **IMPORTANT:** Rules in this file **override** the Master file.")
    lines.append("> Only deviations from the Master are documented here.")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    lines.append("## Service-Specific Overrides")
    lines.append("")
    
    lines.append("### Database Overrides")
    lines.append("- No overrides — use Master database strategy")
    lines.append("")
    
    lines.append("### API Overrides")
    lines.append("- No overrides — use Master API pattern")
    lines.append("")
    
    lines.append("### Security Overrides")
    lines.append("- No overrides — use Master security considerations")
    lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("## Service-Specific Components")
    lines.append("- Add service-specific components as needed")
    lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("## Recommendations")
    lines.append("- Refer to MASTER.md for all architecture rules")
    lines.append("- Add specific overrides as needed for this service")
    lines.append("")
    
    return "\n".join(lines)


# ============ CLI SUPPORT ============
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate Backend Architecture System")
    parser.add_argument("query", help="Search query (e.g., 'e-commerce platform')")
    parser.add_argument("--project-name", "-p", type=str, default=None, help="Project name")
    parser.add_argument("--format", "-f", choices=["ascii", "markdown"], default="ascii", help="Output format")
    parser.add_argument("--persist", action="store_true", help="Save to architecture-system/ folder")
    parser.add_argument("--service", type=str, default=None, help="Service name for override file")
    parser.add_argument("--output-dir", "-o", type=str, default=None, help="Output directory")

    args = parser.parse_args()

    result = generate_architecture_system(
        args.query, 
        args.project_name, 
        args.format,
        persist=args.persist,
        service=args.service,
        output_dir=args.output_dir
    )
    print(result)
