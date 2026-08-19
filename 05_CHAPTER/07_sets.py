# WHAT IS SET ?
# Definition:
#     A set is an unordered, mutable collection of unique elements.
#        1.Unordered → no fixed order (elements may appear in different order each time).
#        2.Mutable → you can add or remove items.
#        3.Unique → duplicates are not allowed.
#        4.Written with curly braces { }.

# Features:
#       1. Removes duplicates automatically
#       2. Unordered (no indexing)
#       3. Heterogeneous elements (different data types allowed)

# 🔹 Set Operations (like in mathematics)
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A | B)  # Union → {1, 2, 3, 4, 5, 6}
# print(A & B)  # Intersection → {3, 4}
# print(A - B)  # Difference → {1, 2}
# print(A ^ B)  # Symmetric Difference → {1, 2, 5, 6}
# 🔹 Adding & Removing Elements
# s = {1, 2, 3}
# s.add(4)         # add element
# s.remove(2)      # remove element (error if not found)
# s.discard(5)     # remove safely (no error if not found)
# print(s)
# 🔹 Empty set ⚠️
# a = {}       # ❌ this creates a dictionary, not a set
# b = set()    # ✅ correct way to make an empty set

s = {3, 23, 2, 11}

print(s, type(s))
# print(s[3]) # You are not allowed to do something like this