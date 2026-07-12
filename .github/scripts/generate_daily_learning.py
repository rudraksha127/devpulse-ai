#!/usr/bin/env python3
"""Generate one high-quality daily learning note in README.md."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import re

README_PATH = Path("README.md")

CATEGORIES = [
    "Data Structures",
    "Algorithms",
    "System Design",
    "Operating Systems",
    "DBMS",
    "Computer Networks",
    "OOP",
    "C++",
    "Java",
    "Python",
    "JavaScript",
    "React",
    "Node.js",
    "Express.js",
    "MongoDB",
    "PostgreSQL",
    "SQL",
    "Git",
    "GitHub",
    "Docker",
    "Kubernetes",
    "Linux",
    "AWS",
    "Azure",
    "GCP",
    "DevOps",
    "Terraform",
    "CI/CD",
    "AI Engineering",
    "Prompt Engineering",
    "RAG",
    "Agentic AI",
    "LLM Fundamentals",
    "Machine Learning",
    "Deep Learning",
    "REST API",
    "GraphQL",
    "Authentication",
    "Redis",
    "Web Security",
]

TOPIC_TITLES = {
    "Data Structures": "Hash Table Collision Resolution",
    "Algorithms": "Sliding Window Pattern",
    "System Design": "Load Balancing Strategies",
    "Operating Systems": "Virtual Memory and Paging",
    "DBMS": "B+ Tree Indexing",
    "Computer Networks": "TCP Three-Way Handshake",
    "OOP": "Single Responsibility Principle",
    "C++": "RAII with Smart Pointers",
    "Java": "JVM Heap and Garbage Collection",
    "Python": "Decorators and Function Wrapping",
    "JavaScript": "Event Loop and Microtasks",
    "React": "Virtual DOM Reconciliation",
    "Node.js": "Non-Blocking I/O Architecture",
    "Express.js": "Middleware Execution Pipeline",
    "MongoDB": "Embedding vs Referencing",
    "PostgreSQL": "MVCC Transaction Model",
    "SQL": "Window Functions for Analytics",
    "Git": "Rebase vs Merge",
    "GitHub": "Pull Request Review Workflow",
    "Docker": "Multi-Stage Docker Builds",
    "Kubernetes": "Rolling Update Strategy",
    "Linux": "Process Signals and Lifecycle",
    "AWS": "S3 Lifecycle Policies",
    "Azure": "Managed Identity Authentication",
    "GCP": "Pub/Sub Delivery Semantics",
    "DevOps": "Blue-Green Deployment",
    "Terraform": "Remote State Management",
    "CI/CD": "Trunk-Based Delivery Pipelines",
    "AI Engineering": "Feature Store Fundamentals",
    "Prompt Engineering": "Few-Shot Prompt Design",
    "RAG": "Chunking and Retrieval Optimization",
    "Agentic AI": "Planning and Tool-Oriented Agents",
    "LLM Fundamentals": "Self-Attention Mechanism",
    "Machine Learning": "Bias-Variance Trade-off",
    "Deep Learning": "Backpropagation and Gradients",
    "REST API": "HTTP Idempotency Design",
    "GraphQL": "N+1 Query Prevention",
    "Authentication": "JWT Access and Refresh Tokens",
    "Redis": "Cache-Aside Pattern",
    "Web Security": "Preventing SQL Injection",
}

CATEGORY_CONTEXT = {
    "Data Structures": "performance-critical services such as caches, key-value stores, and compilers",
    "Algorithms": "search, recommendation, and data-processing pipelines",
    "System Design": "high-traffic distributed platforms",
    "Operating Systems": "resource management inside servers and containers",
    "DBMS": "query planning and fast lookup in transactional databases",
    "Computer Networks": "reliable communication between distributed systems",
    "OOP": "large codebases that need maintainability",
    "C++": "memory-safe systems programming",
    "Java": "enterprise backend runtime behavior",
    "Python": "framework extension and reusable tooling",
    "JavaScript": "responsive frontend and server runtimes",
    "React": "efficient interactive user interfaces",
    "Node.js": "I/O heavy API services",
    "Express.js": "API composition and request lifecycle control",
    "MongoDB": "document-data modeling in evolving products",
    "PostgreSQL": "concurrent transactional workloads",
    "SQL": "reporting and analytical workloads",
    "Git": "team collaboration and clean history",
    "GitHub": "code review quality and release safety",
    "Docker": "portable and reproducible deployments",
    "Kubernetes": "zero-downtime service delivery",
    "Linux": "process supervision and operational debugging",
    "AWS": "cost-efficient cloud storage",
    "Azure": "secretless service-to-service access",
    "GCP": "event-driven asynchronous architectures",
    "DevOps": "safe and frequent production releases",
    "Terraform": "reliable infrastructure automation",
    "CI/CD": "high-confidence shipping velocity",
    "AI Engineering": "training-serving feature consistency",
    "Prompt Engineering": "controllable LLM behavior",
    "RAG": "factual and source-grounded assistants",
    "Agentic AI": "multi-step automated workflows",
    "LLM Fundamentals": "understanding transformer model behavior",
    "Machine Learning": "model generalization on unseen data",
    "Deep Learning": "stable neural-network training",
    "REST API": "resilient API retry semantics",
    "GraphQL": "scalable API resolver performance",
    "Authentication": "secure session architecture",
    "Redis": "latency reduction in read-heavy systems",
    "Web Security": "defending production APIs from injection attacks",
}

CODE_LANGUAGE = {
    "Data Structures": "python",
    "Algorithms": "python",
    "System Design": "python",
    "Operating Systems": "c",
    "DBMS": "sql",
    "Computer Networks": "python",
    "OOP": "java",
    "C++": "cpp",
    "Java": "java",
    "Python": "python",
    "JavaScript": "javascript",
    "React": "tsx",
    "Node.js": "javascript",
    "Express.js": "javascript",
    "MongoDB": "javascript",
    "PostgreSQL": "sql",
    "SQL": "sql",
    "Git": "bash",
    "GitHub": "yaml",
    "Docker": "dockerfile",
    "Kubernetes": "yaml",
    "Linux": "bash",
    "AWS": "bash",
    "Azure": "bash",
    "GCP": "bash",
    "DevOps": "yaml",
    "Terraform": "hcl",
    "CI/CD": "yaml",
    "AI Engineering": "python",
    "Prompt Engineering": "python",
    "RAG": "python",
    "Agentic AI": "python",
    "LLM Fundamentals": "python",
    "Machine Learning": "python",
    "Deep Learning": "python",
    "REST API": "typescript",
    "GraphQL": "typescript",
    "Authentication": "typescript",
    "Redis": "typescript",
    "Web Security": "typescript",
}

CODE_SNIPPETS = {
    "Hash Table Collision Resolution": """from dataclasses import dataclass\n\n@dataclass\nclass Entry:\n    key: str\n    value: str\n\nclass ChainedHashMap:\n    def __init__(self, buckets: int = 16) -> None:\n        self._table: list[list[Entry]] = [[] for _ in range(buckets)]\n\n    def _index(self, key: str) -> int:\n        return hash(key) % len(self._table)\n\n    def set(self, key: str, value: str) -> None:\n        bucket = self._table[self._index(key)]\n        for entry in bucket:\n            if entry.key == key:\n                entry.value = value\n                return\n        bucket.append(Entry(key, value))\n\n    def get(self, key: str) -> str | None:\n        for entry in self._table[self._index(key)]:\n            if entry.key == key:\n                return entry.value\n        return None""",
    "Sliding Window Pattern": """def longest_unique_substring(s: str) -> int:\n    left = 0\n    seen: dict[str, int] = {}\n    best = 0\n\n    for right, char in enumerate(s):\n        if char in seen and seen[char] >= left:\n            left = seen[char] + 1\n        seen[char] = right\n        best = max(best, right - left + 1)\n\n    return best""",
    "Load Balancing Strategies": """class RoundRobinBalancer:\n    def __init__(self, hosts: list[str]) -> None:\n        self.hosts = hosts\n        self.idx = 0\n\n    def next_host(self) -> str:\n        host = self.hosts[self.idx]\n        self.idx = (self.idx + 1) % len(self.hosts)\n        return host""",
    "Virtual Memory and Paging": """#include <stdio.h>\n#include <stdint.h>\n\nuint32_t page_number(uint32_t address, uint32_t page_size) {\n    return address / page_size;\n}\n\nuint32_t offset(uint32_t address, uint32_t page_size) {\n    return address % page_size;\n}\n\nint main(void) {\n    uint32_t addr = 0xCAFEBABE;\n    uint32_t size = 4096;\n    printf(\"page=%u offset=%u\\n\", page_number(addr, size), offset(addr, size));\n    return 0;\n}""",
}


