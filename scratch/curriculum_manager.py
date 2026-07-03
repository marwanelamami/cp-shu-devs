import os
import re
import json
import argparse

# Paths
topic_list_path = r"d:\3-Projects\cp-shu-devs\topic-list.md"
docs_dir = r"d:\3-Projects\cp-shu-devs\docs"
topics_dir = os.path.join(docs_dir, "topics")
roadmap_path = os.path.join(docs_dir, "roadmap.html")
cache_dir = os.path.join(docs_dir, "..", ".agents")
cache_path = os.path.join(cache_dir, "syllabus_cache.json")
mkdocs_path = r"d:\3-Projects\cp-shu-devs\mkdocs.yml"

# Hand-written guidebooks mapping to YouKn0wWho Topic IDs/slugs
guidebooks = {
    "topics/basics/01-intro-to-cp/intro-to-cp.md": "competitive_programming",
    "topics/basics/01-intro-to-cp/complexity-analysis.md": "complexity_analysis",
    "topics/basics/02-arrays/static-arrays.md": "arrays",
    "topics/basics/02-arrays/dynamic-arrays.md": "arrays",
    "topics/basics/03-kadanes-algorithm/kadanes-algorithm.md": "kadanes-algorithm",
    "topics/basics/04-sliding-window/fixed-size.md": "sliding_window_technique",
    "topics/basics/04-sliding-window/variable-size.md": "sliding_window_technique",
    "topics/basics/05-two-pointers/two-pointers.md": "two_pointers",
    "topics/basics/06-prefix-sums/prefix-sums.md": "prefix_sum"
}

overrides = {v: k for k, v in guidebooks.items()}


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

def parse_problem_line(line):
    # Pattern: - [Name](URL) (ID: problem_id | Difficulty: Diff | Solves: ...)
    match = re.search(r"-\s+\[([^\]]+)\]\(([^)]+)\)", line)
    if not match:
        return None
    name = match.group(1).strip()
    url = match.group(2).strip()
    
    # Determine platform
    platform = "Other"
    if "codeforces.com" in url:
        platform = "Codeforces"
    elif "cses.fi" in url:
        platform = "CSES"
    elif "atcoder.jp" in url:
        platform = "AtCoder"
    elif "vjudge.net" in url:
        platform = "VJudge"
    elif "leetcode.com" in url:
        platform = "LeetCode"
    elif "spoj.com" in url:
        platform = "SPOJ"
    elif "codechef.com" in url:
        platform = "CodeChef"
    elif "hackerrank.com" in url:
        platform = "HackerRank"
        
    pid = ""
    difficulty = "Medium"
    id_match = re.search(r"ID:\s*([^|\s)]+)", line)
    if id_match:
        pid = id_match.group(1).strip(" `")
    diff_match = re.search(r"Difficulty:\s*([^|)]+)", line)
    if diff_match:
        difficulty = diff_match.group(1).strip()
        
    return {
        "id": pid,
        "name": name,
        "url": url,
        "platform": platform,
        "difficulty": difficulty
    }

def get_difficulty_span(diff):
    diff_clean = diff.strip()
    diff_color = "#334155" # default slate
    if "very easy" in diff_clean.lower():
        diff_color = "#059669" # green
    elif "easy" in diff_clean.lower():
        diff_color = "#2563eb" # blue
    elif "medium" in diff_clean.lower():
        diff_color = "#d97706" # amber
    elif "hard" in diff_clean.lower():
        diff_color = "#ef4444" # red
    return f'<span style="color: {diff_color}; font-weight: 600;">{diff_clean}</span>'

def get_importance_span(imp):
    imp_clean = imp.strip()
    imp_color = "#334155"
    if "high" in imp_clean.lower():
        imp_color = "#ef4444"
    elif "medium" in imp_clean.lower():
        imp_color = "#d97706"
    elif "low" in imp_clean.lower():
        imp_color = "#059669"
    return f'<span style="color: {imp_color}; font-weight: 600;">{imp_clean}</span>'

