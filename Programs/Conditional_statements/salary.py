# Accept salary and years of service as inputs. Use conditional statements to calculate the bonus. If the years of service are more than 10, the employee gets a 10% bonus. If it lies between 6 and 10, the bonus is 8%. If less than 6, the bonus is 5%. Print the final salary after adding the bonus.


salary = float(input("Enter your salary: "))
years = int(input("Enter years of service: "))
if years > 10:
    bonus = salary * 0.10
elif 6 <= years <= 10:
    bonus = salary * 0.08
else:
    bonus = salary * 0.05

final_salary = salary + bonus
print("Bonus Amount: Rs", bonus)
print("Final Salary after adding bonus: Rs", final_salary)
