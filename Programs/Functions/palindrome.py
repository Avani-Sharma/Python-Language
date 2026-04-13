def is_palindrome(s):
    s = str(s).lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome("Racecar"))
print(is_palindrome(121))
print(is_palindrome(123))

# 100-200 palindrome number using functions 
def is_palindrome(s):
    s = str(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
for i in range(100, 201):
    if is_palindrome(i):
        print(i)

# 100-200 palindrome number two pointer approach
for i in range(100, 201):
    s = str(i)
    left = 0
    right = len(s) - 1
    is_pal = True
    while left < right:
        if s[left] != s[right]:
            is_pal = False
            break
        left += 1
        right -= 1
    if is_pal:
        print(i)