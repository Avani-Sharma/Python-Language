# Sort Values of First List Using Character Count
s = ['a', 'acdf', 'fg', 'ads']
for i in range(len(s)):
  for j in range(i+1, len(s)):
    if len(s[i]) > len(s[j]):
      s[i], s[j] = s[j], s[i]
print(s)