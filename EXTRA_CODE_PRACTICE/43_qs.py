# 1.Create a dictionary student = {"name": "John", "age": 20, "grade": "A"}
# and:
#       i.Print the value of "name" .
#       ii.Change "grade" to "A+" .
#       iii.Add a new key "city" with value "Delhi" .
# 2.Create a dictionary of three friends and their phone numbers. Use:
#       i.keys() to get all names
#       ii.values() to get all numbers
#       iii.items() to loop over key-value pairs and print them


# 1.
student = {"name": "John", "age": 20, "grade": "A"}
print(f"Original dictionary: {student}")

# i. Print the value of "name" 
print(f"Student's name: {student['name']}")

# ii. Change "grade" to "A+" 
student["grade"] = "A+"
print(f"After grade update: {student}")

# iii. Add a new key "city" 
student["city"] = "Delhi"
print(f"After adding city: {student}")

# 2.
phonebook = {
    "Alice": "111-222-3333",
    "Bob": "444-555-6666",
    "Charlie": "777-888-9999"
}

# i. Get all names using keys()
print(f"Names: {phonebook.keys()}")

# ii. Get all numbers using values() 
print(f"Phone Numbers: {phonebook.values()}")

# iii. Loop over key-value pairs using items() 
print("\n--- Phonebook Entries ---")
for name, number in phonebook.items():
    print(f"{name}: {number}")