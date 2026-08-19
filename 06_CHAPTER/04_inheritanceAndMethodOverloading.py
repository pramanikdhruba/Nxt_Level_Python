class Animal : # Parent class (superclass)
    location = "Australia"

    def __init__(self , name):
        self.name = name
    
    def speak(self):
        print("Speaking now....")

# inherit Animal class 
class Dog(Animal) : # This is how inheritance is done in python
    def speak(self): # method overloading
        super().speak() # we are using the speak function of the parent class
        print("woof!")


a = Animal("Dog")
a.speak()
d = Dog("Bruno")
d.speak()
print(d.location)