# 1. *args → Non-Keyword Arguments
# Collects extra positional arguments into a tuple.
# Useful when you don’t know how many arguments will be passed.
# ✅ Use Case: Handle any number of positional arguments.


def sum(*args): 
    # args will be a tuple of all the values passed to sum 
    total = 0
    for item in args:
        total += item 
    return total


print(sum(342, 2, 7, 9))