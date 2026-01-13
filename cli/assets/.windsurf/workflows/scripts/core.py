# -*- coding: utf-8 -*-
"""
Backend Architect Skill Core - BM25 search engine for backend architecture guides
"""

import csv
import re
from pathlib import Path
from math import log
from collections import defaultdict

# ============ CONFIGURATION ============
DATA_DIR = Path(__file__).parent.parent / "data"
MAX_RESULTS = 3

CSV_CONFIG = {
    "architecture": {
        "file": "architectures.csv",
        "search_cols": ["id", "name", "description", "use_case", "key_components"],
        "output_cols": ["id", "name", "description", "use_case", "trade_offs", "key_components", "ref_pattern"]
    },
    "database": {
        "file": "databases.csv",
        "search_cols": ["Category", "Technology", "Key Feature 2025", "Use Case Primary"],
        "output_cols": ["Category", "Technology", "Key Feature 2025", "Use Case Primary", "Consistency Model", "License/Model"]
    },
    "security": {
        "file": "security.csv",
        "search_cols": ["id", "name", "owasp_category", "prevention_pattern", "2025_standard"],
        "output_cols": ["id", "name", "owasp_category", "risk_level", "prevention_pattern", "tooling_ref", "2025_standard", "checklist_item"]
    },
    "product": {
        "file": "product.csv",
        "search_cols": ["id", "name", "core_entities", "critical_features", "recommended_stack_ref"],
        "output_cols": ["id", "name", "core_entities", "critical_features", "data_consistency", "performance_bottleneck", "recommended_stack_ref", "2025_standard"]
    },
    "language": {
        "file": "languages.csv",
        "search_cols": ["id", "name", "frameworks", "key_features", "use_case"],
        "output_cols": ["id", "name", "type", "frameworks", "key_features", "best_practices", "performance_profile", "ecosystem_tools", "use_case"]
    },
    "api": {
        "file": "api-patterns.csv",
        "search_cols": ["ID", "Pattern_Name", "Primary_Use_Case", "Key_Strength"],
        "output_cols": ["ID", "Pattern_Name", "Primary_Use_Case", "Transport_Protocol", "Data_Format", "Key_Strength", "Key_Weakness", "Trend_2025_Status"]
    },
    "naming": {
        "file": "naming-conventions.csv",
        "search_cols": ["id", "technology", "element_type", "convention", "example"],
        "output_cols": ["id", "technology", "element_type", "convention", "example", "anti_pattern", "note"]
    },
    "error": {
        "file": "error-codes.csv",
        "search_cols": ["id", "protocol", "code", "name", "description"],
        "output_cols": ["id", "protocol", "code", "name", "description", "http_mapping", "handling_strategy", "fix_recommendation"]
    },
    "platform": {
        "file": "platform.csv",
        "search_cols": ["Category", "Tool", "Type", "Key Feature"],
        "output_cols": ["Category", "Tool", "Type", "License", "Key Feature", "2025 Trend Status"]
    }
}

STACK_CONFIG = {
    "go": {"file": "stacks/go.csv"},
    "python": {"file": "stacks/python.csv"},
    "node": {"file": "stacks/node.csv"},
    "java": {"file": "stacks/java.csv"},
    "dotnet": {"file": "stacks/dotnet.csv"},
    "rust": {"file": "stacks/rust.csv"}
}

# Common columns for all stacks
_STACK_COLS = {
    "search_cols": ["id", "name", "category", "recommendation", "reasoning"],
    "output_cols": ["id", "name", "category", "recommendation", "reasoning", "config_snippet"]
}

AVAILABLE_STACKS = list(STACK_CONFIG.keys())
AVAILABLE_DOMAINS = list(CSV_CONFIG.keys())


