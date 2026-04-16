# 1. write() Method: Writes a single string to the file
# "w" mode will overwrite old data
# Example
with open("file.txt", "w") as file:
    file.write("Hello Avani\n")
    file.write("Welcome to Python")


# writelines() Method: Writes multiple lines (list of strings)
# Example
lines = ["Hello\n", "This is Python\n", "File Handling"]
with open("file.txt", "w") as file:
    file.writelines(lines)