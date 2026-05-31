# Mathematical Optimization in Python

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> "Don't be the guy digging for gold; be the guy selling the shovel." 

This repository serves as an educational framework and optimization sandbox. It documents the evolution of algorithmic problem-solving—specifically covering foundational mathematical challenges (such as Project Euler problems 1–100)—by transforming naive, brute-force iterations into elite, highly optimized, production-ready code.

The core objective here is **pedagogy and performance engineering**. Instead of presenting static code-dumps, each module focuses on architectural scalability, strict type safety, unit testing, and mathematical shortcuts that drop time complexies from linear $O(n)$ down to constant time $O(1)$.

---

## 🚀 Architectural Standards

Every solution in this repository is treated like a critical micro-component of a high-throughput backend system. We enforce:

* **Strict Type Hinting:** Utilizing Python's `typing` module to ensure static analysis compliance.
* **Comprehensive Docstrings:** Clearly detailing execution context, edge-case constraints, and Big O complexity analysis.
* **Algorithmic Evolution:** Documenting the transition from **Naive** $\rightarrow$ **Idomatic** $\rightarrow$ **Mathematical Mastery**.
* **Robust Testing:** Standardized unit tests using `pytest` to guarantee deterministic results across all optimization rewrites.

---

## Optimization Catalog & Methodology

Below is the index of algorithmic implementations. Each directory contains the source module, optimized variants, and formal analysis.

| Problem / Concept | Core Mathematical Focus | Naive Complexity | Optimized Complexity | Status |
| :--- | :--- | :--- | :--- | :--- |
| **001: Multiples of 3 & 5** | Arithmetic Progressions / Inclusion-Exclusion | $O(n)$ Time \| $O(1)$ Space | $O(1)$ Time \| $O(1)$ Space | 🟢 Complete |
| **002: Even Fibonacci** | Linear Recurrence / Golden Ratio Matrix | $O(n)$ Time \| $O(1)$ Space | $O(\log n)$ Time \| $O(1)$ Space| 🟡 In Progress |
| **003: Prime Factorization** | Trial Division / Sieve of Eratosthenes | $O(n)$ Time \| $O(1)$ Space | $O(\sqrt{n})$ Time \| $O(1)$ Space | ⏳ Planned |

---

##  Deep Dive Example: Problem 001 (Multiples of 3 and 5)

To illustrate the methodology of this repository, consider the problem of summing all multiples of 3 or 5 below a given limit $N$.

### 1. The Naive Approach (Linear Check)
A standard loop evaluates every single integer up to $N$. While readable, this scales poorly as $N \to \infty$.
```python
# Linear Time Optimization (Idiomatic Python)
def sum_multiples_loop(limit: int) -> int:
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)