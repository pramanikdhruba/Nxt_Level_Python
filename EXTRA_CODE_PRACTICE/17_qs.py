# print this :
# *
# **
# ***
# ****

row = int(input("Enter Number of row : "))

for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end="")
    print("",end="\n")
    #  or simply print()