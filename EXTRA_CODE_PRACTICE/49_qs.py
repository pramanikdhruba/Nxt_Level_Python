# Getters and Setters
#   1.Create a class Employee with a private attribute _salary .
#       i.Use @property to define a getter for salary .
#       ii.Use @salary.setter to prevent setting negative values (print a warning instead).
#       iii.Create an object and test by setting positive and negative salaries.


# 1. Create a class Employee
class Employee:
    """Represents an employee with a salary."""
    def __init__(self, initial_salary):
        # Use the setter during initialization
        self.salary = initial_salary  # This calls the @salary.setter
        
    # i. Use @property to define a getter for salary
    @property
    def salary(self):
        """Getter for _salary.""" 
        return self._salary 

    # ii. Use @salary.setter to prevent negative values
    @salary.setter
    def salary(self, value):
        """Setter for _salary, prevents negative values."""
        if value < 0:
            print(f"Warning: Cannot set negative salary. Salary remains {self._salary}.")
        else:
            self._salary = value

# iii. Create an object and test
print("--- Testing Getters and Setters ---")
emp = Employee(50000)
print(f"Initial salary: {emp.salary}")

# Test setting a positive salary
emp.salary = 60000 
print(f"New salary: {emp.salary}")

# Test setting a negative salary
emp.salary = -1000 
print(f"Salary after attempt to set negative: {emp.salary}")
