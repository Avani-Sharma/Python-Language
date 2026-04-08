# Print all numbers from 1 to 100, but use the continue statement to skip the numbers which are perfectly divisible by 3.

for i in range(1, 101):
    if i % 3 == 0:           
        continue              
    print(i, end=" ")
