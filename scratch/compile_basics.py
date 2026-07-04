import os
import yaml

mkdocs_path = r"d:\3-Projects\cp-shu-devs\mkdocs.yml"
docs_dir = r"d:\3-Projects\cp-shu-devs\docs"
output_path = r"d:\3-Projects\cp-shu-devs\basics_compiled.md"

def extract_files(nav_item):
    files = []
    if isinstance(nav_item, str):
        if nav_item.endswith(".md"):
            files.append(nav_item)
    elif isinstance(nav_item, list):
        for item in nav_item:
            files.extend(extract_files(item))
    elif isinstance(nav_item, dict):
        for key, val in nav_item.items():
            files.extend(extract_files(val))
    return files

def main():
    with open(mkdocs_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # Find the "Basics" section in nav
    basics_nav = None
    for item in config.get("nav", []):
        if isinstance(item, dict) and "Basics" in item:
            basics_nav = item["Basics"]
            break

    if not basics_nav:
        print("Error: Could not find 'Basics' in mkdocs.yml navigation.")
        return

    # Extract all md files in order
    md_files = extract_files(basics_nav)
    print(f"Found {len(md_files)} markdown files in Basics category.")

    compiled_content = []
    for rel_path in md_files:
        full_path = os.path.join(docs_dir, rel_path)
        if not os.path.exists(full_path):
            print(f"Warning: File not found: {full_path}")
            continue

        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        compiled_content.append(f"# START_FILE: {rel_path}\n"
                                f"================================================================================\n"
                                f"{content}\n"
                                f"================================================================================\n"
                                f"# END_FILE: {rel_path}\n\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("".join(compiled_content))

    print(f"Successfully compiled all Basics files into '{output_path}'.")

if __name__ == "__main__":
    main()
