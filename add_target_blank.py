#!/usr/bin/env python3
import re
import os
import sys

# Directory to process
root = "/home/bluedragon/CODE/opencode/vibe-coding-playbook"
# Extensions to process
exts = [".md"]
# Files to exclude (relative to root)
exclude = {
    "ai_answers",  # directory
    "pictures",  # directory
    ".opencode",  # directory
    ".ai",  # directory
    "docs/CONVENTIONS.md",  # maybe we want to keep as is? but we can process
    # Actually we want to process all .md except ai_answers and maybe pictures
}

# Pattern for markdown link: [text](url)
# We want to capture the whole link and replace with [text](url){target="_blank" rel="noopener"}
# But only if url starts with http:// or https://
pattern = re.compile(r"(\[([^\]]+)\]\((https?://[^\)\s]+)\))")


def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    def replace(match):
        full = match.group(1)
        text = match.group(2)
        url = match.group(3)
        # Avoid double processing: if already has {target...} skip
        if '{target="_blank"}' in full or 'rel="noopener"' in full:
            return full
        return f'[{text}]({url}){{target="_blank" rel="noopener"}}'

    new_content = pattern.sub(replace, content)

    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {path}")
        return True
    else:
        print(f"No change: {path}")
        return False


def main():
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip excluded directories
        if "ai_answers" in dirpath.split(os.sep):
            continue
        if "pictures" in dirpath.split(os.sep):
            continue
        if ".opencode" in dirpath.split(os.sep):
            continue
        if ".ai" in dirpath.split(os.sep):
            continue
        for f in filenames:
            if any(f.endswith(ext) for ext in exts):
                full = os.path.join(dirpath, f)
                process_file(full)


if __name__ == "__main__":
    main()
