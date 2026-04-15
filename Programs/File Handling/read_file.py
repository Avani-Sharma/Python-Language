# readlines : this function returns the list of all the lines which is stored into the file 
# read function : returns all the content of file into the form of text
# readline: this function returns one by one line. one line at a time.

file = open('file.txt', 'r')
content = file.read()
content1 = file.readline()
content2 = file.readlines()
print(content)
print(content1)
print(content2)
file.close()