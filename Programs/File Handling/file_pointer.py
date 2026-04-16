# When you open a file, Python uses a file pointer (cursor)
# This pointer shows where you are currently reading or writing in the file.

# tell() Method: Returns the current position of the cursor

# Example
with open("file.txt", "r") as file:
    print(file.tell())   
    file.read(5)
    print(file.tell())   


# seek() Method: Used to move the cursor to a specific position
# Syntax: file.seek(position)
# Example
with open("file.txt", "r") as file:
    file.seek(5)       
    data = file.read()
    print(data)