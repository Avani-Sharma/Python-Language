print("===================================== Student Grading and Attendance System ===================================")
print()

# Take input from user Student Basic Details: Name, Roll_Number, Marks-(0-100), Attendance_Percentage
Name = input("Enter Name: ")
Roll_Number = int(input("Enter Roll No.: "))
Attendance_Percentage = float(input("Enter Attendance Percentage(%): "))
print()

# Take marks of 5 Subjects: Computer_Architecture, HTML, Maths, Python, Cloud_Computing
Computer_Architecture = int(input("Enter marks of Computer Architecture: "))
HTML = int(input("Enter marks of HTML: "))
Maths = int(input("Enter marks of Maths: "))
Python = int(input("Enter marks of Python: "))
Cloud_Computing = int(input("Enter marks of Cloud Computing: "))
print()

# Calculate Total aur Average of marks
Total = Computer_Architecture + HTML + Maths + Python + Cloud_Computing
Average = Total/5

# Decide Grades: (90-100 → A+), (80-89 → A), (70-79 → B), (60-69 → C), (50-59 → D), (Marks<50 → F)
if Average >= 90:
    Grade = "A+"
elif Average >= 80:
    Grade = "A"
elif Average >= 70:
    Grade = "B"
elif Average >= 60:
    Grade = "C"
elif Average >= 50:
    Grade = "D"
else:
    Grade = "F"

# Check Attendance: (Attendance >= 75% → "Allowed to sit in exam"), (Attendance < 75% → "Not allowed to sit in exam")
if Attendance_Percentage>=75:
    attendance_status = "Allowed to sit in exam"
else: 
    attendance_status = "Not allowed to sit in exam"

# Step 6: Pass/Fail Remark
if Average >= 50 and Attendance_Percentage >= 75:
    remark = "PASS"
else:
    remark = "FAIL"
print()

# Print the Result: Student Name, Roll Number, Subject Marks, Total Marks, Average Marks, Grade and Attendance Status 
print("============================================ Student Report =================================================")
print("Name:                 ", Name)
print("Roll Number:          ", Roll_Number)
print()
print("-------------------------------------------------------------------------------------------------------------")
print("Marks - Computer Arch:", Computer_Architecture)
print("Marks - HTML:         ", HTML)
print("Marks - Maths:        ", Maths)
print("Marks - Python:       ", Python)
print("Marks - Cloud Comp.:  ", Cloud_Computing)
print()
print("-------------------------------------------------------------------------------------------------------------")
print("Total Marks:          ", Total)
print("Average Marks:        ", round(Average,2))
print("Grade:                ", Grade)
print("Attendance:           ", Attendance_Percentage, "% -", attendance_status)
print("Final Remark:         ", remark)
print("=============================================================================================================")