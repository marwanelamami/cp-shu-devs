# Intro to CP & Complexity

**Category:** Basics  
**Difficulty:** 🟢 Very Easy

---

## What competitive programming is

Competitive programming is the practice of solving clearly specified algorithmic problems under strict time and memory limits. Your solution is judged automatically against hidden tests, so the goal is not only correctness but also efficiency and robustness.

Two skills are trained at the same time:

- Designing algorithms: choosing the right idea and reasoning about why it works.
- Implementing them well: writing code that is correct, fast, and safe under pressure.

## Why it matters

This style of problem solving builds mathematical thinking, pattern recognition, and disciplined implementation. It also mirrors the kind of reasoning tested in technical interviews and programming contests.

## The online judge model

Most competitive programming happens on an online judge such as Codeforces or CSES.

The workflow is simple:

1. Read the statement and constraints carefully.
2. Design an algorithm that is correct and fast enough.
3. Implement it.
4. Submit it.
5. Receive a verdict.

Common verdicts:

| Verdict | Meaning |
|---|---|
| Accepted | Correct output within limits |
| Wrong Answer | Incorrect output on at least one test |
| Time Limit Exceeded | Logic may be correct, but too slow |
| Runtime Error | Program crashed during execution |
| Compilation Error | Code did not compile |

There is no partial credit. A solution either passes all tests or it does not.

## Algorithms and data structures

An **algorithm** is the sequence of steps used to solve a problem. A **data structure** is the way data is organized so those steps can be done efficiently.

The same problem can become easy or hard depending on the data structure you choose. In competitive programming, strong solutions usually come from matching the right algorithm with the right structure.

## Measuring efficiency

We usually measure efficiency in terms of the input size `n`. Instead of counting seconds directly, we count how the number of operations grows as `n` grows.

Examples:

- A single array access is constant time.
- A full traversal over an array is linear time.
- A nested loop over all pairs is often quadratic time.

If an algorithm performs n² + n + 2 operations, we describe it as O(n²), because the dominant growth term matters most for large input sizes.

## Big-O notation

Big-O is an upper bound on how runtime grows.

| Complexity | Name | Max n safe in ~1s |
|---|---|---|
| O(1) | Constant | Any |
| O(log n) | Logarithmic | Any |
| O(n) | Linear | ~10⁸ |
| O(n log n) | Linearithmic | ~10⁷ |
| O(n²) | Quadratic | ~10⁴ |
| O(2ⁿ) | Exponential | ~20 |
| O(n!) | Factorial | ~12 |

## Small examples

- One loop over n elements → O(n).
- Two separate loops over n → still O(n), not O(n²).
- A loop inside a loop over n → usually O(n²).
- An inner loop that always runs exactly 10 times → still O(n) overall.

```python
# O(n)
for i in range(n):
    print(i)

# O(n) — two loops, not nested
for i in range(n):
    print(i)
for i in range(n):
    print(i)

# O(n²) — nested loops
for i in range(n):
    for j in range(n):
        print(i, j)

# Still O(n) — inner loop is constant
for i in range(n):
    for j in range(10):
        print(i, j)
```

## Practice

| # | Problem | Platform | Difficulty |
|---|---|---|---|
| 1 | [Watermelon](https://codeforces.com/problemset/problem/4/A) | Codeforces | 🟢 Very Easy |
| 2 | [Way Too Long Words](https://codeforces.com/problemset/problem/71/A) | Codeforces | 🟢 Very Easy |
| 3 | [Team](https://codeforces.com/problemset/problem/231/A) | Codeforces | 🟢 Very Easy |

## Source notes

- [Session 1 Slides](https://drive.google.com/open?id=1qLEuowC8HPBUd8VHO-lth6u3nothMG3L)