def build_problems_table(problems):
    if not problems:
        return "This topic contains no problems."
    table = "| ID | Problem | Platform | Difficulty |\n|---|---|---|---|\n"
    for idx, p in enumerate(problems):
        pid = p["id"] if p["id"] else f"custom_{idx+1}"
        diff_span = get_difficulty_span(p["difficulty"])
        table += f'| {pid} | [{p["name"]}]({p["url"]}) | {p["platform"]} | {diff_span} |\n'
    return table

def parse_custom_problems_table(content):
    custom_problems = []
    # Match markdown table row: | index | [Name](URL) | Platform | Difficulty |
    for line in content.splitlines():
        match = re.match(r"^\s*\|\s*\d+\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]+)\|\s*([^|]+)\|", line)
        if match:
            name = match.group(1).strip()
            url = match.group(2).strip()
            platform = match.group(3).strip()
            raw_diff = match.group(4).strip()
            
            clean_diff = re.sub(r"<[^>]+>", "", raw_diff).strip()
            clean_diff = clean_diff.lstrip("●").strip()
            
            pid = ""
            if "codeforces.com" in url:
                parts = url.strip("/").split("/")
                if len(parts) >= 2:
                    pid = f"codeforces_{parts[-2]}{parts[-1]}".lower()
            elif "cses.fi" in url:
                parts = url.strip("/").split("/")
                if len(parts) >= 1:
                    pid = f"cses_{parts[-1]}".lower()
                    
            custom_problems.append({
                "id": pid,
                "name": name,
                "url": url,
                "platform": platform,
                "difficulty": clean_diff
            })
    return custom_problems

