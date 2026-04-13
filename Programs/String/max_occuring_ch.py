s = "banana"
visited = ""
for ch in s:
    if ch not in visited:
        count = 0
        for i in s:
            if ch == i:
                count += 1
        print(ch, ":", count)
        visited += ch

# using dictionary
s = "this is"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)