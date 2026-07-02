# Welcome to CP Playbook

<style>
  :root {
    --primary-gradient: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%);
    --bg-card: #ffffff;
    --border-color: #e5e7eb;
    --text-muted: #6b7280;
  }
  
  [data-md-color-scheme="slate"] {
    --bg-card: #1e293b;
    --border-color: #334155;
    --text-muted: #94a3b8;
  }

  .hp-hero {
    background: var(--primary-gradient);
    border-radius: 16px;
    padding: 3.5rem 2rem;
    color: white;
    text-align: center;
    margin-bottom: 2.5rem;
    box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.2);
    position: relative;
    overflow: hidden;
  }
  .hp-hero::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at 80% 20%, rgba(255,255,255,0.15) 0%, transparent 50%);
    pointer-events: none;
  }
  .hp-title {
    font-size: 2.75rem !important;
    font-weight: 800 !important;
    color: white !important;
    margin: 0 0 1rem 0 !important;
    letter-spacing: -0.025em;
    line-height: 1.2;
  }
  .hp-subtitle {
    font-size: 1.15rem;
    max-width: 700px;
    margin: 0 auto 2rem auto;
    opacity: 0.9;
    line-height: 1.6;
  }
  .hp-cta-group {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
  }
  .hp-btn {
    display: inline-flex;
    align-items: center;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.2s ease;
    text-decoration: none !important;
  }
  .hp-btn-primary {
    background: white;
    color: #2563eb !important;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
  }
  .hp-btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    background: #f8fafc;
  }
  .hp-btn-secondary {
    background: rgba(255, 255, 255, 0.15);
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.3);
  }
  .hp-btn-secondary:hover {
    background: rgba(255, 255, 255, 0.25);
    transform: translateY(-2px);
  }

  /* Grid features */
  .hp-features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-bottom: 3rem;
  }
  .hp-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 1.75rem;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    transition: all 0.2s ease;
  }
  .hp-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 20px -3px rgba(0,0,0,0.08);
  }
  .hp-card-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
    display: inline-block;
  }
  .hp-card h3 {
    margin: 0 0 0.5rem 0 !important;
    font-size: 1.25rem !important;
    font-weight: 700 !important;
  }
  .hp-card p {
    margin: 0 !important;
    color: var(--text-muted);
    font-size: 0.95rem;
    line-height: 1.5;
  }

  /* Section Header */
  .hp-section-header {
    text-align: center;
    margin-bottom: 2rem;
  }
  .hp-section-header h2 {
    font-size: 2rem !important;
    font-weight: 800 !important;
    margin-bottom: 0.5rem !important;
  }
  .hp-section-header p {
    color: var(--text-muted);
    max-width: 600px;
    margin: 0 auto !important;
  }
</style>

<div class="hp-hero">
  <h1 class="hp-title">CP Playbook</h1>
  <p class="hp-subtitle">Structured algorithms, verified implementations, time complexity insights, and curated practice tasks to accelerate your competitive programming and LCPC/ICPC preparation.</p>
  <div class="hp-cta-group">
    <a href="topics/basics/01-intro-to-cp/intro-to-cp/" class="hp-btn hp-btn-primary">Get Started 🚀</a>
    <a href="#syllabus-map" class="hp-btn hp-btn-secondary">Explore Syllabus 🗺️</a>
  </div>
</div>

<div class="hp-features">
  <div class="hp-card">
    <span class="hp-card-icon">📚</span>
    <h3>Structured Syllabus</h3>
    <p>Follow a progressive curriculum path from programming language foundations to complex modular math, graph structures, and dynamics.</p>
  </div>
  <div class="hp-card">
    <span class="hp-card-icon">⚡</span>
    <h3>Verified Code templates</h3>
    <p>Grab highly-optimized, copy-paste ready C++ and Python implementations to streamline your training and contest performance.</p>
  </div>
  <div class="hp-card">
    <span class="hp-card-icon">🏆</span>
    <h3>Curated Problems</h3>
    <p>Challenge yourself with high-quality problems selected from Codeforces, CSES, and AtCoder to reinforce every concept you learn.</p>
  </div>
</div>

<div class="hp-section-header" id="syllabus-map">
  <h2>Interactive Topic Roadmap</h2>
  <p>Toggle baselines and click on specific topics to jump directly to their playbook guides.</p>
</div>

