# Exception Handling and Custom Errors
#  1.Write a program that asks the user to enter a number and handles:
#       i.ValueError if the input is not a number
#       ii.ZeroDivisionError if you try to divide by zero
#  2.Create a custom exception NegativeNumberError and raise it when the user enters a negative number.


# 2. Create a custom exception NegativeNumberError
class NegativeNumberError(Exception): 
    """Raised when the user enters a negative number.""" 
    pass

# 1. Write a program that asks for a number
print("--- Testing Exception Handling ---")
try:
    user_input = input("Enter a positive number: ") 
    
    # 1.i Handle ValueError
    num = int(user_input) 
    
    # 2. Raise custom error for negative number
    if num < 0:
        raise NegativeNumberError("Error: Negative numbers are not allowed.") 
    
    # 1.ii Handle ZeroDivisionError
    result = 100 / num 
    print(f"100 / {num} = {result}")

except ValueError:
    print("Error: Invalid input. That was not a number.") 
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except NegativeNumberError as e:
    print(e) 