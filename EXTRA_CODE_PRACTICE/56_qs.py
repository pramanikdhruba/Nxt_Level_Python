# 1.Combine a decorator with *args and **kwargs support so it can wrap any function regardless of its parameters.
# 2.Implement __add__ in a Vector class so that adding two Vector objects returns a new Vector with summed components.
# 3.Create a small program where invalid user input raises a custom exception, logs the error, and continues execution instead of crashing

# 1.
def universal_logger(func):
    """A decorator that can wrap any function.""" 
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished.")
        return result
    return wrapper

@universal_logger
def add(a, b):
    return a + b

@universal_logger
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

print("--- Testing Bonus 1 (Universal Decorator) ---")
add(10, 20)
greet(name="Bob", greeting="Hi")


# 2.
class Vector:
    """A 2D vector class that supports addition."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Returns a new Vector with summed components.""" 
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        """A simple representation for printing."""
        return f"Vector({self.x}, {self.y})"

print("\n--- Testing Bonus 2 (Vector __add__) ---")
v1 = Vector(1, 2)
v2 = Vector(5, 3)
v3 = v1 + v2 # This uses the __add__ method
print(f"{v1} + {v2} = {v3}")


# 3.
import logging

# Configure logging to file
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Create a custom exception
class InvalidAgeError(Exception): 
    """Raised for invalid age input."""
    pass

def get_age():
    """Continuously asks for age until valid input is given."""
    while True:
        try:
            age_input = input("Enter your age (or 'exit' to quit): ")
            if age_input.lower() == 'exit':
                print("Exiting.")
                break
                
            age = int(age_input)
            
            if age < 0 or age > 120:
                # Raise custom exception for invalid input
                raise InvalidAgeError(f"Invalid age entered: {age}") 
            
            print(f"Valid age entered: {age}. Thank you!")
            break # Exit loop on success
            
        except ValueError:
            # Handle non-integer input
            print("Error: Please enter a valid number.")
            logging.error(f"ValueError: User entered non-numeric input '{age_input}'") 
        except InvalidAgeError as e:
            # Handle custom exception
            print(f"Error: {e}. Age must be between 0 and 120.")
            logging.error(e) 
        
        # The program continues execution after logging 
        print("Please try again.\n")

print("\n--- Testing Bonus 3 (Robust Program) ---")
get_age()
print("Program finished.")
