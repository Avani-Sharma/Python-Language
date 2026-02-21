# seperate out even odd elements from the list print index
li = [1,2,3,4,5,6]
even_index = []
odd_index = []
for i in range(len(li)):
    if li[i] % 2 == 0:
        even_index.append(i)
    else:
        odd_index.append(i)
print("Even index:", even_index)
print("Odd index:", odd_index)

# seperate out even odd elements from the list 
li = [1,2,3,4,5,6]
even = []
odd= []
for num in li:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("even", even)
print("odd", odd)