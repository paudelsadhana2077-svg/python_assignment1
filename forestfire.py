
districts = [
    ("Chitwan", "Bagmati", 36, 18, 25, 40),
    ("Kaski", "Gandaki", 27, 55, 10, 5),
    ("Dang", "Lumbini", 33, 30, 35, 20),
    ("Bardiya", "Lumbini", 38, 15, 32, 35),
    ("Ilam", "Koshi", 24, 70, 8, 3),
    ("Makwanpur", "Bagmati", 31, 40, 18, 12)
]

# Create dictionary for risk levels
risk_groups = {
    "Low": [],
    "Moderate": [],
    "High": [],
    "Extreme": []
}

# Store provinces that need alerts
alert_provinces = set()

for district, province, temp, humidity, wind, rain_days in districts:

    score = 0

    # Temperature points
    if temp > 35:
        score += 3
    elif temp > 30:
        score += 2
    elif temp > 25:
        score += 1

    # Humidity points
    if humidity < 20:
        score += 3
    elif humidity < 35:
        score += 2
    elif humidity < 50:
        score += 1

    # Wind speed points
    if wind > 30:
        score += 2
    elif wind > 15:
        score += 1

    # Days since rain points
    if rain_days > 30:
        score += 3
    elif rain_days > 14:
        score += 2
    elif rain_days > 7:
        score += 1

    # Find risk level
    if score >= 9:
        risk = "Extreme"
    elif score >= 7:
        risk = "High"
    elif score >= 4:
        risk = "Moderate"
    else:
        risk = "Low"

    # Group district and score
    risk_groups[risk].append((district, score))

    # Collect provinces with High or Extreme risk
    if risk == "High" or risk == "Extreme":
        alert_provinces.add(province)

# Display results
for risk, district_list in risk_groups.items():
    print(f"{risk:<8}: {district_list}")

print("Provinces to alert:", sorted(alert_provinces))
