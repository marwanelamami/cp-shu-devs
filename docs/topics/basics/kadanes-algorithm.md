# Kadane's Algorithm

**Category:** Basics  
**Difficulty:** 🟡 Easy

---

## Problem statement

Kadane's algorithm solves the **maximum subarray sum** problem:

> Find a non-empty contiguous subarray with the largest possible sum.

This is one of the classic array problems because it reduces an O(n²) brute-force into a linear-time O(n) solution.

## Brute force

A direct approach tries every starting index and extends right while tracking the best sum.

```python
def brute_force(nums):
    best = nums[0]
    for i in range(len(nums)):
        cur = 0
        for j in range(i, len(nums)):
            cur += nums[j]
            best = max(best, cur)
    return best
```

This works but costs O(n²).

## Key insight

If the running sum becomes negative, keeping it will only hurt any future subarray. So discard it and start fresh.

Two cases:

- `[4, -1, 7]` — maximum sum is 10. We must include -1 to connect 4 and 7.
- `[1, -3, 7]` — maximum sum is 7. Including -3 just to keep the 1 is not worth it.

The rule: if the current subarray sum goes negative, reset and start a new subarray.

## Linear solution

```python
def kadane(nums):
    max_sum = nums[0]
    cur_sum = 0

    for x in nums:
        cur_sum = max(cur_sum, 0)  # reset if negative
        cur_sum += x
        max_sum = max(max_sum, cur_sum)

    return max_sum
```

`cur_sum` always holds the best subarray sum ending at the current position. Initializing `max_sum` from `nums[0]` (not zero) handles the all-negative case correctly.

## Returning the actual subarray

To return the interval, track a left pointer and update the best bounds whenever a new maximum is found.

```python
def kadane_window(nums):
    max_sum = nums[0]
    cur_sum = 0
    left = 0
    best_l = best_r = 0

    for right in range(len(nums)):
        if cur_sum < 0:
            cur_sum = 0
            left = right

        cur_sum += nums[right]

        if cur_sum > max_sum:
            max_sum = cur_sum
            best_l, best_r = left, right

    return max_sum, best_l, best_r
```

## Complexity

| Metric | Value |
|---|---|
| Time | O(n) — single pass |
| Space | O(1) — only a few variables |

## Connection to sliding window

The version that returns the subarray is essentially a variable-size sliding window. When the constraint (non-negative sum) is broken, the left pointer jumps to the current position. This pattern appears repeatedly in other sliding window problems.

## Practice

| # | Problem | Platform | Difficulty |
|---|---|---|---|
| 1 | [Maximum Subarray Sum](https://cses.fi/problemset/task/1643) | CSES | 🟡 Easy |
| 2 | [Maximum Subarray Sum II](https://cses.fi/problemset/task/1644) | CSES | 🟠 Medium |
| 3 | [Lamps](https://codeforces.com/problemset/problem/363/B) | Codeforces | 🟡 Easy |

## Source notes

- [Kadane's Algorithm Notes](https://drive.google.com/open?id=1x_W1epn7zn5XrAVJlgyh-1k2IvYaCP5ILcVTpFECeUY)
