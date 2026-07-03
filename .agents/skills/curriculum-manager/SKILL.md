---
name: curriculum-manager
description: >-
  Project-local skill to manage the competitive programming playbook's curriculum.
  It handles generating placeholder pages, formatting handwritten files, and updating
  the navigation tree in mkdocs.yml.
---

# Curriculum Manager Skill

## Overview
This skill provides commands to manage the CP Playbook curriculum. It reads the syllabus information from a temporary cache (generated from the `topic-list.md` database) and formats both custom handwritten files and under-construction placeholder pages consistently.

## Quick Start
Run the following commands to process curriculum files:
```bash
# 1. Parse topic-list.md and cache syllabus data locally
python scratch/curriculum_manager.py parse-cache

# 2. Auto-generate under-construction placeholders
python scratch/curriculum_manager.py generate-placeholders

# 3. Format handwritten files with professional headers and tables
python scratch/curriculum_manager.py format-handwritten

# 4. Update the mkdocs.yml navigation tree
python scratch/curriculum_manager.py update-navigation
```

## Workflows

### Formatting Guidelines
- **Metadata Header**: All pages (both placeholders and handwritten) must contain a professional header below the main title:
  `**Category:** CategoryName &nbsp;|&nbsp; **Difficulty:** <span style="color: #2563eb; font-weight: 600;">DifficultyValue</span> &nbsp;|&nbsp; **Importance:** <span style="color: #ef4444; font-weight: 600;">ImportanceValue</span>`
- **Emojis**: No emojis are allowed anywhere in headers, resource links, or text to maintain a clean, professional style.
- **Resources**: C++/General resources parsed from YouKn0wWho Academy are completely excluded. Only show custom resources (like Python resources).
- **Practice Problems**: Merge custom problem tables and Academy problems into a single unified table containing:
  - ID
  - Problem (name linked to platform URL)
  - Platform
  - Difficulty
- **Back Link**: Append `[Return to Home](../../../index.md)` (or `../../index.md` depending on folder depth) at the very bottom.
