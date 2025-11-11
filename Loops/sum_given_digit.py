# Print the sum of the digits of a number (e.g., if the number is 1234, the output should be 10).

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10      # Get the last digit
    sum = sum + digit     # Add it to sum
    num = num // 10       # Remove the last digit
print("Sum of digits:", sum)


