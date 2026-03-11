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
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
        
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
aged = input()
# 8. Write a program using nested if to check whether a number is greater than
# 50, and if yes, check whether it is also greater than 100.
# 9. Write a program using if-elif-else to check whether a number is positive,
# negative, or zero.
# 10. Write a program using elif to assign grades based on marks:
# A (90–100), B (80–89), C (70–79), D (60–69), F (below 60).
# 11. Write a program using elif to check whether a given day number (1–7)
# corresponds to Monday–Sunday.
# 12. Write a program using elif to find the largest among three numbers.
# 13. Write a program using elif to check whether a year is a leap year or not.
# 14. Write a program using elif to classify a person’s age group: Child, Teen, Adult, or
# Senior.
# 15. Write a program using elif to check whether a character is a vowel, consonant,
# digit, or special character.
# 16. Write a program using elif to build a simple calculator for +, -, *, and /.
# 17. Write a program using elif to check whether a number is divisible by 2, 3, 5, or
# none of them.
# 18. Write a program using elif to convert a numeric month value (1–12) into the month
# name.
# 19. Write a program using elif to check the type of triangle: Equilateral, Isosceles, or
# Scalene.
# 20. Write a program using elif to determine the season based on month number.
# 21. Write a program using elif to calculate electricity bill based on unit ranges.

# 22. Write a program using elif to check whether a number is one-digit, two-digit,
# three-digit, or more.
# 23. Write a program using elif to check the result of a student: Distinction, First
# Class, Second Class, Pass, or Fail.
# 24. Write a program using elif to convert percentage into grade category.
# 25. Write a program using elif to check traffic light action based on color input.
# 26. Write a program using elif to classify temperature as Cold, Moderate, or Hot.
# 27. Write a program using elif to check whether a number is prime, composite, or
# neither.
# 28. Write a program using elif to check the type of input number: zero, positive even,
# positive odd, or negative.