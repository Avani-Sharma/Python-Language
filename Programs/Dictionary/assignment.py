# 1. Count Character Frequency: Write a function that takes a string and returns a dictionary
# where the key is the character and the value is the number of times that character appears.
# Example: Input 'banana' → Output {'b':1, 'a':3, 'n':2}.
s = "avani sharma"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

# 2. Merge Two Dictionaries with Sum: Given two dictionaries containing integer values, merge
# them. If a key appears in both dictionaries, add their values. Example: d1={'a':10,'b':20},
# d2={'b':5,'c':15} → Output {'a':10,'b':25,'c':15}.
d1 = {'a':10,'b':20}
d2 = {'b':5,'c':15}
d3 = {}
for key, value in d1.items():
    d3[key] = value
for key, value in d2.items():
    if key in d3:
        d3[key] += value
    else:
        d3[key] = value
print(d3)

# 3. Group Words by First Letter: Given a list of words, create a dictionary where the key is the
# first letter and the value is the list of words starting with that letter. Example:
# ['apple','ant','banana','ball'] → {'a':['apple','ant'], 'b':['banana','ball']}.
li = ['apple', 'ant', 'banana', 'ball']
d = {}
for word in li:
    first = word[0]
    if first  in d:
        d[first].append(word)
    else:
        d[first] = [word]
print(d)

# 4. Group Numbers by Even and Odd: Given a list of numbers, create a dictionary with keys
# 'even' and 'odd' and store numbers accordingly. Example: [1,2,3,4,5] →
# {'odd':[1,3,5],'even':[2,4]}.
li = [1,2,3,4,5]
d = {'even':[], 'odd':[]}
for num in li:
    if num % 2 == 0:
        d['even'].append(num)
    else:
        d['odd'].append(num)
print(d)

# 5. Check if All Values are Unique: Write a code that checks if all values in a dictionary are
# unique. Example: {'a':1,'b':2,'c':3} → True, {'a':1,'b':2,'c':1} → False.
d = {'a':1,'b':2,'c':3}
d1 = []
unique = True
for v in d.values():
    if v in d1:
        unique = False
        break
    d1.append(v)
print(unique)

# 6. Valid Parenthesis: Given a string containing brackets (), {}, [], determine if the string is valid.
# A string is valid if every opening bracket has a corresponding closing bracket of the same type
# and in the correct order.
