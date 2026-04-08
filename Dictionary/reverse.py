data = {"a": 1, "b": 2, "c": 3}
rev = {}

for k, v in data.items():
    rev[v] = k

print(rev)
