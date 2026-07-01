# Sliding Window

**Category:** Basics | **Difficulty:** 🟠 Medium

---

## Intuition

Sliding window maintains a window (subarray) that expands and shrinks as it moves across the array. It's the go-to technique for problems asking for the best subarray of fixed or variable size.

## Python Template

```python
# Fixed-size window (size k)
def fixed_window(a, k):
    window_sum = sum(a[:k])
    best = window_sum
    for i in range(k, len(a)):
        window_sum += a[i] - a[i-k]
        best = max(best, window_sum)
    return best

# Variable-size window (longest subarray with condition)
def variable_window(a):
    l = best = cur = 0
    seen = set()
    for r in range(len(a)):
        while a[r] in seen:   # shrink until valid
            seen.remove(a[l])
            l += 1
        seen.add(a[r])
        best = max(best, r - l + 1)
    return best
```

## Resources

- 📹 [Video — Sliding Window](https://www.youtube.com/watch?v=p-ss2JNygmA)
- 📖 [USACO Guide — Sliding Window](https://usaco.guide/silver/sliding-window)

## Problems

| # | Problem | Platform | Difficulty |
|---|---------|----------|------------|
| 1 | [Playlist](https://cses.fi/problemset/task/1141) | CSES | 🟡 Easy |
| 2 | [Towers](https://cses.fi/problemset/task/1073) | CSES | 🟡 Easy |
| 3 | [Maximum Subarray Sum II](https://cses.fi/problemset/task/1644) | CSES | 🟠 Medium |
| 4 | [Longest Subarray](https://codeforces.com/problemset/problem/1873/E) | Codeforces | 🟡 Easy |
