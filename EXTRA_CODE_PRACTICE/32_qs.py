# Defining Functions
# 1.Write a function greet() that prints "Hello, Python Learner!" when
# called.
# Write a function square(num) that returns the square of a given number. Test
# it with different numbers


# 1.
def greet():
    print("Hello World!")
greet()

# .2
def square(num):
    return num*num

value = int(input("Enter a number: "))
square_of_num = square(value)
print(f"square : {square_of_num}")