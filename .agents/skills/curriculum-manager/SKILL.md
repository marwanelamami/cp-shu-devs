---
name: curriculum-manager
description: >-
  Project-local skill to manage the competitive programming playbook's curriculum.
  Supports formatting handwritten guidebooks, auto-generating placeholder files,
  and updating the flattened sidebar navigation tree in mkdocs.yml.
---

# Curriculum Manager

This skill manages the CP Playbook curriculum through three dedicated sub-skills/sub-workflows. These workflows leverage the master CLI script located at `scratch/curriculum_manager.py`.

---

## Sub-Skill 1: Format / Create Handwritten Topics

Use this workflow when creating a new custom topic guidebook or formatting an existing one to match the playbook's professional styling.

### Steps
1. **Prepare Written Content**: Write or update your markdown explanation in the target directory (e.g. `docs/topics/basics/02-arrays/static-arrays.md`).
2. **Format/Rebuild**: Run the formatting command to automatically clean up headers and inject metadata and problem tables:
   ```bash
   python scratch/curriculum_manager.py format-handwritten
   ```

### Formatting Specifications
- **Top Metadata Block**: Injects a clean, horizontal, styled text line directly below the main title:
  `**Category:** CategoryName &nbsp;|&nbsp; **Difficulty:** <span style="color: #2563eb; font-weight: 600;">DifficultyValue</span> &nbsp;|&nbsp; **Importance:** <span style="color: #ef4444; font-weight: 600;">ImportanceValue</span>`
- **Exclusion of Emojis**: Emojis are strictly forbidden to ensure a professional academic style.
- **Python-Only Resources**: All C++ and general YouKn0wWho reference resources are excluded. Only custom Python resources are displayed.
- **Unified Problems Table**: Automatically merges your manually defined practice problems and YouKn0wWho Academy's problems into a single deduplicated table:
  - Columns: ID, Problem, Platform, Difficulty.
  - Colors are dynamically applied to difficulties (Very Easy: Green, Easy: Blue, Medium: Amber, Hard: Red).
- **Home Navigation Link**: Appends a relative back link at the very bottom (e.g., `[Return to Home](../../../index.md)`).

---

## Sub-Skill 2: Generate / Update Placeholder Pages

Use this workflow to auto-generate placeholder pages for any curriculum topics that do not have handwritten guidebooks prepared yet.

### Steps
1. **Rebuild Cache (If Database Changed)**: Parse the temporary topic database list:
   ```bash
   python scratch/curriculum_manager.py parse-cache
   ```
2. **Generate Placeholders**: Generate the "Under Construction" files:
   ```bash
   python scratch/curriculum_manager.py generate-placeholders
   ```

### Layout Specifications
- **Under Construction Box**: Displays a styled info admonition stating:
  ```markdown
  !!! info "Under Construction"
      No content has been prepared for this topic/subtopic yet. We are actively developing the content and will be releasing it soon!
  ```
- **YouKn0wWho Academy Reference**: Points students to the topic's interactive syllabus on YouKn0wWho Academy.
- **Additional Resources**: Displays custom Python resources if present; otherwise, displays a "No other additional resources were added to this topic" notice.

---

## Sub-Skill 3: Rebuild Navigation Tree

Use this workflow to update the sidebar menu navigation in `mkdocs.yml` whenever new files are added or restructured.

### Steps
1. Run the update navigation command:
   ```bash
   python scratch/curriculum_manager.py update-navigation
   ```

### Flattening Rules
- **Single-Topic Subcategories**: If a subcategory contains exactly one page (e.g. *"Intro to Programming"* has only *"What is Programming?"*), it is flattened into a direct link in the navigation sidebar (toggling is bypassed).
- **Multi-Topic Subcategories**: If a subcategory contains multiple pages (e.g. *"Learn a Language"*), it is kept as an expandable folder.
- **Automatic Path Matching**: Matches handwritten subdirectory paths (`01-intro-to-cp/`, `02-arrays/`, etc.) exactly so that MkDocs preserves folder expand/collapse and active page states correctly.

---

## Formatting & Design Rules

### 1. Professional Tone and Aesthetics
- **No Emojis**: Emojis are strictly prohibited in titles, headers, lists, admonitions, or anywhere else on documentation pages.
- **Top Metadata Header**: Every topic page must display its Category, Difficulty, and Importance styled horizontally directly below the title:
  `**Category:** CategoryName &nbsp;|&nbsp; **Difficulty:** <span style="color: #...; font-weight: 600;">DifficultyValue</span> &nbsp;|&nbsp; **Importance:** <span style="color: #...; font-weight: 600;">ImportanceValue</span>`
- **Dynamic Color Spans**: Use professional colors for difficulties/importances (Very Easy: `#059669` green, Easy: `#2563eb` blue, Medium: `#d97706` amber, Hard: `#ef4444` red).

### 2. Resource Filters
- **Python/Custom Only**: Do not include C++ or general YouKn0wWho Academy resource links. Only output custom links or Python resources.
- If no resources are available, output:
  ```markdown
  ## Additional Resources
  No other additional resources were added to this topic.
  ```

### 3. Practice Problems Table
- **Deduplicated & Merged**: Combine custom manual problems and YouKn0wWho Academy problems into a single markdown table.
- **Columns**: ID | Problem | Platform | Difficulty.
- If no problems exist, output:
  ```markdown
  ## Practice Problems
  This topic contains no problems.
  ```
