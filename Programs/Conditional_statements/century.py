# Input a year and check whether it is a century year or not.

year = int(input("enter year: "))
if year%100==0:
    print("century year")
else:
    print("not a century year")