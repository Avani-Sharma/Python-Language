# file handling: is the process of the handling file or storing the data into the permanent storage.

# file: file stores the data like audio, video, text
# files are of two types: 
# 1. text file(human readable files)
# 2. binary file (0 & 1) (non-readable)

# file read: here we're opening the file into the read mode. it means the script only access to read the file.
# mode = access 
# syntax: open('filepath', 'mode')

# example
file = open('file.txt', 'r')
content = file.read()
print(content)
# after performing all the operations on the file we have to close that file by using the .close method
file.close()


# whenever we read or write a file then the script use a pointer to iterate over the file to read or write
# contents into the file
# file.seek()
# whenever we want to check the position of the pointer then we have to use the file.tell() method.
# file.tell()
# whenever we want to move the pointer at some position file.seek(position)
# file.seek(25)