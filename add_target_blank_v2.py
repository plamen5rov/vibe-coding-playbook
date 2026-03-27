#!/usr/bin/env python3
import re
import os

# Directory to process
root = '/home/bluedragon/CODE/opencode/vibe-coding-playbook'

# Pattern to match markdown links: [text](url) and also bare URLs in < >
# We'll process in two passes:
# 1. Handle [text](url) patterns
# 2. Handle <url> patterns (but avoid those already in code blocks or already processed)

link_pattern = re.compile(r'(\[([^\]]+)\]\((https?://[^\)\s]+)\))')
bare_url_pattern = re.compile(r'(<)(https?://[^>]+)(>)')

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Process [text](url) links
    def replace_link(match):
        full = match.group(1)
        text = match.group(2)
        url = match.group(3)
        # Skip if already processed
        if '{target="_blank"}' in full or 'rel="noopener"' in full:
            return full
        return f'[{text}]({url}){{target="_blank" rel="noopener"}}'
    
    new_content = link_pattern.sub(replace_link, content)
    
    # Process <url> bare links
    def replace_bare(match):
        lt = match.group(1)
        url = match.group(2)
        gt = match.group(3)
        # Skip if already processed (shouldn't happen with bare URLs)
        if '{target="_blank"}' in match.group(0) or 'rel="noopener"' in match.group(0):
            return match.group(0)
        return f'{lt}{url}{gt}{{{"target=\"_blank\" rel=\"noopener\"}}}'
    
    # But we need to be careful not to process URLs inside code blocks or backticks
    # Simple approach: split by code blocks, process only non-code parts
    # We'll use a simple regex to avoid processing inside ``` blocks and `single backticks`
    
    # Instead, let's do a more targeted approach: only process bare URLs that are not already linked
    # and not in obvious code contexts by checking if they're not part of a larger link pattern
    
    # For simplicity in this run, let's just process the Resources table which uses <url> format
    # and a few other known cases
    
    # Actually let's do a safer approach: process line by line and avoid obvious code blocks
    lines = new_content.split('\n')
    processed_lines = []
    in_code_block = False
    
    for line in lines:
        stripped = line.strip()
        # Track code block state
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            processed_lines.append(line)
            continue
            
        if not in_code_block:
            # Process bare URLs in this line
def replace_bare_line(match):
    lt = match.group(1)
    url = match.group(2)
    gt = match.group(3)
    # Skip if this looks like it's already part of a processed link
    # Check if there's {{target...}} nearby in the original match
    if 'target="_blank"' in match.group(0) or 'rel="noopener"' in match.group(0):
        return match.group(0)
    target_attr = '{target="_blank" rel="noopener"}'
    return f'{lt}{url}{gt}{target_attr}'
            
            target_attr = '{target="_blank" rel="noopener"}'
            line = bare_url_pattern.sub(lambda m: f'{m.group(1)}{m.group(2)}{m.group(3)}{target_attr}', line)
        
        processed_lines.append(line)
    
    new_content = '\n'.join(processed_lines)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated: {path}')
        return True
    else:
        # Only print if we actually looked at the file (not excluded)
        rel_path = os.path.relpath(path, root)
        if not any(ex in rel_path for ex in ['ai_answers', 'pictures', '.opencode', '.ai']):
            print(f'No change: {rel_path}')
        return False

def main():
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip excluded directories
        rel_path = os.path.relpath(dirpath, root)
        if any(ex in rel_path for ex in ['ai_answers', 'pictures', '.opencode', '.ai']):
            # Don't process files in these directories
            continue
        for f in filenames:
            if f.endswith('.md'):
                full = os.path.join(dirpath, f)
                process_file(full)

if __name__ == '__main__':
    main()