# If-Else Conditional Statements
# Create a program that checks if a person is eligible to vote (age >= 18)
age = int(input("Enter your age :"))

if(age >= 18) :
    print(f'Your are eligible for vote.')
elif(age < 18) :
    print(f'Your are not eligible for vote.')