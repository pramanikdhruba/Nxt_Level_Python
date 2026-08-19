# Variable Scope and Docstrings

# 1. Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.
# 2. Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring

def increment():
    counter = 0   # Local variable initialized to 0 each time
    counter += 1
    print("Counter value:", counter)

# Calling the function multiple times
increment()
increment()
increment()


def multiply(a, b):
    """
    This function takes two numbers as input and returns their product.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.
    """
    return a * b

# Displaying the docstring using help()
help(multiply)
print(multiply.__doc__)
