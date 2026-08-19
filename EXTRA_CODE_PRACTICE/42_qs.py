# Sets and Set Methods
# 1.Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3 ?)
# 2.Add 5 to the set, remove 2 , and check if 4 is in the set.
# 3.Create two sets:
#       i.a = {1, 2, 3}
#       ii.b = {3, 4, 5}
#       iii.Find their:
#        Union
#        Intersection
#        Difference ( a - b )

# 1.
my_set = {1, 2, 3, 3, 4}
print(my_set)


# 2.
my_set = {1, 2, 3, 4}

# Add 5 to the set 
my_set.add(5)
print(f"After adding 5: {my_set}")

# Remove 2 from the set 
my_set.remove(2)
print(f"After removing 2: {my_set}")

# Check if 4 is in the set 
print(f"Is 4 in the set? {4 in my_set}")

# 3.
a = {1, 2, 3} 
b = {3, 4, 5}  

# Union 
print(f"Union (a | b): {a.union(b)}")

# Intersection 
print(f"Intersection (a & b): {a.intersection(b)}")

# Difference (a - b) 
print(f"Difference (a - b): {a.difference(b)}")