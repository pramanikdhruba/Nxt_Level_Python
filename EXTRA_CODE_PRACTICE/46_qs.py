# Constructor and Attributes
# 1.Create a class Person with a constructor ( __init__ ) that accepts name and age
# as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age2.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object and print the person's name and age
p1 = Person("Alice", 25)
print(f"Name: {p1.name}")
print(f"Age: {p1.age}")