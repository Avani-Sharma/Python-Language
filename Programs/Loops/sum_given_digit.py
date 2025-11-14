# Print the sum of the digits of a number (e.g., if the number is 1234, the output should be 10).

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10      # Get the last digit
    sum = sum + digit     # Add it to sum
    num = num // 10       # Remove the last digit
print("Sum of digits:", sum)

# for loop
n = input()
sum=0
for digit in n:
    sum = sum+ int(digit)
print(sum)

# sum of all multiples of 7 between 1 to 100
sum =0
i =1 
while i<=100:
    if(i%7==0):
        sum = sum+i
    i+=1
print(sum)

# for loop
sum=0
for i in range(1, 100):
    if(i%7==0):
        sum = sum+i
print(sum)
