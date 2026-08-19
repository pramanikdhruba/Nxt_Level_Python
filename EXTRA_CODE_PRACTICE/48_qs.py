# Decorators in Python
#   1.Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!" .
#   2.Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.


# 1.
def logger(func):
    """Prints 'Function is being called' before the function runs.""" 
    def wrapper():
        print("Function is being called") 
        func()
    return wrapper

# 2. Use it to decorate a function say_hello()
@logger
def say_hello():
    """Prints 'Hello!'.""" 
    print("Hello!") 

# Test the decorated function
print("--- Testing logger decorator ---")
say_hello()





# 2.
import time

# 1. Write a decorator timer
def timer(func):
    """Calculates how long a function takes to execute.""" 
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function '{func.__name__}' took {end_time - start_time:.6f} seconds to run.")
        return result
    return wrapper

# 2. Test it with a function that sums numbers from 1 to 1,000,000
@timer
def sum_large_list():
    """Sums numbers from 1 to 1,000,000.""" 
    return sum(range(1, 1000001))

# Test the timed function
print("\n--- Testing timer decorator ---")
total = sum_large_list()
print(f"Sum: {total}")