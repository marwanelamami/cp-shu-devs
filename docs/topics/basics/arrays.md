# Arrays

**Category:** Basics | **Difficulty:** 🟢 Very Easy

---

## Key Concepts

- Indexing, iteration, slicing
- Searching and sorting
- Subarrays vs subsequences
- Frequency arrays

## Python Template

```python
# Read array
n = int(input())
a = list(map(int, input().split()))

# Frequency array
from collections import Counter
freq = Counter(a)

# Prefix sum
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + a[i]

# Sum of subarray [l, r] (0-indexed)
def range_sum(l, r):
    return prefix[r+1] - prefix[l]
```

## Resources

- 📹 [Video — Arrays (Arabic)](https://www.youtube.com/watch?v=jJVaDl_dePk)
- 📖 [Arrays Blog](https://cp-algorithms.com/)

## Problems

| # | Problem | Platform | Difficulty |
|---|---------|----------|------------|
| 1 | [Missing Number](https://cses.fi/problemset/task/1083) | CSES | 🟢 Very Easy |
| 2 | [Increasing Array](https://cses.fi/problemset/task/1094) | CSES | 🟢 Very Easy |
| 3 | [Helpful Maths](https://codeforces.com/problemset/problem/339/A) | Codeforces | 🟢 Very Easy |
| 4 | [Permutations](https://cses.fi/problemset/task/1070) | CSES | 🟡 Easy |
| 5 | [Maximum Subarray Sum](https://cses.fi/problemset/task/1643) | CSES | 🟡 Easy |
