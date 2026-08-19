# Creating Command Line Utilities
# 1.Write a small script count_lines.py that takes a filename as input and prints
#   how many lines are in the file.
#   Example usage:
#                 python count_lines.py tasks.txt
#                 # Output: Number of lines: 4

# 2.Write a command-line utility search_word.py that takes two arguments:
#         i.A filename
#         ii.A word to search and prints how many times the word appears in the file

# 1.
# count_lines.py  -> file name
import sys  # Import sys module to read command-line arguments

def count_lines_in_file(filename):
    """Counts the number of lines in a given file."""
    try:
        # Open the file in read mode
        with open(filename, 'r') as f:
            lines = f.readlines()  # Read all lines into a list
            return len(lines)      # Return the number of lines in the file
    except FileNotFoundError:
        # Handle case when the file does not exist
        return f"Error: The file '{filename}' was not found."
    except Exception as e:
        # Handle any other unexpected errors
        return f"An error occurred: {e}"

# This block ensures code only runs when script is executed directly
if __name__ == "__main__":
    # sys.argv stores command-line arguments: 
    # sys.argv[0] = script name, sys.argv[1] = filename
    if len(sys.argv) != 2:
        # If user didn’t provide exactly one argument (filename), show usage
        print("Usage: python count_lines.py <filename>")
    else:
        filename = sys.argv[1]  # Get the filename from command-line arguments
        line_count = count_lines_in_file(filename)  # Call the function

        # Check if line_count is an integer (successful case)
        if isinstance(line_count, int):
            print(f"Number of lines: {line_count}")  # Print total line count
        else:
            # If an error message string was returned, print it
            print(line_count)


# 2.
# search_word.py -> file name
import sys
import re

def search_for_word(filename, word):
    """Counts how many times a word appears in a file (case-insensitive)."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            # Use regex to find all occurrences of the word as a whole word, ignoring case
            # \b ensures we match whole words only (e.g., 'art' doesn't match 'start')
            matches = re.findall(r'\b' + re.escape(word) + r'\b', content, re.IGNORECASE)
            return len(matches)
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python search_word.py <filename> <word_to_search>")
    else:
        filename = sys.argv[1]
        word = sys.argv[2]
        word_count = search_for_word(filename, word)
        if isinstance(word_count, int):
            print(f"The word '{word}' appears {word_count} time(s).")
        else:
            print(word_count)