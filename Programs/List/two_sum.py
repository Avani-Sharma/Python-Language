li = [3,2,4]
target = 6

arr = [(num, i) for i, num in enumerate(li)]
arr.sort()

left = 0
right = len(arr) - 1

while left < right:
    s = arr[left][0] + arr[right][0]

    if s == target:
        print([arr[left][1], arr[right][1]])
        break
    elif s < target:
        left += 1
    else:
        right -= 1