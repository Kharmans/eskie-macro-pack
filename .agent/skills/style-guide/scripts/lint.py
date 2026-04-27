import sys
import re
import argparse
from pathlib import Path

def lint_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    errors = []
    
    for i, line in enumerate(lines):
        line_num = i + 1
        
        # Check for tabs
        if '\t' in line:
            errors.append(f"Line {line_num}: Contains tabs instead of spaces.")
            
        # Check for missing EMP | prefix in console.log/warn/error
        # This regex looks for string literals as the first argument to console.*
        log_match = re.search(r'console\.(log|warn|error|info)\s*\(\s*([\'"`])(.*?)\2', line)
        if log_match:
            msg = log_match.group(3)
            if not msg.startswith('EMP |'):
                errors.append(f"Line {line_num}: console statement missing 'EMP | ' prefix. Found: {msg}")
                
    if errors:
        print(f"Linting errors found in {file_path}:")
        for error in errors:
            print(f"  - {error}")
        return False
    else:
        print(f"Linting passed for {file_path}")
        return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lint eskie-macro-pack JS files for style guide adherence.")
    parser.add_argument("file", help="Path to the JS file to lint")
    args = parser.parse_args()
    
    if not Path(args.file).exists():
        print(f"Error: File {args.file} not found.")
        sys.exit(1)
        
    success = lint_file(args.file)
    sys.exit(0 if success else 1)
