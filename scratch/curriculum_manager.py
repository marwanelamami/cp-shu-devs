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
    "topics/basics/what-is-programming.md": "programming",
    "topics/basics/setting-up-the-environment.md": "intro_to_cpp",
    "topics/basics/01-intro-to-cp/intro-to-cp.md": "competitive_programming",
    "topics/basics/01-intro-to-cp/complexity-analysis.md": "complexity_analysis",
    "topics/basics/fast-input-output.md": "fast_input_output",
    "topics/basics/02-arrays/static-arrays.md": "arrays",
    "topics/basics/02-arrays/dynamic-arrays.md": "arrays",
    "topics/basics/03-kadanes-algorithm/kadanes-algorithm.md": "kadanes-algorithm",
    "topics/basics/04-sliding-window/fixed-size.md": "sliding_window_technique",
    "topics/basics/04-sliding-window/variable-size.md": "sliding_window_technique",
    "topics/basics/05-two-pointers/two-pointers.md": "two_pointers",
    "topics/basics/recursion.md": "recursion",
    "topics/basics/divisors.md": "divisors",
    "topics/basics/gcd-and-lcm.md": "gcd_and_lcm",
    "topics/basics/harmonic-number.md": "harmonic_series",
    "topics/basics/06-prefix-sums/prefix-sums.md": "prefix_sum",
    "topics/basics/prefix-xor.md": "prefix_xor",
    "topics/basics/intro-to-basic-data-structures.md": "stl_intro"
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
        
    def arrange_row(row):
        if len(row) == 3:
            high = [item for item in row if item[3] == "high"]
            others = [item for item in row if item[3] != "high"]
            if len(high) == 1 and len(others) == 2:
                return [others[0], high[0], others[1]]
            elif len(high) == 2 and len(others) == 1:
                return [high[0], high[1], others[0]]
            return row
        elif len(row) == 2:
            high = [item for item in row if item[3] == "high"]
            others = [item for item in row if item[3] != "high"]
            if len(high) == 1 and len(others) == 1:
                return [high[0], others[0]]
            return row
        return row
        
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
    .rm-container { margin: 1.5rem 0; max-width: 100%; }
    .rm-legend {
      display: flex; gap: 1.5rem; margin-bottom: 1.5rem;
      font-size: 0.85rem; align-items: center; flex-wrap: wrap;
    }
    .rm-legend-item { display: flex; align-items: center; gap: 0.4rem; }
    .rm-legend-dot { width: 10px; height: 10px; border-radius: 50%; }

    /* Category accordion */
    .rm-category {
      border: 1px solid var(--md-typeset-color, #e2e8f0);
      border-radius: 6px; margin-bottom: 0.75rem;
      background: var(--md-card-background, #ffffff); overflow: hidden;
    }
    .rm-category-header {
      padding: 0.85rem 1.25rem;
      background: var(--md-default-bg-color, #f8fafc);
      display: flex; justify-content: space-between; align-items: center;
      cursor: pointer; font-weight: 600; user-select: none;
      transition: background 0.15s ease;
      position: relative; z-index: 3;
    }
    .rm-category-header:hover { background: var(--md-default-bg-color-hover, #f1f5f9); }
    .rm-category.open .rm-category-header { border-bottom: 1px solid var(--md-typeset-color, #e2e8f0); }
    .rm-category-title { font-size: 0.95rem; display: flex; align-items: center; gap: 0.5rem; }
    .rm-category-badge {
      font-size: 0.7rem; padding: 0.1rem 0.4rem; border-radius: 9999px;
      background: #e0e7ff; color: #4f46e5; font-weight: 500;
    }
    .rm-category-content { display: none; padding: 1.25rem; }
    .rm-category.open .rm-category-content { display: block; }
    .rm-toggle-icon { font-size: 1.1rem; color: #64748b; font-weight: bold; }

    /* Tree flow */
    .rm-tree {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      position: relative;
      gap: 3.5rem; /* Increased vertical gap between milestone layers */
    }

    /* Milestone accordion */
    .rm-milestone {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .rm-milestone-header {
      display: flex; align-items: center; justify-content: center; gap: 0.5rem;
      cursor: pointer; user-select: none;
      padding: 0.5rem 1rem; border-radius: 6px;
      font-weight: 600; font-size: 0.9rem; color: #4f46e5;
      background: rgba(79, 70, 229, 0.06); border: 1px solid rgba(79, 70, 229, 0.15);
      transition: all 0.2s ease; margin: 0 auto; width: fit-content; min-width: 200px;
      position: relative; z-index: 2;
    }
    .rm-milestone-header:hover { background: rgba(79, 70, 229, 0.12); }
    .rm-milestone-header .rm-ms-icon {
      font-size: 0.8rem; transition: transform 0.3s ease;
    }
    .rm-milestone.open .rm-milestone-header .rm-ms-icon { transform: rotate(90deg); }
    
    .rm-milestone-body {
      overflow: hidden;
      max-height: 0;
      opacity: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 3.5rem; /* Increased gap between internal rows */
      transition: max-height 0.5s cubic-bezier(0.4,0,0.2,1), opacity 0.4s ease 0.1s;
      width: 100%;
      box-sizing: border-box;
      padding: 0;
    }
    .rm-milestone.open .rm-milestone-body {
      max-height: 3000px;
      opacity: 1;
      margin-top: 3.5rem; /* Space between header and first internal row */
    }

    /* Topic row */
    .rm-row {
      display: flex; align-items: center; justify-content: center;
      gap: 1.5rem; width: 100%;
      position: relative; z-index: 2;
    }

    /* Topic card */
    .rm-topic {
      display: flex; justify-content: space-between; align-items: center; gap: 0.5rem;
      padding: 0.55rem 0.85rem;
      border: 1px solid var(--md-typeset-color, #e2e8f0);
      border-radius: 6px; background: var(--md-default-bg-color, #ffffff);
      text-decoration: none !important; color: var(--md-typeset-color, #1e293b) !important;
      font-size: 0.82rem; font-weight: 500;
      transition: all 0.15s ease, opacity 0.4s ease, transform 0.4s ease;
      min-width: 180px; max-width: 280px; box-sizing: border-box; flex: 0 1 auto;
      position: relative; z-index: 2;
    }
    .rm-topic:hover {
      border-color: #3b82f6; background: #eff6ff; color: #1d4ed8 !important;
      transform: translateY(-1px); box-shadow: 0 2px 8px rgba(59,130,246,0.15);
    }

    /* Animated items inside milestones */
    .rm-milestone .rm-anim-item {
      opacity: 0;
      transform: translateY(12px);
      transition: opacity 0.4s ease, transform 0.4s ease;
    }
    .rm-milestone.open .rm-anim-item { opacity: 1; transform: translateY(0); }

    /* Dynamic SVG connectors */
    .rm-tree-svg {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      overflow: visible;
      z-index: 1;
    }
    
    /* Theme color variables */
    :root {
      --rm-connector-color: #cbd5e1;
    }

    /* Badges */
    .rm-badge {
      font-size: 0.6rem; font-weight: 600; padding: 0.1rem 0.35rem;
      border-radius: 3px; color: #fff; text-transform: uppercase;
      letter-spacing: 0.025em; white-space: nowrap;
    }
    .rm-badge.high { background: #ef4444; }
    .rm-badge.medium { background: #f59e0b; }
    .rm-badge.low { background: #10b981; }

    /* Construction notice */
    .rm-construction-notice {
      padding: 0.85rem 1.25rem; background: rgba(37,99,235,0.08);
      border: 1px solid rgba(37,99,235,0.2); border-radius: 6px;
      margin-bottom: 1.25rem; font-size: 0.85rem;
      color: var(--md-typeset-color, #1e293b); line-height: 1.5;
      width: 100%; box-sizing: border-box;
    }

    /* Dark mode */
    [data-md-color-scheme="slate"] {
      --rm-connector-color: #475569;
    }
    [data-md-color-scheme="slate"] .rm-category { background: #1e293b; border-color: #334155; }
    [data-md-color-scheme="slate"] .rm-category-header { background: #0f172a; }
    [data-md-color-scheme="slate"] .rm-category-header:hover { background: #1e293b; }
    [data-md-color-scheme="slate"] .rm-category.open .rm-category-header { border-bottom-color: #334155; }
    [data-md-color-scheme="slate"] .rm-topic {
      background: #0f172a; border-color: #334155; color: #cbd5e1 !important;
    }
    [data-md-color-scheme="slate"] .rm-topic:hover {
      border-color: #3b82f6; background: #1e293b; color: #60a5fa !important;
      box-shadow: 0 2px 8px rgba(59,130,246,0.25);
    }
    [data-md-color-scheme="slate"] .rm-milestone-header {
      color: #818cf8; background: rgba(129,140,248,0.06); border-color: rgba(129,140,248,0.2);
    }
    [data-md-color-scheme="slate"] .rm-milestone-header:hover { background: rgba(129,140,248,0.12); }

    /* Mobile */
    @media (max-width: 640px) {
      .rm-row { flex-direction: column; gap: 0.5rem; }
      .rm-topic { min-width: 0; max-width: 100%; width: 100%; }
      .rm-tree-svg { display: none; }
      .rm-milestone .rm-anim-item { opacity: 1; transform: none; }
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
        
        has_cat_content = False
        cat_html = f"""
    <!-- Category: {cat_name} -->
    <div class="rm-category" id="cat-{cat_slug}">
      <div class="rm-category-header" onclick="toggleCategory(this)">
        <span class="rm-category-title">{cat_name} <span class="rm-category-badge" style="{badge_style}">{badge_text}</span></span>
        <span class="rm-toggle-icon">+</span>
      </div>
      <div class="rm-category-content">
"""
        if cat_name != "Basics":
            cat_html += """        <div class="rm-construction-notice">
          The content for this milestone is currently under development. We are actively writing explanations and selecting practice problems for these topics, which will be released soon!
        </div>
"""
        cat_html += """        <div class="rm-tree">
"""
        
        milestone_blocks = []
        for sub_name, topics in subs.items():
            if not topics:
                continue
            has_cat_content = True
            
            sub_items = []
            for topic in topics:
                topic_id = topic["id"]
                if not topic_id:
                    topic_id = slugify(topic["name"])
                    
                imp = (topic.get("importance") or "Medium").lower()
                imp_badge = "medium"
                if "high" in imp:
                    imp_badge = "high"
                elif "low" in imp:
                    imp_badge = "low"
                badge_label = imp.capitalize()
                
                if cat_name != "Basics":
                    link = f"https://youkn0wwho.academy/topic-list/{topic_id.replace('_', '-')}"
                    target_attr = 'target="_blank"'
                else:
                    target_attr = 'target="_parent"'
                    if topic_id in overrides:
                        link = overrides[topic_id]
                    else:
                        topic_slug = slugify(topic["name"])
                        link = f"topics/{cat_slug}/{topic_slug}/"
                        
                if link.endswith(".md"):
                    link = link[:-3] + "/"
                    
                if cat_name == "Basics" and topic["name"] == "Arrays":
                    sub_items.append(("Static Arrays", "topics/basics/02-arrays/static-arrays/", target_attr, "high", "High"))
                    sub_items.append(("Dynamic Arrays", "topics/basics/02-arrays/dynamic-arrays/", target_attr, "high", "High"))
                elif cat_name == "Basics" and topic["name"] == "Sliding Window":
                    sub_items.append(("Fixed Size Sliding Window", "topics/basics/04-sliding-window/fixed-size/", target_attr, "high", "High"))
                    sub_items.append(("Variable Size Sliding Window", "topics/basics/04-sliding-window/variable-size/", target_attr, "high", "High"))
                else:
                    sub_items.append((topic["name"], link, target_attr, imp_badge, badge_label))
            
            milestone_html = ""
            if len(sub_items) == 1:
                name, link, target_attr, imp_badge, badge_label = sub_items[0]
                milestone_html = f"""          <div class="rm-row">
            <a href="{link}" {target_attr} class="rm-topic">
              <span>{name}</span>
              <span class="rm-badge {imp_badge}">{badge_label}</span>
            </a>
          </div>"""
            else:
                milestone_slug = slugify(sub_name)
                milestone_html = f"""          <div class="rm-milestone" id="ms-{cat_slug}-{milestone_slug}">
            <div class="rm-milestone-header" onclick="toggleMilestone(this)">
              <span class="rm-ms-icon">&#9654;</span>
              <span>{sub_name}</span>
            </div>
            <div class="rm-milestone-body">
"""
                chunked_rows = [sub_items[j:j + 3] for j in range(0, len(sub_items), 3)]
                step_index = 0
                for r_idx, row in enumerate(chunked_rows):
                    arranged_row = arrange_row(row)
                    
                    row_delay = f"{step_index * 0.06:.2f}s"
                    milestone_html += f'              <div class="rm-row rm-anim-item" style="transition-delay:{row_delay}">\n'
                    for item in arranged_row:
                        name, link, target_attr, imp_badge, badge_label = item
                        milestone_html += f'                <a href="{link}" {target_attr} class="rm-topic">\n'
                        milestone_html += f'                  <span>{name}</span>\n'
                        milestone_html += f'                  <span class="rm-badge {imp_badge}">{badge_label}</span>\n'
                        milestone_html += f'                </a>\n'
                    milestone_html += f'              </div>\n'
                    step_index += 1
                        
                milestone_html += """            </div>
          </div>"""
                
            milestone_blocks.append(milestone_html)
            
        category_tree_html = "\n".join(milestone_blocks)
        cat_html += category_tree_html
        cat_html += """
        </div>
      </div>
    </div>
"""
        if has_cat_content:
            roadmap_html += cat_html
            
    roadmap_html += """
  </div>

  <script>
    function sendHeight() {
      const height = document.body.scrollHeight || document.documentElement.scrollHeight;
      window.parent.postMessage({ type: 'resize-roadmap', height: height }, '*');
    }

    function drawRoadmapConnections() {
      const trees = document.querySelectorAll('.rm-tree');
      trees.forEach(tree => {
        const treeRect = tree.getBoundingClientRect();
        if (treeRect.width === 0 || treeRect.height === 0) return;

        let svg = tree.querySelector('svg.rm-tree-svg');
        if (!svg) {
          svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
          svg.setAttribute('class', 'rm-tree-svg');
          tree.appendChild(svg);
        }

        svg.innerHTML = `
          <defs>
            <marker id="arrow-dynamic" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--rm-connector-color)" />
            </marker>
          </defs>
        `;

        const layers = [];
        for (let child of tree.children) {
          if (child.classList.contains('rm-row')) {
            if (child.offsetHeight > 0) {
              layers.push({ type: 'row', element: child });
            }
          } else if (child.classList.contains('rm-milestone')) {
            const header = child.querySelector('.rm-milestone-header');
            if (header && header.offsetHeight > 0) {
              layers.push({ type: 'header', element: header });
            }
            if (child.classList.contains('open')) {
              const body = child.querySelector('.rm-milestone-body');
              if (body) {
                const bodyRows = body.querySelectorAll('.rm-row');
                bodyRows.forEach(row => {
                  if (row.offsetHeight > 0) {
                    layers.push({ type: 'row', element: row });
                  }
                });
              }
            }
          }
        }

        function getLayerNodes(layer) {
          if (layer.type === 'row') {
            return Array.from(layer.element.querySelectorAll('.rm-topic'));
          } else {
            return [layer.element];
          }
        }

        for (let i = 0; i < layers.length - 1; i++) {
          const sources = getLayerNodes(layers[i]);
          const targets = getLayerNodes(layers[i + 1]);
          if (sources.length === 0 || targets.length === 0) continue;

          const sourceRects = sources.map(node => node.getBoundingClientRect());
          const targetRects = targets.map(node => node.getBoundingClientRect());

          const connections = [];

          // 1. For each source, find closest target
          sources.forEach((src, sIdx) => {
            const sr = sourceRects[sIdx];
            const sx = sr.left - treeRect.left + sr.width / 2;
            
            let closestTgtIdx = 0;
            let minDistance = Infinity;
            targets.forEach((tgt, tIdx) => {
              const tr = targetRects[tIdx];
              const tx = tr.left - treeRect.left + tr.width / 2;
              const dist = Math.abs(sx - tx);
              if (dist < minDistance) {
                minDistance = dist;
                closestTgtIdx = tIdx;
              }
            });
            connections.push({ sIdx, tIdx: closestTgtIdx });
          });

          // 2. For each target, find closest source
          targets.forEach((tgt, tIdx) => {
            const tr = targetRects[tIdx];
            const tx = tr.left - treeRect.left + tr.width / 2;
            
            let closestSrcIdx = 0;
            let minDistance = Infinity;
            sources.forEach((src, sIdx) => {
              const sr = sourceRects[sIdx];
              const sx = sr.left - treeRect.left + sr.width / 2;
              const dist = Math.abs(sx - tx);
              if (dist < minDistance) {
                minDistance = dist;
                closestSrcIdx = sIdx;
              }
            });
            
            // Check if this connection is already added
            const exists = connections.some(c => c.sIdx === closestSrcIdx && c.tIdx === tIdx);
            if (!exists) {
              connections.push({ sIdx: closestSrcIdx, tIdx });
            }
          });

          // 3. Draw smooth rounded-elbow connectors (straight down / across / down,
          // with quarter-round corners) instead of lopsided S-curves. This keeps
          // connectors clean even when source and target are far apart horizontally.
          //
          // All connectors in this layer bend at one shared horizontal split line
          // (rather than each connector's own midpoint). Boxes in a row can have
          // slightly different heights (e.g. a one-line box next to a two-line box),
          // which would otherwise give each connector a slightly different bend
          // height and cause sibling lines that curve the same direction to cross
          // one another right where they fanned out.
          const allSy = sourceRects.map(r => r.bottom - treeRect.top + 6);
          const allTy = targetRects.map(r => r.top - treeRect.top - 8);
          const maxSy = Math.max(...allSy);
          const minTy = Math.min(...allTy);
          const splitY = maxSy < minTy ? (maxSy + minTy) / 2 : null;

          connections.forEach(({ sIdx, tIdx }) => {
            const sr = sourceRects[sIdx];
            const sx = sr.left - treeRect.left + sr.width / 2;
            const sy = sr.bottom - treeRect.top + 6; // Offset down by 6px to prevent touching the box

            const tr = targetRects[tIdx];
            const tx = tr.left - treeRect.left + tr.width / 2;
            const ty = tr.top - treeRect.top - 8; // Offset up by 8px for the arrowhead to clear the box cleanly

            const dx = tx - sx;
            const midY = splitY !== null ? splitY : sy + (ty - sy) / 2;

            let d;
            if (Math.abs(dx) < 1) {
              // Same column: perfectly straight vertical line
              d = `M ${sx} ${sy} L ${tx} ${ty}`;
            } else {
              // Rounded elbow: down -> curve -> across -> curve -> down.
              // The corner radius on the way OUT of the source (rStart) can be
              // generous since nothing sits there. The corner on the way IN to
              // the target (rEnd) is kept smaller and a minimum straight "tail"
              // is reserved right before the box, so the arrowhead marker sits
              // on a plain straight segment instead of overlapping the curve's
              // own bend (which is what made arrowheads look hooked/curled).
              const sign = dx > 0 ? 1 : -1;
              const availTop = midY - sy;
              const availBottom = ty - midY;
              // The arrowhead marker itself occupies ~17.5px right at the path's end
              // (markerHeight 7 * strokeWidth 2.5). minTail must clear that footprint
              // with room to spare, or the marker overlaps the curve's own bend and
              // the two blend into a hooked/doubled shape instead of a clean arrow.
              const minTail = 24;
              const rStart = Math.max(0, Math.min(14, Math.abs(dx) / 2, availTop));
              const rEnd = Math.max(0, Math.min(10, Math.abs(dx) / 2, availBottom - minTail));
              d = `M ${sx} ${sy} ` +
                  `L ${sx} ${midY - rStart} ` +
                  `Q ${sx} ${midY}, ${sx + sign * rStart} ${midY} ` +
                  `L ${tx - sign * rEnd} ${midY} ` +
                  `Q ${tx} ${midY}, ${tx} ${midY + rEnd} ` +
                  `L ${tx} ${ty}`;
            }

            const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            path.setAttribute('d', d);
            path.setAttribute('stroke', 'var(--rm-connector-color)');
            path.setAttribute('stroke-width', '2.5');
            path.setAttribute('fill', 'none');
            path.setAttribute('stroke-linecap', 'butt');
            path.setAttribute('stroke-linejoin', 'round');
            path.setAttribute('marker-end', 'url(#arrow-dynamic)');
            svg.appendChild(path);
          });
        }
      });
    }

    let drawLoopActive = false;
    function triggerDrawLoop(duration = 600) {
      const startTime = Date.now();
      function loop() {
        drawRoadmapConnections();
        if (Date.now() - startTime < duration) {
          requestAnimationFrame(loop);
        } else {
          drawRoadmapConnections();
        }
      }
      requestAnimationFrame(loop);
    }

    function toggleCategory(el) {
      const parent = el.parentElement;
      if (parent.classList.contains('disabled')) return;
      parent.classList.toggle('open');
      const icon = el.querySelector('.rm-toggle-icon');
      if (icon) {
        icon.textContent = parent.classList.contains('open') ? '−' : '+';
      }
      setTimeout(sendHeight, 50);
      triggerDrawLoop(600);
    }

    function toggleMilestone(el) {
      const milestone = el.parentElement;
      milestone.classList.toggle('open');
      setTimeout(sendHeight, 50);
      triggerDrawLoop(600);
    }

    // Draw initial connections and handle window changes
    window.addEventListener('load', () => {
      drawRoadmapConnections();
      sendHeight();
    });
    window.addEventListener('resize', () => {
      drawRoadmapConnections();
      sendHeight();
    });
    
    // Fallbacks
    setInterval(drawRoadmapConnections, 500);
    setInterval(sendHeight, 500);
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
