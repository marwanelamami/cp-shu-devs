# Kadane's Algorithm

**Category:** Basics | **Difficulty:** 🟡 Easy

---

## Intuition

Kadane's algorithm finds the maximum sum subarray in O(n) by tracking the best sum ending at each position. At every index, you decide: extend the previous subarray or start fresh.

## Python Template

```python
def kadane(a):
    max_sum = cur = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        max_sum = max(max_sum, cur)
    return max_sum

n = int(input())
a = list(map(int, input().split()))
print(kadane(a))
```

## Resources

- 📹 [Video — Kadane's Algorithm](https://www.youtube.com/watch?v=86CQq3pKSUw)
- 📖 [CP-Algorithms — Maximum Subarray](https://cp-algorithms.com/others/maximum_average_segment.html)

## Problems

| # | Problem | Platform | Difficulty |
|---|---------|----------|------------|
| 1 | [Maximum Subarray Sum](https://cses.fi/problemset/task/1643) | CSES | 🟡 Easy |
| 2 | [Maximum Subarray Sum II](https://cses.fi/problemset/task/1644) | CSES | 🟠 Medium |
| 3 | [Lamps](https://codeforces.com/problemset/problem/363/B) | Codeforces | 🟡 Easy |
