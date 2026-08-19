# 1.Write a program that reads a file and creates another file with all words converted to uppercase.
# 2.Create a script that deletes all .tmp files from the current directory using os and os.remove() .
# 3.Write a Python command-line tool that takes a folder name and prints the total size of all files inside it (use os.path.getsize() ).



# 1.
source_filename = 'notes.txt'
output_filename = 'notes_upper.txt'

try:
    with open(source_filename, 'r') as f_in:
        content = f_in.read()
    
    with open(output_filename, 'w') as f_out:
        f_out.write(content.upper())
        
    print(f"File '{output_filename}' created with uppercase content.")
except FileNotFoundError:
    print(f"Error: Source file '{source_filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# 2.
import os

# Let's create some dummy .tmp files for demonstration
for i in range(3):
    with open(f'file{i}.tmp', 'w') as f:
        f.write('temporary file')
print("Created dummy .tmp files.")

# Find and delete .tmp files
deleted_files = []
current_directory = os.getcwd()
for filename in os.listdir(current_directory):
    if filename.endswith(".tmp"):
        try:
            os.remove(os.path.join(current_directory, filename))
            deleted_files.append(filename)
        except OSError as e:
            print(f"Error deleting file {filename}: {e}")

if deleted_files:
    print(f"\nSuccessfully deleted the following files: {deleted_files}")
else:
    print("\nNo .tmp files found to delete.")

# 3.
# folder_size.py
import os
import sys

def get_folder_size(folder_path):
    """Calculates the total size of all files in a folder."""
    if not os.path.isdir(folder_path):
        return f"Error: '{folder_path}' is not a valid directory."
        
    total_size = 0
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                total_size += os.path.getsize(item_path)
        return total_size
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python folder_size.py <folder_name>")
    else:
        folder_name = sys.argv[1]
        size = get_folder_size(folder_name)
        
        if isinstance(size, int):
            # Convert size to KB for readability
            size_kb = size / 1024
            print(f"Total size of files in '{folder_name}': {size_kb:.2f} KB")
        else:
            print(size)