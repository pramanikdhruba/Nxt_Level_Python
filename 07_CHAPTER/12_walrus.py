# The walrus operator (:=) is a feature introduced in Python 3.8.
# It’s called the walrus operator because := looks like the eyes and tusks of a walrus 🦭.
# 🔹 What It Does
# It allows you to assign a value to a variable as part of an expression.
# So instead of writing a statement in two steps, you can do it in one.

# Example Without Walrus
# data = input("Enter text: ")
# while data != "quit":
#     print(f"You typed: {data}")
#     data = input("Enter text: ")

# Example With Walrus
# while (data := input("Enter text: ")) != "quit":
#     print(f"You typed: {data}")


def very_slow_func():
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    return 70

# # a = very_slow_func()
# if((a:=very_slow_func())>10):
#     print(a)

# else:
#     print("Its not greater than 10")

while(data:=input("Enter the value: ")):
    print(data)
    if data == "q":
        break 


