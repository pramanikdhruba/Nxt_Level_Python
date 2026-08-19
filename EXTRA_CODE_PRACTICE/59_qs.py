# OS and Shutil Modules
# 1.Use the os module to:
#       i.Print the current working directory
#       ii.List all files and folders in the current directory
#       iii.Create a new folder my_folder
# Use the shutil module to:
#       i.Copy a file from one folder to another
#       ii.Move a file to a new folder
#       iii.Delete a file (careful: irreversible!)


# 1.
import os

# 1. Print the current working directory
print(f"Current Working Directory: {os.getcwd()}") 

# 2. List all files and folders
print(f"\nFiles and Folders in Current Directory: {os.listdir('.')}")

# 3. Create a new folder
folder_name = 'my_folder'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"\nFolder '{folder_name}' created successfully.")
else:
    print(f"\nFolder '{folder_name}' already exists.")


# 2.
import os
import shutil

# Setup for the demonstration
# Create a dummy file and folders
source_folder = 'source_folder'
dest_folder = 'dest_folder'
file_to_manage = 'original_file.txt'

# Create necessary directories and a file
os.makedirs(source_folder, exist_ok=True)
os.makedirs(dest_folder, exist_ok=True)
with open(os.path.join(source_folder, file_to_manage), 'w') as f:
    f.write('This is the original file.')

print(f"Setup complete: Created '{source_folder}', '{dest_folder}', and a sample file called {file_to_manage}.")

# 1. Copy a file
source_path = os.path.join(source_folder, file_to_manage)
dest_path_copy = os.path.join(dest_folder, 'copied_file.txt')
shutil.copy(source_path, dest_path_copy)
print(f"\nFile copied to '{dest_path_copy}'.")

# 2. Move a file
dest_path_move = os.path.join(dest_folder, 'moved_file.txt')
shutil.move(source_path, dest_path_move) 
print(f"File moved to '{dest_path_move}'.")

# 3. Delete a file
file_to_delete = os.path.join(dest_folder, 'copied_file.txt')
if os.path.exists(file_to_delete):
    # For safety, this part is commented out. Uncomment to run.
    # os.remove(file_to_delete)
    # print(f"File '{file_to_delete}' has been deleted.")
    print(f"\nTo delete the file, uncomment the os.remove line for '{file_to_delete}'.") 
else:
    print(f"File '{file_to_delete}' does not exist.")