def cmd_parse_cache():
    if not os.path.exists(topic_list_path):
        print(f"Error: Temporary topic database '{topic_list_path}' not found.")
        return
        
    with open(topic_list_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    data = {}
    current_cat = None
    current_sub = None
    
    n = len(lines)
    i = 0
    while i < n:
        line = lines[i].strip()
        if line.startswith("## ") and not "Table of Contents" in line:
            current_cat = line[3:].strip()
            i += 1
            continue
        elif line.startswith("### "):
            current_sub = line[4:].strip()
            i += 1
            continue
        elif line.startswith("#### "):
            topic_name = line[5:].strip()
            if "Original C++ Templates" in topic_name or "🛠️" in topic_name:
                i += 1
                continue
                
            topic = {
                "name": topic_name,
                "category": current_cat or "Basics",
                "subcategory": current_sub or "General",
                "id": "",
                "difficulty": "",
                "importance": "",
                "phase": "",
                "interview": "",
                "python_resources": [],
                "problems": []
            }
            
            i += 1
            state = None
            while i < n:
                next_line = lines[i]
                stripped = next_line.strip()
                if stripped.startswith("#") or stripped == "---":
                    break
                    
                clean_line = stripped.replace("**", "")
                if clean_line.startswith("- Topic ID:"):
                    topic["id"] = clean_line.replace("- Topic ID:", "").strip(" `")
                elif clean_line.startswith("- Difficulty:"):
                    topic["difficulty"] = clean_line.replace("- Difficulty:", "").strip()
                elif clean_line.startswith("- Importance:"):
                    topic["importance"] = clean_line.replace("- Importance:", "").strip()
                elif clean_line.startswith("- Phase:"):
                    topic["phase"] = clean_line.replace("- Phase:", "").strip()
                elif clean_line.startswith("- Interview Topic:"):
                    topic["interview"] = clean_line.replace("- Interview Topic:", "").strip()
                elif stripped.startswith("**Python Resources**:"):
                    state = "python"
                elif stripped.startswith("**Practice Problems**:"):
                    state = "problems"
                elif stripped.startswith("**C++ Resources**:") or stripped.startswith("**General Resources**:") or stripped.startswith("**C++ & General Resources**:"):
                    state = "cpp"  # ignore these resources
                else:
                    if state == "python":
                        # Check if line contains a link
                        topic["python_resources"].append(next_line.rstrip())
                    elif state == "problems":
                        prob = parse_problem_line(next_line)
                        if prob:
                            topic["problems"].append(prob)
                i += 1
                
            tid = topic["id"] if topic["id"] else slugify(topic_name)
            data[tid] = topic
            data[slugify(topic_name)] = topic
            i -= 1
        i += 1
        
    os.makedirs(cache_dir, exist_ok=True)
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully cached {len(data)} topics to '{cache_path}'.")

def load_cache():
    if not os.path.exists(cache_path):
        print(f"Error: Cache file '{cache_path}' not found. Please run 'parse-cache' command first.")
        return None
    with open(cache_path, "r", encoding="utf-8") as f:
        return json.load(f)

def cmd_generate_placeholders():
    data = load_cache()
    if not data:
        return
        
    os.makedirs(topics_dir, exist_ok=True)
    
    # Track categories for generating index.md files
    categories = {}
    
    # We iterate over unique topics in cache
    unique_topics = {}
    for key, topic in data.items():
        unique_topics[topic["name"]] = topic
        
    for topic_name, topic in unique_topics.items():
        cat_slug = slugify(topic["category"])
        topic_slug = slugify(topic_name)
        topic_id = topic["id"] if topic["id"] else topic_slug
        
        # Skip hand-written guidebooks and splits
        if topic_id in overrides or (topic_name == "Arrays") or (topic_name == "Sliding Window"):
            continue
            
        cat_dir = os.path.join(topics_dir, cat_slug)
        os.makedirs(cat_dir, exist_ok=True)
        
        # Populate category structure for index.md
        cat_name = topic["category"]
        if cat_name not in categories:
            categories[cat_name] = {}
        sub_name = topic["subcategory"]
        if sub_name not in categories[cat_name]:
            categories[cat_name][sub_name] = []
        categories[cat_name][sub_name].append(topic)
        
        topic_file = os.path.join(cat_dir, f"{topic_slug}.md")
        
        # Format resources
        python_text = "\n".join(topic["python_resources"]).strip()
        resources_md = "No other additional resources were added to this topic."
        if "http" in python_text:
            resources_md = f"### Recommended Python Resources\n{python_text}"
            
        # Format difficulty/importance spans
        diff_span = get_difficulty_span(topic["difficulty"] or "Basic")
        imp_span = get_importance_span(topic["importance"] or "High")
        
        # Format problems table
        problems_table = build_problems_table(topic["problems"])
        
        content = f"""---
title: {topic_name}
---

# {topic_name}

**Category:** {topic['category']} &nbsp;|&nbsp; **Difficulty:** {diff_span} &nbsp;|&nbsp; **Importance:** {imp_span}

---

!!! info "Under Construction"
    No content has been prepared for this topic/subtopic yet. We are actively developing the content and will be releasing it soon!

---

## YouKn0wWho Academy Reference
While we prepare our written explanations for this topic, you can follow the interactive path and submit solutions directly on the YouKn0wWho Academy platform:

[YouKn0wWho Academy Topic Syllabus](https://youkn0wwho.academy/topic-list)

---

## Additional Resources
{resources_md}

---

## Practice Problems
{problems_table}

---

[Return to Home](../../index.md)
"""
        with open(topic_file, "w", encoding="utf-8") as f:
            f.write(content)
            
    # Generate index.md for each category folder
    for cat_name, subs in categories.items():
        cat_slug = slugify(cat_name)
        cat_dir = os.path.join(topics_dir, cat_slug)
        index_file = os.path.join(cat_dir, "index.md")
        
        topics_list_md = ""
        for sub_name, topics in subs.items():
            topics_list_md += f"\n### {sub_name}\n"
            for t in topics:
                t_slug = slugify(t["name"])
                topics_list_md += f"- [{t['name']}]({t_slug}/) (Importance: {t['importance'] or 'Medium'})\n"
                
        index_content = f"""---
title: {cat_name}
---

# {cat_name}

Welcome to the **{cat_name}** guidebook notes, curriculum structure, and practice sets. Use the list below to navigate through the topics.

---

{topics_list_md}

---

[Return to Home](../../index.md)
"""
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(index_content)
            
    print("Placeholder pages and indexes generated successfully.")

def cmd_format_handwritten():
    data = load_cache()
    if not data:
        return
        
    for rel_path, topic_key in guidebooks.items():
        full_path = os.path.join(docs_dir, rel_path)
        if not os.path.exists(full_path):
            print(f"Warning: Handwritten guidebook not found: {full_path}")
            continue
            
        topic = data.get(topic_key)
        if not topic:
            # Fallback for kadanes-algorithm which doesn't exist in topic-list.md
            topic = {
                "name": "Kadane's Algorithm",
                "category": "Basics",
                "difficulty": "Easy",
                "importance": "High",
                "python_resources": [],
                "problems": [
                    {"id": "cses_1643", "name": "Maximum Subarray Sum", "url": "https://cses.fi/problemset/task/1643", "platform": "CSES", "difficulty": "Easy"},
                    {"id": "cses_1644", "name": "Maximum Subarray Sum II", "url": "https://cses.fi/problemset/task/1644", "platform": "CSES", "difficulty": "Hard"},
                    {"id": "codeforces_363b", "name": "Lamps", "url": "https://codeforces.com/problemset/problem/363/B", "platform": "Codeforces", "difficulty": "Easy"}
                ]
            }
            
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Parse custom problems table from the file before cleaning it
        custom_problems = parse_custom_problems_table(content)
        
        # Clean existing bottom sections and metadata
        clean_patterns = [
            r"^\s*Category:.*$",
            r"^\s*\*\*Category:\*\*.*$",
            r"^\s*Difficulty:.*$",
            r"^\s*\*\*Difficulty:\*\*.*$",
            r"^\s*---+\s*$",  # Clean metadata line separator
            r"\n##\s+(Practice|Practice Problems|Curated Practice Problems)\s*\n.*$",
            r"\n##\s+Additional Resources\s*\n.*$",
            r"\n##\s+YouKn0wWho Academy Reference\s*\n.*$",
            r"\n##\s+Topic Details\s*\n.*$",
            r"\n+\[Return to Home\].*$"
        ]
        
        # Read line by line to keep the title (# Header) and actual handwritten body
        lines = content.splitlines()
        body_lines = []
        skip_meta = False
        
        title_found = False
        title_text = topic["name"]
        
        for line in lines:
            stripped = line.strip()
            # Identify title
            if stripped.startswith("# ") and not title_found:
                title_text = stripped[2:].strip()
                title_found = True
                body_lines.append(line)
                continue
                
            # Skip old metadata lines at the top of the file
            if title_found and not body_lines[-1].strip() and (
                stripped.startswith("Category:") or 
                stripped.startswith("**Category:**") or 
                stripped.startswith("Difficulty:") or 
                stripped.startswith("**Difficulty:**") or
                stripped.startswith("---")
            ):
                # This is old metadata or its separator, skip it
                continue
                
            body_lines.append(line)
            
        body = "\n".join(body_lines).strip()
        
        # Re-apply clean of bottom sections to body
        for pattern in [
            r"\n##\s+(Practice|Practice Problems|Curated Practice Problems)\s*\n.*$",
            r"\n##\s+Additional Resources\s*\n.*$",
            r"\n##\s+YouKn0wWho Academy Reference\s*\n.*$",
            r"\n##\s+Topic Details\s*\n.*$",
            r"\n+\[Return to Home\].*$"
        ]:
            body = re.sub(pattern, "", body, flags=re.DOTALL | re.IGNORECASE)
            
        # Re-apply old metadata clean on body to be extra safe
        body_cleaned_lines = []
        lines_body = body.splitlines()
        for idx, line in enumerate(lines_body):
            stripped = line.strip()
            if idx > 0 and idx < 7 and (
                stripped.startswith("Category:") or 
                stripped.startswith("**Category:**") or 
                stripped.startswith("Difficulty:") or 
                stripped.startswith("**Difficulty:**") or
                stripped.startswith("---")
            ):
                continue
            body_cleaned_lines.append(line)
            
        body = "\n".join(body_cleaned_lines).strip()
        # Clean any consecutive empty lines
        body = re.sub(r"\n{3,}", "\n\n", body)
        
        # Insert metadata block below title
        title_pattern = rf"^#\s+{re.escape(title_text)}\s*\n*"
        diff_span = get_difficulty_span(topic["difficulty"] or "Easy")
        imp_span = get_importance_span(topic["importance"] or "High")
        
        metadata_block = f"**Category:** {topic['category']} &nbsp;|&nbsp; **Difficulty:** {diff_span} &nbsp;|&nbsp; **Importance:** {imp_span}\n\n---\n"
        
        if re.search(title_pattern, body, re.MULTILINE):
            body = re.sub(title_pattern, f"# {title_text}\n\n{metadata_block}\n", body, count=1, flags=re.MULTILINE)
        else:
            body = f"# {title_text}\n\n{metadata_block}\n\n{body}"
            
        # Merge practice problems
        academy_problems = topic["problems"]
        seen_urls = set()
        merged_problems = []
        
        # Add custom manual problems first
        for p in custom_problems:
            url_norm = p["url"].lower().rstrip("/")
            if url_norm not in seen_urls:
                seen_urls.add(url_norm)
                merged_problems.append(p)
                
        # Add academy problems second
        for p in academy_problems:
            url_norm = p["url"].lower().rstrip("/")
            if url_norm not in seen_urls:
                seen_urls.add(url_norm)
                merged_problems.append(p)
                
        problems_table = build_problems_table(merged_problems)
        
        # Additional resources (Python resources only)
        python_text = "\n".join(topic["python_resources"]).strip()
        resources_md = "No other additional resources were added to this topic."
        if "http" in python_text:
            resources_md = f"### Recommended Python Resources\n{python_text}"
            
        new_content = f"""{body.strip()}

---

## Additional Resources
{resources_md}

---

## Practice Problems
{problems_table}

---

[Return to Home](../../../index.md)
"""
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"Successfully formatted handwritten guidebook: {rel_path}")

