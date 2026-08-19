# Static & Class Methods
# 1.Create a class MathUtils with:
#      i.A @staticmethod called add(a, b) that returns a + b .
#      ii.A @classmethod called description(cls) that prints "This is a
#      iii.utility class for math operations."
# 2.Call both methods without creating an object.


# 1. Create a class MathUtils
class MathUtils: 
    """A utility class for math operations.""" 

    # 1.1 A @staticmethod called add(a, b)
    @staticmethod
    def add(a, b): 
        """Returns a + b."""
        return a + b

    # 1.2 A @classmethod called description(cls)
    @classmethod
    def description(cls): 
        """Prints the class description."""
        print("This is a utility class for math operations.") 

# 2. Call both methods without creating an object
print("--- Testing Static & Class Methods ---")
print(f"Static method add(5, 10): {MathUtils.add(5, 10)}")
print("Class method description(): ", end="")
MathUtils.description()