# Two Pointers

**Category:** Basics | **Difficulty:** 🟡 Easy

---

## Intuition

Two pointers uses two indices moving through an array — usually from both ends toward the middle, or both moving right. It reduces O(n²) brute force to O(n) for problems involving pairs or subarrays.

## Python Template

```python
# Two sum (sorted array)
def two_sum(a, target):
    l, r = 0, len(a) - 1
    while l < r:
        s = a[l] + a[r]
        if s == target:
            return l, r
        elif s < target:
            l += 1
        else:
            r -= 1
    return -1, -1

# Merge two sorted arrays (two pointer style)
def merge(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    return result + a[i:] + b[j:]
```

## Resources

- 📹 [Video — Two Pointers](https://www.youtube.com/watch?v=on0-X0h-ksg)
- 📖 [USACO Guide — Two Pointers](https://usaco.guide/silver/two-pointers)

## Problems

| # | Problem | Platform | Difficulty |
|---|---------|----------|------------|
| 1 | [Ferris Wheel](https://cses.fi/problemset/task/1090) | CSES | 🟡 Easy |
| 2 | [Apartments](https://cses.fi/problemset/task/1084) | CSES | 🟡 Easy |
| 3 | [Sum of Two Values](https://cses.fi/problemset/task/1640) | CSES | 🟡 Easy |
| 4 | [Stick Lengths](https://cses.fi/problemset/task/1074) | CSES | 🟡 Easy |
| 5 | [Sum of Three Values](https://cses.fi/problemset/task/1641) | CSES | 🟠 Medium |