def cmd_update_navigation():
    # Parse categories, subcategories, and topics for the nav tree
    data = load_cache()
    if not data:
        return
        
    parsed_tree = {}
    unique_topics = {}
    for key, topic in data.items():
        unique_topics[topic["name"]] = topic
        
    for topic_name, topic in unique_topics.items():
        cat_name = topic["category"]
        if cat_name not in parsed_tree:
            parsed_tree[cat_name] = {}
        sub_name = topic["subcategory"]
        if sub_name not in parsed_tree[cat_name]:
            parsed_tree[cat_name][sub_name] = []
        parsed_tree[cat_name][sub_name].append(topic_name)
        
    # Build nav string
    nav_str = "nav:\n  - Home: index.md\n"
    
    for cat_name, subs in parsed_tree.items():
        if cat_name != "Basics":
            continue
        cat_slug = slugify(cat_name)
        tab_name = cat_name
        if cat_name == "Data Structures (DS)":
            tab_name = "Data Structures"
        elif cat_name == "Dynamic Programming (DP)":
            tab_name = "Dynamic Programming"
            
        tab_name_clean = tab_name.replace('"', "'")
        has_content = False
        sub_items_str = ""
        
        for sub_name, topics in subs.items():
            if not topics:
                continue
            has_content = True
            
            # Gather all navigation items for this subcategory
            sub_items = []
            for topic in topics:
                topic_clean = topic.replace('"', "'")
                # Handle splits
                if topic == "Arrays":
                    sub_items.append(("Static Arrays", "topics/basics/02-arrays/static-arrays.md"))
                    sub_items.append(("Dynamic Arrays", "topics/basics/02-arrays/dynamic-arrays.md"))
                elif topic == "Sliding Window":
                    sub_items.append(("Fixed Size", "topics/basics/04-sliding-window/fixed-size.md"))
                    sub_items.append(("Variable Size", "topics/basics/04-sliding-window/variable-size.md"))
                else:
                    topic_dict = unique_topics.get(topic, {})
                    topic_id = topic_dict.get("id") if topic_dict.get("id") else slugify(topic)
                    if topic_id in overrides:
                        sub_items.append((topic_clean, overrides[topic_id]))
                    else:
                        topic_slug = slugify(topic)
                        sub_items.append((topic_clean, f"topics/{cat_slug}/{topic_slug}.md"))
            
            sub_name_clean = sub_name.replace('"', "'")
            # If the subcategory has exactly one item, flatten it to a single navigation link
            if len(sub_items) == 1:
                item_title, item_path = sub_items[0]
                sub_items_str += f"    - \"{sub_name_clean}\": {item_path}\n"
            else:
                # Multiple items: keep as expandable group
                sub_items_str += f"    - \"{sub_name_clean}\":\n"
                for item_title, item_path in sub_items:
                    sub_items_str += f"      - \"{item_title}\": {item_path}\n"
                    
        if has_content:
            nav_str += f"  - \"{tab_name_clean}\":\n" + sub_items_str
            
    nav_str += "  - Useful Links: resources.md"
    
    # Read mkdocs.yml
    with open(mkdocs_path, "r", encoding="utf-8") as f:
        yml = f.read()
        
    nav_start = yml.find("nav:")
    plugins_start = yml.find("plugins:")
    
    if nav_start != -1 and plugins_start != -1:
        new_yml = yml[:nav_start] + nav_str + "\n\n" + yml[plugins_start:]
        # Remove navigation.sections feature if present to keep sidebar collapsible
        new_yml = new_yml.replace("    - navigation.sections\n", "")
        new_yml = new_yml.replace("    - navigation.sections", "")
        
        with open(mkdocs_path, "w", encoding="utf-8") as f:
            f.write(new_yml)
        print("Successfully updated 'mkdocs.yml' navigation tree.")
    else:
        print("Error: Could not locate nav: or plugins: in mkdocs.yml")


