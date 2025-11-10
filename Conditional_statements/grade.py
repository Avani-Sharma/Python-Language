# Take the percentage and print grades:
# 80–100 → A
# 60–79 → B
# 40–59 → C
# Below 40 → Fail

percentage = int(input("enter percentage: "))
if 80<= percentage <=100:
    print("grade A")
elif 60 <= percentage <= 79:
    print("grade B")
elif 40 <= percentage <=59:
    print("grade C")
else:
    print("fail")