# create a list containing the table of 5 

# Method 1 --->
table  = []
for i in range(1,11):
    table.append(5*i)

# Method 2 --->
table1 = [ 5*i for i in range(1,11) ]

print(table , "\n" ,table1 , sep="")

# A list comprehension is a short and elegant way to create lists. Instead of writing a long for loop, you can build a list in one line.