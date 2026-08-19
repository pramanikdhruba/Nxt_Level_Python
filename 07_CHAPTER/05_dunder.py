# "Dunder methods," also known as "magic methods" or "special methods," are predefined methods in Python that have double underscores (or "dunders") at the beginning and end of their names, such as __init__ or __add__. 
# These methods provide a way to define specific behaviors for built-in operations or functionalities when applied to custom classes. By implementing dunder methods within your classes, you can customize how your objects interact with Python's language constructs and operators. 
class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    
    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary}"
    
    def __len__(self):
        return len(self.name)


e = Employee("Harry", 43566)
# print(init(e)) # error 
print(len(e))
print(e.name, e.salary)
print(str(e))
print(repr(e))



# Dunder methods, also known as magic methods, in Python are primarily inbuilt in the sense that they are predefined by the Python language and its built-in types. They provide a standardized way for objects to interact with Python's core functionalities, such as operators, built-in functions, and object lifecycle events.
# However, they are also user-defined in the context of custom classes. While the names and purpose of dunder methods (e.g., __init__, __add__, __len__, __str__) are predefined, you, as a developer, implement or override these methods within your own classes to define how your custom objects behave when interacting with these built-in operations.