# Write a program that asks the user to input three sides of a triangle. Use conditional statements to check if the triangle is valid (sum of any two sides must be greater than the third). Print whether the triangle is valid or not.


side_1 = int(input("enter side_1: "))
side_2 = int(input("enter side_2: "))
side_3 = int(input("enter side_3: "))
if (side_1 + side_2 >side_3) and (side_2 + side_3 >side_1) and (side_1 + side_3>side_2):
    print("triangle is valid")
else:
    print("triangle is not valid")