@dataclass(frozen=True)
class Topic:
    category: str
    title: str


def read_readme() -> str:
    if README_PATH.exists():
        return README_PATH.read_text(encoding="utf-8")
    return "# daily-log\n\n"


def extract_used_topics(readme_content: str) -> set[str]:
    pattern = re.compile(r"^## 📖 Topic\s*\n(.+)$", re.MULTILINE)
    return {match.group(1).strip() for match in pattern.finditer(readme_content)}


def explanation_text(topic: Topic) -> str:
    context = CATEGORY_CONTEXT[topic.category]
    return (
        f"{topic.title} is a core interview topic because it forces you to reason about correctness, "
        f"performance, and trade-offs at the same time. In practical systems, this concept appears in {context}. "
        "When engineers understand not just the API but also the operational behavior, they make stronger design decisions "
        "under real production constraints such as latency, memory limits, concurrency, and failure handling.\n\n"
        "A good way to approach this concept is to identify its invariants first. Invariants are guarantees that must remain true "
        "before and after each operation. If you can explain those invariants clearly, you can derive complexity, edge cases, and "
        "test strategy naturally. This is exactly what interviewers evaluate: whether you can move from abstract definition to a "
        "repeatable engineering method that survives unusual inputs and scaling pressure.\n\n"
        "You should also connect this topic to trade-off analysis. No design is universally best; every design optimizes one axis while "
        "compromising another. For example, improving speed may increase memory usage, and increasing consistency may reduce write throughput. "
        "Professional engineering means choosing consciously based on workload shape, reliability targets, and operational cost instead of "
        "copying defaults. That mindset turns textbook knowledge into architecture judgment.\n\n"
        f"From an implementation perspective, {topic.title} is usually expressed through small, composable units with explicit boundaries. "
        "Each unit should do one thing well, expose a measurable contract, and fail predictably. This keeps systems debuggable and makes "
        "performance tuning easier because bottlenecks are observable. During interviews, clear decomposition often matters as much as the "
        "final code because it demonstrates that you can ship maintainable solutions in team environments.\n\n"
        "Finally, practice explaining complexity and limitations in plain language. A strong answer does not stop at "
        "\"this works\"; it includes why it works, when it fails, and how to improve it incrementally. That level of explanation mirrors "
        "real production work where engineers justify decisions in design docs and review discussions."
    )


