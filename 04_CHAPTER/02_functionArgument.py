# This is parameters      ||    plus is a default parameter
def add(a, b, plus=0):
    x = a + b + plus
    return x

# This is arguments
c = add(3, 5, 2)
print(c)

c1 = add(b=5, a=3)
print(c1)