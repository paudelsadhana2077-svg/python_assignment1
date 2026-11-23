
meters = {
    "H-101": [1200, 1265, 1340, 1520, 1590],
    "H-102": [880, 910, 945, 975, 1010],
    "H-103": [2300, 2420, 2470, 2530, 2700]
}

slabs = [
    (20, 4),
    (30, 7),
    (50, 9),
    (float("inf"), 11)
]

total_revenue = 0
spikes = []

for household, readings in meters.items():

    # Calculate monthly consumption
    monthly_units = []

    for i in range(1, len(readings)):
        units = readings[i] - readings[i - 1]
        monthly_units.append(units)

    # Calculate average consumption
    average = sum(monthly_units) / len(monthly_units)

    # Calculate latest month's bill
    units = monthly_units[-1]
    bill = 0

    for slab_units, rate in slabs:

        if units <= 0:
            break

        used = min(units, slab_units)

        bill += used * rate
        units -= used

    total_revenue += bill

    # Print household information
    print(
        f"{household}: monthly units {monthly_units}, "
        f"avg {average}, latest bill Rs {bill}"
    )

    # Find consumption spikes
    for i in range(1, len(monthly_units)):

        previous = monthly_units[i - 1]
        current = monthly_units[i]

        if current > previous * 1.5:
            spikes.append(
                (household, i + 1, previous, current)
            )

# Display consumption spikes
print("Spikes (>50% jump):")

for household, month, previous, current in spikes:
    print(
        f"  {household} month {month}: "
        f"{previous} -> {current} units"
    )

# Display total revenue
print("Total latest-month revenue: Rs", total_revenue)