def internal_working(topic: Topic) -> str:
    return (
        "1. Define the invariant and data flow for each operation.\n"
        "2. Map operations to time and space complexity under expected load.\n"
        "3. Handle edge conditions explicitly (empty input, retries, contention, malformed data).\n"
        "4. Add observability points (metrics, logs, traces) around critical paths.\n"
        "5. Validate with deterministic tests and workload-oriented scenarios before release."
    )


def code_example(topic: Topic) -> str:
    language = CODE_LANGUAGE[topic.category]
    snippet = CODE_SNIPPETS.get(
        topic.title,
        f"""def explain_{topic.category.lower().replace('+', 'plus').replace('/', '_').replace('.', '').replace('-', '_').replace(' ', '_')}() -> dict[str, str]:\n    return {{\n        \"topic\": \"{topic.title}\",\n        \"category\": \"{topic.category}\",\n        \"focus\": \"Use clear invariants, measurable behavior, and safe defaults.\"\n    }}""",
    )
    return f"```{language}\n{snippet}\n```"


def use_cases(topic: Topic) -> str:
    return (
        f"- Designing interview-ready solutions for {topic.category} problems with clear trade-offs.\n"
        f"- Improving production reliability in systems that depend on {topic.title.lower()}.\n"
        "- Building code review checklists that catch correctness and performance risks early."
    )


