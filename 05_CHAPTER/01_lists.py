# ------- WHAT IS LISTS -------

# A list in Python is a versatile, ordered collection of items. Think of it as a container where you can store multiple values of different data types, and you can change its contents later on.

# Key Characteristics :

#    1.Ordered: The items in a list have a defined order, and that order will not change unless you modify it. The first item you add stays in the first position, the second in the second, and so on.

#    2.Mutable (Changeable): You can change, add, and remove items from a list after it has been created. This flexibility is one of its most powerful features.

#    3.Allows Duplicates: Lists can contain items with the same value. For example, [1, 2, 2, 3] is a valid list.

#    4.Heterogeneous: A single list can store items of different data types, such as integers, strings, and even other lists.



# ------------- DIFFERENCE BETWEEN ARRAY AND LISTS -------------

# 1.Data Type :
#   Array: An array is homogeneous, meaning all its elements must be of the same data type (e.g., all integers or all floating-point numbers). This uniformity is crucial for its performance benefits.
#   List: A list is heterogeneous, allowing you to store elements of different data types within the same collection. For instance, a single Python list can contain an integer, a string, and another list.


# 2.Memory Allocation and Performance :
#   Array: Arrays store elements in contiguous memory locations. This direct, unbroken block of memory allows for fast access to elements because the computer can calculate the precise location of any element based on its index. This is especially advantageous for mathematical computations on large datasets.
#   List: In Python, a list is essentially a dynamic array of pointers. Each element in the list is an object with its own memory location, and the list itself stores references (pointers) to these objects. While this provides flexibility, it can lead to slower performance for numerical operations compared to arrays, as it involves an extra step of following the pointers to the actual data.


# 3.Mutability and Size :
#     Array: Traditional arrays have a fixed size that is determined when they are created. While you can change the values of the elements, you cannot easily add or remove elements without creating a new array.
#     List: Python lists are mutable and dynamic. You can easily add, remove, or change elements, and the list will automatically resize itself as needed.


# 4.Functionality and Use Cases :
#     Array: Arrays, especially those found in libraries like NumPy in Python, are optimized for numerical and mathematical operations. They support element-wise operations, which are significantly faster than iterating through a list to perform the same calculations.
#     List: Lists are a more general-purpose data structure in Python. Their flexibility makes them ideal for a wide range of tasks where the data may be of mixed types or the size of the collection needs to change frequently


# Empty Lists
noMarks = []
# List of Integers
marks = [ 54 , 23 , 64 , 93 , 32]
# Lists of mixed data types
mixed = [ 43 , "Hello" , False , 4.2 ]

# Slicing
print(marks[2:4])
print(marks[2])
# print(mixed[4]) # Error Index out of bound