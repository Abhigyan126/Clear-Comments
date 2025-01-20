# Python Comment Remover

This Python script removes comments from a specified file. It supports various comment styles from different programming languages.

## Functionality

The `remove_comments.py` script takes a file path as input and removes comments from the code. It offers two options:

1. **Overwrite the original file:** This removes comments and saves the modified content directly to the same file.
2. **Save to a new file:** This removes comments and saves the modified content to a new file specified by the user.

The script supports the following comment styles:

* Python style comments (#)
* C/C++/Java/JavaScript style single-line comments (//)
* C/C++/Java/JavaScript/other C-like languages block comments (/* ... */)
* HTML/XML style comments ()
* Shell style comments (#!)
* Ruby style comments (#)
* Python triple-quoted multi-line comments (""" ... """ or ''' ... ''')

## Usage

1. Save the script as `remove_comments.py`.
2. Open a terminal and navigate to the directory containing the script and the target code file.
3. Run the script using the following command:

```bash
python remove_comments.py <file_path> ```