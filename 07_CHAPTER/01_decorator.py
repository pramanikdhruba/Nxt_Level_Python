# What is a Decorator?
# A decorator in Python is a function that takes another function as input, adds some extra functionality to it, and returns the modified function—without changing the original function’s code.
# It’s often used for:
#        1.Logging
#        2.Authentication
#        3.Measuring execution time
#        4.Caching results
#        5.Validating inputs

# ✅ So, decorators = functions that modify other functions in a clean, reusable way.

# Decorators is a function that takes a function, it creates a new function inside its body(wrapper). Then it returns that new function

def decorator(func) :
    def wrapper():
        print("I am about to execute a function......")
        func()
        print("I have executed this function.....")
    return wrapper

@decorator 
def say_hello() :
    print("Hello!")

# @decorator is just shorthand for:
# say_hello = decorator(say_hello)

# f = decorator(say_hello)
# f()
'''
f will look something like this 
def f():
    print("I am about to execute a function......")
    func()
    print("I have executed this function.....")
'''