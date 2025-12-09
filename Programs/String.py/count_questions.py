# count vowels in string
s = "avanisharma"
vowel = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowel:
        count+=1
print("vowel: ", count)

# count consonants in string
s = "avanisharma"
vowel = "aeiouAEIOU"
count = 0
for ch in s:
    if ch not in vowel:
        count+=1
print("consonants: ", count)

# count uppercase in string
s = "avaniSHARMA"
count = 0
for ch in s:
    if ch.isupper():
        count+=1
print("uppercase: ", count)

# count lowercase in string
s = "avaniSHARMA"
count = 0
for ch in s:
    if ch.islower():
        count+=1
print("lowercase: ", count)

# count digit in string 
s = "avaniSHARMA230324"
count = 0
for ch in s:
    if ch.isdigit():
        count+=1
print("digit: ", count)

# count space in string
s = "avani SHARMA"
count = 0
for ch in s:
    if ch == " ":
        count+=1
print("space: ", count)

# count special character
s = "avaniSHARMA@#$12"
count = 0
for ch in s:
    if not ch.isalnum():
        count+=1
print("special character: ", count)

# count total characters
s = "avaniSHARMA@#$12"
print("total character: ", len(s))

# count word in string
s = "avani SHARMA @#$12"
words = s.split()
print("word: ", len(words))