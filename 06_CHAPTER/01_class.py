# Class: Class is a blueprint or a template. Eg. Form for an Exam that contains name, age, electives, father's name etc

# Object: Specific instance created from the template (class.). Eg. Form which contains the data for John Doe

class Employee :
    company = "HP"

    def get_salary(self):
        # self is important here because self ia a way to reference the object of the class which is being created 
        # self is a reference to the current object (instance) of the class.
        # When you create an object from a class, self allows the methods inside the class to access attributes and methods that belong to that particular object. 
        return 34000
 
e1 = Employee() # An Onject of the class employee is created here 

print(e1.get_salary()) # Employee e's get salary method is called 

e2 = Employee()
print(e2.get_salary())
print(e2.company)