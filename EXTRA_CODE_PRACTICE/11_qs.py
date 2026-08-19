# If-Else Conditional Statements
# Write a program that takes a number from the user and prints “Even” if it is
# even, otherwise “Odd”

value = int(input('Enter A Number :'))

if(value%2 == 0):
    print(f"Even Number.")
elif(value%2 != 0):
    print(f"Odd Number.")