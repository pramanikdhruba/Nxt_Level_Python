class Employee:
    company = "HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # Static Method 
    @staticmethod
    def sum(a, b):
        return a+b
    
    # Class Method
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls , new_company):
        cls.company = new_company

e1 = Employee("Jack", 3455)
e2 = Employee("Jill", 3465)

# print(Employee.company)
# print(Employee.name) # this will throw an error || AttributeError: type object 'Employee' has no attribute 'name'
# e1.print_info()
# e2.print_info()

# print(e2.sum(5, 23))
print(Employee.company)
e1.change_company("Acer")
print(Employee.company)

# Instance Methods: These are the most common type of method. They operate on a specific instance of a class and receive the instance itself as their first argument (conventionally named self). They can access and modify both instance-specific data and class-level data.

# Class Methods: These methods operate on the class itself, not a specific instance. They receive the class as their first argument (conventionally named cls) and are defined using the @classmethod decorator. They can access and modify class-level data but cannot directly access instance-specific data. They are often used for alternative constructors or operations related to the class as a whole. 

# Static Methods: These are utility functions that are logically associated with a class but do not operate on the instance or the class itself. They do not receive self or cls as their first argument and are defined using the @staticmethod decorator. They cannot access or modify instance or class state directly.