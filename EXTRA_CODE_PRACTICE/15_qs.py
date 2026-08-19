# Print the multiplication table of a number (entered by user).

num = int(input("Enter A Number : "))

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")