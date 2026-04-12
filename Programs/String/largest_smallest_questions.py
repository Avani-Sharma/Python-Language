# find largest word in string
s = "I love programming in python"
words = s.split()
largest = ""
for w in words:
    if len(w) > len(largest):
        largest = w
print("Largest word:", largest)

# find smallest word in string
s = "I love programming in python"
words = s.split()
smallest = words[0]
for w in words:
    if len(w) < len(smallest):
        smallest = w
print("Smallest word:", smallest)

# find lagest substring without repeating characters
s = "abcabcbb"
largest = ""
temp = ""
for ch in s:
    if ch not in temp:
        temp += ch
    else:
        if len(temp) > len(largest):
            largest = temp
        temp = temp[temp.index(ch)+1:] + ch
if len(temp) > len(largest):
    largest = temp
print("Longest substring without repeating:", largest)