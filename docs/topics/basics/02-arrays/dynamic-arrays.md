# Dynamic Arrays

**Category:** Basics  
**Difficulty:** <span style="color: #059669; font-weight: 600;">● Very Easy</span>

---

Dynamic arrays are a much more common alternative to static arrays. They are useful because they can grow as elements are added. In JavaScript and Python, these are the default arrays.

Unlike static arrays, with dynamic arrays we don’t have to specify a size upon initialization. In different languages, dynamic arrays may be assigned a default size — Java being `10` and C# being `4`. Regardless, these are automatically resized at runtime as the array grows.

## Insertion at the End

When inserting at the end of a dynamic array, the next empty space is found and the element is inserted there. Consider an array of size `3` where we push elements into it until we run out of space.

```python
# Insert n in the last position of the array
def pushback(self, n):
    if self.length == self.capacity:
        self.resize()

    # insert at next empty position
    self.arr[self.length] = n
    self.length += 1
```

![Dynamic array insertion](../images/arrays/arrays-5.svg)

## Resize

Since the array is dynamic in size, we can continue to add elements. This is achieved by copying over the values to a new static array that is double the size of the original. The resulting array will have new space allocated for it in memory.

```python
def resize(self):
    # Create new array of double capacity
    self.capacity = 2 * self.capacity
    newArr = [0] * self.capacity

    # Copy elements to newArr
    for i in range(self.length):
        newArr[i] = self.arr[i]
    self.arr = newArr
```

![Resize operation](../images/arrays/arrays-6.svg)

When all elements from the first array have been copied over, the original static array is deallocated.

Adding elements to a dynamic array runs in \(O(1)\) **amortized** time. Amortized time complexity is the average time taken per operation over a sequence of operations. The resize operation itself is \(O(n)\), but since it is not performed on every insertion, the average time per operation is \(O(1)\) — but only if we double the capacity on each resize.

## Why Double the Capacity?

Imagine filling up an array of size `8` starting from a size `1` array. The capacity would grow as: `1 → 2 → 4 → 8`.

![Why double capacity](../images/arrays/arrays-7.svg)

To analyze the time complexity we must account for the **sum of all operations** that occurred before the last one. To achieve an array of size `8`:

$$1 + 2 + 4 + 8 = 15 \text{ operations}$$

The pattern is that the last (dominating) term is always greater than or equal to the sum of all terms before it:

$$1 + 2 + 4 = 7 < 8$$

Generally, for any array of size \(n\), it takes at most \(2n\) operations to create it, which belongs to \(O(n)\). Since inserting \(n\) elements is \(O(n)\), the amortized cost of a single insertion is \(O(1)\).

> With time complexity analysis we are concerned with asymptotic analysis — how quickly runtime grows as input size grows. We don’t distinguish between \(O(2n)\) and \(O(n)\) because both grow linearly. Constant terms and coefficients are dropped.

## Other Operations

Inserting or removing from the **middle** of a dynamic array works the same as a static array — elements must be shifted right or left to make space or fill the gap. This runs in \(O(n)\) time.

```python
a = []
a.append(7)      # amortized O(1)
a.pop()          # O(1)
a[i]             # O(1)
a.insert(1, 10)  # O(n) — shifts elements
a.pop(1)         # O(n) — shifts elements
```

## Time & Space Complexity

| Operation | Big-O Time | Notes |
|---|---|---|
| Access | \(O(1)\) | |
| Insertion at end | \(O(1)\)\* | Amortized; occasional resize is \(O(n)\) |
| Insertion in middle | \(O(n)\) | Shifting required |
| Deletion at end | \(O(1)\) | |
| Deletion in middle | \(O(n)\) | Shifting required |

## Useful Patterns

Arrays are often combined with:

- Frequency counting
- Prefix sums
- Two pointers
- Sliding window
- Kadane’s algorithm

---

## YouKn0wWho Academy Reference
While we prepare our written explanations for this topic, you can follow the interactive path and submit solutions directly on the YouKn0wWho Academy platform:

