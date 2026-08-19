# SYNTAX TO DECLARE A STRING

# name = "Dhruv"
name1 = 'Dhruv'
# name = ''' Dhurv ia a good boy'''
print(name1)


# INDEXING
name = "Harry" 

# name = "H   a   r  r   y"
#         0   1   2  3   4
#        -5  -4  -3 -2  -1

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4]) # name[-4+5] name[1]
print(name[-5])


# DOUBTS
s = "hello"
print(id(s))   # memory address of "hello"

s = "world"    # now s points to a new string
print(id(s))   # memory address changes
print(id("hello"))

# s[0] = "H"   # trying to change first character but through an error

a = "hello"
b = "hello"
print(a is b)  # True (both point to the same object)

# When we say strings are immutable, we mean:
# ➡️ Once a string object is created in memory, its contents cannot be changed.

# But when you “overwrite” a string variable, you’re not changing the original string — you’re just making the variable point to a new string object.