# ============ BM25 IMPLEMENTATION ============
class BM25:
    """BM25 ranking algorithm for text search"""

    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.corpus = []
        self.doc_lengths = []
        self.avgdl = 0
        self.idf = {}
        self.doc_freqs = defaultdict(int)
        self.N = 0

    def tokenize(self, text):
        """Lowercase, split, remove punctuation, filter short words"""
        text = re.sub(r'[^\w\s]', ' ', str(text).lower())
        return [w for w in text.split() if len(w) > 2]

    def fit(self, documents):
        """Build BM25 index from documents"""
        self.corpus = [self.tokenize(doc) for doc in documents]
        self.N = len(self.corpus)
        if self.N == 0:
            return
        self.doc_lengths = [len(doc) for doc in self.corpus]
        self.avgdl = sum(self.doc_lengths) / self.N

        for doc in self.corpus:
            seen = set()
            for word in doc:
                if word not in seen:
                    self.doc_freqs[word] += 1
                    seen.add(word)

        for word, freq in self.doc_freqs.items():
            self.idf[word] = log((self.N - freq + 0.5) / (freq + 0.5) + 1)

    def score(self, query):
        """Score all documents against query"""
        query_tokens = self.tokenize(query)
        scores = []

        for idx, doc in enumerate(self.corpus):
            score = 0
            doc_len = self.doc_lengths[idx]
            term_freqs = defaultdict(int)
            for word in doc:
                term_freqs[word] += 1

            for token in query_tokens:
                if token in self.idf:
                    tf = term_freqs[token]
                    idf = self.idf[token]
                    numerator = tf * (self.k1 + 1)
                    denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                    score += idf * numerator / denominator

            scores.append((idx, score))

        return sorted(scores, key=lambda x: x[1], reverse=True)


# ============ SEARCH FUNCTIONS ============
def _load_csv(filepath):
    """Load CSV and return list of dicts"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _search_csv(filepath, search_cols, output_cols, query, max_results):
    """Core search function using BM25"""
    if not filepath.exists():
        return []

    data = _load_csv(filepath)

    # Build documents from search columns
    documents = [" ".join(str(row.get(col, "")) for col in search_cols) for row in data]

    # BM25 search
    bm25 = BM25()
    bm25.fit(documents)
    ranked = bm25.score(query)

    # Get top results with score > 0
    results = []
    for idx, score in ranked[:max_results]:
        if score > 0:
            row = data[idx]
            results.append({col: row.get(col, "") for col in output_cols if col in row})

    return results


def detect_domain(query):
    """Auto-detect the most relevant domain from query"""
    query_lower = query.lower()

    domain_keywords = {
        "architecture": ["architecture", "microservices", "monolith", "serverless", "cqrs", "event-driven", "hexagonal", "clean", "layered", "modular"],
        "database": ["database", "postgresql", "mysql", "mongodb", "redis", "cassandra", "clickhouse", "sql", "nosql", "vector", "timescale"],
        "security": ["security", "owasp", "injection", "auth", "encryption", "vulnerability", "secrets", "container", "api security", "gdpr"],
        "product": ["ecommerce", "saas", "fintech", "social", "chat", "iot", "marketplace", "booking", "crm", "analytics", "ai agent", "rag"],
        "language": ["rust", "golang", "java", "python", "node", "typescript", "dotnet", "elixir", "php", "ruby", "c++", "framework"],
        "api": ["rest", "graphql", "grpc", "websocket", "sse", "trpc", "mcp", "api", "endpoint", "http"],
        "naming": ["naming", "convention", "variable", "function", "class", "table", "column", "camelcase", "snake_case"],
        "error": ["error", "exception", "status code", "http 4", "http 5", "grpc error", "handling", "retry"],
        "platform": ["kubernetes", "terraform", "argocd", "vault", "observability", "gitops", "devops", "platform", "iac"]
    }

    scores = {domain: sum(1 for kw in keywords if kw in query_lower) for domain, keywords in domain_keywords.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "architecture"


def search(query, domain=None, max_results=MAX_RESULTS):
    """Main search function with auto-domain detection"""
    if domain is None:
        domain = detect_domain(query)

    config = CSV_CONFIG.get(domain, CSV_CONFIG["architecture"])
    filepath = DATA_DIR / config["file"]

    if not filepath.exists():
        return {"error": f"File not found: {filepath}", "domain": domain}

    results = _search_csv(filepath, config["search_cols"], config["output_cols"], query, max_results)

    return {
        "domain": domain,
        "query": query,
        "file": config["file"],
        "count": len(results),
        "results": results
    }


def search_stack(query, stack, max_results=MAX_RESULTS):
    """Search stack-specific guidelines"""
    if stack not in STACK_CONFIG:
        return {"error": f"Unknown stack: {stack}. Available: {', '.join(AVAILABLE_STACKS)}"}

    filepath = DATA_DIR / STACK_CONFIG[stack]["file"]

    if not filepath.exists():
        return {"error": f"Stack file not found: {filepath}", "stack": stack}

    results = _search_csv(filepath, _STACK_COLS["search_cols"], _STACK_COLS["output_cols"], query, max_results)

    return {
        "domain": "stack",
        "stack": stack,
        "query": query,
        "file": STACK_CONFIG[stack]["file"],
        "count": len(results),
        "results": results
    }
