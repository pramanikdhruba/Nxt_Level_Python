# create a file called myFile.txt and write the content of the file 

f = open("myFile.txt", "w")

string = '''John Doe is a nice guy.He lives in Nyc and he works with Python.His favorite package is Pandas'''

f.write(string)
f.close()