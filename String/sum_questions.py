# sum of digit in string
s = "a1b2c3"
sum_digit = 0
for ch in s:
    if ch.isdigit():
        sum_digit += int(ch)
print("Sum of digits:", sum_digit)

# sum of numbers present in string
s = "a12b5c100"
sum_num = 0
temp = ""
for ch in s:
    if ch.isdigit():
        temp += ch
    else:
        if temp != "":
            sum_num += int(temp)
            temp = ""
# last number add
if temp != "":
    sum_num += int(temp)
print("Sum of numbers:", sum_num)