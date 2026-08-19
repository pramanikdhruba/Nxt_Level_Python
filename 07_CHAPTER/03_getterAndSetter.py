# Encapsulation
# 1.Getter (Accessor) Method:
#       A getter method is used to retrieve or "get" the value of an attribute. It provides a controlled way to read an attribute's value, rather than directly accessing the attribute itself. This allows for potential validation, formatting, or computation before the value is returned. 
# 2.Setter (Mutator) Method:
#       A setter method is used to modify or "set" the value of an attribute. It provides a controlled way to update an attribute's value, allowing for validation, transformation, or other logic to be applied before the new value is assigned. This helps maintain data integrity and consistency. 

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @property # getter
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1].upper()}"
        self.name = new_name

e = Employee( "Jack Doe" , 34555)

print(e.first_name)
e.first_name = "John"
print(e.name)

# print(e.first_name)
# e.first_name = "JOHN"
# print(e.name)