# Walrus Operator
# 1.Use the walrus operator to read input until the user enters "quit" . Print each input as it is entered.
# 2.Use the walrus operator in a list comprehension to store lengths of words from ["python", "rocks", "ai"] in a list while filtering out words shorter than 4 characters.


# 1.
print("--- Testing Walrus Operator (Input Loop) ---")
print('Enter text (type "quit" to stop):')
# Use walrus operator to assign and check in the loop condition
while (line := input("> ")) != "quit":
    print(f"You entered: {line}")
print("Loop finished.")

# 2.
print("\n--- Testing Walrus Operator (List Comprehension) ---")
words = ["python", "rocks", "ai"]

# Use walrus operator to store length (n) and filter by it
filtered_lengths = [n for word in words if (n := len(word)) >= 4]
print(f"Words: {words}")
print(f"Lengths of words >= 4 chars: {filtered_lengths}")