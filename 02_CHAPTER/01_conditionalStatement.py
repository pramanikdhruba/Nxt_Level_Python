# if statement
age = 12

if(age>18):
    print("you can drive")
    print("Thank you")
print("End of program")


# if-else statement
age1 = int(input("Enter your age : "))

if(age>18):
    print("you can drive")
else:
    print("you cannot drive") 

print("End of program")


# if-elif-else statement
age2 = int(input("Enter your age : "))

if(age>18):
    print("You can drive")
elif(age==18):
    print("Lets schedule an interview")
elif(age==0):
    print("Hey you are just born")
else:
    print("Sorry you cannot drive")

# match-case statement || alternate of switch-case statement

a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You won a charger")
    case 3:
        print("You won $3")
    case 6:
        print("You won a camera")
    case _:
        print("Better luck next time")