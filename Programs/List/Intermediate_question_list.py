# 1. Rotate a List Left by One Position: The first element moves to the end.
li = [10,20,30,40,50]
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
print("A: ", li)

# 2. Find Index of All Occurrences of a Given Element: all index positions where the target element occurs.
nums = [5, 2, 7, 2, 9, 2]
target = 2
indexes = []
for i in range(len(nums)):
    if nums[i] == target:
        indexes.append(i)
print("B: ", indexes)

# 3. Remove All Negative Numbers from a List: Remove all negative numbers and return the updated list.
nums = [5, 2, 7, 2, 9, 2]
target = 2
indexes = []
for i in range(len(nums)):
    if nums[i] == target:
        indexes.append(i)
print("C: ", indexes)

# 4. Check Whether a List is Palindrome: Check whether the list reads the same forward and backward.
nums = [3, -1, 5, -7, 8, -2]
result = []
for num in nums:
    if num >= 0:
        result.append(num)
print("D: ", result)

# 5. Merge Two Lists and Remove Duplicates: Merge two lists into one and remove duplicate elements.
list1 = [1, 2, 3]
list2 = [3, 4, 5]
merged = list1 + list2
result = list(set(merged))
result.sort()
print("E: ", result)

# 6. Find Pairs Whose Sum Equals Target Value: all pairs of elements whose sum equals the target value.
nums = [2, 4, 3, 5, 7]
target = 7
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print("F: ", (nums[i], nums[j]))

# 7. Find Missing Number from 1 to n: list contains numbers from 1 to n with one number missing. 
nums = [1, 2, 4, 5, 6]
n = len(nums) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)
print("G: ", expected_sum - actual_sum)

# 8. Remove elements that occur more than once and keep only unique elements.
nums = [1, 2, 2, 3, 4, 4, 5]
result = []
for num in nums:
    if nums.count(num) == 1:
        result.append(num)
print("H: ", result)