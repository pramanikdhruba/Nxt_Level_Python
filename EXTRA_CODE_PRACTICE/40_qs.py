# LIST METHODS

# 1. Start with numbers = [5, 2, 9, 1, 7] and do the following:
#     i.Sort the list in ascending order.
#     ii.Append the number 10 to the list.
#     iii.Remove the number 2 from the list

# 2.Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.


# 1.
numbers = [5, 2, 9, 1, 7]
print(f"Original list: {numbers}")

# i. Sort the list in ascending order
numbers.sort()
print(f"Sorted list: {numbers}")

# ii. Append the number 10 
numbers.append(10)
print(f"After appending 10: {numbers}")

# iii. Remove the number 2 
numbers.remove(2)
print(f"After removing 2: {numbers}")


# 2.
names = ["Alice", "Bob", "Charlie"]
print(f"Original names: {names}")

# Use the insert() method to add "David" at index 1 
names.insert(1, "David")
print(f"After inserting 'David': {names}")