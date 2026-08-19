# In Python, modules are files containing Python code (functions, classes, variables, etc.) that can be imported and used in other Python programs. They are primarily categorized into the following types:

# - Built in Modules 
# - External Modules  || Third-Party Modules
# - User-Defined Modules
# - Package Module



# List of all the built in Modules: https://docs.python.org/3/py-modindex.html
# To import External module we have to run the command in the terminal pip install ______
import math 
import os 
import mymodule
import requests
# pip install requests

print(math.sqrt(16))
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)


# The __pycache__ directory in Python is a folder automatically created by the Python interpreter to store compiled bytecode files for Python modules. When a Python module (a .py file) is imported into another script i.e., mymodule.py , Python compiles this module into bytecode, which is a lower-level, platform-independent representation of the code. 




# Package Module Example : 
# In Python, a package is a way to organize and structure related modules into a directory hierarchy. While a module is a single Python file containing code, a package is essentially a directory that groups multiple modules together, often along with sub-packages for further organization.



# my_project/
# ├── main.py
# └── my_package/
#     ├── __init__.py
#     ├── module_a.py
#     └── sub_package/
#         ├── __init__.py
#         └── module_b.py
# In this example, my_package is a package containing module_a.py and a sub-package sub_package, which in turn contains module_b.py. This structure allows for organized and manageable code in larger applications.
# to import module_b.py
# from my_package.sub_package import module_b