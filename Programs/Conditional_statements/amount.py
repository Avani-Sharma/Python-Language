# Write a Python program to compute the income tax payable by an individual based on their annual income using these rules: Income below Rs 2,50,000 - No tax; Rs 2.5-5 lakh - 5% tax; Rs 5-10 lakh - 20% tax; Above Rs 10 lakh - 30% tax. Display the calculated tax and final payable amount.


income = float(input("Enter your annual income (in Rs): "))
if income < 250000:
    tax = 0
    print("No tax")
elif 250000 <= income <= 500000:
    tax = 0.05 * income
    print("5% tax applied")
elif 500000 < income <= 1000000:
    tax = 0.20 * income
    print("20% tax applied")
else:
    tax = 0.30 * income
    print("30% tax applied")

final_amount = income - tax

print("Annual Income: Rs", income)
print("Calculated Tax: Rs", tax)
print("Amount after Tax: Rs", final_amount)

