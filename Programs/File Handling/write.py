# 1. write() Method: is used to write the contents into the file which takes the argument as string.
# file.write('this is the content which i want to write into the file')
# 'w': write mode is used to write the content into the file. If the file doesn't exists then it creates the 
# file first and then write the content into this file.
# "w" mode will overwrite old data
# Example
with open("file.txt", "w") as file:
    file.write("Hello Avani\n")
    file.write("Welcome to Python")
    print(file)


# writelines() Method: Writes multiple lines (list of strings)
# Example
lines = ["Hello\n", "This is Python\n", "File Handling"]
with open("file.txt", "w") as file:
    file.writelines(lines)
