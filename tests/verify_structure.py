import re
import sys
from pathlib import Path

def verify_requirements(file_path):
    # Read file
    try:
        content = Path(file_path).read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

    lines = content.splitlines()

    # Map Section Name -> Prefix
    sections_map = {
        'Goals': 'G',
        'Environment': 'E',
        'System': 'S',
        'Project': 'P'
    }
    
    current_section_name = None
    
    # State tracking
    section_found = {k: False for k in sections_map}
    section_has_content = {k: False for k in sections_map}

    errors = []

    # Regex patterns
    # Matches: ## Goals
    main_section_re = re.compile(r'^##\s+(\w+)')

    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # 1. Detect Main Section (## Goals)
        m_sec = main_section_re.match(stripped)
        if m_sec:
            name = m_sec.group(1)
            # Only track if it's one of our target sections
            if name in sections_map:
                current_section_name = name
                section_found[name] = True
            else:
                current_section_name = name 
            continue

        # 2. Content Check
        if stripped and current_section_name in sections_map:
             section_has_content[current_section_name] = True

    # Summary Checks
    for sec_name in sections_map:
        if not section_found[sec_name]:
            errors.append(f"Missing required section: {sec_name}")
        elif not section_has_content[sec_name]:
            errors.append(f"Section '{sec_name}' is empty.")

    if errors:
        print("Verification Failed:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("Requirements structure verified successfully.")

if __name__ == "__main__":
    verify_requirements("requirements.md")
