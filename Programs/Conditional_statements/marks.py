# Accept marks in three subjects from the user. Use if-elif statements to determine whether the student has passed or failed. The student passes if all marks are 35 or above. If all marks are above 80, print 'Distinction'. Display each subject mark along with the result.



subject_1 = int(input("Enter marks in Subject 1: "))
subject_2 = int(input("Enter marks in Subject 2: "))
subject_3 = int(input("Enter marks in Subject 3: "))
print("Subject 1:", subject_1)
print("Subject 2:", subject_2)
print("Subject 3:", subject_3)
if subject_1 > 80 and subject_2 > 80 and subject_3 > 80:
    print("Result: Distinction")
elif subject_1 >= 35 and subject_2 >= 35 and subject_3 >= 35:
    print("Result: Passed")
else:
    print("Result: Failed")
