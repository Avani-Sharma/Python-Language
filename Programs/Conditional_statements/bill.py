# Develop a Python program to calculate an electricity bill. Take the number of units consumed as input. For up to 100 units: Rs 5/unit; For 101-300 units: Rs 7/unit; Above 300 units: Rs 10/unit. Display the total payable bill along with a proper message.

unit = int(input("Enter number of units consumed: "))
if unit <= 100:
    bill = unit * 5
elif 101 <= unit <= 300:
    bill = unit * 7
else:
    bill = unit * 10

print("Units consumed:", unit)
print("Total bill amount: Rs", bill)