def interview_qas(topic: Topic) -> str:
    return (
        f"1. **Question:** What invariant defines correctness for {topic.title.lower()}?  \n"
        "   **Short Answer:** Correctness depends on preserving the core rule after every operation and validating it with edge-case tests.\n"
        f"2. **Question:** How do you choose between alternative designs for {topic.category}?  \n"
        "   **Short Answer:** Compare latency, throughput, memory, consistency, and operational complexity against expected workload.\n"
        "3. **Question:** What is a production risk interview candidates often miss?  \n"
        "   **Short Answer:** Ignoring failure paths such as retries, partial failures, and observability gaps that hide real bottlenecks."
    )


def common_mistakes(topic: Topic) -> str:
    return (
        "- Focusing on syntax without stating invariants or complexity assumptions.\n"
        "- Ignoring edge cases like empty inputs, high-cardinality data, or concurrent access.\n"
        "- Choosing patterns by popularity instead of workload and reliability requirements."
    )


def further_reading(topic: Topic) -> str:
    return (
        "- [MDN Web Docs](https://developer.mozilla.org/)\n"
        "- [GeeksforGeeks - Computer Science Fundamentals](https://www.geeksforgeeks.org/computer-science/)")


def key_takeaways(topic: Topic) -> str:
    return (
        f"- {topic.title} is best learned by combining theory, complexity analysis, and implementation practice.\n"
        "- Interview-quality answers explain trade-offs, edge cases, and operational constraints.\n"
        "- Production-quality code keeps behavior explicit, testable, and observable."
    )


def render_note(topic: Topic, date_str: str) -> str:
    return (
        f"# 📅 Daily Learning - {date_str}\n\n"
        "## 📖 Topic\n"
        f"{topic.title}\n\n"
        "## 🎯 Why it Matters\n"
        f"{topic.title} is directly relevant to {CATEGORY_CONTEXT[topic.category]}.\n\n"
        "| Dimension | Interview Value | Production Value |\n"
        "| --- | --- | --- |\n"
        f"| Core concept | Tests conceptual clarity in {topic.category} | Improves design quality under constraints |\n"
        "| Trade-offs | Shows decision-making maturity | Prevents costly architecture mistakes |\n"
        "| Edge cases | Demonstrates depth under pressure | Reduces incidents and regressions |\n\n"
        "## 🧠 Explanation\n"
        f"{explanation_text(topic)}\n\n"
        "## ⚙️ Internal Working\n"
        f"{internal_working(topic)}\n\n"
        "## 💻 Code Example\n"
        f"{code_example(topic)}\n\n"
        "## 📌 Real-world Use Cases\n"
        f"{use_cases(topic)}\n\n"
        "## 🚀 Interview Questions\n"
        f"{interview_qas(topic)}\n\n"
        "## ❌ Common Mistakes\n"
        f"{common_mistakes(topic)}\n\n"
        "## 📚 Further Reading\n"
        f"{further_reading(topic)}\n\n"
        "## 📝 Key Takeaways\n"
        f"{key_takeaways(topic)}\n"
    )


def choose_topic(used_topics: set[str], date_ordinal: int) -> Topic | None:
    start_index = date_ordinal % len(CATEGORIES)
    for offset in range(len(CATEGORIES)):
        category = CATEGORIES[(start_index + offset) % len(CATEGORIES)]
        title = TOPIC_TITLES[category]
        if title not in used_topics:
            return Topic(category=category, title=title)
    return None


def update_readme(readme_content: str, note: str) -> str:
    stripped = readme_content.rstrip()
    if not stripped:
        return f"# daily-log\n\n{note}\n"
    return f"{stripped}\n\n---\n\n{note}\n"


def main() -> int:
    today = datetime.now(timezone.utc).date()
    date_str = today.isoformat()

    readme_content = read_readme()
    if f"# 📅 Daily Learning - {date_str}" in readme_content:
        print("README already has today's note. No change required.")
        return 0

    used_topics = extract_used_topics(readme_content)
    topic = choose_topic(used_topics=used_topics, date_ordinal=today.toordinal())

    if topic is None:
        print("All configured topics are already used. Add more topics to continue non-repeating updates.")
        return 0

    note = render_note(topic=topic, date_str=date_str)
    new_content = update_readme(readme_content=readme_content, note=note)

    if new_content == readme_content:
        print("No README change detected.")
        return 0

    README_PATH.write_text(new_content, encoding="utf-8")
    print(f"Added daily learning note: {topic.title} ({topic.category}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
