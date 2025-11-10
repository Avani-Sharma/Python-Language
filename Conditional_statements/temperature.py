# Write a Python program that takes the temperature in Celsius as input and categorizes it as follows: above 38 degrees means 'High Fever', between 36 degrees and 38 degrees means 'Normal', and below 36 degrees means 'Below Normal'. Display the entered temperature and the result with an appropriate message.

temperature = float(input("Enter temperature in Celsius: "))
if temperature > 38:
    print("High Fever")
elif 36 <= temperature <= 38:
    print("Normal")
else:
    print("Below Normal")
print("Entered Temperature:", temperature, "°C")



# Accept a temperature in Celsius and print “Hot” if greater than 30, else “Cold”.
temp = float(input("enter temperature: "))
if temp>30:
    print("hot")
else:
    print("cold")