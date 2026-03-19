# Count the number of vowels in a string
s = "avani sharma"
count = 0
for ch in s:
    if ch in "aeiou":
        count+=1
print("count vowels: ", count)

# Count consonants, digits, and special characters.
s = "avani@sharma1220"
consonants = 0
digits = 0
special_ch = 0
for ch in s:
    if ch.isalpha():
        if ch not in "aeiouAEIOU":
            consonants+=1
    elif ch.isdigit():
        digits+=1
    else:
        special_ch+=1
print("consonants:", consonants)
print("digits:", digits)
print("special character:", special_ch)

# Reverse a string without using slicing.
s = "python is fun"
rev = ""
for i in range(len(s)-1, -1, -1):
    rev+= s[i]
print(rev)

# Check if a string is a palindrome (without slicing).
s = "madam"
rev = ""
for ch in rev:
    rev +=ch
if ch == rev:
    print("palindrome")
else:
    print("not palindrome")