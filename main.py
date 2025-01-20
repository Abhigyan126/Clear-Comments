import re
import sys
import os

def remove_comments(file_path, overwrite=False):
    try:
        # Read file content
        with open(file_path, 'r') as file:
            content = file.readlines()

        # Regex patterns for different types of comments
        comment_patterns = [
            # Python style comments (#)
            re.compile(r'#.*'),
            
            # C/C++/Java/JavaScript style single-line comments (//)
            re.compile(r'//.*'),
            
            # C/C++/Java/JavaScript/other C-like languages block comments (/* ... */)
            re.compile(r'/\*.*?\*/', re.DOTALL),
            
            # HTML/XML style comments <!-- ... -->
            re.compile(r'<!--.*?-->', re.DOTALL),
            
            # Shell style comments (#!)
            re.compile(r'#!.*'),
            
            # Ruby style comments (#)
            re.compile(r'#.*'),
            
            # Python triple-quoted multi-line comments (""" ... """ or ''' ... ''')
            re.compile(r'"""(?:[^"\\]|\\.)*?"""', re.DOTALL),
            re.compile(r"'''(?:[^'\\]|\\.)*?'''", re.DOTALL),
        ]

        cleaned_lines = []
        inside_block_comment = False

        for line in content:
            # Check for block comments (multi-line) and remove
            if not inside_block_comment:
                # Loop through each comment pattern
                for pattern in comment_patterns:
                    line = re.sub(pattern, '', line)
            
            # Handle multi-line block comments (/* ... */)
            if '/*' in line:
                inside_block_comment = True
            if inside_block_comment and '*/' in line:
                inside_block_comment = False
            
            # Strip leading and trailing whitespace
            line = line.rstrip()

            # Add line if it's not empty after comment removal
            if line.strip():
                cleaned_lines.append(line)

        if overwrite:
            with open(file_path, 'w') as file:
                file.write('\n'.join(cleaned_lines))
            print(f"Comments removed and saved to the same file: {file_path}")
        else:
            new_file_path = input("Enter the path for the new file: ").strip()
            with open(new_file_path, 'w') as file:
                file.write('\n'.join(cleaned_lines))
            print(f"Comments removed and saved to: {new_file_path}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python comment_remover.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        sys.exit(1)

    print(f"Processing file: {file_path}")
    choice = input("Do you want to overwrite the file? (yes/no): ").strip().lower()

    if choice in ['yes', 'y']:
        remove_comments(file_path, overwrite=True)
    else:
        remove_comments(file_path, overwrite=False)

if __name__ == "__main__":
    main()
