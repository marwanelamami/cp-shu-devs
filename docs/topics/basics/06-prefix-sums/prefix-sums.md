# Prefix Sums

**Category:** Basics  
**Difficulty:** 🟢 Easy

---

A prefix sum is a super useful technique that can be used with arrays. Suppose we have an array `nums = [2, -1, 3, -3, 4]`. The basic idea here is that we create an array, say, `prefix`, and fill it up such that the value at its $i$-th index denotes the running sum of a `nums` subarray that starts from $0$ and goes up to and including the $i$-th index. This is extremely useful when we want to retrieve the sum of a subarray ending at an arbitrary index, say $i$.

So, given an array `[2, -1, 3, -3, 4]`, the prefix sum array would be `[2, 1, 4, 1, 5]`.

## Range Sum Query Example

> **Q: Given an array of values, design a data structure that can query the sum of a subarray of the values.**

First, let's build our prefix sum. We can do this in a class called `PrefixSum`, which will take the array `nums` that we want to build a prefix sum for. We can then add each of the numbers in `nums` to a variable called `total` and append the `total` to our `prefix` array at each iteration.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <defs>
    <style>
      /* Default / Light mode styles */
      .label { font-family: 'Courier New', Courier, monospace; font-size: 16px; font-weight: bold; fill: #1e293b; letter-spacing: 1px; }
      .box { fill: #f8fafc; stroke: #475569; stroke-width: 1.5px; rx: 2px; }
      .val { font-family: 'Courier New', Courier, monospace; font-size: 18px; font-weight: bold; fill: #1e293b; text-anchor: middle; dominant-baseline: middle; }
      .arrow-path { fill: none; stroke: #475569; stroke-width: 1.5px; stroke-dasharray: 4,4; marker-end: url(#arrow); }
      .arrow-head { fill: #475569; }

      /* Slate / Dark mode styles */
      [data-md-color-scheme="slate"] .label { fill: #ffffff; }
      [data-md-color-scheme="slate"] .box { fill: #1e1e1e; stroke: #ffffff; }
      [data-md-color-scheme="slate"] .val { fill: #ffffff; }
      [data-md-color-scheme="slate"] .arrow-path { stroke: #ffffff; }
      [data-md-color-scheme="slate"] .arrow-head { fill: #ffffff; }

      /* Animation Keyframes */
      @keyframes active-step-0 {
        0%, 16.66% { opacity: 1; }
        16.67%, 100% { opacity: 0; }
      }
      @keyframes active-step-1 {
        0%, 16.66% { opacity: 0; }
        16.67%, 33.33% { opacity: 1; }
        33.34%, 100% { opacity: 0; }
      }
      @keyframes active-step-2 {
        0%, 33.33% { opacity: 0; }
        33.34%, 50% { opacity: 1; }
        50.01%, 100% { opacity: 0; }
      }
      @keyframes active-step-3 {
        0%, 50% { opacity: 0; }
        50.01%, 66.66% { opacity: 1; }
        66.67%, 100% { opacity: 0; }
      }
      @keyframes active-step-4 {
        0%, 66.66% { opacity: 0; }
        66.67%, 83.33% { opacity: 1; }
        83.34%, 100% { opacity: 0; }
      }

      /* Visibility keyframes for prefix values */
      @keyframes show-val-0 {
        0%, 100% { opacity: 1; }
      }
      @keyframes show-val-1 {
        0%, 16.66% { opacity: 0; }
        16.67%, 100% { opacity: 1; }
      }
      @keyframes show-val-2 {
        0%, 33.33% { opacity: 0; }
        33.34%, 100% { opacity: 1; }
      }
      @keyframes show-val-3 {
        0%, 50% { opacity: 0; }
        50.01%, 100% { opacity: 1; }
      }
      @keyframes show-val-4 {
        0%, 66.66% { opacity: 0; }
        66.67%, 100% { opacity: 1; }
      }

      /* Highlight borders of nums boxes */
      @keyframes border-nums-0 {
        0%, 83.33% { stroke: #ff3860; stroke-width: 3px; filter: drop-shadow(0 0 3px #ff3860); }
        83.34%, 100% { stroke: inherit; stroke-width: inherit; filter: none; }
      }
      @keyframes border-nums-1 {
        0%, 16.66% { stroke: inherit; stroke-width: inherit; filter: none; }
        16.67%, 83.33% { stroke: #ff3860; stroke-width: 3px; filter: drop-shadow(0 0 3px #ff3860); }
        83.34%, 100% { stroke: inherit; stroke-width: inherit; filter: none; }
      }
      @keyframes border-nums-2 {
        0%, 33.33% { stroke: inherit; stroke-width: inherit; filter: none; }
        33.34%, 83.33% { stroke: #ff3860; stroke-width: 3px; filter: drop-shadow(0 0 3px #ff3860); }
        83.34%, 100% { stroke: inherit; stroke-width: inherit; filter: none; }
      }
      @keyframes border-nums-3 {
        0%, 50% { stroke: inherit; stroke-width: inherit; filter: none; }
        50.01%, 83.33% { stroke: #ff3860; stroke-width: 3px; filter: drop-shadow(0 0 3px #ff3860); }
        83.34%, 100% { stroke: inherit; stroke-width: inherit; filter: none; }
      }
      @keyframes border-nums-4 {
        0%, 66.66% { stroke: inherit; stroke-width: inherit; filter: none; }
        66.67%, 83.33% { stroke: #ff3860; stroke-width: 3px; filter: drop-shadow(0 0 3px #ff3860); }
        83.34%, 100% { stroke: inherit; stroke-width: inherit; filter: none; }
      }

      .nums-box-0 { animation: border-nums-0 12s infinite; }
      .nums-box-1 { animation: border-nums-1 12s infinite; }
      .nums-box-2 { animation: border-nums-2 12s infinite; }
      .nums-box-3 { animation: border-nums-3 12s infinite; }
      .nums-box-4 { animation: border-nums-4 12s infinite; }

      .val-prefix-0 { animation: show-val-0 12s infinite; }
      .val-prefix-1 { animation: show-val-1 12s infinite; }
      .val-prefix-2 { animation: show-val-2 12s infinite; }
      .val-prefix-3 { animation: show-val-3 12s infinite; }
      .val-prefix-4 { animation: show-val-4 12s infinite; }

      .step-0-group { animation: active-step-0 12s infinite; }
      .step-1-group { animation: active-step-1 12s infinite; }
      .step-2-group { animation: active-step-2 12s infinite; }
      .step-3-group { animation: active-step-3 12s infinite; }
      .step-4-group { animation: active-step-4 12s infinite; }
    </style>
    
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" class="arrow-head" />
    </marker>
  </defs>

  <!-- Labels -->
  <text x="300" y="55" text-anchor="middle" class="label">nums</text>
  <text x="300" y="265" text-anchor="middle" class="label">prefix</text>

  <!-- Nums Array Boxes -->
  <rect x="163" y="80" width="50" height="50" class="box nums-box-0" />
  <rect x="219" y="80" width="50" height="50" class="box nums-box-1" />
  <rect x="275" y="80" width="50" height="50" class="box nums-box-2" />
  <rect x="331" y="80" width="50" height="50" class="box nums-box-3" />
  <rect x="387" y="80" width="50" height="50" class="box nums-box-4" />

  <!-- Nums Array Values -->
  <text x="188" y="105" class="val">2</text>
  <text x="244" y="105" class="val">-1</text>
  <text x="300" y="105" class="val">3</text>
  <text x="356" y="105" class="val">-3</text>
  <text x="412" y="105" class="val">4</text>

  <!-- Prefix Array Boxes -->
  <rect x="163" y="190" width="50" height="50" class="box" />
  <rect x="219" y="190" width="50" height="50" class="box" />
  <rect x="275" y="190" width="50" height="50" class="box" />
  <rect x="331" y="190" width="50" height="50" class="box" />
  <rect x="387" y="190" width="50" height="50" class="box" />

  <!-- Prefix Array Values -->
  <text x="188" y="215" class="val val-prefix-0">2</text>
  <text x="244" y="215" class="val val-prefix-1">1</text>
  <text x="300" y="215" class="val val-prefix-2">4</text>
  <text x="356" y="215" class="val val-prefix-3">1</text>
  <text x="412" y="215" class="val val-prefix-4">5</text>

  <!-- Step 0 Arrows (nums[0] -> prefix[0]) -->
  <g class="step-0-group">
    <path d="M 188,130 L 188,184" class="arrow-path" />
  </g>

  <!-- Step 1 Arrows (nums[0..1] -> prefix[1]) -->
  <g class="step-1-group">
    <path d="M 188,130 C 188,160 240,160 242,184" class="arrow-path" />
    <path d="M 244,130 C 244,160 248,160 246,184" class="arrow-path" />
  </g>

  <!-- Step 2 Arrows (nums[0..2] -> prefix[2]) -->
  <g class="step-2-group">
    <path d="M 188,130 C 188,170 294,155 296,184" class="arrow-path" />
    <path d="M 244,130 C 244,170 298,160 299,184" class="arrow-path" />
    <path d="M 300,130 C 300,170 302,165 301,184" class="arrow-path" />
  </g>

  <!-- Step 3 Arrows (nums[0..3] -> prefix[3]) -->
  <g class="step-3-group">
    <path d="M 188,130 C 188,170 350,155 352,184" class="arrow-path" />
    <path d="M 244,130 C 244,170 352,160 353,184" class="arrow-path" />
    <path d="M 300,130 C 300,170 354,165 355,184" class="arrow-path" />
    <path d="M 356,130 C 356,170 358,168 357,184" class="arrow-path" />
  </g>

  <!-- Step 4 Arrows (nums[0..4] -> prefix[4]) -->
  <g class="step-4-group">
    <path d="M 188,130 C 188,175 406,155 408,184" class="arrow-path" />
    <path d="M 244,130 C 244,175 408,160 409,184" class="arrow-path" />
    <path d="M 300,130 C 300,175 410,165 410,184" class="arrow-path" />
    <path d="M 356,130 C 356,175 412,170 411,184" class="arrow-path" />
    <path d="M 412,130 C 412,175 414,172 413,184" class="arrow-path" />
  </g>
</svg>

```python
class PrefixSum:

    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
```

After building this sum, we can calculate the sum of any subarray that starts at `left` and ends at `right` in $O(1)$ time.

We can do this by `prefix[right] - prefix[left - 1]`. The `- 1` will ensure we exclude the running sum of all the numbers before `left`. However, if `left` points to `0`, to avoid an index out of bounds error, we can use a ternary operator to check if `left` is `0` in which case we will return `0` as a substitute for `prefix[left - 1]`.

```python
    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return preRight - preLeft
```

Let's visualize how prefix sum is calculated in $O(1)$ time where `L = 2` and `R = 3` and the case where `L = 0` and `R = 3` (where no prefix exists for the first element).

![Prefix Sum Range Visualization](../images/prefix-sums/prefix-sums-1.svg)

## Time & Space Complexity

### Time Complexity
The time complexity to build the initial prefix sum is $O(n)$. However, to calculate a range sum, we will only perform $O(1)$ operations no matter how large the array is.

### Space Complexity
The space complexity to store the prefix sum array is $O(n)$. If we don't need the initial array, we can actually overwrite it with its prefix sum, which will bring the space complexity down from $O(n)$ to $O(1)$. This works because the size of an array's prefix sums will be the same as the size of the array.

## Closing Notes

It should also be noted that sum is not the only operation we can perform using this technique. We can also calculate a prefix product and other prefix operations.

We can also do the opposite and get a **postfix sum**, which would be a running sum of all the elements starting from the end of the array and going backwards.
