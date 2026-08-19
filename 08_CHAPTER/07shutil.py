# In Python, shutil is a built-in standard library module that stands for “Shell Utilities.”
# It provides higher-level functions for file operations compared to os.

# 🔎 What shutil can do:

#   1. Copying files/folders
#         shutil.copy(src, dst) → Copy a file.
#         shutil.copytree(src, dst) → Copy an entire folder (recursively).
#   2.Moving / Renaming files
#         shutil.move(src, dst) → Move a file or folder.
#   3.Deleting folders (recursively)
#         shutil.rmtree(path) → Delete a folder with all its files inside (unlike os.rmdir() which only deletes empty folders).
#   4.Archiving
#         shutil.make_archive(base_name, format, root_dir) → Create .zip, .tar, etc. archives.
#         shutil.unpack_archive() → Extract archives.
#   5.File metadata
#         shutil.chown() → Change file owner (Unix).
#         shutil.copystat() → Copy file permissions, timestamps, etc.

import shutil 

shutil.rmtree("dir1")
shutil.copy("dhruba.txt" , "john.txt")

shutil.move("john.txt", "dir1/")