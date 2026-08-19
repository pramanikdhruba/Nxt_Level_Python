# Simple Inheritance
# Create a base class Animal with a method sound() that prints "Some sound" .
# Create a derived class Dog that overrides sound() to print "Bark!" .
# Create an object of Dog and call sound() .

# 3. Simple Inheritance
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    # Override the sound() method
    def sound(self):
        print("Bark!")

# Create an object of Dog and call sound()
my_dog = Dog()
my_dog.sound()