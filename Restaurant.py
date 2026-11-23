
# Restaurant Menu
menu = {
    1: ("Momo", 180),
    2: ("Chowmein", 150),
    3: ("Thakali Set", 450),
    4: ("Lassi", 120)
}

# Customer Orders
orders = [
    "1:2,4:2",
    "3:1,1:1,9:3",
    "2:3,1:2,4:1"
]

# Initialize variables
items_sold = {}
invalid_codes = []
day_collection = 0

# Process each table
for i, order in enumerate(orders, start=1):

    subtotal = 0

    # Separate food items
    items = order.split(",")

    # Process each food item
    for item in items:

        code, quantity = item.split(":")

        code = int(code)
        quantity = int(quantity)

        # Check invalid food code
        if code not in menu:
            invalid_codes.append(code)
            continue

        # Get food name and price
        name = menu[code][0]
        price = menu[code][1]

        # Calculate subtotal
        subtotal += price * quantity

        # Count sold items
        items_sold[name] = items_sold.get(name, 0) + quantity

    # Calculate service charge and VAT
    service = subtotal * 0.10
    vat = (subtotal + service) * 0.13

    bill = subtotal + service + vat

    # Update daily collection
    day_collection += bill

    print(f"Table {i}: subtotal Rs {subtotal}, "
          f"bill with service + VAT Rs {bill:.2f}")

# Find best seller
best_seller = max(items_sold, key=items_sold.get)

# Display final results
print("Items sold:", items_sold)
print("Best seller:", best_seller,
      "| Invalid codes:", invalid_codes)

print(f"Day's collection: Rs {day_collection:.2f}")
