
lakes = {
    "Tsho Rolpa": (20.0, 24.0,
                   [17.2, 17.5, 18.3, 19.0, 20.1, 22.0, 24.4, 25.0]),

    "Imja": (15.0, 18.0,
             [12.0, 12.1, 12.3, 12.2, 12.6, 13.0, 13.1, 13.3]),

    "Thulagi": (30.0, 33.0,
                [28.0, 28.9, 29.5, 30.2, 30.4, 30.1, 29.8, 29.6])
}

groups = {
    "Normal": [],
    "Watch": [],
    "Danger": []
}

for lake, data in lakes.items():

    warning, danger, readings = data

    # Calculate hourly rises
    rises = []

    for i in range(1, len(readings)):
        rise = readings[i] - readings[i - 1]
        rises.append(round(rise, 2))

    # Find lake status
    status = "Normal"
    status_hour = None

    for hour, level in enumerate(readings):

        if level >= danger:
            status = "Danger"
            status_hour = hour
            break

        elif level >= warning:
            status = "Watch"
            status_hour = hour

    # Check rapid rise
    rapid_count = 0
    rapid_rise = False

    for rise in rises:

        if rise > 0.5:
            rapid_count += 1
        else:
            rapid_count = 0

        if rapid_count >= 3:
            rapid_rise = True

    # Add lake to status group
    groups[status].append(lake)

    # Prepare status message
    if status_hour is not None:
        status_text = f"{status} (from hour {status_hour})"
    else:
        status_text = status

    if rapid_rise:
        status_text += " + RAPID RISE"

    # Print lake information
    print(
        f"{lake:<10} max {max(readings):.1f} m, "
        f"biggest rise {max(rises):.1f} m, "
        f"status {status_text}"
    )

# Print status groups
print(groups)

# Print evacuation message
if groups["Danger"]:
    print("EVACUATE downstream of:", ", ".join(groups["Danger"]))
