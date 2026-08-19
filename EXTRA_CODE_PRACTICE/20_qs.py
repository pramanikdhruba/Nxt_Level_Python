# Use a while loop to reverse a given number (e.g., 123 → 321).

value = int(input("Enter a number : "))

reverse_num = 0
# num = int(input("Enter a number: "))
# reversed_num = int(str(num)[::-1])
# print("Reversed number:", reversed_num)

while value > 0 :
    digit = value % 10
    reverse_num = reverse_num * 10 + digit
    value //= 10

print("Reversed Number :",reverse_num)