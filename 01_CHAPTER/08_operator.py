# Python operators are special symbols that perform operations on variables and values. They are categorized into several types:
#   1.Arithmetic Operators:
#       Used for mathematical calculations.
#            + (Addition)
#            - (Subtraction)
#            * (Multiplication)
#            / (Division)
#            % (Modulo - returns the remainder of a division)
#            ** (Exponentiation - raises the first operand to the power of the second)
#            // (Floor Division - returns the integer part of the quotient)
#   2.Assignment Operators:
#       Used to assign values to variables.
#            = (Assignment)
#            += (Add and assign)      ||  simple meaning a = a + _
#            -= (Subtract and assign) ||  simple meaning a = a - _
#            *= (Multiply and assign) ||  simple meaning a = a * _
#            /= (Divide and assign)   ||  simple meaning a = a / _
#            %= (Modulo and assign)   ||  simple meaning a = a % _
#            **= (Exponentiate and assign)
#            //= (Floor divide and assign)
#   3.Comparison (Relational) Operators:
#       Used to compare two values and return a Boolean result (True or False).
#            == (Equal to)
#            != (Not equal to)
#            > (Greater than)
#            < (Less than)
#            >= (Greater than or equal to)
#            <= (Less than or equal to)
#   4.Logical Operators:
#       Used to combine conditional statements.
#            and (Logical AND)
#            or (Logical OR)
#            not (Logical NOT)
#   5.Identity Operators:
#       Used to compare the memory locations of two objects.
#            is (Returns True if both variables point to the same object)
#            is not (Returns True if both variables do not point to the same object)
#   6.Membership Operators:
#       Used to test if a sequence contains a specific value.
#            in (Returns True if a value is found in the sequence)
#            not in (Returns True if a value is not found in the sequence)
#   7.Bitwise Operators:
#        Used to perform operations on individual bits of integers.
#             & (Bitwise AND)
#             | (Bitwise OR)
#             ^ (Bitwise XOR)
#             ~ (Bitwise NOT)
#             << (Left shift)
#             >> (Right shift)

a = 34
b = 2 

# Arithmetic Operator 
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a % b = ", a % b)
print("a // b = ", a // b)
print("a ** b = ", a ** b)

# Conditional Operators 
print(a>4)
print(a<4)
print(a<=4)
print(a>=4)
print(a==4) # Is a equal to 4?
print(a==34) # Is a equal to 34?
print(a!=34) # Is a not equal to 34?

c = True 
d = False

# Logical Operators
print("and Operator...")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("or Operator...")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("not Operator...")
print(not(True) ) 
print(not(False) ) 

e = 55
print(e)
e *= 3
print(e)