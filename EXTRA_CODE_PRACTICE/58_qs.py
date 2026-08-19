# Read, Write, and Append Files
# 1.Write a program that writes three lines of text to a file tasks.txt .
# 2.Open tasks.txt in append mode and add a new line "Task Completed!" .
# 3.Read the file and print all lines as a list using readlines() .

# 1.
# Write three lines to tasks.txt
lines_to_write = [
    "Plan the project layout.\n",
    "Code the file handling module.\n",
    "Test the command line utility.\n"
]

try:
    with open('tasks.txt', 'w') as f:
        f.writelines(lines_to_write)
    print("'tasks.txt' created with three tasks.")
except IOError as e:
    print(f"An error occurred: {e}")


# 2.
# Append a new line to tasks.txt
try:
    with open('tasks.txt', 'a') as f:
        f.write("Task Completed!\n")
    print("Appended 'Task Completed!' to 'tasks.txt'.")
except IOError as e:
    print(f"An error occurred: {e}")

# 3.
# Read all lines from tasks.txt into a list
try:
    with open('tasks.txt', 'r') as f:
        lines_list = f.readlines()
        print("Lines from tasks.txt as a list:")
        print(lines_list)
except FileNotFoundError:
    print("Error: 'tasks.txt' not found. Please run the previous scripts first.")
except IOError as e:
    print(f"An error occurred: {e}")