sentence = "python is easy and python is powerful"
words = sentence.split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)
