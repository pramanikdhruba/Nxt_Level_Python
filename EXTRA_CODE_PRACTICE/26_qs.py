# Given text = "Python Programming" , do the following:
# Print the first 6 characters
# Print the last 6 characters
# Print every second character from the string
text = "Python Programming"
first_six = text[0:6]
last_six = text[6:12]
every_second_char = text[0:-1:2]
print(f"{first_six+last_six}")
print(every_second_char)