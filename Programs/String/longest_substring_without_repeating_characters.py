s = "abcabcd"
max_len = 0
for i in range(len(s)):
    seen = set()
    for j in range(i, len(s)):
        if s[j] in seen:
            break
        seen.add(s[j])
        max_len = max(max_len, j-i+1)
print(max_len)