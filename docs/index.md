---
hide:
  - navigation
  - toc
---

# CP Playbook

Welcome to the CP Playbook, a structured curriculum and collection of training resources maintained by the SHU Developers Club. This handbook provides organized notes, optimized code implementations, complexity analysis, and curated practice tasks to help you prepare for competitive programming contests, including LCPC and ICPC.

---

## Interactive Syllabus Roadmap

Use the accordion menu below to explore the topics in sequence. Click on any active category or subcategory to expand it, and click on any topic to go directly to its guidebook notes.

<style>
  .rm-container {
    margin: 1.5rem 0;
    max-width: 100%;
  }
  .rm-legend {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
    font-size: 0.85rem;
    align-items: center;
  }
  .rm-legend-item {
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }
  .rm-legend-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
  }
  
  .rm-category {
    border: 1px solid var(--md-typeset-color, #e2e8f0);
    border-radius: 6px;
    margin-bottom: 0.75rem;
    background: var(--md-card-background, #ffffff);
    overflow: hidden;
  }
  .rm-category-header {
    padding: 0.85rem 1.25rem;
    background: var(--md-default-bg-color, #f8fafc);
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    font-weight: 600;
    user-select: none;
    transition: background 0.15s ease;
  }
  .rm-category-header:hover {
    background: var(--md-default-bg-color-hover, #f1f5f9);
  }
  .rm-category.open .rm-category-header {
    border-bottom: 1px solid var(--md-typeset-color, #e2e8f0);
  }
  .rm-category-title {
    font-size: 0.95rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  .rm-category-badge {
    font-size: 0.7rem;
    padding: 0.1rem 0.4rem;
    border-radius: 9999px;
    background: #e0e7ff;
    color: #4f46e5;
    font-weight: 500;
  }
  .rm-category.disabled {
    opacity: 0.6;
  }
  .rm-category.disabled .rm-category-header {
    cursor: not-allowed;
  }
  .rm-category.disabled .rm-category-badge {
    background: #f1f5f9;
    color: #64748b;
  }
  .rm-category-content {
    display: none;
    padding: 1rem 1.25rem;
  }
  .rm-category.open .rm-category-content {
    display: block;
  }
  .rm-toggle-icon {
    font-size: 1.1rem;
    color: #64748b;
    font-weight: bold;
  }

  .rm-subcategory {
    margin-bottom: 1.25rem;
    border-left: 2px solid #cbd5e1;
    padding-left: 1rem;
  }
  .rm-subcategory:last-child {
    margin-bottom: 0.5rem;
  }
  .rm-subcategory-title {
    font-weight: 600;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
    color: var(--md-typeset-color, #334155);
    display: flex;
    justify-content: space-between;
    cursor: pointer;
    user-select: none;
  }
  .rm-subcategory-content {
    display: none;
  }
  .rm-subcategory.open .rm-subcategory-content {
    display: block;
  }
  
  .rm-topics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 0.5rem;
    margin-top: 0.5rem;
  }
  .rm-topic {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 0.75rem;
    border: 1px solid var(--md-typeset-color, #e2e8f0);
    border-radius: 4px;
    background: var(--md-default-bg-color, #ffffff);
    text-decoration: none !important;
    color: var(--md-typeset-color, #1e293b) !important;
    font-size: 0.85rem;
    font-weight: 500;
    transition: all 0.15s ease;
  }
  .rm-topic:hover {
    border-color: #3b82f6;
    background: #eff6ff;
    color: #1d4ed8 !important;
  }
  
  .rm-badge {
    font-size: 0.65rem;
    font-weight: 600;
    padding: 0.1rem 0.35rem;
    border-radius: 3px;
    color: #ffffff;
    text-transform: uppercase;
    letter-spacing: 0.025em;
  }
  .rm-badge.high { background: #ef4444; }
  .rm-badge.medium { background: #f59e0b; }
  .rm-badge.low { background: #10b981; }

  /* Dark mode overrides */
  [data-md-color-scheme="slate"] .rm-category {
    background: #1e293b;
    border-color: #334155;
  }
  [data-md-color-scheme="slate"] .rm-category-header {
    background: #0f172a;
  }
  [data-md-color-scheme="slate"] .rm-category-header:hover {
    background: #1e293b;
  }
  [data-md-color-scheme="slate"] .rm-category.open .rm-category-header {
    border-bottom-color: #334155;
  }
  [data-md-color-scheme="slate"] .rm-category.disabled .rm-category-badge {
    background: #334155;
    color: #94a3b8;
  }
  [data-md-color-scheme="slate"] .rm-subcategory {
    border-left-color: #475569;
  }
  [data-md-color-scheme="slate"] .rm-topic {
    background: #0f172a;
    border-color: #334155;
    color: #cbd5e1 !important;
  }
  [data-md-color-scheme="slate"] .rm-topic:hover {
    border-color: #3b82f6;
    background: #1e293b;
    color: #60a5fa !important;
  }
</style>

<div class="rm-container">
  <div class="rm-legend">
    <div class="rm-legend-item">
      <span class="rm-legend-dot" style="background:#ef4444;"></span>
      <span>High Importance</span>
    </div>
    <div class="rm-legend-item">
      <span class="rm-legend-dot" style="background:#f59e0b;"></span>
      <span>Medium Importance</span>
    </div>
    <div class="rm-legend-item">
      <span class="rm-legend-dot" style="background:#10b981;"></span>
      <span>Low Importance</span>
    </div>
  </div>

  <!-- Basics Category -->
  <div class="rm-category open" id="cat-basics">
    <div class="rm-category-header" onclick="toggleCategory(this)">
      <span class="rm-category-title">Basics <span class="rm-category-badge">Active</span></span>
      <span class="rm-toggle-icon">−</span>
    </div>
    <div class="rm-category-content">
      
      <!-- Subcategory: Intro to Programming -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Intro to Programming</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/01-intro-to-programming/intro-to-programming/" class="rm-topic">
              <span>What is Programming?</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Learn a Language -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Learn a Language</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/02-learn-a-language/intro-to-cpp/" class="rm-topic">
              <span>Intro to C++ & Environment</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/02-learn-a-language/variables-and-data-types/" class="rm-topic">
              <span>Data Types, Variables & I/O</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/02-learn-a-language/operators/" class="rm-topic">
              <span>Operators</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/02-learn-a-language/conditional-statements/" class="rm-topic">
              <span>Conditional Statements</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/02-learn-a-language/loops/" class="rm-topic">
              <span>Loops</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/02-learn-a-language/functions/" class="rm-topic">
              <span>Functions</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/02-learn-a-language/arrays/" class="rm-topic">
              <span>Arrays</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/02-learn-a-language/strings/" class="rm-topic">
              <span>Strings</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/02-learn-a-language/pointers/" class="rm-topic">
              <span>Pointers & References</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/02-learn-a-language/structures/" class="rm-topic">
              <span>Structures</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Intro to Competitive Programming -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Intro to Competitive Programming</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/03-intro-to-cp/intro-to-cp/" class="rm-topic">
              <span>What is Competitive Programming?</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Bitwise Thinking -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Bitwise Thinking</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/04-bitwise-thinking/bitwise-operations/" class="rm-topic">
              <span>Bitwise Operations & Bitmasks</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Complexity Analysis -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Complexity Analysis</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/05-complexity-analysis/complexity-analysis/" class="rm-topic">
              <span>Big O & Complexity Analysis</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/05-complexity-analysis/fast-input-output/" class="rm-topic">
              <span>Fast Input Output</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Recursion -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Recursion</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/06-recursion/recursion/" class="rm-topic">
              <span>Recursion Foundations</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Very Basic Math -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Very Basic Math</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/07-very-basic-math/divisors/" class="rm-topic">
              <span>Divisors</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/07-very-basic-math/gcd-and-lcm/" class="rm-topic">
              <span>GCD & LCM</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/07-very-basic-math/harmonic-series/" class="rm-topic">
              <span>Harmonic Series</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Range Queries Without Updates -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Range Queries Without Updates</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/08-range-queries-without-updates/prefix-sum/" class="rm-topic">
              <span>Prefix Sum</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/08-range-queries-without-updates/prefix-xor/" class="rm-topic">
              <span>Prefix XOR</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Standard Template Library (STL) -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Standard Template Library (STL)</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/09-stl/stl-intro/" class="rm-topic">
              <span>Intro to STL & Iterators</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/09-stl/pairs-and-tuples/" class="rm-topic">
              <span>Pairs & Tuples</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/09-stl/vector/" class="rm-topic">
              <span>Vector</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/09-stl/stack/" class="rm-topic">
              <span>Stack</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/09-stl/queue/" class="rm-topic">
              <span>Queue</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/09-stl/priority-queue/" class="rm-topic">
              <span>Priority Queue / Heap</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/09-stl/deque/" class="rm-topic">
              <span>Deque</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/09-stl/set/" class="rm-topic">
              <span>Set & Multiset</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/09-stl/map/" class="rm-topic">
              <span>Map & Unordered Map</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/09-stl/bitset/" class="rm-topic">
              <span>Bitset</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/09-stl/list/" class="rm-topic">
              <span>List / Linked List</span>
              <span class="rm-badge medium">Med</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Leveraging Monotonicity -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Leveraging Monotonicity</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/10-leveraging-monotonicity/binary-search/" class="rm-topic">
              <span>Binary Search</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/10-leveraging-monotonicity/two-pointers/" class="rm-topic">
              <span>Two Pointers</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Basic Sorting Algorithms -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Basic Sorting Algorithms</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/11-basic-sorting-algorithms/bubble-sort/" class="rm-topic">
              <span>Bubble Sort</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/11-basic-sorting-algorithms/selection-sort/" class="rm-topic">
              <span>Selection Sort</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/11-basic-sorting-algorithms/insertion-sort/" class="rm-topic">
              <span>Insertion Sort</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/11-basic-sorting-algorithms/counting-sort/" class="rm-topic">
              <span>Counting Sort</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/11-basic-sorting-algorithms/merge-sort/" class="rm-topic">
              <span>Merge Sort</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/11-basic-sorting-algorithms/quick-sort/" class="rm-topic">
              <span>Quick Sort</span>
              <span class="rm-badge medium">Med</span>
            </a>
            <a href="topics/basics/11-basic-sorting-algorithms/radix-sort/" class="rm-topic">
              <span>Radix Sort</span>
              <span class="rm-badge low">Low</span>
            </a>
            <a href="topics/basics/11-basic-sorting-algorithms/stl-sort/" class="rm-topic">
              <span>STL Sort & Comparators</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Divide & Conquer -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Divide & Conquer</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/12-divide-and-conquer/divide-and-conquer/" class="rm-topic">
              <span>Divide & Conquer</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Greedy & Constructive -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Greedy & Constructive</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/13-greedy-and-constructive/greedy-algorithms/" class="rm-topic">
              <span>Greedy Algorithms</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/13-greedy-and-constructive/constructive-algorithms/" class="rm-topic">
              <span>Constructive Algorithms</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: 2D Prefix Sum -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>2D Prefix Sum</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/14-2d-prefix-sum/2d-prefix-sum/" class="rm-topic">
              <span>2D Prefix Sum</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: More Techniques -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>More Techniques</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/15-more-techniques/difference-array/" class="rm-topic">
              <span>Difference Array</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/15-more-techniques/sliding-window/" class="rm-topic">
              <span>Sliding Window</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Bit Manipulation -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Bit Manipulation</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/16-bit-manipulation/bit-manipulation/" class="rm-topic">
              <span>Bit Manipulation</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/16-bit-manipulation/the-xor-trick/" class="rm-topic">
              <span>The XOR Trick</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Basic Modular Arithmetic -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Basic Modular Arithmetic</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/17-basic-modular-arithmetic/binary-exponentiation/" class="rm-topic">
              <span>Binary Exponentiation</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/17-basic-modular-arithmetic/fermats-little-theorem/" class="rm-topic">
              <span>Fermat & Modular Inverse</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Basic Counting -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Basic Counting</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/18-basic-counting/permutations-and-combinations/" class="rm-topic">
              <span>Combinatorics Basics (nCr)</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/18-basic-counting/stars-and-bars/" class="rm-topic">
              <span>Stars & Bars</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/18-basic-counting/pigeonhole-principle/" class="rm-topic">
              <span>Pigeonhole Principle</span>
              <span class="rm-badge medium">Med</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Very Basic Graphs -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Very Basic Graphs</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/19-very-basic-graphs/graph-representations/" class="rm-topic">
              <span>Introduction & Representation</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- Disabled/Soon Categories -->
  <div class="rm-category disabled">
    <div class="rm-category-header">
      <span class="rm-category-title">Data Structures (DS) <span class="rm-category-badge">Coming Soon</span></span>
    </div>
  </div>
  <div class="rm-category disabled">
    <div class="rm-category-header">
      <span class="rm-category-title">Graph Theory <span class="rm-category-badge">Coming Soon</span></span>
    </div>
  </div>
  <div class="rm-category disabled">
    <div class="rm-category-header">
      <span class="rm-category-title">Number Theory <span class="rm-category-badge">Coming Soon</span></span>
    </div>
  </div>
  <div class="rm-category disabled">
    <div class="rm-category-header">
      <span class="rm-category-title">Combinatorics <span class="rm-category-badge">Coming Soon</span></span>
    </div>
  </div>
  <div class="rm-category disabled">
    <div class="rm-category-header">
      <span class="rm-category-title">Math <span class="rm-category-badge">Coming Soon</span></span>
    </div>
  </div>
  <div class="rm-category disabled">
    <div class="rm-category-header">
      <span class="rm-category-title">Strings <span class="rm-category-badge">Coming Soon</span></span>
    </div>
  </div>
  <div class="rm-category disabled">
    <div class="rm-category-header">
      <span class="rm-category-title">Dynamic Programming (DP) <span class="rm-category-badge">Coming Soon</span></span>
    </div>
  </div>
  <div class="rm-category disabled">
    <div class="rm-category-header">
      <span class="rm-category-title">Game Theory <span class="rm-category-badge">Coming Soon</span></span>
    </div>
  </div>
  <div class="rm-category disabled">
    <div class="rm-category-header">
      <span class="rm-category-title">Geometry <span class="rm-category-badge">Coming Soon</span></span>
    </div>
  </div>
  <div class="rm-category disabled">
    <div class="rm-category-header">
      <span class="rm-category-title">Miscellaneous <span class="rm-category-badge">Coming Soon</span></span>
    </div>
  </div>
</div>

<script>
  function toggleCategory(el) {
    const parent = el.parentElement;
    if (parent.classList.contains('disabled')) return;
    parent.classList.toggle('open');
    const icon = el.querySelector('.rm-toggle-icon');
    if (icon) {
      icon.textContent = parent.classList.contains('open') ? '−' : '+';
    }
  }

  function toggleSubcategory(el) {
    const parent = el.parentElement;
    parent.classList.toggle('open');
    const toggle = el.querySelector('.rm-sub-toggle');
    if (toggle) {
      toggle.textContent = parent.classList.contains('open') ? '−' : '+';
    }
  }
</script>

---

## Training Methodology

To get the most out of this playbook:

1. **Follow the Roadmap**: Topics are ordered sequentially, building on top of previous concepts.
2. **Review Code Examples**: Check out the optimized templates for each topic.
3. **Practice**: Solve the linked problems at the end of each topic on platforms like Codeforces and CSES.
