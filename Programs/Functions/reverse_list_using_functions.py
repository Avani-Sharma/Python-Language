# write a program to reverse a list

def reverse_list(lst):
    rev_list = []
    for i in range(len(lst) - 1, -1, -1):
        rev_list.append(lst[i])
    return rev_list
nums = [1, 2, 3, 4, 5]
print(reverse_list(nums))
