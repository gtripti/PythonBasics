myFile = open('myFile.txt')
print(myFile.read())
# cursor moves to the end now we need to reset the cursor to the end
myFile.read()
myFile.seek(0)
contents = myFile.read()
contents
myFile.seek(0)

# read lines
myFile.readlines()

# open text files at any location in computer -- provide the full file path 
# f1 = open("C:\Users\aashshar\PythonBasics\myFile.txt")
# close the file manually
myFile.close()

# new way of accessing the file
with open('myFile.txt') as myFile :
    contents = myFile.read() 
contents 
# open file in read mode -- default
with open('myFile.txt' , mode='r') as myFile :
    contents = myFile.read()
contents
# open file in write mode --- overwites existing file or creates a new file 
with open('f1.txt' , mode='w') as f :
    f.write('I created a new file')
with open('f1.txt') as f:
    contents = f.read()
contents

# open file in append mode
with open('myFile.txt', mode='a') as myFile:
    myFile.write('\nThis is the forth line')
with open('myFile.txt' , mode='r') as myFile :
    contents = myFile.read()
contents

# mode = 'r+' for reading and writing
# mode 'w+' for writing and reading -- overwrites the existing file
