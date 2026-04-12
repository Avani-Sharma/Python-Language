s = "babad"
result = ""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        substring = s[i:j]
        if substring == substring[::-1]:
            if len(substring)> len(result):
                result = substring
print(result)