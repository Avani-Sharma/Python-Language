# Create a program that accepts marks in three subjects from the user. Calculate the average and based on the average marks, assign grades as follows: above 90 - Excellent, 75-90 - Good, 60-74 - Average, below 60 - Fail. Display both the average and the grade.



a = int(input("Enter marks in subject 1: "))
b = int(input("Enter marks in subject 2: "))
c = int(input("Enter marks in subject 3: "))
avg = (a + b + c) / 3
if avg > 90:
    grade = "Excellent"
elif avg >= 75 and avg <= 90:
    grade = "Good"
elif avg >= 60 and avg < 75:
    grade = "Average"
else:
    grade = "Fail"
print("Average marks:", avg)
print("Grade:", grade)