👉 [YouKn0wWho Academy Topic Syllabus](https://youkn0wwho.academy/topic-list)

---

## Additional Resources
### 🐍 Recommended Python Resources (First Priority)
*Python lists function as dynamic arrays. For fixed-size static arrays, pre-allocate list memory.*
  - [Python Lists & Dynamic Arrays | Real Python](https://realpython.com/python-lists-tuples/)
  - [Pre-allocating lists in Python for efficiency](https://stackoverflow.com/questions/10324831/how-to-preallocate-lists-in-python)

### 📘 Additional General & C++ Resources (Second Priority)
- [Arrays  | Tech With Tim](https://www.youtube.com/watch?v=1FVBeLD_FdE&list=PLzMcBGfZo4-lmGC8VW0iu6qfMHjy7gLQ3&index=9) ⭐ 🎥
  - [C++ Arrays | Programiz](https://www.programiz.com/cpp-programming/arrays) ⭐
  - [Passing Array to a Function in C++ Programming | Programiz](https://www.programiz.com/cpp-programming/passing-arrays-function)
  - [C++ Multidimensional Arrays | Programiz](https://www.programiz.com/cpp-programming/multidimensional-arrays)
  - [C++ pass arrays to functions | Bro Code](https://youtu.be/VQSroKMqISE)


---

## Topic Details
- **Difficulty**: Basic
- **Importance**: High
- **Phase**: Phase 0
- **Interview Topic**: Yes

---

## Curated Practice Problems
- [Max](https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/E) (ID: `gym_287309e` | Difficulty: Easy | Solves: 557)
- [Easy Fibonacci ](https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Y) (ID: `gym_287309y` | Difficulty: Easy | Solves: 552 ⭐)
- [Summation](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/A) (ID: `gym_287310a` | Difficulty: Easy | Solves: 673 ⭐)
- [Searching](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/B) (ID: `gym_287310b` | Difficulty: Easy | Solves: 638 ⭐)
- [Replacement](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/C) (ID: `gym_287310c` | Difficulty: Easy | Solves: 574)
- [Lowest Number](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/E) (ID: `gym_287310e` | Difficulty: Easy | Solves: 581 ⭐)
- [Reversing](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/F) (ID: `gym_287310f` | Difficulty: Medium | Solves: 600 ⭐)
- [Palindrome Array](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/G) (ID: `gym_287310g` | Difficulty: Medium | Solves: 575 ⭐)
- [Sorting](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/H) (ID: `gym_287310h` | Difficulty: Medium | Solves: 530 ⭐)
- [Smallest Pair](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/I) (ID: `gym_287310i` | Difficulty: Medium | Solves: 495 ⭐)
- [Max Subarray ](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/L) (ID: `gym_287310l` | Difficulty: Medium | Solves: 417 ⭐)
- [Replace MinMax](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M) (ID: `gym_287310m` | Difficulty: Medium | Solves: 453 ⭐)
- [Minimize Number](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P) (ID: `gym_287310p` | Difficulty: Medium | Solves: 427 ⭐)
- [Count Subarrays](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/Q) (ID: `gym_287310q` | Difficulty: Medium | Solves: 342)
- [Permutation with arrays](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/R) (ID: `gym_287310r` | Difficulty: Medium | Solves: 405 ⭐)
- [Search In Matrix](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/S) (ID: `gym_287310s` | Difficulty: Hard | Solves: 396 ⭐)
- [Matrix](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/T) (ID: `gym_287310t` | Difficulty: Hard | Solves: 389 ⭐)
- [Is B a subsequence of A ? ](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/U) (ID: `gym_287310u` | Difficulty: Hard | Solves: 381 ⭐)
- [Frequency Array](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/V) (ID: `gym_287310v` | Difficulty: Hard | Solves: 434 ⭐)
- [Mirror Array](https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/W) (ID: `gym_287310w` | Difficulty: Hard | Solves: 362)
- [2D Array - DS](https://vjudge.net/problem/HackerRank-2d-array) (ID: `hackerrank_2d_array` | Difficulty: Hard | Solves: 296 ⭐)

---

[Return to Home](../../../index.md)
