# Tuples and Operations on Tuples
# 1.Create a tuple coordinates = (10, 20) and print both elements.
# 2.Try to modify the tuple by setting coordinates[0] = 50 — note what
# happens.
# 3.Convert the tuple to a list, change its first element to 50 , and convert it back to a tuple.

# 1.
coordinates = (10, 20)
print(f"The first element is: {coordinates[0]}")
print(f"The second element is: {coordinates[1]}")

# 2.
coordinates = (10, 20)
print(f"Original tuple: {coordinates}")

# Convert the tuple to a list 
temp_list = list(coordinates)

# Change the first element in the list 
temp_list[0] = 50

# Convert the list back to a tuple 
coordinates = tuple(temp_list)
print(f"Modified tuple: {coordinates}")

# 3.
coordinates = (10, 20)
print(f"Original tuple: {coordinates}")

# Convert the tuple to a list 
temp_list = list(coordinates)

# Change the first element in the list 
temp_list[0] = 50

# Convert the list back to a tuple 
coordinates = tuple(temp_list)
print(f"Modified tuple: {coordinates}")