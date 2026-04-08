s = 'silent'
s1 = 'listen'
is_anagram = True
for c in s:
    if c not in s1:
        is_anagram = False
if is_anagram:
    print("Anagram")
else:
    print("not an anagram")