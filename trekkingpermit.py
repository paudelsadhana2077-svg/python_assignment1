
fees = {
    "Everest": {"Nepali": 100, "SAARC": 1500, "Foreign": 3000},
    "Annapurna": {"Nepali": 100, "SAARC": 1000, "Foreign": 3000},
    "Langtang": {"Nepali": 100, "SAARC": 1500, "Foreign": 3000}
}

visitors = [
    ("Aarav", "Nepali", 22, "Everest"),
    ("Emma", "Foreign", 34, "Annapurna"),
    ("Rahul", "SAARC", 8, "Langtang"),
    ("John", "Foreign", 65, "Everest"),
    ("Mina", "Nepali", 30, "Annapurna"),
    ("Li", "Foreign", 28, "Everest")
]

# Initialize variables
revenue = {"Everest": 0, "Annapurna": 0, "Langtang": 0}
categories = set()
area_count = {}
total_revenue = 0

# Process visitors
for name, category, age, area in visitors:

    # Calculate permit fee
    if age < 10:
        fee = 0
    elif age >= 60:
        fee = fees[area][category] // 2
    else:
        fee = fees[area][category]

    # Update records
    revenue[area] += fee
    total_revenue += fee
    categories.add(category)
    area_count[area] = area_count.get(area, 0) + 1

    print(f"{name:<6} {area:<10} Rs {fee:>7}")

# Find busiest area
busiest = max(area_count, key=area_count.get)

# Display results
print("Revenue by area:", revenue)
print("Busiest area:", busiest,
      f"({area_count[busiest]} visitors)")
print("Visitor categories:", sorted(categories))
print("Total revenue: Rs", total_revenue)
