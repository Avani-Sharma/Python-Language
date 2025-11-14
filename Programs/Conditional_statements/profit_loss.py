# Accept the cost price and selling price and print whether there is a profit or loss.

cp = float(input("enter cost price: "))
sp = float(input("enter selling price: "))
if sp>cp:
    print("profit")
elif sp<cp:
    print("loss")
else:
    print("no profit or no loss")