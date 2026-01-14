dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"d": 40, "e": 50}

merged = {}

for k, v in dict1.items():
    merged[k] = v

for k, v in dict2.items():
    merged[k] = v

print("Merged Dictionary:", merged)
