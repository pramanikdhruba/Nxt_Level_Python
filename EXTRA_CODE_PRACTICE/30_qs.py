# String Manipulation Challenges
# Given sentence = "Coding in Python is fun" , replace "fun" with
# "awesome" and print it.
# Find the index of the word "Python" in sentence .
# Convert the entire sentence to uppercase and print it.

sentence = "Coding in Python is fun"

# 1️⃣ Replace "fun" with "awesome"
new_sentence = sentence.replace("fun", "awesome")
print("After replacement:", new_sentence)

# 2️⃣ Find the index of the word "Python"
index_python = sentence.find("Python")
print("Index of 'Python':", index_python)

# 3️⃣ Convert the entire sentence to uppercase
uppercase_sentence = sentence.upper()
print("Uppercase sentence:", uppercase_sentence)
