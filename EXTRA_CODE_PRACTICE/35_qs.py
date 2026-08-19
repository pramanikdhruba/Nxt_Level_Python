# Recursion in Python
# 1.Write a recursive function factorial(n) that returns the factorial of a number.
# 2.Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

# 1.
def factorial(n):
    # base case
    if  n==0:
        return 1
    return n*factorial(n-1)

first_fact = factorial(5)
print(f"FACTORIAL : {first_fact}")

# 2.
def sum_of_digits(n):
    # Base case: if n is a single digit, return n
    if n < 10:
        return n
    else:
        # Recursive case: last digit + sum of remaining digits
        return n % 10 + sum_of_digits(n // 10)

# Example usage
num = 12345
print("Sum of digits:", sum_of_digits(num))
