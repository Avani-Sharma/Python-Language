# Write a program that accepts a student's attendance percentage. If attendance is below 75, print 'Not eligible for exam.' If between 75 and 85, print 'Eligible but needs improvement.' If above 85, print 'Excellent attendance.' Show the exact percentage and decision clearly.


attendance = float(input("Enter your attendance percentage: "))
if attendance > 85:
    print("Attendance:", attendance, "% - Excellent attendance.")
elif 75 <= attendance <= 85:
    print("Attendance:", attendance, "% - Eligible but needs improvement.")
else:
    print("Attendance:", attendance, "% - Not eligible for exam.")
