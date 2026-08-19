from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
#         [3, 3, 4, 5, 6]
#         [6, 4, 5, 6]
#         [10, 5, 6]
#         [15, 6]
#         [21]

def sum(a, b):
    return a + b 
# adding the number from left to right 


c = reduce(sum, numbers)
print(c)

# 1. map()
# Applies a function to each element of an iterable (list, tuple, etc.).
# Returns a new iterable (in Python 3 → returns a map object, usually converted to list).
# ✅ Use Case: Transform each element.

# 2. filter()
# Applies a function that returns True/False to each element.
# Keeps only the elements where the function returns True.
# ✅ Use Case: Select elements from a sequence.

# 3. reduce()
# Comes from functools module → from functools import reduce.
# Applies a function cumulatively to the items of an iterable.
# Reduces the iterable to a single value.
# ✅ Use Case: Combine all elements into one (sum, product, max, etc.)