# 1. Write a program using nested if to check whether a number is positive,
# negative, or zero, and if positive, also check whether it is even or odd.
n = int(input())
if n>0: 
    if n%2==0:
        print("even")
    else:
        print("odd")
elif n<0:
    print("negative")
else:
    print("zero")

# 2. Write a program using nested if to find the greatest among three numbers.
a, b, c = map(int, input().split())
if a > b:
    if a > c:
        print("Greatest number is:", a)
    else:
        print("Greatest number is:", c)
else:
    if b > c:
        print("Greatest number is:", b)
    else:
        print("Greatest number is:", c)
        
# 3. Write a program using nested if to check whether a student has passed or
# failed, and if passed, assign a grade based on marks.
marks = int(input())
if marks>=50:
    print("passed")
    if marks>=90:
        print("grade A")
    elif marks>=70:
        print("grade B")
    elif marks>=50:
        print("grade c")
else:
    print("failed")

# 4. Write a program using nested if to check whether a person is eligible to
# vote, and if eligible, check whether they are a first-time voter.
age = int(input())
if age>=18:
    print("elgibile to vote")
    if age==18:
        print("first-time voter")
    else:
        print("not a first-time voter")
else:
    print("not eligible")

# 5. Write a program using nested if to check whether a number is divisible by 5
# and if yes, check whether it is also divisible by 10.
num = int(input())
if num%5==0:
    print("divisible by 5")
    if num%10==0:
        print("also divisible by 10")
    else:
        print("but not divisible by 10")
else:
    print("not divisible by 5")

# 6. Write a program using nested if to check whether a character is an
# alphabet, and if it is an alphabet, check whether it is a vowel or consonant.
ch = input()
if 'a'<=ch<='z' or 'A'<=ch<='Z':
    print("alphabet")
    if ch in 'aeiouAEIOU':
        print("vowel")
    else:
        print("consonant")
else:
    print("not alphabet")

# 7. Write a program using nested if to check whether a person is eligible for a
# job based on age, and if eligible, check whether they have the required qualification.
age_job = int(input())
if age_job>=21:
    print("eligible for job")
    qualification = input("yes/no: ")
    if qualification == 'yes':
        print("have required qualification")
    else:
        print("not have required qualification")
else:
    print("not eligible for job")

# 8. Write a program using nested if to check whether a number is greater than 50, and if yes,
#  check whether it is also greater than 100.
nums = int(input())
if nums>50:
    print("greater than 50")
    if nums>100:
        print("also greater than 100")
    else:
        print("but not greater than 100")
else:
    print("not greater than 50")

# 9. Write a program using if-elif-else to check whether a number is positive,
# negative, or zero.
numb = int(input())
if numb>0:
    print("positive")
elif numb<0:
    print("negative")
else:
    print("zero")

# 10. Write a program using elif to assign grades based on marks:
# A (90–100), B (80–89), C (70–79), D (60–69), F (below 60).
mark = int(input())
if 90<=mark<=100:
    print("A")
elif 80<=mark<=89:
    print("B")
elif 70<=mark<=79:
    print("C")
elif 60<=mark<=69:
    print("D")
elif marks<60:
    print("F")
else:
    print("invalid marks")

# 11. Write a program using elif to check whether a given day number (1–7)
# corresponds to Monday–Sunday.
day_num = int(input())
if day_num == 1:
    print("monday")
elif day_num == 2:
    print("tuesday")
elif day_num == 3:
    print("wednesday")
elif day_num == 4:
    print("thursday")
elif day_num == 5:
    print("friday")
elif day_num == 6:
    print("saturday")
elif day_num == 7:
    print("sunday")
else:
    print("invalid num")

# 12. Write a program using elif to find the largest among three numbers.
d,e, f= map(int, input().split())
if d>e and d>f:
    print("d is greater")
elif e>d and e>f:
    print("e is greater")
else:
    print("f is greater")

# 13. Write a program using elif to check whether a year is a leap year or not.
year = int(input())
if year%4==0:
    print("leap year")
elif year%100 ==0:
    print("not a leap year")
elif year%400 == 0:
    print("leap year")
else:
    print("not a leap year")

# 14. Write a program using elif to classify a person’s age group: Child, Teen, Adult, or
# Senior.
person_age = int(input())
if person_age<=10:
    print("child")
elif 11<=person_age <=18:
    print("teen")
elif 17<=person_age<=21:
    print("adult")
else:
    print("senior")

# 15. Check whether a character is vowel, consonant, digit, or special character
ch = input("Enter character: ")
if ch.isalpha():
    if ch in "aeiouAEIOU":
        print("vowel")
    else:
        print("consonant")
elif ch.isdigit():
    print("digit")
else:
    print("special character")


# 16. Simple calculator
a = int(input("first number: "))
b = int(input("second number: "))
op = input("operator (+,-,*,/): ")
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("invalid operator")


# 17. Check divisibility by 2, 3, 5
num = int(input("Enter number: "))
if num % 2 == 0:
    print("divisible by 2")
elif num % 3 == 0:
    print("divisible by 3")
elif num % 5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 2,3,5")

# 18. Month number to month name
month = int(input("Enter month number: "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("invalid month")


# 19. Type of triangle
a, b, c = map(int, input("Enter three sides: ").split())
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


# 20. Season based on month
m = int(input("Enter month number: "))
if m in [12, 1, 2]:
    print("Winter")
elif m in [3, 4, 5]:
    print("Spring")
elif m in [6, 7, 8]:
    print("Summer")
elif m in [9, 10, 11]:
    print("Autumn")
else:
    print("invalid month")


# 21. Electricity bill calculation
units = int(input("Enter units: "))
if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = units * 2
elif units <= 300:
    bill = units * 3
else:
    bill = units * 5

print("Electricity bill:", bill)


# 22. Check digit length
num = int(input("Enter number: "))
n = abs(num)
if n < 10:
    print("one digit")
elif n < 100:
    print("two digit")
elif n < 1000:
    print("three digit")
else:
    print("more than three digit")


# 23. Student result
marks = int(input("Enter marks: "))
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 50:
    print("Second Class")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")


# 24. Percentage to grade
p = int(input("Enter percentage: "))
if p >= 90:
    print("Grade A")
elif p >= 80:
    print("Grade B")
elif p >= 70:
    print("Grade C")
elif p >= 60:
    print("Grade D")
else:
    print("Grade F")


# 25. Traffic light
color = input("Enter traffic light color: ")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready")
elif color == "green":
    print("Go")
else:
    print("invalid color")


# 26. Temperature classification
temp = int(input("Enter temperature: "))
if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Moderate")
else:
    print("Hot")


# 27. Prime, composite, or neither
n = int(input("Enter number: "))
if n < 2:
    print("Neither prime nor composite")
else:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("Prime")
    else:
        print("Composite")


# 28. Number type
num = int(input("Enter number: "))
if num == 0:
    print("zero")
elif num > 0 and num % 2 == 0:
    print("positive even")
elif num > 0 and num % 2 != 0:
    print("positive odd")
else:
    print("negative")