# remove elements: use (.remove) method
s = {1,2,3,4,5}
s.remove(1)
print(s)


# remove elements: use (.discard) method 
# discard is used to remove particular element from the set if the element is present into the set, 
# then it will remove the element otherwise it will not give any error
s = {1,2,3,4,5}
result = s.discard(50)
print(result)


# pop method: remove randomly elements from the set and return that 
s = {10, 20, 30, 40}
removed = s.pop()   
print("Removed element:", removed)
print("Remaining set:", s)