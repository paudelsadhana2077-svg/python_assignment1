
matches = [
    ("W", 10, 1, 5, "Layla"),
    ("W", 3, 2, 4, "Tigreal"),
    ("L", 2, 6, 3, "Layla"),
    ("W", 8, 0, 6, "Gusion"),
    ("W", 5, 2, 9, "Layla"),
    ("W", 1, 3, 12, "Tigreal"),
    ("L", 4, 5, 2, "Gusion"),
    ("W", 7, 2, 8, "Layla")
]

total_matches = len(matches)
wins = 0

current_streak = 0
longest_streak = 0

hero_kda = {}

for result, kills, deaths, assists, hero in matches:

    # Calculate wins and winning streak
    if result == "W":
        wins += 1
        current_streak += 1

        if current_streak > longest_streak:
            longest_streak = current_streak

    else:
        current_streak = 0

    # Avoid division by zero
    if deaths == 0:
        deaths = 1

    # Calculate KDA
    kda = (kills + assists) / deaths

    # Store KDA for each hero
    if hero not in hero_kda:
        hero_kda[hero] = []

    hero_kda[hero].append(kda)

# Calculate win rate
win_rate = (wins / total_matches) * 100

print("Win rate:", round(win_rate, 1), "%")
print("Longest win streak:", longest_streak)

# Display hero games and average KDA
print("\nHero Statistics:")

for hero, kdas in hero_kda.items():
    games = len(kdas)
    average_kda = sum(kdas) / games

    print(hero, "- Games:", games,
          "Average KDA:", round(average_kda, 2))

# Find most-played hero
most_played = max(hero_kda, key=lambda hero: len(hero_kda[hero]))

print("\nMost played hero:", most_played)
