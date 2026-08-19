# Introduction to Lists
# 1.Create a list fruits = ["apple", "banana", "cherry"] .
#     i.Print the first fruit.
#     ii.Replace "banana" with "orange".
#     iii.Print the length of the list.

# 2.Create a list of numbers from 1 to 10 .
#     i.Print the first three numbers using slicing.
#     ii.Print the last three numbers using slicing

# 1.
fruits = ["apple", "banana", "cherry"] 

# i. Print the first fruit 
print(f"First fruit: {fruits[0]}")

# ii. Replace "banana" with "orange" 
fruits[1] = "orange"
print(f"List after replacement: {fruits}")

# iii. Print the length of the list 
print(f"Length of the list: {len(fruits)}")


# 2.
# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
print(f"Original list: {numbers}")

# 1. Print the first three numbers using slicing 
print(f"First three numbers: {numbers[:3]}")

# 2. Print the last three numbers using slicing 
print(f"Last three numbers: {numbers[-3:]}")