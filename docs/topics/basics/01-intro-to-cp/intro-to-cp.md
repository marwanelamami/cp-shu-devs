# Intro to CP & Complexity

**Category:** Basics  
**Difficulty:** 🟢 Very Easy

---

This topic covers the fundamentals of Competitive Programming, the metrics we use to judge algorithm efficiency, and how to analyze code complexity.

## What is Competitive Programming?

Competitive programming is a mind sport that combines two distinct but equally important skills:

1. **Designing algorithms**: Requiring problem-solving abilities and mathematical thinking.
2. **Implementing them**: Writing the code correctly and efficiently under tight time pressure.

![What is CP](images/intro-to-cp/intro-1.png)

In competitive programming, you are given a problem statement accompanied by strict execution time and memory limits. Your goal is to write a program that solves the problem correctly and within these bounds.

Once submitted, your solution is judged automatically by an online system. It is either accepted or it is not — there is no partial credit, and no "almost correct" solutions.

## Why Competitive Programming?

Engaging in competitive programming offers several key benefits:

- **Tech Career Preparation**: Technical interviews at top technology companies test exactly these problem-solving and implementation skills.
- **Mathematical Growth**: It builds mathematical maturity and refines your ability to reason under constraints.
- **Problem-Solving Mindset**: You are not just learning a list of algorithms; you are building a structured way of thinking.

As Antti Laaksonen states in the *Competitive Programmer's Handbook*:
> “It takes a long time to become a good competitive programmer, but it is also an opportunity to learn a lot.”

## The Competition Ladder

The competitive programming landscape is structured like a ladder, scaling from local challenges to international arenas.

![The Competition Ladder](images/intro-to-cp/intro-2.svg)

## The Online Judge

In competitive programming, you submit your code through a web interface. The online judge compiles your code and runs it against a set of hidden test cases. You never get to see these test cases; you must think of edge cases and verify your solution’s correctness on your own before submitting.

Every submission returns exactly one of the following verdicts:

| Verdict | Meaning |
|---|---|
| Accepted | Correct output, within time limit |
| Wrong Answer | Incorrect output on at least one case |
| Time Limit Exceeded | Correct logic, too slow |
| Runtime Error | Crash — division by zero, out of bounds, etc. |
| Compilation Error | Code didn’t compile |

## Your First Problem

To understand how to read problem constraints and construct solutions, we begin by analyzing a starter problem.

![Your First Problem](images/intro-to-cp/intro-3.png)

## Algorithms & Data Structures

Every solution in competitive programming is composed of an algorithm working in tandem with one or more data structures. If you modify one, the entire performance of your solution changes. An algorithm is only as fast as the data structures it runs on.

- **Algorithm**: A step-by-step method to solve a problem. It must be both correct and efficient. Think of it as *the recipe* — it defines what actions to perform and in what order.
- **Data Structure**: A concrete way to organize and store data so that operations can be performed efficiently. It is *the container*, and its shape determines which operations are cheap and which are expensive.

## Measuring Algorithm Efficiency

Rather than measuring execution time in seconds (which varies depending on hardware), we count the number of basic operations the algorithm performs relative to the input size \(n\).

### Example Code Analysis

```python
a = 1 + 1           # 2 operations (constant time)
for i in range(n):  # n operations
    for j in range(n):  # n^2 operations
        print(i, j)
```

The total number of operations is represented by the Complexity Equation:

$$T(n) = n^2 + n + 2$$

As \(n\) grows extremely large, only the dominant term matters. The constants and smaller terms become negligible noise. This is the foundation of **Asymptotic Analysis** — we drop the smaller terms (\(n\) and \(2\)) to focus on the dominant rate of growth: \(n^2\).

## Asymptotic Analysis & Bounds

In asymptotic analysis, we evaluate the growth rate of algorithms under different scenarios:

- **Worst Case (Upper Bound)**: The maximum number of operations the algorithm could perform.
- **Average Case (Tight Bound)**: The expected behavior on typical inputs.
- **Best Case (Lower Bound)**: The minimum operations required under ideal inputs.

![Asymptotic Analysis Bounds](images/intro-to-cp/intro-4.png)

## Big-O Notation

![Big-O Notation Graph](images/intro-to-cp/intro-5.png)

Big-O notation is the mathematical language we use to express the upper bound of an algorithm’s growth rate:

- **Mathematical Definition**: We write \(T(n) = O(f(n))\) to indicate that, for large \(n\), your algorithm’s operations grow no faster than \(f(n)\).
- **In Plain English**: It is an upper bound on how your algorithm scales — a worst-case guarantee that your algorithm will never perform worse than this.

### Example

For the function:

$$T(n) = 3n^2 + 100n + 500$$

This simplifies to \(T(n) = O(n^2)\). We ignore the coefficient \(3\), the linear term \(100n\), and the constant \(500\). We only focus on the dominant shape of growth, which is quadratic (\(n^2\)).

## The Complexity Ladder

The higher you go up the ladder, the faster the algorithm’s performance degrades as the input size \(n\) increases.

![Complexity Ladder](images/intro-to-cp/intro-6.jpg)

| Complexity | Type | Max \(n\) safe in ~1s |
|---|---|---|
| \(O(1)\) | Constant | Any |
| \(O(\log n)\) | Logarithmic | Any |
| \(O(\sqrt{n})\) | Square Root | ~\(10^{16}\) |
| \(O(n)\) | Linear | ~\(10^{8}\) |
| \(O(n \log n)\) | Linearithmic | ~\(10^{7}\) |
| \(O(n^2)\) | Quadratic | ~\(10^{4}\) |
| \(O(n^3)\) | Cubic | ~\(10^{2}\) |
| \(O(2^n)\) | Exponential | ~\(20\) |
| \(O(n!)\) | Factorial | ~\(12\) |

## Complexity Analysis Examples

Below are five practical examples demonstrating how to evaluate the Big-O complexity of different code structures.

### Example 1 — Linear Search

```python
for i in range(1, n+1):
    if A[i] == t: return True
```

**Complexity**: \(O(n)\) — Linear time.

### Example 2 — Two Sequential Loops

```python
for i in range(1, n+1):
    if A[i] == t: return True
for i in range(1, n+1):
    if B[i] == t: return True
```

The loops run one after the other. Total steps are \(n + n = 2n\). Since we drop constant factors:

$$2n \rightarrow O(n)$$

### Example 3 — Nested Loops

```python
for i in range(1, n+1):
    for j in range(1, n+1):
        if A[i] == B[j]: return True
```

**Complexity**: \(O(n^2)\) — Quadratic time.

### Example 4 — Dependent Boundaries

```python
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if A[i] == A[j]: return True
```

Even though the inner loop runs fewer iterations on average, the quadratic growth shape is preserved:

$$\frac{n(n-1)}{2} = \frac{1}{2}n^2 - \frac{1}{2}n \rightarrow O(n^2)$$

### Example 5 — Constant Inner Loop

```python
for i in range(1, n+1):
    for j in range(1, 11):
        print(A[i][j])
```

The inner loop runs exactly \(10\) times regardless of \(n\). Since \(10\) is a constant:

$$10 \times n = 10n \rightarrow O(n)$$
