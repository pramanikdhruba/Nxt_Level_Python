# Write a program that counts how many vowels are in a given string.
# Take a user input string and check if it is a palindrome (same forwards and backwards).
# 1.Count vowels in a given string
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)

# 2. Check if the string is a palindrome
# Remove spaces and convert to lowercase for accurate comparison
clean_text = text.replace(" ", "").lower()

if clean_text == clean_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