<div style="width:100%;overflow-x:auto;">
<svg xmlns="http://www.w3.org/2000/svg" id="svg-root" viewBox="0 0 1000 800" width="100%" style="display:block;">
  <defs>
    <!-- Drop Shadow Filter for nodes -->
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.1"/>
    </filter>
  </defs>
  <style>
    .node-text {
      font-family: "Anthropic Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 18px;
      fill: #111827;
      user-select: none;
    }
    .node-text-disabled {
      font-family: "Anthropic Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 18px;
      fill: #9ca3af;
      user-select: none;
    }
    .node-title {
      font-weight: 600;
    }
    .category-card {
      fill: #fcfcfb;
      stroke: #4f46e5;
      stroke-width: 1.5;
      cursor: pointer;
      rx: 6px;
    }
    .category-card-disabled {
      fill: #f9fafb;
      stroke: #d1d5db;
      stroke-width: 1.5;
      cursor: not-allowed;
      opacity: 0.6;
      rx: 6px;
    }
    .coming-soon-badge {
      font-family: "Anthropic Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 15px;
      font-weight: 500;
      fill: #9ca3af;
      text-anchor: end;
      user-select: none;
      opacity: 0.8;
    }
    .subcategory-card {
      fill: #fafafa;
      stroke: #9ca3af;
      stroke-width: 1.2;
      cursor: pointer;
      rx: 6px;
    }
    .topic-card {
      fill: #ffffff;
      stroke: #e5e7eb;
      stroke-width: 1;
      cursor: pointer;
      rx: 6px;
    }
    .topic-card:hover {
      stroke: #3b82f6;
      fill: #f0f9ff;
    }
    .link-icon {
      fill: #9ca3af;
      cursor: pointer;
    }
    .link-icon:hover {
      fill: #3b82f6;
    }
    .toggle-icon {
      fill: #6b7280;
      cursor: pointer;
    }
    .line-branch {
      fill: none;
      stroke: #d1d5db;
      stroke-width: 1.5;
      stroke-linecap: round;
    }
    .importance-badge {
      font-family: "Anthropic Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 13px;
      font-weight: bold;
      fill: #ffffff;
      text-anchor: middle;
      dominant-baseline: middle;
    }
    .legend-text {
      font-family: "Anthropic Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 15px;
      fill: #374151;
      font-weight: 500;
    }
  </style>
  <!-- Legend: each item is circle then text, with enough gap between items -->
  <g transform="translate(340, 18)">
    <circle cx="6" cy="12" r="7" fill="#ef4444" />
    <text x="20" y="17" class="legend-text">High Importance</text>
    <circle cx="186" cy="12" r="7" fill="#f59e0b" />
    <text x="200" y="17" class="legend-text">Medium Importance</text>
    <circle cx="400" cy="12" r="7" fill="#10b981" />
    <text x="414" y="17" class="legend-text">Low Importance</text>
  </g>
  <!-- Containers for dynamic rendering -->
  <g id="lines-container"></g>
  <g id="nodes-container"></g>
  <script type="text/javascript">
    // The structured roadmap data
    const roadmapData = [{"title": "Basics", "id": "basics", "subcategories": [{"title": "Intro to Programming", "id": "intro_to_programming", "topics": [{"title": "What is Programming?", "id": "programming", "importance": 3}]}, {"title": "Learn a Language", "id": "learning_a_language", "topics": [{"title": "Intro to C++ and Setting up the Environment", "id": "intro_to_cpp", "importance": 3}, {"title": "Data Types, Variables and Input Output", "id": "variables_and_data_types", "importance": 3}, {"title": "Operators", "id": "operators", "importance": 3}, {"title": "Conditional Statements", "id": "conditional_statements", "importance": 3}, {"title": "Loops", "id": "loops", "importance": 3}, {"title": "Functions", "id": "functions", "importance": 3}, {"title": "Arrays", "id": "arrays", "importance": 3}, {"title": "Strings", "id": "strings", "importance": 3}, {"title": "Pointers and References", "id": "pointers", "importance": 3}, {"title": "Structures", "id": "structures", "importance": 3}]}, {"title": "Intro to Competitive Programming", "id": "intro_to_cp", "topics": [{"title": "What is Competitive Programming?", "id": "competitive_programming", "importance": 3}]}, {"title": "Bitwise Thinking", "id": "bitwise_thinking", "topics": [{"title": "Bitwise Operations and Bitmasks", "id": "bitwise_operations", "importance": 3}]}, {"title": "Complexity Analysis", "id": "complexity_analysis", "topics": [{"title": "Big O Notation and Time and Space Complexity Analysis", "id": "complexity_analysis", "importance": 3}, {"title": "Fast Input Output", "id": "fast_input_output", "importance": 3}]}, {"title": "Recursion", "id": "recursion", "topics": [{"title": "Recursion", "id": "recursion", "importance": 3}]}, {"title": "Very Basic Math", "id": "very_basic_math", "topics": [{"title": "Divisors", "id": "divisors", "importance": 3}, {"title": "GCD and LCM", "id": "gcd_and_lcm", "importance": 3}, {"title": "Harmonic Number", "id": "harmonic_series", "importance": 3}]}, {"title": "Range Queries Without Updates", "id": "range_queries_without_updates", "topics": [{"title": "Prefix Sum", "id": "prefix_sum", "importance": 3}, {"title": "Prefix XOR", "id": "prefix_xor", "importance": 3}]}, {"title": "Standard Template Library (STL)", "id": "stl", "topics": [{"title": "Intro to STL, Containers and Iterators", "id": "stl_intro", "importance": 3}, {"title": "Pairs and Tuples", "id": "pairs_and_tuples", "importance": 3}, {"title": "Vector", "id": "vector", "importance": 3}, {"title": "Stack", "id": "stack", "importance": 3}, {"title": "Queue", "id": "queue", "importance": 3}, {"title": "Priority Queue / Heap", "id": "priority_queue", "importance": 3}, {"title": "Deque", "id": "deque", "importance": 3}, {"title": "Set, Unordered Set and Multiset", "id": "set", "importance": 3}, {"title": "Map and Unordered Map", "id": "map", "importance": 3}, {"title": "Bitset", "id": "bitset", "importance": 3}, {"title": "List / Linked List", "id": "list", "importance": 2}]}, {"title": "Leveraging Monotonicity", "id": "leveraging_monotonicity", "topics": [{"title": "Binary Search", "id": "binary_search", "importance": 3}, {"title": "Two Pointers", "id": "two_pointers", "importance": 3}]}, {"title": "Basic Sorting Algorithms", "id": "basic_sorting_algorithms", "topics": [{"title": "Bubble Sort", "id": "bubble_sort", "importance": 3}, {"title": "Selection Sort", "id": "selection_sort", "importance": 3}, {"title": "Insertion Sort", "id": "insertion_sort", "importance": 3}, {"title": "Counting Sort", "id": "counting_sort", "importance": 3}, {"title": "Merge Sort", "id": "merge_sort", "importance": 3}, {"title": "Quick Sort", "id": "quick_sort", "importance": 2}, {"title": "Radix Sort", "id": "radix_sort", "importance": 1}, {"title": "C++ STL Sort and Custom Comparator", "id": "stl_sort", "importance": 3}]}, {"title": "Divide and Conquer", "id": "divide_and_conquer", "topics": [{"title": "Divide and Conquer", "id": "divide_and_conquer", "importance": 3}]}, {"title": "Greedy and Constructive", "id": "greedy_and_constructive", "topics": [{"title": "Basic Greedy Algorithms", "id": "greedy_algorithms", "importance": 3}, {"title": "Basic Constructive Algorithms", "id": "constructive_algorithms", "importance": 3}]}, {"title": "2D Prefix Sum", "id": "2d_prefix_sum", "topics": [{"title": "2D Prefix Sum", "id": "2d_prefix_sum", "importance": 3}]}, {"title": "More Techniques", "id": "more_techniques", "topics": [{"title": "Difference Array", "id": "difference_array", "importance": 3}, {"title": "Sliding Window Technique", "id": "sliding_window_technique", "importance": 3}]}, {"title": "Bit Manipulation", "id": "bit_manipulation", "topics": [{"title": "Bit Manipulation", "id": "bit_manipulation", "importance": 3}, {"title": "The XOR Trick", "id": "the_xor_trick", "importance": 3}]}, {"title": "Basic Modular Arithmetic", "id": "modular_arithmetic", "topics": [{"title": "Binary Exponentiation and Basic Modular Arithmetic", "id": "binary_exponentiation", "importance": 3}, {"title": "Fermat's Little Theorem and Modular Inverse", "id": "fermats_little_theorem", "importance": 3}]}, {"title": "Basic Counting", "id": "basic_counting", "topics": [{"title": "Permutations, Combinations and Basic Counting Problems", "id": "permutations_and_combinations", "importance": 3}, {"title": "Stars and Bars", "id": "stars_and_bars", "importance": 3}, {"title": "Pigeonhole Principle", "id": "pigeonhole_principle", "importance": 2}]}, {"title": "Very Basic Graphs", "id": "very_basic_graphs", "topics": [{"title": "Introduction to Graphs | Definitions and Representations", "id": "graph_representations", "importance": 3}]}]}, {"title": "Data Structures (DS)", "id": "data_structures", "subcategories": [{"title": "Segment Tree", "id": "segment_tree", "topics": [{"title": "Segment Tree (Point Update Range Query)", "id": "segment_tree", "importance": 3}, {"title": "Segment Tree with Lazy Propagation", "id": "segment_tree_with_lazy_propagation", "importance": 3}, {"title": "Persistent Segment Tree", "id": "persistent_segment_tree", "importance": 3}, {"title": "Persistent Segment Tree with Lazy Propagation", "id": "persistent_segment_tree_with_lazy_propagation", "importance": 1}, {"title": "2D Segment Tree", "id": "2d_segment_tree", "importance": 1}, {"title": "Dynamic Segment Tree", "id": "dynamic_segment_tree", "importance": 2}, {"title": "2D Dynamic Segment Tree", "id": "2d_dynamic_segment_tree", "importance": 1}, {"title": "Merge Sort Tree", "id": "merge_sort_tree", "importance": 2}, {"title": "Iterative Segment Tree", "id": "iterative_segment_tree", "importance": 1}, {"title": "Segment Tree Merging", "id": "segment_tree_merging", "importance": 1}, {"title": "Segment Tree Beats", "id": "segment_tree_beats", "importance": 2}, {"title": "XOR Segment Tree", "id": "xor_segment_tree", "importance": 1}, {"title": "Historic Information on Segment Trees", "id": "historic_information_on_segment_trees", "importance": 1}]}, {"title": "Binary Indexed Tree (BIT)", "id": "binary_indexed_tree", "topics": [{"title": "BIT / Fenwick Tree", "id": "bit", "importance": 3}, {"title": "Lower bound on BIT", "id": "lower_bound_on_bit", "importance": 2}, {"title": "BIT with Range Update and Range Query", "id": "bit_with_range_update_and_range_query", "importance": 2}, {"title": "2D BIT", "id": "2d_bit", "importance": 2}, {"title": "2D BIT with Range Update and Range Query", "id": "2d_bit_with_range_update_and_range_query", "importance": 1}]}, {"title": "Sparse Table", "id": "sparse_table", "topics": [{"title": "Sparse Table", "id": "sparse_table", "importance": 3}, {"title": "Sparse Table 2D", "id": "sparse_table_2d", "importance": 2}, {"title": "Disjoint Sparse Table", "id": "disjoint_sparse_table", "importance": 1}]}, {"title": "Trie", "id": "trie", "topics": [{"title": "Trie on Strings and Bits", "id": "trie", "importance": 3}, {"title": "Persistent Trie", "id": "persistent_trie", "importance": 1}]}, {"title": "Disjoint Set Union (DSU)", "id": "dsu", "topics": [{"title": "DSU / Union Find", "id": "dsu", "importance": 3}, {"title": "DSU with Rollbacks", "id": "dsu_with_rollbacks", "importance": 2}, {"title": "Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)", "id": "reachability_tree", "importance": 2}, {"title": "Partially Persistent DSU", "id": "partially_persistent_dsu", "importance": 1}, {"title": "Persistent DSU", "id": "persistent_dsu", "importance": 1}, {"title": "Augmented DSU / Weighted DSU", "id": "augmented_dsu", "importance": 2}, {"title": "DSU on Tree and Small to Large Merging", "id": "dsu_on_tree", "importance": 3}, {"title": "[Trick] Maintaining Log N DSU / Range Parallel DSU", "id": "maintaining_log_n_dsu", "importance": 1}]}, {"title": "Square Root Decomposition", "id": "sqrt_decomposition", "topics": [{"title": "Basic SQRT Decomposition", "id": "sqrt_decomposition", "importance": 3}, {"title": "Splitting Objects into Light and Heavy / Case Processing", "id": "splitting_objects_into_light_and_heavy", "importance": 3}, {"title": "Batch Processing / SQRT Decomposition on Queries", "id": "batch_processing", "importance": 2}, {"title": "SQRT Decomposition Split and Build Technique", "id": "sqrt_decomposition_split_and_build_technique", "importance": 1}, {"title": "SQRT Fragmented Tree / Block Tree / SQRT Decomposition on Trees", "id": "sqrt_fragmented_tree", "importance": 1}, {"title": "Mo's Algorithm", "id": "mos_algorithm", "importance": 3}, {"title": "Rollback Mo and Mo's with DSU", "id": "mos_with_dsu", "importance": 2}, {"title": "Mo's on Tree", "id": "mos_on_tree", "importance": 1}, {"title": "Sweepline Mo", "id": "sweepline_mo", "importance": 1}, {"title": "Mo's with Update / 3D Mo (Offline)", "id": "mos_with_update", "importance": 1}, {"title": "Mo's with Update / 3D Mo (Online)", "id": "mos_online", "importance": 1}, {"title": "4D Mo", "id": "4d_mo", "importance": 1}]}, {"title": "Heavy Light Decomposition (HLD)", "id": "hld", "topics": [{"title": "Heavy Light Decomposition (HLD) ft Subtrees and Path Query", "id": "hld", "importance": 3}]}, {"title": "Centroid Decomposition", "id": "centroid_decomposition", "topics": [{"title": "Centroid Decomposition", "id": "centroid_decomposition", "importance": 3}, {"title": "Persistent Centroid Decomposition", "id": "persistent_centroid_decomposition", "importance": 1}]}, {"title": "Long Path Decomposition", "id": "", "topics": [{"title": "Long Path Decomposition", "id": "long_path_decomposition", "importance": 1}]}, {"title": "BST", "id": "binary_search_tree", "topics": [{"title": "Binary Search Tree (BST)", "id": "bst", "importance": 3}]}, {"title": "Balanced Binary Search Tree (BBST)", "id": "bbst", "topics": [{"title": "Treap", "id": "treap", "importance": 3}, {"title": "Implicit Treap", "id": "implicit_treap", "importance": 3}, {"title": "Persistent Treap", "id": "persistent_treap", "importance": 1}, {"title": "Rope", "id": "rope", "importance": 1}, {"title": "Splay Tree", "id": "splay_tree", "importance": 1}]}, {"title": "Link Cut Tree (LCT)", "id": "lct", "topics": [{"title": "Link Cut Tree (LCT)", "id": "lct", "importance": 3}, {"title": "Euler Tour Tree (ETT)", "id": "ett", "importance": 1}, {"title": "Top Tree / AAA Tree", "id": "top_tree", "importance": 1}, {"title": "Link Cut Cactus", "id": "link_cut_cactus", "importance": 1}]}, {"title": "Policy Based Data Structures", "id": "policy_based_data_structures", "topics": [{"title": "Ordered Set", "id": "ordered_set", "importance": 3}, {"title": "GP Hash Table", "id": "gp_hash_table", "importance": 3}]}, {"title": "More Tree Data Structures", "id": "more_tree_data_structures", "topics": [{"title": "Wavelet Tree", "id": "wavelet_tree", "importance": 3}, {"title": "Cartesian Tree", "id": "cartesian_tree", "importance": 2}, {"title": "K-Dimensional Tree (KD Tree)", "id": "kd_tree", "importance": 2}, {"title": "SQRT Tree", "id": "sqrt_tree", "importance": 1}, {"title": "Permutation Tree", "id": "permutation_tree", "importance": 2}, {"title": "PQ Tree", "id": "pq_tree", "importance": 1}]}, {"title": "Dynamic Connectivity", "id": "dynamic_connectivity", "topics": [{"title": "Dynamic Connectivity Problem (Offline)", "id": "dynamic_connectivity_problem", "importance": 3}, {"title": "Dynamic Connectivity Problem (Online) / HDLT Algorithm", "id": "online_dynamic_connectivity_problem", "importance": 1}]}, {"title": "Monotonic Data Structures", "id": "monotonic_data_structures", "topics": [{"title": "Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum", "id": "all_subarray_maximum_minimum", "importance": 3}, {"title": "Monotonic Queue", "id": "monotonous_queue", "importance": 3}, {"title": "Monotonic Queue 2D", "id": "monotonous_queue_2d", "importance": 2}, {"title": "Monotonic Deque", "id": "monotonic_deque", "importance": 1}]}, {"title": "Miscellaneous", "id": "miscellaneous", "topics": [{"title": "Interval Set", "id": "interval_set", "importance": 1}, {"title": "Persistent Array", "id": "persistent_array", "importance": 1}, {"title": "Persistent Queue", "id": "persistent_queue", "importance": 1}, {"title": "Persistent Meldable Heap / Leftist Heap", "id": "persistent_heap", "importance": 1}]}, {"title": "Techniques", "id": "techniques", "topics": [{"title": "Venice Technique", "id": "venice_technique", "importance": 2}, {"title": "Offline Queries", "id": "offline_queries", "importance": 3}, {"title": "Static to Dynamic Trick / Log Decomposition", "id": "static_to_dynamic_trick", "importance": 2}, {"title": "Divide and Conquer on Queries", "id": "divide_and_conquer_on_queries", "importance": 3}, {"title": "CDQ Divide and Conquer", "id": "cdq_divide_and_conquer", "importance": 2}, {"title": "Queue Undo Trick", "id": "queue_undo_trick", "importance": 2}, {"title": "Priority Queue Undo Trick", "id": "priority_queue_undo_trick", "importance": 1}]}]}, {"title": "Graph Theory", "id": "graph_theory", "subcategories": [{"title": "Graph Traversal", "id": "graph_traversal", "topics": [{"title": "Depth First Search (DFS)", "id": "dfs", "importance": 3}, {"title": "Breadth First Search (BFS)", "id": "bfs", "importance": 3}, {"title": "DFS Tree", "id": "dfs_tree", "importance": 3}, {"title": "Topological Sorting", "id": "topological_sorting", "importance": 3}, {"title": "Tree Diameter", "id": "tree_diameter", "importance": 3}, {"title": "Euler Tour Technique", "id": "euler_tour_technique", "importance": 3}, {"title": "Inverse Graph", "id": "inverse_graph", "importance": 2}]}, {"title": "Lowest Common Ancestor (LCA)", "id": "lca", "topics": [{"title": "Binary Lifting and LCA", "id": "binary_lifting_and_lca", "importance": 3}, {"title": "LCA in O(1)", "id": "lca_in_o1", "importance": 1}]}, {"title": "Graph Connectivity", "id": "graph_connectivity", "topics": [{"title": "Strongly Connected Components (SCC)", "id": "scc", "importance": 3}, {"title": "Incremental SCC", "id": "incremental_scc", "importance": 1}, {"title": "Articulation Bridges and Bridge Tree", "id": "articulation_bridges_and_bridge_tree", "importance": 3}, {"title": "Online Articulation Bridges", "id": "online_articulation_bridges", "importance": 1}, {"title": "Articulation Points and Block Cut Tree", "id": "articulation_points", "importance": 3}, {"title": "Three Edge Connectivity", "id": "three_edge_connectivity", "importance": 1}, {"title": "Four Edge Connectivity", "id": "four_edge_connectivity", "importance": 1}, {"title": "Dynamic K-Connectivity", "id": "dynamic_k_connectivity", "importance": 1}, {"title": "Ear Decomposition", "id": "ear_decomposition", "importance": 1}]}, {"title": "Orientation", "id": "orientation", "topics": [{"title": "Strong Orientation", "id": "strong_orientation", "importance": 2}, {"title": "ST-numbering / Bipolar Orientation", "id": "st_numbering", "importance": 1}]}, {"title": "Minimum Spanning Tree (MST)", "id": "minimum_spanning_tree", "topics": [{"title": "Minimum Spanning Tree (MST) - Prim's and Kruskal's", "id": "mst", "importance": 3}, {"title": "Steiner Tree Problem", "id": "steiner_tree_problem", "importance": 2}, {"title": "Boruvka's Algorithm", "id": "boruvkas_algorithm", "importance": 2}, {"title": "Minimum Diameter Spanning Tree", "id": "minimum_diameter_spanning_tree", "importance": 1}, {"title": "Manhattan MST", "id": "manhattan_mst", "importance": 1}, {"title": "Euclidean MST", "id": "euclidean_mst", "importance": 1}, {"title": "Directed MST", "id": "directed_mst", "importance": 2}, {"title": "Dynamic MST", "id": "dynamic_mst", "importance": 1}, {"title": "Kirchoffs Theorem ft Number of MSTs", "id": "kirchoffs_theorem_ft_number_of_msts", "importance": 2}]}, {"title": "Shortest Paths", "id": "shortest_paths", "topics": [{"title": "Dijkstra's Algorithm", "id": "dijkstras_algorithm", "importance": 3}, {"title": "[Trick] Dijkstra on Segment Tree", "id": "dijkstra_on_segment_tree", "importance": 2}, {"title": "Floyd Warshall", "id": "floyd_warshall", "importance": 3}, {"title": "Bellman Ford", "id": "bellman_ford", "importance": 3}, {"title": "Shortest Path Faster Algorithm (SPFA)", "id": "spfa", "importance": 1}, {"title": "Johnson's Alogrithm", "id": "johnsons_algorithm", "importance": 1}, {"title": "0/1 BFS", "id": "0_1_bfs", "importance": 2}, {"title": "Dial's algorithm", "id": "dials_algorithm", "importance": 1}, {"title": "Eppsteins Algorithm", "id": "eppsteins_algorithm", "importance": 1}, {"title": "Suurballe's Algorithm", "id": "suurballes_algorithm", "importance": 1}, {"title": "A* Algorithm", "id": "a_star_algorithm", "importance": 2}]}, {"title": "Cycles", "id": "cycles", "topics": [{"title": "Cycle Detection", "id": "cycle_detection", "importance": 3}, {"title": "[Problem] Minimum Weight Cycle For Each Vertex", "id": "minimum_weight_cycle_for_each_vertex", "importance": 2}, {"title": "[Problem] Minimum Weight Cycle For Each Edge", "id": "minimum_weight_cycle_for_each_edge", "importance": 2}, {"title": "Minimum Mean Weight Cycle", "id": "minimum_mean_weight_cycle", "importance": 1}, {"title": "Number of 3 and 4 length Cycles", "id": "number_of_3_and_4_length_cycles", "importance": 2}]}, {"title": "More Tree Stuff", "id": "more_tree_stuff", "topics": [{"title": "Virtual Tree / Auxiliary Tree", "id": "virtual_tree", "importance": 3}, {"title": "Rerooting Technique", "id": "rerooting_technique", "importance": 3}, {"title": "Union of Two Paths on a Tree", "id": "path_union", "importance": 2}, {"title": "Intersection of Two Paths on a Tree", "id": "path_intersection", "importance": 2}, {"title": "[Problem] Number of Paths of Each Length in a Tree", "id": "number_of_paths_of_each_length_in_a_tree", "importance": 2}, {"title": "Dynamic Online Tree Diameter", "id": "dynamic_diameter_online", "importance": 1}, {"title": "[Problem] Tree Orientation to Maximize Pairs of Reachable Nodes", "id": "tree_orientation_to_maximize_pairs_of_reachable_nodes", "importance": 1}]}, {"title": "Satisfiability", "id": "satisfiability", "topics": [{"title": "2 SAT", "id": "2_sat", "importance": 3}, {"title": "3 SAT", "id": "3_sat", "importance": 1}, {"title": "System Of Difference Constraints", "id": "system_of_difference_constraints", "importance": 2}]}, {"title": "Eulerian Path", "id": "eulerian_path", "topics": [{"title": "Eulerian Path and Cycle", "id": "eulerian_path_and_cycle", "importance": 3}]}, {"title": "Hamiltonian Path", "id": "hamiltonian_path", "topics": [{"title": "Hamiltonian Path and Cycle", "id": "hamiltonian_path_and_cycle", "importance": 2}, {"title": "Hamiltonian Path Heuristic Algorithm", "id": "hamiltonian_path_heuristic_algorithm", "importance": 1}]}, {"title": "Cliques and Independent Sets", "id": "cliques_and_independent_sets", "topics": [{"title": "Maximum Clique", "id": "maximum_clique", "importance": 3}, {"title": "Maximum Independent Set (MIS)", "id": "maximum_independent_set", "importance": 3}]}, {"title": "Graph Coloring", "id": "graph_coloring", "topics": [{"title": "Chromatic Number", "id": "chromatic_number", "importance": 2}, {"title": "Welsh-Powell Algorithm", "id": "welsh_powell_algorithm", "importance": 1}, {"title": "Chromatic Polynomial ft Number of DAGs", "id": "chromatic_polynomial_ft_number_of_dags", "importance": 1}, {"title": "Edge Coloring of Simple Graph", "id": "edge_coloring_of_simple_graph", "importance": 1}, {"title": "Edge Coloring of Bipartite Graph", "id": "edge_coloring_of_bipartite_graph", "importance": 1}]}, {"title": "Graph Counting", "id": "graph_counting", "topics": [{"title": "Counting Labeled Graphs", "id": "counting_labeled_graphs", "importance": 1}, {"title": "Prufer Code", "id": "prufer_code", "importance": 3}, {"title": "[Problem] Number of Arborescences with n Nodes", "id": "number_of_arborescences_with_n_nodes", "importance": 1}, {"title": "Tuttes Theorem ft Arborescences in a Graph", "id": "tuttes_theorem_ft_arborescences_in_a_graph", "importance": 1}, {"title": "BEST Theorem", "id": "best_theorem", "importance": 1}]}, {"title": "Dynamic Acyclic Graphs (DAG)", "id": "dynamic_acyclic_graphs", "topics": [{"title": "DAG Reachability", "id": "dag_reachability", "importance": 2}, {"title": "Incremental DAG Reachability", "id": "dynamic_dag_reachability", "importance": 1}]}, {"title": "Dominators", "id": "dominators", "topics": [{"title": "Dominator Tree", "id": "dominator_tree", "importance": 2}]}, {"title": "Special Graphs", "id": "special_graphs", "topics": [{"title": "Cactus Graph", "id": "cactus_graph", "importance": 2}, {"title": "Tournament Graph", "id": "tournament_graph", "importance": 2}, {"title": "Chordal Graph", "id": "chordal_graph", "importance": 1}]}, {"title": "Flow and Min Cut", "id": "flow_and_min_cut", "topics": [{"title": "Maximum Flow / Minimum Cut", "id": "max_flow", "importance": 3}, {"title": "Min Cost Max Flow (MCMF)", "id": "min_cost_max_flow", "importance": 3}, {"title": "Min Cost Max Flow with Negative Cycles", "id": "min_cost_max_flow_with_negative_cycles", "importance": 1}, {"title": "Maximum Closure Problem", "id": "maximum_closure_problem", "importance": 2}, {"title": "L-R Flow", "id": "l_r_flow", "importance": 2}, {"title": "Gomory-Hu Tree", "id": "gomory_hu_tree", "importance": 1}, {"title": "Gomory-Hu Tree of a Planar Graph", "id": "gomory_hu_tree_of_a_planar_graph", "importance": 1}, {"title": "Stoer Wagner Algorithm", "id": "stoer_wagner_algorithm", "importance": 2}, {"title": "Chinese Postman Problem", "id": "chinese_postman_problem", "importance": 2}, {"title": "Uniqueness of Min Cut", "id": "unique_min_cut", "importance": 1}, {"title": "Maximum Density Subgraph", "id": "maximum_density_subgraph", "importance": 1}, {"title": "Min Cut in a Planar Graph", "id": "min_cut_in_a_planar_graph", "importance": 2}, {"title": "Max Cut in a Planar Graph", "id": "max_cut_in_a_planar_graph", "importance": 1}]}, {"title": "Matching", "id": "matching", "topics": [{"title": "Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)", "id": "bipartite_matching", "importance": 3}, {"title": "Hungarian Algorithm / Bipartite Weighted Matching", "id": "hungarian_algorithm", "importance": 3}, {"title": "Blossom Algorithm Unweighted / General Matching / Randomized General Matching", "id": "blossom_algorithm_unweighted", "importance": 2}, {"title": "Blossom Algorithm Weighted / General Weighted Matching", "id": "blossom_algorithm_weighted", "importance": 1}, {"title": "Stable Marriage Problem", "id": "stable_marriage_problem", "importance": 1}, {"title": "Konig's Theorem and Maximum Independent Set in Bipartite Graphs", "id": "maximum_independent_set_in_bipartite_graphs", "importance": 2}, {"title": "Halls Theorem", "id": "halls_theorem", "importance": 2}, {"title": "Matching using Determinants", "id": "matching_using_determinants", "importance": 1}]}, {"title": "Partially Ordered Set (POSET)", "id": "poset", "topics": [{"title": "POSET ft Dilworth's and Mirsky's Theorem", "id": "poset_ft_dilworths_and_mirskys_theorem", "importance": 3}]}, {"title": "Miscellaneous", "id": "miscellaneous", "topics": [{"title": "Functional Graphs", "id": "functional_graphs", "importance": 2}, {"title": "Degree Sequences, Erdos-Gallai Theorem, Gale-Ryser Theorem and Havel–Hakimi Algorithm", "id": "degree_sequences", "importance": 2}, {"title": "Tree Isomorphism", "id": "tree_isomorphism", "importance": 2}, {"title": "Binarizing a Tree", "id": "binarizing_a_tree", "importance": 1}, {"title": "Planarity Check", "id": "planarity_check", "importance": 1}]}]}, {"title": "Number Theory", "id": "number_theory", "subcategories": [{"title": "Primes and Divisors", "id": "primes_and_divisors", "topics": [{"title": "Sieve, Prime Factorization and Divisors", "id": "sieve", "importance": 3}, {"title": "Linear Sieve", "id": "linear_sieve", "importance": 2}, {"title": "Segmented Sieve", "id": "segmented_sieve", "importance": 2}, {"title": "Sieve upto 1e9", "id": "sieve_upto_1e9", "importance": 1}, {"title": "Miller-Rabin Primality Test", "id": "miller_rabin_primality_test", "importance": 2}, {"title": "Pollard Rho", "id": "pollard_rho", "importance": 2}, {"title": "Prime Counting Function", "id": "prime_counting_function", "importance": 2}, {"title": "Prime Gap", "id": "prime_gap", "importance": 2}, {"title": "[Problem] Counting Numbers Having Exactly K Divisors", "id": "k_divisors", "importance": 1}, {"title": "[Problem] Smallest Number Having Exactly K Divisors", "id": "smallest_number_having_exactly_k_divisors", "importance": 1}, {"title": "Sum of The Number of Divisors in cbrt(n)", "id": "sum_of_the_number_of_divisors_in_cbrt_n", "importance": 1}, {"title": "Wilson's Theorem", "id": "wilsons_theorem", "importance": 2}, {"title": "Implicit Prime Factorization", "id": "implicit_prime_factorization", "importance": 1}]}, {"title": "Multiplicative Functions", "id": "multiplicative_functions", "topics": [{"title": "Number of Divisors / Sum of Divisors / Sigma Function", "id": "sigma_function", "importance": 3}, {"title": "Euler's Totient Function / Phi Function", "id": "eulers_totient_function", "importance": 3}, {"title": "Power Tower /  Generalized Euler theorem", "id": "power_tower", "importance": 2}, {"title": "Mobius Function and Mobius Inversion", "id": "mobius_function", "importance": 3}, {"title": "Dirichlet convolution", "id": "dirichlet_convolution", "importance": 2}, {"title": "Min_25 Sieve", "id": "min_25_sieve", "importance": 1}, {"title": "Powerful Number Sieve / PN Sieve", "id": "powerful_number_sieve", "importance": 1}]}, {"title": "Euclidean Algorithm", "id": "euclidean_algorithm", "topics": [{"title": "Euclidean Algorithm", "id": "euclidean_algorithm", "importance": 3}, {"title": "Extended Euclid", "id": "extended_euclid", "importance": 3}, {"title": "Bezout's Identity", "id": "bezouts_identity", "importance": 3}, {"title": "Chicken McNugget Theorem", "id": "chicken_mcnugget_theorem", "importance": 2}]}, {"title": "Modular Arithmetic", "id": "modular_arithmetic", "topics": [{"title": "Linear Congruence Equation", "id": "linear_congruence_equation", "importance": 2}, {"title": "Chinese Remainder Theorem (CRT)", "id": "crt", "importance": 3}, {"title": "Primitive Root", "id": "primitive_root", "importance": 2}, {"title": "Multiplicative Order and Carmichael's Lambda Function", "id": "multiplicative_order", "importance": 2}, {"title": "Discrete Log / Baby Step Giant Step", "id": "discrete_log", "importance": 3}, {"title": "Discrete Root", "id": "discrete_root", "importance": 2}, {"title": "Discrete Root in O(P^(1/4))", "id": "discrete_root_in_o_p_1_4", "importance": 1}, {"title": "Discrete Square Root, Tonelli Shanks Algorithm, Cipolla's Algorithm", "id": "tonelli_shanks_algorithm", "importance": 1}, {"title": "Number of Distinct Kth Powers Modulo N", "id": "number_of_distinct_kth_powers_modulo_n", "importance": 1}, {"title": "Number of Solutions to X^2 = 1 mod M", "id": "number_of_solutions_to_x_2_1_mod_m", "importance": 1}]}, {"title": "Linear Diophantine Equations", "id": "linear_diophantine_equations", "topics": [{"title": "Linear Diophantine Equation with Two Variables", "id": "linear_diophantine_equation_with_two_variables", "importance": 3}, {"title": "Linear Diophantine Equation with N Variables", "id": "linear_diophantine_equation_with_n_variables", "importance": 2}, {"title": "Trivariable Linear Diophantine Equation with Nonnegative Solutions", "id": "trivariable_linear_diophantine_equation_with_nonnegative_solutions", "importance": 1}, {"title": "Multivariable Linear Diophantine Equation with Nonnegative Solutions", "id": "multivariable_linear_diophantine_equation_with_nonnegative_solutions", "importance": 2}, {"title": "Linear Diophantine With N Unknowns and Two Equations", "id": "linear_diophantine_with_n_unknowns_and_two_equations", "importance": 1}]}, {"title": "Solutions to Equations", "id": "solutions_to_equations", "topics": [{"title": "Number of Solutions to a Basic Linear Algebraic Equation", "id": "number_of_solutions_to_a_basic_linear_algebraic_equation", "importance": 3}, {"title": "Number of Solutions to a Basic Linear Algebraic Equation using Meet in the Middle", "id": "number_of_solutions_to_a_basic_linear_algebraic_equation_with_variable_upper_bound_constraints", "importance": 1}, {"title": "Number of Nonnegative Integer Solutions to ax + by ≤ c", "id": "number_of_nonnegative_integer_solutions_to_ax_by_c", "importance": 2}, {"title": "Number of Integer Solutions to 1/x + 1/y = 1/k", "id": "number_of_integer_solutions_to_1_x_1_y_1_k", "importance": 1}, {"title": "Two / Three / Four Squares Theorem", "id": "two_squares_theorem", "importance": 1}, {"title": "Pell's Equation", "id": "pells_equation", "importance": 1}]}, {"title": "Floor Sum", "id": "floor_sum", "topics": [{"title": "Sum of Floors", "id": "sum_of_floors", "importance": 3}, {"title": "Floor Sum and Mod Sum of Arithmetic Progression", "id": "floor_sum_of_arithmetic_progression", "importance": 2}, {"title": "Generalized Floor Sum of Arithmetic Progression", "id": "generalized_floor_sum_of_arithmetic_progression", "importance": 1}]}, {"title": "Fibonacci Numbers", "id": "fibonacci_numbers", "topics": [{"title": "Fibonacci Numbers", "id": "fibonacci_numbers", "importance": 3}, {"title": "[Problem] LCM of Fibonacci Numbers", "id": "lcm_of_fibonacci_numbers", "importance": 1}, {"title": "Pisano Period", "id": "pisano_period", "importance": 1}, {"title": "Phi Field", "id": "phi_field", "importance": 2}]}, {"title": "Miscellaneous", "id": "miscellaneous", "topics": [{"title": "Pythagorean Triplets", "id": "pythagorean_triplets", "importance": 2}, {"title": "[Problem] Min of Mod of Arithmetic Progression", "id": "min_of_mod_of_arithmetic_progression", "importance": 1}, {"title": "Sqrt Decomposition of Mod of Arithmetic Progression", "id": "sqrt_decomposition_of_mod_of_arithmetic_progression", "importance": 1}, {"title": "Factorial Number System", "id": "factoradic_number_system", "importance": 1}, {"title": "Stern-Brocot Tree and Rational Approximation", "id": "rational_approximation_stern_brocot_tree", "importance": 1}, {"title": "[Problem] Number of a * x mod p in a Range", "id": "number_of_ax_mod_p_in_a_range", "importance": 2}, {"title": "[Problem] Smallest Nonnegative Integer x s.t. l ≤ a * x mod p ≤ r", "id": "smallest_nonnegative_integer_x_s_t_l_ax_mod_p_r", "importance": 1}]}]}, {"title": "Combinatorics", "id": "combinatorics", "subcategories": [{"title": "Techniques", "id": "techniques", "topics": [{"title": "Contribution Technique", "id": "contribution_technique", "importance": 3}, {"title": "Product Trick", "id": "product_trick", "importance": 2}]}, {"title": "Catalan", "id": "catalan", "topics": [{"title": "Catalan Numbers", "id": "catalan_numbers", "importance": 3}, {"title": "Catalan Convolution", "id": "catalan_convolution", "importance": 2}]}, {"title": "Inclusion Exclusion", "id": "inclusion_exclusion", "topics": [{"title": "Principle of Inclusion and Exclusion (PIE)", "id": "principle_of_inclusion_and_exclusion", "importance": 3}, {"title": "Derangements", "id": "derangements", "importance": 3}, {"title": "Inclusion Exclusion on Multiples", "id": "inclusion_and_exclusion_on_multiples", "importance": 3}]}, {"title": "Factorials and Binomial Coefficients (nCr)", "id": "binomial_coefficient", "topics": [{"title": "Lucas Theorem", "id": "lucas_theorem", "importance": 3}, {"title": "nCr Modulo Any Mod", "id": "ncr_modulo_any_mod", "importance": 2}, {"title": "Large Factorials and Binomial Coefficients", "id": "large_factorials", "importance": 2}, {"title": "Legendre's Formula", "id": "legendres_formula", "importance": 2}, {"title": "Prefix Sum Queries of Binomial Coefficients", "id": "prefix_sum_queries_of_nci", "importance": 2}, {"title": "Prefix Sum of Binomial Coefficients for a Fixed Large N", "id": "sum_of_nci_for_a_fixed_large_n", "importance": 1}, {"title": "Sum of nCr Over a Fixed Congruence Class", "id": "sum_of_ncr_over_a_fixed_congruence_class", "importance": 2}, {"title": "[Problem] Sum of nCr(a[i], K) for each K from 1 to N", "id": "sum_of_ncr_a_i_k_for_each_k_from_1_to_n", "importance": 2}]}, {"title": "Stirling Numbers", "id": "stirling_numbers", "topics": [{"title": "Stirling Numbers (Basic)", "id": "stirling_numbers", "importance": 3}, {"title": "Stirling Number of the First Kind for Fixed N", "id": "stirling_number_of_the_first_kind_for_fixed_n", "importance": 2}, {"title": "Stirling Number of the First Kind for Fixed K", "id": "stirling_number_of_the_first_kind_for_fixed_k", "importance": 1}, {"title": "Stirling Number of the Second Kind for Fixed N", "id": "stirling_number_of_the_second_kind_for_fixed_n", "importance": 2}, {"title": "Stirling Number of the Second Kind for Fixed K", "id": "stirling_number_of_the_second_kind_for_fixed_k", "importance": 1}]}, {"title": "Partitions", "id": "partitions", "topics": [{"title": "Partitions of an Integer, Partition Function and Pentagonal Number Theorem", "id": "partition_function", "importance": 2}, {"title": "Partitions of a Set / Bell Number", "id": "bell_number", "importance": 2}]}, {"title": "Miscellaneous", "id": "miscellaneous", "topics": [{"title": "Burnside's Lemma / Polya Enumeration Theorem", "id": "burnside_lemma", "importance": 2}, {"title": "Bertrand's Ballot Theorem", "id": "bertrands_ballot_theorem", "importance": 2}, {"title": "Young Tableaus and the Hook Length Formula", "id": "young_tableaus", "importance": 1}]}]}, {"title": "Math", "id": "math", "subcategories": [{"title": "Convolution", "id": "convolution", "topics": [{"title": "Fast Fourier Transform (FFT)", "id": "fft", "importance": 3}, {"title": "Number Theoretic Transform (NTT)", "id": "ntt", "importance": 3}, {"title": "2D FFT / NTT", "id": "2d_fft_ntt", "importance": 2}, {"title": "Online FFT / NTT", "id": "online_ntt", "importance": 2}, {"title": "Fast Walsh Hadamard Transform (FWHT) and its Variations", "id": "fwht", "importance": 3}, {"title": "GCD Convolution", "id": "gcd_convolution", "importance": 2}, {"title": "LCM Convolution", "id": "lcm_convolution", "importance": 2}]}, {"title": "Polynomial", "id": "polynomial", "topics": [{"title": "Generating Functions", "id": "generating_functions", "importance": 3}, {"title": "Polynomial Inverse", "id": "polynomial_inverse", "importance": 2}, {"title": "Polynomial Exp", "id": "polynomial_exp", "importance": 2}, {"title": "Polynomial Log", "id": "polynomial_log", "importance": 2}, {"title": "Polynomial Pow", "id": "polynomial_pow", "importance": 3}, {"title": "Polynomial Sqrt", "id": "polynomial_sqrt", "importance": 2}, {"title": "Polynomial Composition", "id": "polynomial_composition", "importance": 1}, {"title": "Multipoint Evaluation", "id": "multipoint_evaluation", "importance": 2}, {"title": "Chirp Z Transform", "id": "chirp_z_transform", "importance": 2}, {"title": "Polynomial Interpolation", "id": "polynomial_interpolation", "importance": 2}, {"title": "Polynomial Shift", "id": "polynomial_shift", "importance": 2}, {"title": "Shift of Sampling Points of Polynomial", "id": "polynomial_shift_sampling_points", "importance": 1}, {"title": "Polyomial Division and Remainder", "id": "polynomial_division_and_remainder", "importance": 2}, {"title": "Polynomial Roots Under a Modulo", "id": "polynomial_roots_under_modulo", "importance": 1}, {"title": "Resultant of Two Polynomials and Half-GCD Algorithm", "id": "resultant_of_two_polynomials", "importance": 1}, {"title": "Lagrange Interpolation", "id": "lagrange_interpolation", "importance": 3}, {"title": "[Problem] Sum of r^i * poly(i)", "id": "polynomial_sum", "importance": 1}, {"title": "Polynomial with Binomial Coefficients", "id": "polynomial_with_binomial_coefficients", "importance": 1}, {"title": "Subset Sum Problem using Generating Functions", "id": "subset_sum_problem_using_generating_functions", "importance": 2}, {"title": "Polynomial Factorization of (x^n - 1) and Cyclotomic Polynomials", "id": "polynomial_factorization_of_xn_minus_1", "importance": 1}, {"title": "Schwartz–Zippel Lemma", "id": "schwartz_zippel_lemma", "importance": 1}, {"title": "Lagrange Inversion Theorem", "id": "lagrange_inversion_theorem", "importance": 1}]}, {"title": "Matrices", "id": "matrices", "topics": [{"title": "Matrix Exponentiation", "id": "matrix_exponentiation", "importance": 3}, {"title": "Permanent of a Matrix", "id": "permanent_of_a_matrix", "importance": 2}, {"title": "Freivald's Algorithm", "id": "freivalds_algorithm", "importance": 1}, {"title": "Vandermonde Matrix", "id": "vandermonde_matrix", "importance": 1}, {"title": "Hafnian of a Matrix / Number of Perfect Matchings in a Graph", "id": "hafnian_of_a_matrix", "importance": 1}, {"title": "Frobenius Form of a Matrix and Fast Matrix Power", "id": "frobenius_form_of_a_matrix", "importance": 1}]}, {"title": "Linear Recurrence", "id": "linear_recurrence", "topics": [{"title": "Linear Recurrence Relations", "id": "linear_recurrence_relations", "importance": 2}, {"title": "Linear Recurrence using Cayley-Hamilton Theorem in O(N^2 log K)", "id": "linear_recurrence_using_cayley_hamilton_theorem", "importance": 3}, {"title": "Linear Recurrence using Generating Functions in O(N log N log K)", "id": "linear_recurrence_using_generating_functions", "importance": 2}, {"title": "Linear Recurrence with Polynomial Coefficients", "id": "linear_recurrence_with_polynomial_coefficients", "importance": 1}, {"title": "Linear Recurrence on Matrices", "id": "linear_recurrence_on_matrices", "importance": 1}, {"title": "Generating Function of a Linear Recurrence", "id": "generating_function_of_a_linear_recurrence", "importance": 1}, {"title": "Berlekamp Massey", "id": "berlekamp_messey", "importance": 3}, {"title": "Reeds-Sloane Algorithm", "id": "reeds_sloane_algorithm", "importance": 1}]}, {"title": "Linear Algebra", "id": "linear_algebra", "topics": [{"title": "Gaussian Elimination", "id": "gaussian_elimination", "importance": 3}, {"title": "Gaussian Elimination Modulo 2", "id": "gaussian_elimination_modulo_2", "importance": 2}, {"title": "Determinant of a Matrix", "id": "determinant_under_prime_modulo", "importance": 2}, {"title": "Determinant under Composite Modulo", "id": "determinant_under_composite_modulo", "importance": 1}, {"title": "Characteristic Polynomial and Hesserberg Matrix", "id": "characteristic_polynomial", "importance": 1}, {"title": "[Problem] Determinant of Product Matrix", "id": "determinant_of_product_matrix", "importance": 1}, {"title": "Determinant of Sparse Matrix and Black Box Linear Algebra", "id": "determinant_of_sparse_matrix", "importance": 1}, {"title": "[Problem] Determinant of Permutant and Circulant Matrix", "id": "determinant_of_permutant_matrix", "importance": 1}, {"title": "GCD Determinant / Smith's Determinant", "id": "gcd_determinant", "importance": 1}, {"title": "Cauchy–Binet formula", "id": "cauchy_binet_formula", "importance": 1}, {"title": "Inverse of a Matrix", "id": "inverse_of_a_matrix", "importance": 2}, {"title": "Inverse of a Matrix modulo 2", "id": "inverse_of_a_matrix_modulo_2", "importance": 1}, {"title": "Thomas Algorithm", "id": "thomas_algorithm", "importance": 1}, {"title": "Vector Space and XOR Basis", "id": "basis_vector", "importance": 3}, {"title": "[Technique] XOR Basis ft Reduced Row Echelon Form", "id": "basis_vector_reduced_row_echelon_form", "importance": 2}, {"title": "[Technique] XOR Basis ft Lexicographically Largest Basis", "id": "basis_vector_ft_lexicographically_largest_basis", "importance": 2}, {"title": "XOR Basis with Deletions (Online)", "id": "basis_vector_with_deletions", "importance": 1}, {"title": "q Binomial", "id": "q_binomial", "importance": 2}]}, {"title": "Formulas", "id": "formulas", "topics": [{"title": "Gauss's Eureka Theorem", "id": "gausss_eureka_theorem", "importance": 2}, {"title": "Titu's Lemma", "id": "titus_lemma", "importance": 2}, {"title": "Lifting-the-exponent(LTE) Lemma", "id": "lte_lemma", "importance": 1}, {"title": "Faulhaber's Formula and Bernoulli Numbers", "id": "faulhabers_formula", "importance": 2}]}, {"title": "Calculus", "id": "calculus", "topics": [{"title": "Differentiation and Integration", "id": "integration", "importance": 2}, {"title": "Line Integral", "id": "line_integral", "importance": 1}]}, {"title": "Probabilities and Expected Values", "id": "probabilities_and_expected_values", "topics": [{"title": "Probabilities and Expected Values", "id": "probabilities_and_expected_values", "importance": 3}, {"title": "Expected Value Powers Technique", "id": "expected_value_powers_technique", "importance": 3}, {"title": "The Slime Trick", "id": "the_slime_trick", "importance": 1}, {"title": "Expected Occurrence Time as Substring", "id": "expected_occurrence_time_as_substring", "importance": 1}, {"title": "Gambler's Ruin", "id": "gamblers_ruin", "importance": 1}, {"title": "Martingale", "id": "martingale", "importance": 1}]}, {"title": "Mathematical Optimization", "id": "mathematical_optimization", "topics": [{"title": "Lagrange Multiplier", "id": "lagrange_multiplier", "importance": 2}, {"title": "Linear Programming / Simplex Algorithm", "id": "simplex_algorithm", "importance": 2}, {"title": "Duality in Linear Programming (LP <> Flow)", "id": "duality_in_linear_programming", "importance": 1}, {"title": "Dinkelbach Algorithm", "id": "dinkelbach_algorithm", "importance": 1}]}, {"title": "Miscellaneous", "id": "miscellaneous", "topics": [{"title": "Continued Fractions", "id": "continued_fractions", "importance": 1}, {"title": "Polynomial Real Roots", "id": "polynomial_root_finding", "importance": 1}, {"title": "Finite Field Arithmetic Binary", "id": "finite_field_arithmetic_binary", "importance": 1}]}]}, {"title": "Strings", "id": "strings", "subcategories": [{"title": "String Matching", "id": "string_matching", "topics": [{"title": "Knuth Morris Pratt (KMP) and Prefix Automaton", "id": "kmp", "importance": 3}, {"title": "Z Algorithm", "id": "z_algorithm", "importance": 3}, {"title": "String Matching using Bitsets", "id": "string_matching_using_bitsets", "importance": 2}, {"title": "String Matching with FFT ft Wildcard Matching", "id": "string_matching_with_fft", "importance": 2}]}, {"title": "Hashing", "id": "hashing", "topics": [{"title": "String Hashing", "id": "string_hashing", "importance": 3}, {"title": "2D String Hashing", "id": "2d_string_hashing", "importance": 2}, {"title": "XOR Hashing", "id": "xor_hashing", "importance": 3}, {"title": "Multiset Hashing", "id": "multiset_hashing", "importance": 3}]}, {"title": "Aho Corasick", "id": "aho_corasick", "topics": [{"title": "Aho Corasick", "id": "aho_corasick", "importance": 3}, {"title": "Dynamic Aho Corasick", "id": "dynamic_aho_corasick", "importance": 2}]}, {"title": "Suffix Structures", "id": "suffix_structures", "topics": [{"title": "Suffix Array", "id": "suffix_array", "importance": 3}, {"title": "Isomorphic Suffix Array", "id": "isomorphic_suffix_array", "importance": 1}, {"title": "Dynamic Suffix Array", "id": "dynamic_suffix_array", "importance": 1}, {"title": "Suffix Automaton", "id": "suffix_automaton", "importance": 3}, {"title": "[Problem] Distinct Substring Queries in Range", "id": "suffix_automaton_ft_distinct_substring_queries_in_range", "importance": 1}, {"title": "Suffix Tree", "id": "suffix_tree", "importance": 1}]}, {"title": "Palindromes", "id": "palindromes", "topics": [{"title": "Palindromic Tree / Eertree", "id": "palindromic_tree", "importance": 3}, {"title": "Persistent Palindromic Tree", "id": "persistent_palindromic_tree", "importance": 1}, {"title": "Manachers Algorithm", "id": "manachers_algorithm", "importance": 3}, {"title": "[Problem] Minimum Palindrome Factorization", "id": "minimum_palindrome_factorization", "importance": 1}, {"title": "[Problem] Number of Palindromes in Range", "id": "number_of_palindromes_in_range", "importance": 2}]}, {"title": "Longest Common Subsequence (LCS)", "id": "lcs", "topics": [{"title": "Longest Common Subsequence (LCS)", "id": "lcs", "importance": 3}, {"title": "All Substring Longest Common Subsequence", "id": "all_substring_longest_common_subsequence", "importance": 1}, {"title": "Bit LCS", "id": "bit_lcs", "importance": 1}, {"title": "Cyclic LCS", "id": "cyclic_lcs", "importance": 1}, {"title": "LCS on RLE compressed string", "id": "lcs_on_rle_compressed_string", "importance": 1}]}, {"title": "Miscellaneous", "id": "miscellaneous", "topics": [{"title": "Balanced Brackets", "id": "balanced_brackets", "importance": 3}, {"title": "Expression Parsing", "id": "expression_parsing", "importance": 1}, {"title": "Lyndon Factorization / Duval Algorithm", "id": "lyndon_factorization", "importance": 1}, {"title": "Finding Repetitions / Main-Lorentz Algorithm", "id": "main_lorentz_algorithm", "importance": 1}, {"title": "De Bruijn Sequence", "id": "de_bruijn_sequence", "importance": 1}]}]}, {"title": "Dynamic Programming (DP)", "id": "dynamic_programming", "subcategories": [{"title": "Intro to DP", "id": "intro_to_dp", "topics": [{"title": "Knapsack and Basic Dynamic Programming", "id": "knapsack", "importance": 3}, {"title": "Knapsack and Subset Sum Optimizations", "id": "subset_sum_in_sqrt", "importance": 3}]}, {"title": "Digit DP", "id": "digit_dp", "topics": [{"title": "Digit DP", "id": "digit_dp", "importance": 3}]}, {"title": "DP Optimizations", "id": "dp_optimizations", "topics": [{"title": "Divide and Conquer Optimization", "id": "divide_and_conquer_optimization", "importance": 3}, {"title": "Knuth Optimization", "id": "knuth_optimization", "importance": 3}, {"title": "Aliens Trick / WQS Binary Search", "id": "aliens_trick", "importance": 2}, {"title": "1D1D DP Optimization", "id": "1d1d_dp_optimization", "importance": 2}, {"title": "DP Optimization using Data Structures [Some Practice Problems]", "id": "dp_optimization_using_data_structures", "importance": 3}]}, {"title": "Convex Hull Trick (CHT)", "id": "convex_hull_trick", "topics": [{"title": "Convex Hull Trick (CHT) and Dynamic CHT", "id": "cht", "importance": 3}, {"title": "Persistent CHT", "id": "persistent_cht", "importance": 1}]}, {"title": "Li Chao Tree", "id": "li_chao_tree", "topics": [{"title": "Li Chao Tree", "id": "li_chao_tree", "importance": 2}, {"title": "Persistent Li Chao Tree", "id": "persistent_li_chao_tree", "importance": 1}, {"title": "Extended Li Chao tree", "id": "extended_li_chao_tree", "importance": 1}]}, {"title": "Bit Related DP", "id": "bit_related_dp", "topics": [{"title": "Bitmask DP", "id": "bitmask_dp", "importance": 3}, {"title": "Sum Over Subsets DP (SOS DP)", "id": "sos_dp", "importance": 3}, {"title": "[Problem] Subset Union of Bitsets", "id": "subset_union_of_bitsets", "importance": 1}, {"title": "Subset Convolution", "id": "subset_convolution", "importance": 2}, {"title": "[Trick] Dynamic Submask Count", "id": "dynamic_submask_count", "importance": 2}, {"title": "[Problem] XOR Equation", "id": "xor_equation", "importance": 1}]}, {"title": "More Tricks", "id": "more_tricks", "topics": [{"title": "Open and Close Interval Trick", "id": "open_and_close_interval_trick", "importance": 2}, {"title": "Slope Trick", "id": "slope_trick", "importance": 2}, {"title": "x2 +1 Trick", "id": "x2_plus_1_trick", "importance": 2}, {"title": "Combining Subtrees Technique", "id": "combining_subtrees_technique", "importance": 3}]}, {"title": "Classic DP", "id": "classic_dp", "topics": [{"title": "Longest Increasing Subsequence (LIS)", "id": "lis", "importance": 3}, {"title": "Interval DP / Range DP / Matrix Chain Multiplication (MCM)", "id": "mcm", "importance": 3}, {"title": "Edit Distance", "id": "edit_distance", "importance": 3}]}, {"title": "Dp on Different Structures", "id": "dp_on_different_structures", "topics": [{"title": "DP on Trees and DAGs", "id": "dp_on_trees_and_dags", "importance": 3}, {"title": "DP on Trees ft Centroid / DSU on Tree", "id": "dp_on_trees_ft_centroid", "importance": 2}, {"title": "DP on Graphs", "id": "dp_on_graphs", "importance": 3}, {"title": "DP on Grid / Grid DP", "id": "grid_dp", "importance": 3}, {"title": "DP on Broken Profile / Profile DP", "id": "profile_dp", "importance": 2}]}, {"title": "State Compression DP", "id": "state_compression_dp", "topics": [{"title": "State Compression DP", "id": "state_compression_dp", "importance": 3}]}, {"title": "Counting DP", "id": "counting_dp", "topics": [{"title": "Counting DP", "id": "counting_dp", "importance": 3}]}, {"title": "Probability and Expectation DP", "id": "probability_and_expectation_dp", "topics": [{"title": "Probability and Expectation DP", "id": "probability_expectation_dp", "importance": 3}]}, {"title": "Game DP", "id": "game_dp", "topics": [{"title": "Game DP / Minimax Algorithm", "id": "game_dp", "importance": 3}]}, {"title": "Miscellaneous", "id": "miscellaneous", "topics": [{"title": "Tree Knapsack / Knapsack on Trees", "id": "tree_knapsack", "importance": 3}, {"title": "Matrix Exponentiation DP", "id": "matrix_exponentiation_dp", "importance": 3}, {"title": "DP with BSGS", "id": "dp_with_bsgs", "importance": 1}, {"title": "DP with Sqrt Decomposition", "id": "dp_with_sqrt_decomposition", "importance": 2}, {"title": "Divide and Conquer DP (not optimization)", "id": "divide_and_conquer_dp", "importance": 2}, {"title": "SOS DP on Trees", "id": "sos_dp_on_trees", "importance": 1}, {"title": "CHT on Trees", "id": "cht_on_trees", "importance": 2}, {"title": "DP on Interval Set / Interval DP (Advanced)", "id": "advanced_interval_dp", "importance": 2}]}]}, {"title": "Game Theory", "id": "game_theory", "subcategories": [{"title": "Impartial Games", "id": "impartial_games", "topics": [{"title": "Impartial Games and Nim", "id": "nim_game", "importance": 3}, {"title": "Sprague-Grundy Theorem", "id": "sprague_grundy_theorem", "importance": 3}, {"title": "Games on Graphs", "id": "games_on_graphs", "importance": 3}, {"title": "Grundy Value on Trees", "id": "grundy_value_on_trees", "importance": 2}, {"title": "Grundy Value on DAGs", "id": "grundy_value_on_dags", "importance": 2}, {"title": "Subtraction Games", "id": "subtraction_games", "importance": 2}]}, {"title": "Partizan Games", "id": "partizan_games", "topics": [{"title": "Partizan Games / Hackenbush", "id": "hackenbush", "importance": 1}]}, {"title": "Classic Games", "id": "classic_games", "topics": [{"title": "Wythoff's Game", "id": "wythoffs_game", "importance": 2}, {"title": "Chomp", "id": "chomp", "importance": 1}, {"title": "Green Hackenbush", "id": "green_hackenbush", "importance": 1}]}, {"title": "Miscellaneous", "id": "miscellaneous", "topics": [{"title": "Adversarial Search / Alpha-Beta Pruning", "id": "alpha_beta_pruning", "importance": 1}, {"title": "Combinatorial Game Theory (CGT)", "id": "cgt", "importance": 1}]}]}, {"title": "Geometry", "id": "geometry", "subcategories": [{"title": "Basics", "id": "basics", "topics": [{"title": "Point and Vector Operations", "id": "point_vector_operations", "importance": 3}, {"title": "Dot and Cross Products", "id": "dot_cross_products", "importance": 3}, {"title": "Lines and Segments Representations", "id": "line_segment_representations", "importance": 3}, {"title": "Intersection of Lines and Segments", "id": "intersection_lines_segments", "importance": 3}, {"title": "Distance from Point to Line / Segment", "id": "distance_point_line", "importance": 3}, {"title": "Projection of Point on Line", "id": "projection_point_line", "importance": 3}, {"title": "Reflection of Point over Line", "id": "reflection_point_line", "importance": 3}, {"title": "Polygon Area and Centroid", "id": "polygon_area_centroid", "importance": 3}, {"title": "Point in Polygon Test", "id": "point_in_polygon", "importance": 3}]}, {"title": "Convex Hull", "id": "convex_hull", "topics": [{"title": "Convex Hull (Graham Scan & Monotone Chain)", "id": "convex_hull", "importance": 3}, {"title": "Dynamic Convex Hull (Online)", "id": "dynamic_convex_hull", "importance": 2}, {"title": "3D Convex Hull", "id": "3d_convex_hull", "importance": 1}, {"title": "Convex Hull Trick (CHT) - Geometry Perspective", "id": "cht_geometry", "importance": 2}]}, {"title": "Sweep Line", "id": "sweep_line", "topics": [{"title": "Sweep Line Technique", "id": "sweep_line", "importance": 3}, {"title": "Segment Intersection (Bentley-Ottmann)", "id": "segment_intersection", "importance": 2}, {"title": "Closest Pair of Points", "id": "closest_pair_points", "importance": 3}]}, {"title": "Circles", "id": "circles", "topics": [{"title": "Circle Representations", "id": "circle_representations", "importance": 3}, {"title": "Intersection of Circle with Line / Segment", "id": "intersection_circle_line", "importance": 3}, {"title": "Intersection of Two Circles", "id": "intersection_two_circles", "importance": 3}, {"title": "Tangents to Circle", "id": "tangents_circle", "importance": 3}, {"title": "Common Tangents of Two Circles", "id": "common_tangents_circles", "importance": 2}, {"title": "Circle Area and Circumference", "id": "circle_area_circumference", "importance": 3}, {"title": "Minimum Enclosing Circle (Welzl's Algorithm)", "id": "minimum_enclosing_circle", "importance": 3}, {"title": "Radical Axis and Radical Center", "id": "radical_axis", "importance": 2}]}, {"title": "Triangles", "id": "triangles", "topics": [{"title": "Triangle Properties (Incircle, Circumcircle, Orthocenter)", "id": "triangle_properties", "importance": 3}, {"title": "Law of Sines and Cosines", "id": "law_sines_cosines", "importance": 3}]}, {"title": "Advanced Polygon Algorithms", "id": "advanced_polygon_algorithms", "topics": [{"title": "Rotating Calipers (Diameter, Width, Minimum Box)", "id": "rotating_calipers", "importance": 3}, {"title": "Minkowski Sum of Convex Polygons", "id": "minkowski_sum", "importance": 2}, {"title": "Half-Plane Intersection", "id": "half_plane_intersection", "importance": 2}, {"title": "Voronoi Diagram and Delaunay Triangulation", "id": "voronoi_delaunay", "importance": 1}, {"title": "Polygon Triangulation", "id": "polygon_triangulation", "importance": 1}, {"title": "Centroid of a Polygon (Non-convex)", "id": "centroid_non_convex", "importance": 1}]}, {"title": "3D Geometry", "id": "3d_geometry", "topics": [{"title": "3D Point and Vector Operations", "id": "3d_point_vector", "importance": 2}, {"title": "Planes and Lines in 3D", "id": "planes_lines_3d", "importance": 2}, {"title": "3D Distance Problems", "id": "3d_distances", "importance": 2}, {"title": "Polyhedron Volume", "id": "polyhedron_volume", "importance": 1}]}, {"title": "Miscellaneous", "id": "miscellaneous", "topics": [{"title": "Pick's Theorem", "id": "picks_theorem", "importance": 3}, {"title": "Euler's Formula for Planar Graphs", "id": "eulers_formula_planar", "importance": 2}, {"title": "Delaunay Triangulation and MST", "id": "delaunay_mst", "importance": 1}, {"title": "Coordinate Compression in Geometry", "id": "coordinate_compression_geometry", "importance": 3}, {"title": "Angle Sorting", "id": "angle_sorting", "importance": 3}]}]}, {"title": "Miscellaneous", "id": "miscellaneous", "subcategories": [{"title": "Search", "id": "search", "topics": [{"title": "Meet in the Middle", "id": "meet_in_middle", "importance": 3}, {"title": "Iterative Deepening DFS (IDDFS)", "id": "iddfs", "importance": 2}, {"title": "Bidirectional Search", "id": "bidirectional_search", "importance": 2}]}, {"title": "Optimization", "id": "optimization", "topics": [{"title": "Ternary Search", "id": "ternary_search", "importance": 3}, {"title": "Hill Climbing", "id": "hill_climbing", "importance": 1}, {"title": "Simulated Annealing", "id": "simulated_annealing", "importance": 2}, {"title": "Genetic Algorithms", "id": "genetic_algorithms", "importance": 1}]}, {"title": "Tricks", "id": "tricks", "topics": [{"title": "Pragmas and Optimization Options in C++", "id": "pragmas", "importance": 2}, {"title": "Custom Allocators", "id": "custom_allocators", "importance": 1}, {"title": "Randomization (mt19937)", "id": "randomization", "importance": 3}]}]}];
    const expandedStates = {};
    // Redirect to topic page when clicked
    function onTopicClick(topicId) {
      const topicUrls = {
        "programming": "topics/basics/01-intro-to-cp/intro-to-cp/",
        "competitive_programming": "topics/basics/01-intro-to-cp/intro-to-cp/",
        "complexity_analysis": "topics/basics/01-intro-to-cp/intro-to-cp/",
        "arrays": "topics/basics/02-arrays/static-arrays/",
        "vector": "topics/basics/02-arrays/dynamic-arrays/",
        "two_pointers": "topics/basics/05-two-pointers/two-pointers/",
        "prefix_sum": "topics/basics/06-prefix-sums/prefix-sums/",
        "sliding_window_technique": "topics/basics/04-sliding-window/fixed-size/"
      };
      const url = topicUrls[topicId];
      if (url) {
        window.location.href = url;
      } else {
        alert("This topic's python guide is currently under development and will be published soon!");
      }
    }
    function toggleNode(nodeKey) {
      expandedStates[nodeKey] = !expandedStates[nodeKey];
      renderRoadmap();
    }
    const BASE_W = 900;
    function getScale() {
      const svg = document.getElementById('svg-root');
      const w = svg.getBoundingClientRect().width || BASE_W;
      return Math.min(Math.max(w / BASE_W, 0.55), 1.6);
    }
    function renderRoadmap() {
      const s = getScale();
      const CAT_H       = Math.round(58  * s);
      const CAT_GAP     = Math.round(14  * s);
      const SUB_H       = Math.round(52  * s);
      const SUB_GAP     = Math.round(14  * s);
      const TOPIC_H     = Math.round(46  * s);
      const TOPIC_GAP   = Math.round(10  * s);
      const LEGEND_H    = Math.round(70  * s);
      const INDENT_SUB  = Math.round(40  * s);
      const INDENT_TOP  = Math.round(40  * s);
      const CAT_FS      = Math.round(20  * s);
      const SUB_FS      = Math.round(18  * s);
      const TOPIC_FS    = Math.round(18  * s);
      const BADGE_FS    = Math.round(13  * s);
      const LEGEND_FS   = Math.round(15  * s);
      const DOT_R       = Math.round(7   * s);
      const BADGE_W     = Math.round(50  * s);
      const BADGE_H     = Math.round(24  * s);
      const VB_W = 1000;
      const nodesContainer = document.getElementById('nodes-container');
      const linesContainer = document.getElementById('lines-container');
      nodesContainer.innerHTML = '';
      linesContainer.innerHTML = '';
      let styleEl = document.getElementById('roadmap-dyn-style');
      if (!styleEl) {
        styleEl = document.createElementNS('http://www.w3.org/2000/svg', 'style');
        styleEl.id = 'roadmap-dyn-style';
        document.getElementById('svg-root').appendChild(styleEl);
      }
      styleEl.textContent = [
        `.node-text { font-size: ${TOPIC_FS}px; }`,
        `.node-text-disabled { font-size: ${TOPIC_FS}px; }`,
        `.coming-soon-badge { font-size: ${Math.round(15*s)}px; }`,
        `.importance-badge { font-size: ${BADGE_FS}px; }`,
        `.legend-text { font-size: ${LEGEND_FS}px; }`,
        `.toggle-icon { font-size: ${Math.round(18*s)}px; }`,
      ].join(' ');
      let y = LEGEND_H;
      const startX = 20;
      roadmapData.forEach((cat, catIdx) => {
        const catKey = `cat-${cat.id || catIdx}`;
        const isCatExpanded = !!expandedStates[catKey];
        const isBasics = cat.title.toLowerCase() === 'basics';
        const catY = y;
        y += CAT_H + CAT_GAP;
        let childYLines = [];
        if (isBasics && isCatExpanded) {
          cat.subcategories.forEach((subcat, subcatIdx) => {
            const subcatKey = `subcat-${cat.id || catIdx}-${subcat.id || subcatIdx}`;
            const isSubcatExpanded = !!expandedStates[subcatKey];
            const subcatX = startX + INDENT_SUB;
            const subcatY = y;
            childYLines.push(subcatY + Math.round(SUB_H / 2));
            y += SUB_H + SUB_GAP;
            let topicYLines = [];
            if (isSubcatExpanded) {
              subcat.topics.forEach((topic) => {
                const topicX = subcatX + INDENT_TOP;
                const topicY = y;
                topicYLines.push(topicY + Math.round(TOPIC_H / 2));
                const topicGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
                topicGroup.setAttribute('transform', `translate(${topicX}, ${topicY})`);
                topicGroup.setAttribute('filter', 'url(#shadow)');
                const cardW = VB_W - topicX - startX;
                const card = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                card.setAttribute('width', cardW);
                card.setAttribute('height', TOPIC_H);
                card.setAttribute('rx', Math.round(6 * s));
                card.setAttribute('class', 'topic-card');
                card.setAttribute('onclick', `onTopicClick('${topic.id}')`);
                topicGroup.appendChild(card);
                let impColor = '#10b981', impText = 'Low';
                if (topic.importance === 3) { impColor = '#ef4444'; impText = 'High'; }
                else if (topic.importance === 2) { impColor = '#f59e0b'; impText = 'Med'; }
                const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                dot.setAttribute('cx', Math.round(18 * s));
                dot.setAttribute('cy', Math.round(TOPIC_H / 2));
                dot.setAttribute('r', DOT_R);
                dot.setAttribute('fill', impColor);
                topicGroup.appendChild(dot);
                const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                text.setAttribute('x', Math.round(36 * s));
                text.setAttribute('y', Math.round(TOPIC_H / 2 + TOPIC_FS * 0.35));
                text.setAttribute('class', 'node-text');
                let titleText = topic.title;
                if (titleText.length > 90) titleText = titleText.substring(0, 87) + '...';
                text.textContent = titleText;
                topicGroup.appendChild(text);
                const badgeGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
                const badgeX = cardW - BADGE_W - Math.round(52 * s);
                const badgeY = Math.round((TOPIC_H - BADGE_H) / 2);
                badgeGroup.setAttribute('transform', `translate(${badgeX}, ${badgeY})`);
                const badgeRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                badgeRect.setAttribute('width', BADGE_W);
                badgeRect.setAttribute('height', BADGE_H);
                badgeRect.setAttribute('rx', Math.round(6 * s));
                badgeRect.setAttribute('fill', impColor);
                badgeGroup.appendChild(badgeRect);
                const badgeText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                badgeText.setAttribute('x', Math.round(BADGE_W / 2));
                badgeText.setAttribute('y', Math.round(BADGE_H / 2));
                badgeText.setAttribute('class', 'importance-badge');
                badgeText.textContent = impText;
                badgeGroup.appendChild(badgeText);
                topicGroup.appendChild(badgeGroup);
                const linkGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
                const iconX = cardW - Math.round(22 * s);
                const iconY = Math.round((TOPIC_H - 16) / 2);
                linkGroup.setAttribute('transform', `translate(${iconX}, ${iconY})`);
                linkGroup.setAttribute('class', 'link-icon');
                linkGroup.setAttribute('onclick', `onTopicClick('${topic.id}')`);
                const linkPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                linkPath.setAttribute('d', 'M10.586 3L12 4.414 7.414 9H9v2H4V6h2v1.586L10.586 3z');
                linkGroup.appendChild(linkPath);
                const linkRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                linkRect.setAttribute('width', 16); linkRect.setAttribute('height', 16);
                linkRect.setAttribute('fill', 'transparent');
                linkGroup.appendChild(linkRect);
                topicGroup.appendChild(linkGroup);
                nodesContainer.appendChild(topicGroup);
                y += TOPIC_H + TOPIC_GAP;
              });
              if (topicYLines.length > 0) {
                const branchX = subcatX + Math.round(20 * s);
                const trunk = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                trunk.setAttribute('class', 'line-branch');
                trunk.setAttribute('d', `M ${branchX} ${subcatY + SUB_H} L ${branchX} ${topicYLines[topicYLines.length - 1]}`);
                linesContainer.appendChild(trunk);
                topicYLines.forEach(tY => {
                  const branch = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                  branch.setAttribute('class', 'line-branch');
                  branch.setAttribute('d', `M ${branchX} ${tY} L ${subcatX + INDENT_TOP} ${tY}`);
                  linesContainer.appendChild(branch);
                });
              }
            }
            const subcatGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
            subcatGroup.setAttribute('transform', `translate(${subcatX}, ${subcatY})`);
            subcatGroup.setAttribute('filter', 'url(#shadow)');
            const subCardW = VB_W - subcatX - startX;
            const subCard = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            subCard.setAttribute('width', subCardW);
            subCard.setAttribute('height', SUB_H);
            subCard.setAttribute('rx', Math.round(6 * s));
            subCard.setAttribute('class', 'subcategory-card');
            subCard.setAttribute('onclick', `toggleNode('${subcatKey}')`);
            subcatGroup.appendChild(subCard);
            const subText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            subText.setAttribute('x', Math.round(15 * s));
            subText.setAttribute('y', Math.round(SUB_H / 2 + SUB_FS * 0.35));
            subText.setAttribute('class', 'node-text node-title');
            subText.textContent = subcat.title;
            subcatGroup.appendChild(subText);
            const subToggle = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            subToggle.setAttribute('x', subCardW - Math.round(22 * s));
            subToggle.setAttribute('y', Math.round(SUB_H / 2 + SUB_FS * 0.35));
            subToggle.setAttribute('class', 'toggle-icon node-title');
            subToggle.textContent = isSubcatExpanded ? '−' : '+';
            subcatGroup.appendChild(subToggle);
            nodesContainer.appendChild(subcatGroup);
          });
          if (childYLines.length > 0) {
            const branchX = startX + Math.round(20 * s);
            const trunk = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            trunk.setAttribute('class', 'line-branch');
            trunk.setAttribute('d', `M ${branchX} ${catY + CAT_H} L ${branchX} ${childYLines[childYLines.length - 1]}`);
            linesContainer.appendChild(trunk);
            childYLines.forEach(sY => {
              const branch = document.createElementNS('http://www.w3.org/2000/svg', 'path');
              branch.setAttribute('class', 'line-branch');
              branch.setAttribute('d', `M ${branchX} ${sY} L ${startX + INDENT_SUB} ${sY}`);
              linesContainer.appendChild(branch);
            });
          }
        }
        const catGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        catGroup.setAttribute('transform', `translate(${startX}, ${catY})`);
        catGroup.setAttribute('filter', 'url(#shadow)');
        const catCardW = VB_W - startX * 2;
        const catCard = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        catCard.setAttribute('width', catCardW);
        catCard.setAttribute('height', CAT_H);
        catCard.setAttribute('rx', Math.round(6 * s));
        if (isBasics) {
          catCard.setAttribute('class', 'category-card');
          catCard.setAttribute('onclick', `toggleNode('${catKey}')`);
        } else {
          catCard.setAttribute('class', 'category-card-disabled');
        }
        catGroup.appendChild(catCard);
        const catText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        catText.setAttribute('x', Math.round(15 * s));
        catText.setAttribute('y', Math.round(CAT_H / 2 + CAT_FS * 0.35));
        catText.setAttribute('class', isBasics ? 'node-text node-title' : 'node-text-disabled node-title');
        catText.setAttribute('font-size', `${CAT_FS}px`);
        catText.textContent = cat.title;
        catGroup.appendChild(catText);
        if (isBasics) {
          const toggle = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          toggle.setAttribute('x', catCardW - Math.round(22 * s));
          toggle.setAttribute('y', Math.round(CAT_H / 2 + CAT_FS * 0.35));
          toggle.setAttribute('class', 'toggle-icon node-title');
          toggle.textContent = isCatExpanded ? '−' : '+';
          catGroup.appendChild(toggle);
        } else {
          const badge = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          badge.setAttribute('x', catCardW - Math.round(8 * s));
          badge.setAttribute('y', Math.round(CAT_H / 2 + CAT_FS * 0.35));
          badge.setAttribute('class', 'coming-soon-badge');
          badge.textContent = 'Coming Soon';
          catGroup.appendChild(badge);
        }
        nodesContainer.appendChild(catGroup);
      });
      const finalH = y + Math.round(40 * s);
      const svgRoot = document.getElementById('svg-root');
      svgRoot.setAttribute('viewBox', `0 0 ${VB_W} ${finalH}`);
    }
    renderRoadmap();
    document.addEventListener('DOMContentLoaded', renderRoadmap);
    window.addEventListener('load', renderRoadmap);
    if (typeof ResizeObserver !== 'undefined') {
      new ResizeObserver(() => renderRoadmap()).observe(document.getElementById('svg-root'));
    } else {
      window.addEventListener('resize', renderRoadmap);
    }
  </script>
</svg>
</div>

<div class="hp-section-header" style="margin-top: 4rem;">
  <h2>How to Train</h2>
  <p>Maximize your learning velocity by combining study, coding, and practice.</p>
</div>

<div class="hp-features" style="margin-bottom: 4rem;">
  <div class="hp-card">
    <span class="hp-card-icon">🎯</span>
    <h3>1. Follow the Roadmap</h3>
    <p>Concepts build on top of each other. Master the basics, recursion, and prefix operations before diving into Segment Trees or Flow.</p>
  </div>
  <div class="hp-card">
    <span class="hp-card-icon">💻</span>
    <h3>2. Run Code Templates</h3>
    <p>Read the notes, understand the time complexities, and study the provided templates. Write your own versions to lock in muscle memory.</p>
  </div>
  <div class="hp-card">
    <span class="hp-card-icon">📈</span>
    <h3>3. Practice & Upsolve</h3>
    <p>Solving problems is the only way to improve. Target the practice problem list at the end of each topic until you can solve them independently.</p>
  </div>
</div>
