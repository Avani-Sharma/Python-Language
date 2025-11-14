# Accept age from the user and check if the person is eligible to vote or not (age ≥ 18).


age = int(input("enter age: "))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")