def cmd_generate_roadmap():
    data = load_cache()
    if not data:
        return
        
    parsed_tree = {}
    unique_topics = {}
    for key, topic in data.items():
        unique_topics[topic["name"]] = topic
        
    for topic_name, topic in unique_topics.items():
        cat_name = topic["category"]
        if cat_name not in parsed_tree:
            parsed_tree[cat_name] = {}
        sub_name = topic["subcategory"]
        if sub_name not in parsed_tree[cat_name]:
            parsed_tree[cat_name][sub_name] = []
        parsed_tree[cat_name][sub_name].append(topic)
        
    roadmap_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CP Playbook Roadmap</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background: transparent;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
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

    .rm-construction-notice {
      padding: 0.85rem 1.25rem;
      background: rgba(37, 99, 235, 0.08); /* 8% indigo/blue tint */
      border: 1px solid rgba(37, 99, 235, 0.2);
      border-radius: 6px;
      margin-top: 0.25rem;
      margin-bottom: 1.25rem;
      font-size: 0.85rem;
      color: var(--md-typeset-color, #1e293b);
      line-height: 1.5;
    }

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
</head>
<body>
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
"""

    for cat_name, subs in parsed_tree.items():
        cat_slug = slugify(cat_name)
        badge_style = "background: #e0e7ff; color: #4f46e5;"
        badge_text = "Active" if cat_name == "Basics" else "Soon"
        
        cat_html = f"""
    <!-- Category: {cat_name} -->
    <div class="rm-category" id="cat-{cat_slug}">
      <div class="rm-category-header" onclick="toggleCategory(this)">
        <span class="rm-category-title">{cat_name} <span class="rm-category-badge" style="{badge_style}">{badge_text}</span></span>
        <span class="rm-toggle-icon">+</span>
      </div>
      <div class="rm-category-content">
"""
        # If not Basics, add construction notice
        if cat_name != "Basics":
            cat_html += """        <div class="rm-construction-notice">
          The content for this milestone is currently under development. We are actively writing explanations and selecting practice problems for these topics, which will be released soon!
        </div>
"""
            
        has_cat_content = False
        for sub_name, topics in subs.items():
            if not topics:
                continue
            has_cat_content = True
            cat_html += f"""
        <!-- Subcategory: {sub_name} -->
        <div class="rm-subcategory">
          <div class="rm-subcategory-title" onclick="toggleSubcategory(this)">
            <span>{sub_name}</span>
            <span class="rm-sub-toggle">+</span>
          </div>
          <div class="rm-subcategory-content">
            <div class="rm-topics-grid">
"""
            for topic in topics:
                topic_id = topic["id"]
                if not topic_id:
                    topic_id = slugify(topic["name"])
                    
                # Importance badge
                imp = (topic.get("importance") or "Medium").lower()
                imp_badge = "medium"
                if "high" in imp:
                    imp_badge = "high"
                elif "low" in imp:
                    imp_badge = "low"
                badge_label = imp.capitalize()
                
                # Routing check
                if cat_name != "Basics":
                    # External route to YouKn0wWho Academy
                    link = f"https://youkn0wwho.academy/topic-list/{topic_id.replace('_', '-')}"
                    target_attr = 'target="_blank"'
                else:
                    # Local route
                    target_attr = 'target="_parent"'
                    if topic_id in overrides:
                        link = overrides[topic_id]
                    elif topic["name"] == "Arrays":
                        # Specials
                        cat_html += f"""
              <a href="topics/basics/02-arrays/static-arrays/" {target_attr} class="rm-topic">
                <span>Static Arrays</span>
                <span class="rm-badge high">High</span>
              </a>
              <a href="topics/basics/02-arrays/dynamic-arrays/" {target_attr} class="rm-topic">
                <span>Dynamic Arrays</span>
                <span class="rm-badge high">High</span>
              </a>
"""
                        continue
                    elif topic["name"] == "Sliding Window":
                        # Specials
                        cat_html += f"""
              <a href="topics/basics/04-sliding-window/fixed-size/" {target_attr} class="rm-topic">
                <span>Fixed Size Sliding Window</span>
                <span class="rm-badge high">High</span>
              </a>
              <a href="topics/basics/04-sliding-window/variable-size/" {target_attr} class="rm-topic">
                <span>Variable Size Sliding Window</span>
                <span class="rm-badge high">High</span>
              </a>
"""
                        continue
                    else:
                        topic_slug = slugify(topic["name"])
                        link = f"topics/{cat_slug}/{topic_slug}/"
                        
                cat_html += f"""
              <a href="{link}" {target_attr} class="rm-topic">
                <span>{topic['name']}</span>
                <span class="rm-badge {imp_badge}">{badge_label}</span>
              </a>
"""
                
            cat_html += """
            </div>
          </div>
        </div>
"""
        cat_html += """
      </div>
    </div>
"""
        if has_cat_content:
            roadmap_html += cat_html
            
    roadmap_html += """
  </div>

  <script>
    function toggleCategory(el) {
      const parent = el.parentElement;
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
</body>
</html>
"""
    with open(roadmap_path, "w", encoding="utf-8") as f:
        f.write(roadmap_html)
        
    print(f"Successfully generated new 'roadmap.html' at: {roadmap_path}")


def main():
    parser = argparse.ArgumentParser(description="Playbook Curriculum Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")
    
    subparsers.add_parser("parse-cache", help="Parse topic-list.md and store in local syllabus cache JSON")
    subparsers.add_parser("generate-placeholders", help="Generate under-construction placeholder files")
    subparsers.add_parser("format-handwritten", help="Format handwritten guidebooks with metadata headers and merged tables")
    subparsers.add_parser("update-navigation", help="Update navigation settings in mkdocs.yml")
    subparsers.add_parser("generate-roadmap", help="Generate interactive syllabus roadmap.html")
    
    args = parser.parse_args()
    
    if args.command == "parse-cache":
        cmd_parse_cache()
    elif args.command == "generate-placeholders":
        cmd_generate_placeholders()
    elif args.command == "format-handwritten":
        cmd_format_handwritten()
    elif args.command == "update-navigation":
        cmd_update_navigation()
    elif args.command == "generate-roadmap":
        cmd_generate_roadmap()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
