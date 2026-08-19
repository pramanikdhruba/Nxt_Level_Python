import os   # Import the OS module for file system operations

# List all files and folders inside "dir"
a = os.listdir("dir")
print(a)  # Example output: ['simple.txt']

# Print current working directory
print(os.getcwd())  # Example: C:\Users\YourName\Desktop

# Check if "harry" exists (file or folder)
print(os.path.exists("harry"))  # Example output: False

# Delete the file "simple.txt" inside "dir"
# os.remove("dir/simple.txt")

# Remove the folder "dir" (works only if it's empty now)
# os.rmdir("dir")
