# Prefix Sums

**Category:** Basics | **Difficulty:** 🟡 Easy

---

## Intuition

A prefix sum array lets you answer range sum queries in O(1) after O(n) preprocessing. Instead of summing a subarray each time, you precompute cumulative sums.

## Python Template

```python
n = int(input())
a = list(map(int, input().split()))

# Build prefix sum
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + a[i]

# Query sum of a[l..r] (0-indexed, inclusive)
def query(l, r):
    return prefix[r+1] - prefix[l]

# 2D prefix sum
def build_2d(grid):
    rows, cols = len(grid), len(grid[0])
    p = [[0]*(cols+1) for _ in range(rows+1)]
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            p[i][j] = grid[i-1][j-1] + p[i-1][j] + p[i][j-1] - p[i-1][j-1]
    return p
```

## Resources

- 📹 [Video — Prefix Sums](https://www.youtube.com/watch?v=pVS3yhlzrlQ)
- 📖 [USACO Guide — Prefix Sums](https://usaco.guide/silver/prefix-sums)

## Problems

| # | Problem | Platform | Difficulty |
|---|---------|----------|------------|
| 1 | [Static Range Sum Queries](https://cses.fi/problemset/task/1646) | CSES | 🟢 Very Easy |
| 2 | [Forest Queries](https://cses.fi/problemset/task/1652) | CSES | 🟡 Easy |
| 3 | [Subarray Sums I](https://cses.fi/problemset/task/1660) | CSES | 🟡 Easy |
| 4 | [Subarray Sums II](https://cses.fi/problemset/task/1661) | CSES | 🟠 Medium |
