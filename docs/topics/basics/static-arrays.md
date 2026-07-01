# Static Arrays

**Category:** Basics  
**Difficulty:** 🟢 Very Easy

---

In languages such as C++, Java, and C#, arrays are created with a fixed size. Once allocated, that size does not change.

Key consequences:

- You can read an element by index in constant time.
- Traversing all elements takes linear time.
- Inserting or deleting in the middle requires shifting elements.

## Main Operations

| Operation | Time | Notes |
|---|---|---|
| Read `arr[i]` | O(1) | Direct address access |
| Traverse array | O(n) | Visit every element |
| Insert at end | O(1) | No shifting needed |
| Delete at end | O(1) | Only update logical length |
| Insert in middle | O(n) | Shift elements right |
| Delete in middle | O(n) | Shift elements left |

## Access and Traversal

Accessing `arr[i]` is fast because the index maps directly to memory. Traversing the whole array costs linear time because every element must be visited.

```python
arr = [1, 3, 5]
value = arr[1]      # O(1)

for x in arr:       # O(n)
    print(x)
```

## Deleting Elements

Deleting from the end is cheap. Deleting from the middle is expensive because the array must remain contiguous, so later elements shift left.

```python
def remove_middle(arr, i):
    for j in range(i + 1, len(arr)):
        arr[j - 1] = arr[j]
```

## Inserting Elements

Inserting at an arbitrary position: shift elements right first, then place the new value.

```python
def insert_middle(arr, i, value, length):
    for j in range(length - 1, i - 1, -1):
        arr[j + 1] = arr[j]
    arr[i] = value
```

## Practice

| # | Problem | Platform | Difficulty |
|---|---|---|---|
| 1 | [Missing Number](https://cses.fi/problemset/task/1083) | CSES | 🟢 Very Easy |
| 2 | [Increasing Array](https://cses.fi/problemset/task/1094) | CSES | 🟢 Very Easy |
| 3 | [Helpful Maths](https://codeforces.com/problemset/problem/339/A) | Codeforces | 🟢 Very Easy |
| 4 | [Permutations](https://cses.fi/problemset/task/1070) | CSES | 🟢 Easy |

## Source notes

- [Static Arrays](https://drive.google.com/open?id=1gt2PgG9IUutOKj4JCO6xsg13B9grKIIaf0z63GFYzGg)
