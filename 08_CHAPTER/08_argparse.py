# argparse is a Python module used for building command-line interfaces (CLI). It makes it easy to write user-friendly scripts that accept arguments from the command line.

# Why use argparse?
#     1.Allows you to pass values when running a Python script.
#     2.Provides automatic help (-h).
#     3.Handles parsing, type checking, and default values.


import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")

parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operation", choices=["add", "sub", "div", "mul"], help="Operation to perform")

args = parser.parse_args()

# print(args)

if(args.operation == "add"):
    print(f"The result is {args.num1 + args.num2}")
elif(args.operation == "sub"):
    print(f"The result is {args.num1 - args.num2}")
elif(args.operation == "mul"):
    print(f"The result is {args.num1 * args.num2}")
elif(args.operation == "div"):
    print(f"The result is {args.num1 / args.num2}")
else:
    print("Some error occurred")


# python 08_argparse.py 8 10 mul || run this in terminal 
# python 08_argparse.py 8 10 div || run this in terminal 
# python 08_argparse.py 8 10 add || run this in terminal 
# python 08_argparse.py 8 10 sub || run this in terminal 