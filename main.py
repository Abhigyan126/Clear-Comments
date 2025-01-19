import re
import sys
import os

def remove_comments(file_path, overwrite=False):
    try:
        # Read file content
        with open(file_path, 'r') as file:
            content = file.readlines()

        # Regex to remove Python comments
        comment_pattern = re.compile(r'#.*')
        cleaned_lines = [
            re.sub(comment_pattern, '', line).rstrip() for line in content
        ]

        # Filter out completely empty lines
        cleaned_lines = [line for line in cleaned_lines if line.strip()]

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
