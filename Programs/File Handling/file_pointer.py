# When you open a file, Python uses a file pointer (cursor)
# This pointer shows where you are currently reading or writing in the file.

# 🟢 1. tell() Method

# 👉 Returns the current position of the cursor

# Example
# with open("file.txt", "r") as file:
#     print(file.tell())   # starting position
#     file.read(5)
#     print(file.tell())   # after reading 5 characters
# ✅ Output (example):
# 0
# 5
# 💡 Meaning:
# Cursor starts at 0
# After reading 5 characters → position becomes 5
# 🟡 2. seek() Method

# 👉 Used to move the cursor to a specific position

# Syntax
# file.seek(position)
# Example
# with open("file.txt", "r") as file:
#     file.seek(5)       # move to position 5
#     data = file.read()
#     print(data)
# 💡 Meaning:
# Cursor jumps to 5th position
# Reading starts from there