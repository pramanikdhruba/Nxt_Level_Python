# 1.Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
# 2.Write a function safe_divide(a, b) that returns the result of a / b , but returns "Cannot divide by zero" if b is 0 .
# 3.Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.


# 1.
def fibonacci(n):
    # Helper recursive function to compute Fibonacci numbers
    def fib(num):
        if num <= 1:
            return num
        else:
            return fib(num - 1) + fib(num - 2)

    # Print the first n Fibonacci numbers
    for i in range(n):
        print(fib(i), end=" ")

# Example usage
fibonacci(10)


# 2.
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

# Example usage
print(safe_divide(10, 2))   # Output: 5.0
print(safe_divide(5, 0))    # Output: Cannot divide by zero


# 3.
import my_utils   # Import the custom module

number = 10

if my_utils.is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")