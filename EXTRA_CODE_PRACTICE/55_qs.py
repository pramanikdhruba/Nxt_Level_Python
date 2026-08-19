# *args and **kwargs
# 1.Write a function sum_all(*args) that accepts any number of integers and returns their sum.
# 2.Write a function print_details(**kwargs) that prints key-value pairs passed as arguments, for example:
        # print_details(name="Alice", age=25, city="Delhi")
        # Output:
        # name: Alice
        # age: 25
        # city: Delhi

# 1.
def sum_all(*args):
    """Accepts any number of integers and returns their sum.""" 
    return sum(args)

print("--- Testing *args ---")
print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40, 50): {sum_all(10, 20, 30, 40, 50)}")

# 2.
def print_details(**kwargs):
    """Prints key-value pairs passed as arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}") # [cite: 50, 51, 52]

print("\n--- Testing **kwargs ---")
print_details(name="Alice", age=25, city="Delhi") 