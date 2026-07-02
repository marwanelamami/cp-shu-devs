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
      
      <!-- Subcategory: Intro to CP & Complexity -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Intro to CP & Complexity</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/01-intro-to-cp/intro-to-cp/" class="rm-topic">
              <span>Intro to CP & Complexity</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Arrays -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Arrays</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/02-arrays/static-arrays/" class="rm-topic">
              <span>Static Arrays</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/02-arrays/dynamic-arrays/" class="rm-topic">
              <span>Dynamic Arrays</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Kadane's Algorithm -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Kadane's Algorithm</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/03-kadanes-algorithm/kadanes-algorithm/" class="rm-topic">
              <span>Kadane's Algorithm</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Sliding Window -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Sliding Window</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/04-sliding-window/fixed-size/" class="rm-topic">
              <span>Fixed Size Window</span>
              <span class="rm-badge high">High</span>
            </a>
            <a href="topics/basics/04-sliding-window/variable-size/" class="rm-topic">
              <span>Variable Size Window</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Two Pointers -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Two Pointers</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/05-two-pointers/two-pointers/" class="rm-topic">
              <span>Two Pointers Technique</span>
              <span class="rm-badge high">High</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Subcategory: Prefix Sums -->
      <div class="rm-subcategory open">
        <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
          <span>Prefix Sums</span>
          <span class="rm-sub-toggle">−</span>
        </div>
        <div class="rm-subcategory-content">
          <div class="rm-topics-grid">
            <a href="topics/basics/06-prefix-sums/prefix-sums/" class="rm-topic">
              <span>Prefix Sums</span>
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
