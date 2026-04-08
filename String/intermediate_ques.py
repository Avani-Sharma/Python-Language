# Count how many times a specific character appears.
s = "avani sharma"
count = 0
for ch in s:
    if ch == 'a':
        count+=1
print("specific ch appear:", count)

# Count digits in a string.
s = "avani2012"
count = 0
for ch in s:
    if '0' <= ch <='9':
        count+=1
print("count digit: ", count)

# Count alphabets and numbers separately.
s = "avanisharma2012"
alphabet_count = 0
number_count = 0
for ch in s:
    if ch.isalpha():
        alphabet_count+=1
    elif ch.isdigit():
        number_count+=1
print("alpha count: ", alphabet_count)
print("digit count: ", number_count)

# Count special characters in a string.
s = "avanisharma@#$%^"
special_ch = 0
for ch in s:
    if not ch.isalnum():
        special_ch+=1
print("special ch:", special_ch)