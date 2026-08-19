# If there is no file then it will throw an error, that why its a better option to wrap it in try and except.
# f = open("harry.txt", "r")
# content = f.read()
# print(content)
# f.close()

try:
    f = open("dhruba.txt", "r")
    content = f.read()
    print(content)
    f.close()

except Exception as e :
    print(e)