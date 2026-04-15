# 1. write() Method

# 👉 Writes a single string to the file

# Example
# with open("file.txt", "w") as file:
#     file.write("Hello Avani\n")
#     file.write("Welcome to Python")
# ✅ Output in file:
# Hello Avani
# Welcome to Python
# 💡 Points:
# Only string is allowed
# Use \n for new line
# "w" mode will overwrite old data
# 🟡 2. writelines() Method

# 👉 Writes multiple lines (list of strings)

# Example
# lines = ["Hello\n", "This is Python\n", "File Handling"]

# with open("file.txt", "w") as file:
#     file.writelines(lines)
# ✅ Output in file:
# Hello
# This is Python
# File Handling
# 💡 Points:
# Takes list of strings
# Does not add newline automatically → you must use \n