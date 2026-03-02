#!/usr/bin/env python3
"""
Fix Fake Citations - Replace all Further Reading sections with standard text
"""

import os
import re

CSE_DIR = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse"

REPLACEMENT = """### Further Reading

Refer to your prescribed textbook and official course materials."""

stats = {"files_checked": 0, "files_fixed": 0}

def fix_file(file_path):
    """Replace Further Reading sections"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False

    original = content

    # Pattern to match "Further Reading" or "References" sections
    # Match the heading and everything until the next ## heading or end of file
    patterns = [
        # ### Further Reading followed by content until next heading or EOF
        r'###\s*Further\s+Reading\s*\n+([\s\S]*?)(?=\n##|\n---|\Z)',
        # ### References
        r'###\s*References\s*\n+([\s\S]*?)(?=\n##|\n---|\Z)',
        # ## Further Reading
        r'##\s*Further\s+Reading\s*\n+([\s\S]*?)(?=\n##|\n---|\Z)',
        # ## References
        r'##\s*References\s*\n+([\s\S]*?)(?=\n##|\n---|\Z)',
    ]

    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            content = re.sub(pattern, REPLACEMENT + '\n\n', content, flags=re.IGNORECASE)

    # Clean up multiple newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    print("=" * 60)
    print("FIX FAKE CITATIONS - Replace Further Reading sections")
    print("=" * 60)

    md_files = []
    for root, dirs, files in os.walk(CSE_DIR):
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))

    print(f"Found {len(md_files)} markdown files")
    print("")

    for file_path in md_files:
        stats["files_checked"] += 1

        if fix_file(file_path):
            stats["files_fixed"] += 1
            topic = os.path.basename(os.path.dirname(file_path))
            print(f"  ✓ Fixed: {topic[:50]}")

    print("")
    print("=" * 60)
    print("COMPLETE")
    print("=" * 60)
    print(f"Files checked: {stats['files_checked']}")
    print(f"Files fixed: {stats['files_fixed']}")

if __name__ == "__main__":
    main()
