# Dynamic Arrays

**Category:** Basics  
**Difficulty:** 🟢 Very Easy

---

Python lists behave like dynamic arrays — they grow automatically when more space is needed. When the internal storage fills up, a larger array is allocated and old elements are copied over.

This resize step is expensive by itself, but it does not happen on every insertion. That is why appending is **amortized O(1)**: over many appends, the average cost per append stays constant.

## Why Amortized O(1)?

When capacity doubles on each resize, building an array of size n takes at most 2n total operations. Even though one resize costs O(n), repeated appends average out to O(1) each.

```python
a = []
a.append(7)      # amortized O(1)
a.pop()          # O(1)
a[i]             # O(1)
a.insert(1, 10)  # O(n) — shifts elements
a.pop(1)         # O(n) — shifts elements
```

## Complexity

| Operation | Time | Notes |
|---|---|---|
| Access | O(1) | |
| Append | O(1)* | Amortized; occasional resize is O(n) |
| Insert in middle | O(n) | Shifting required |
| Delete in middle | O(n) | Shifting required |

## Useful Patterns

Arrays are often combined with:

- Frequency counting
- Prefix sums
- Two pointers
- Sliding window
- Kadane's algorithm

## Practice

| # | Problem | Platform | Difficulty |
|---|---|---|---|
| 1 | [Maximum Subarray Sum](https://cses.fi/problemset/task/1643) | CSES | 🟢 Easy |

## Source notes

- [Dynamic Arrays](https://docs.google.com/document/d/10m3mg6DnY-lYkePVDlsE_TYkiYws5x2r4jg5S-pYtEg/edit?usp=drive_link)
