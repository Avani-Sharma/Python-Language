# count the frequency of words in a sentence
s = "I am Avani. I am from Bhiwadi"
d = {}
li = s.split()
for i in li:
  if i  in d:
    d[i] += 1
  else:
    d[i] =1
print(d)