# Write a Python program that asks the user to input their age and whether they possess a valid ID card(Y/N). Based on these inputs, determine whether the person is eligible to vote. If the person is 18 or older and has a valid ID, print 'Eligible to Vote'. If they are 18 or older but do not have an ID, display 'Get your ID first'. Otherwise, print 'Not eligible to vote'. 


age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID card? (Y/N): ")
if age >= 18 and (has_id == 'Y' or has_id == 'y'):
    print("Eligible to Vote")
elif age >= 18 and (has_id == 'N' or has_id == 'n'):
    print("Get your ID first")
else:
    print("Not eligible to vote")
