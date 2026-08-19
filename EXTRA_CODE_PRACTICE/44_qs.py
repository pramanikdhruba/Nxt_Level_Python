# 1.Write a program that takes a list of numbers and removes all duplicates using a set.
# 2.Given a dictionary of products and their prices, find the product with the highest price.
# 3.Write a program that merges two dictionaries into one.


# 1.
numbers_with_duplicates = [2, 4, 6, 2, 8, 4, 10]

# The easiest way is to convert the list to a set, then back to a list
unique_numbers = list(set(numbers_with_duplicates))

print(f"Original list: {numbers_with_duplicates}")
print(f"List with duplicates removed: {unique_numbers}")

# 2.
products = {
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 75,
    "Monitor": 300
}

# Use the max() function with a custom key
# The key=products.get tells max() to look at the dictionary's values
highest_price_product = max(products, key=products.get)
highest_price = products[highest_price_product]

print(f"The product with the highest price is '{highest_price_product}' at ${highest_price}.")

# 3.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# The ** operator unpacks the dictionaries into a new one
merged_dict = {**dict1, **dict2}

print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")
print(f"Merged Dictionary: {merged_dict}")
