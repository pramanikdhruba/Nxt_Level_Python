# Write a program using match case that simulates a simple calculator.
# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case .

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
operator = input("Enter the operation you want to perform : ")

match operator :
    case "+" :
        print(f"{num1+num2}")
    case "-" :
        print(f"{num1-num2}")
    case "*" :
        print(f"{num1*num2}")
    case "/" :
        print(f"{num1/num2}")
    case "%" :
        print(f"{num1%num2}")
    case "//" :
        print(f"{num1//num2}")
    case "**" :
        print(f"{num1**num2}")
    case _ :
        print(f"Operation cant be perform")