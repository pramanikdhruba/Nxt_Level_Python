text = " i love python programming "

# 1️⃣ Remove extra spaces from both ends
text = text.strip()

# 2️⃣ Convert it to title case
title_case_text = text.title()

# 3️⃣ Count how many times "o" appears
count_o = text.count("o")

# 4️⃣ Check if the string "123abc" is alphanumeric
is_alphanumeric = "123abc".isalnum()

# Display results
print("After stripping:", text)
print("Title case:", title_case_text)
print("Count of 'o':", count_o)
print("Is '123abc' alphanumeric?:", is_alphanumeric)
