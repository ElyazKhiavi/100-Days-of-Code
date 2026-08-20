#!/usr/bin/env python3
"""
Fix internal Markdown links after repository filename normalization.

- Lowercase all relative link paths
- Replace spaces with hyphens
- For .py filenames: replace hyphens with underscores
- Leaves external links (http, https, mailto) untouched
- Handles inline links [text](url) and reference-style [text]: url
"""

import os
import re
from pathlib import Path

DRY_RUN = False   # Set to False to actually write changes

ROOT = os.path.abspath(".")

# Regex to match inline Markdown links: [text](url)
inline_link_re = re.compile(r'(\[[^\]]*\]\()([^)]+)(\))')

# Regex to match reference-style definitions: [label]: url "optional title"
ref_link_re = re.compile(r'^(\[[^\]]*\]:\s*)(\S+)(\s*.*)$', re.MULTILINE)

def transform_path(path: str) -> str:
    """
    Transform a relative path according to repo conventions:
    - lowercase all characters
    - replace spaces with hyphens
    - if file is .py, replace hyphens with underscores in the filename
    """
    # Do not touch absolute URLs or anchors
    if path.startswith(('http://', 'https://', 'mailto:', '#', '/', 'ftp://')):
        return path

    # Lowercase entire path and replace spaces with hyphens
    new_path = path.lower().replace(' ', '-')

    # For .py files, replace hyphens with underscores in the filename only
    if new_path.endswith('.py'):
        # Split directory and filename
        if '/' in new_path:
            dir_part, file_part = new_path.rsplit('/', 1)
            file_part = file_part.replace('-', '_')
            new_path = f"{dir_part}/{file_part}"
        else:
            new_path = new_path.replace('-', '_')

    return new_path

def fix_inline_links(content: str) -> str:
    def repl(match):
        prefix, url, suffix = match.group(1), match.group(2), match.group(3)
        new_url = transform_path(url)
        return f"{prefix}{new_url}{suffix}"
    return inline_link_re.sub(repl, content)

def fix_ref_links(content: str) -> str:
    def repl(match):
        prefix, url, rest = match.group(1), match.group(2), match.group(3)
        new_url = transform_path(url)
        return f"{prefix}{new_url}{rest}"
    return ref_link_re.sub(repl, content)

def process_file(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    updated = fix_inline_links(original)
    updated = fix_ref_links(updated)

    if updated == original:
        print(f"  no changes: {filepath}")
        return

    if DRY_RUN:
        print(f"  [DRY RUN] would update: {filepath}")
        # Show first few changes for preview
        import difflib
        diff = difflib.unified_diff(
            original.splitlines(), updated.splitlines(),
            fromfile='before', tofile='after', lineterm=''
        )
        for line in diff:
            print(f"    {line}")
    else:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"  updated: {filepath}")

def main():
    print(f"Scanning markdown files under: {ROOT}")
    print(f"Dry run: {'ON' if DRY_RUN else 'OFF'}\n")

    md_files = list(Path(ROOT).rglob('*.md'))
    print(f"Found {len(md_files)} markdown files.\n")

    for md_file in md_files:
        # Skip files inside .git or other hidden dirs
        parts = md_file.parts
        if any(part.startswith('.') for part in parts):
            continue
        print(f"Processing: {md_file.relative_to(ROOT)}")
        process_file(str(md_file))

if __name__ == "__main__":
    main()