# Shopping Bill Generator with Quantity and GST

def add_items():
    items = []
    prices = []
    quantities = []

    n = int(input("Enter number of items: "))

    for i in range(n):
        item = input(f"\nEnter item {i+1} name: ")
        price = float(input(f"Enter price of {item}: "))
        qty = int(input(f"Enter quantity of {item}: "))

        items.append(item)
        prices.append(price)
        quantities.append(qty)

    return items, prices, quantities


def calculate_total(prices, quantities):
    total = 0
    for i in range(len(prices)):
        total += prices[i] * quantities[i]
    return total


def apply_discount(total):
    if total >= 5000:
        return total * 0.20
    elif total >= 2000:
        return total * 0.10
    else:
        return 0

# 18% GST
def calculate_gst(amount):
    gst_rate = 0.18   
    return amount * gst_rate


def print_bill(items, prices, quantities, total, discount, gst):
    print("-------------- SHOPPING BILL -------------")
    print("Item\tPrice\tQty\tTotal")

    for i in range(len(items)):
        item_total = prices[i] * quantities[i]
        print(f"{items[i]}\t{prices[i]}\t{quantities[i]}\t{item_total}")

    print("---------------------------------")

    print("Total Amount     : ₹", total)
    print("Discount         : ₹", discount)
    print("Amount After Disc: ₹", total - discount)
    print("GST (18%)        : ₹", gst)

    print("---------------------------------")

    print("Final Payable    : ₹", (total - discount) + gst)

    print("---------------------------------")

    print(" Thank you for shopping!")

items, prices, quantities = add_items()
total = calculate_total(prices, quantities)
discount = apply_discount(total)
gst = calculate_gst(total - discount)
print_bill(items, prices, quantities, total, discount, gst)