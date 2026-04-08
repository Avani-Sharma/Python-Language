# rotate a list left by one position
li = [1,2,3,4,5]
k = 1
left = 0
right = k-1
while left < right:
  li[left], li[right] = li[right], li[left]
  left +=1
  right -=1

left = k
right = len(li)- 1
while left < right:
  li[left], li[right] = li[right], li[left]
  left +=1
  right -=1

left = 0
right = len(li)- 1
while left < right:
  li[left], li[right] = li[right], li[left]
  left +=1
  right -=1
print(li)