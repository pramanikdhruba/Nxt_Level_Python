# File I/O Basics
#       1.Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
#       2.Open notes.txt , read its content, and print it to the console.

# 1.
# Create and write to notes.txt
try:
    with open('notes.txt', 'w') as f:
        f.write("Learning Python is fun!")
    print("'notes.txt' created and written to successfully.")
except IOError as e:
    print(f"An error occurred: {e}")

# 2.
# Read and print the content of notes.txt
try:
    with open('notes.txt', 'r') as f:
        content = f.read()
        print("Content of notes.txt:")
        print(content)
except FileNotFoundError:
    print("Error: 'notes.txt' not found. Please run the previous script first.")
except IOError as e:
    print(f"An error occurred: {e}")