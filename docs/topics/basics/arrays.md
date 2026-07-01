# Arrays

**Category:** Basics  
**Difficulty:** 🟢 Very Easy

---

## Core idea

An array stores elements in contiguous positions and gives direct access by index. Arrays are one of the most important building blocks in competitive programming because many techniques start with scanning, counting, or transforming a sequence.

## Static arrays

In languages such as C++, Java, and C#, arrays are created with a fixed size. Once allocated, that size does not change.

Key consequences:

- You can read an element by index in constant time.
- Traversing all elements takes linear time.
- Inserting or deleting in the middle requires shifting elements.

### Main operations

| Operation | Time | Notes |
|---|---|---|
| Read `arr[i]` | O(1) | Direct address access |
| Traverse array | O(n) | Visit every element |
| Insert at end | O(1) | No shifting needed |
| Delete at end | O(1) | Only update logical length |
| Insert in middle | O(n) | Shift elements right |
| Delete in middle | O(n) | Shift elements left |

## Access and traversal

Accessing `arr[i]` is fast because the index maps directly to memory. Traversing the whole array costs linear time because every element must be visited.

```python
arr = [1, 3, 5]
value = arr[1]      # O(1)

for x in arr:       # O(n)
    print(x)
```

## Deleting elements

Deleting from the end is cheap. Deleting from the middle is expensive because the array must remain contiguous, so later elements shift left.

```python
def remove_middle(arr, i):
    for j in range(i + 1, len(arr)):
        arr[j - 1] = arr[j]
```

## Inserting elements

Inserting at an arbitrary position: shift elements right first, then place the new value.

```python
def insert_middle(arr, i, value, length):
    for j in range(length - 1, i - 1, -1):
        arr[j + 1] = arr[j]
    arr[i] = value
```

## Dynamic arrays

Python lists behave like dynamic arrays — they grow automatically when more space is needed. When the internal storage fills up, a larger array is allocated and old elements are copied over.

This resize step is expensive by itself, but it does not happen on every insertion. That is why appending is **amortized O(1)**: over many appends, the average cost per append stays constant.

### Why amortized O(1)?

When capacity doubles on each resize, building an array of size n takes at most 2n total operations. Even though one resize costs O(n), repeated appends average out to O(1) each.

```python
a = []
a.append(7)   # amortized O(1)
a.pop()       # O(1)
a[i]          # O(1)
a.insert(1, 10)  # O(n) — shifts elements
a.pop(1)         # O(n) — shifts elements
```

## Dynamic array complexity

| Operation | Time | Notes |
|---|---|---|
| Access | O(1) | |
| Append | O(1)* | Amortized; occasional resize is O(n) |
| Insert in middle | O(n) | Shifting required |
| Delete in middle | O(n) | Shifting required |

## Useful patterns

Arrays are often combined with:

- Frequency counting
- Prefix sums
- Two pointers
- Sliding window
- Kadane's algorithm

## Practice

| # | Problem | Platform | Difficulty |
|---|---|---|---|
| 1 | [Missing Number](https://cses.fi/problemset/task/1083) | CSES | 🟢 Very Easy |
| 2 | [Increasing Array](https://cses.fi/problemset/task/1094) | CSES | 🟢 Very Easy |
| 3 | [Helpful Maths](https://codeforces.com/problemset/problem/339/A) | Codeforces | 🟢 Very Easy |
| 4 | [Permutations](https://cses.fi/problemset/task/1070) | CSES | 🟡 Easy |
| 5 | [Maximum Subarray Sum](https://cses.fi/problemset/task/1643) | CSES | 🟡 Easy |

## Source notes

- [Static Arrays](https://drive.google.com/open?id=1gt2PgG9IUutOKj4JCO6xsg13B9grKIIaf0z63GFYzGg)
- [Dynamic Arrays](https://docs.google.com/document/d/10m3mg6DnY-lYkePVDlsE_TYkiYws5x2r4jg5S-pYtEg/edit?usp=drive_link)
