# check if string is pallindrome
n = "naman"
rev = n[::-1]     
if n == rev:
    print("palindrome")
else:
    print("not palindrome")

# find all pallindrome substring
s = "ababa"
for i in range(len(s)):
    for j in range(i+1, len(s)+1):   
        sub = s[i:j]
        if sub == sub[::-1]:
            print(sub)

# longest pallindrome substring
s = "abcbadxyxy"
longest = ""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub = s[i:j]
        if sub == sub[::-1] and len(sub) > len(longest):
            longest = sub
print("Longest palindrome:", longest)