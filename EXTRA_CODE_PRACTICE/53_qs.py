#  map(), filter(), and reduce()
# 1.Use map() to convert [1, 2, 3, 4, 5] into their cubes.
# 2.Use filter() to get only even numbers from [10, 11, 12, 13, 14] .
# 3.Use reduce() from functools to find the product of all elements in [1, 2,3, 4] .

from functools import reduce # [cite: 42]

print("--- Testing map(), filter(), reduce() ---")

# 1. Use map() to convert [1, 2, 3, 4, 5] into their cubes
numbers_map = [1, 2, 3, 4, 5] 
cubes = list(map(lambda x: x**3, numbers_map)) 
print(f"Cubes of {numbers_map}: {cubes}")

# 2. Use filter() to get only even numbers from [10, 11, 12, 13, 14]
numbers_filter = [10, 11, 12, 13, 14] 
evens = list(filter(lambda x: x % 2 == 0, numbers_filter)) 
print(f"Even numbers from {numbers_filter}: {evens}")

# 3. Use reduce() to find the product of all elements in [1, 2, 3, 4]
numbers_reduce = [1, 2, 3, 4] 
product = reduce(lambda x, y: x * y, numbers_reduce) 
print(f"Product of {numbers_reduce}: {product}")