# Append to an existing file called myFile.txt
# It should add the content at the end of the previous content

f = open("myFile.txt" , "a")

string = '''why life is so tough ?'''

f.write(string)

f.close()