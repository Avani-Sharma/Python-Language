# project
print("================ Product Price Analyzer ================")

print()

# ProductName, Price, Stock
products = (
    ("Laptop", 45000, 10),
    ("Phone", 15000, 25),
    ("Headphones", 1200, 50),
    ("Keyboard", 800, 30),
    ("Mouse", 500, 40)
)


print("Available Products (Name -> Price -> Stock):")
for p in products:
    print(p[0], "-> rs.", p[1], "-> Stock:", p[2])


# Most Expensive Product
max_price = products[0][1]
max_product = products[0][0]
for p in products:
    if p[1] > max_price:
        max_price = p[1]
        max_product = p[0]
print("Most Expensive Product:", max_product, "-> rs.", max_price)


# Cheapest Product
min_price = products[0][1]
min_product = products[0][0]
for p in products:
    if p[1] < min_price:
        min_price = p[1]
        min_product = p[0]
print("Cheapest Product:", min_product, "-> rs.", min_price)


# Average Price
total_price = 0
for p in products:
    total_price += p[1]
average_price = total_price / len(products)
print("Average Price: rs.", round(average_price, 2))


# Total Price
print("Total Price of All Products: rs.", total_price)

print()

# Search for a Product
search = input("Enter product name to search: ").title()
found = False
for p in products:
    if p[0] == search:
        print(search, "-> rs.", p[1], "-> Stock:", p[2])
        found = True
        break
if not found:
    print("Product not found!")