
# Cricket ball-by-ball data
balls = "1 4 . W 6 wd 2 1 . 4 nb 1 . . W 6 1 lb2"

# Convert string into list
ball_list = balls.split()

# Initialize variables
score = 0
wickets = 0
extras = 0
fours = 0
sixes = 0
dot_balls = 0
legal_balls = 0

# Process every ball
for ball in ball_list:

    if ball == "W":
        wickets += 1
        legal_balls += 1

    elif ball == ".":
        dot_balls += 1
        legal_balls += 1

    elif ball == "wd":
        score += 1
        extras += 1
        continue

    elif ball == "nb":
        score += 1
        extras += 1
        continue

    elif ball == "lb2":
        score += 2
        extras += 2
        legal_balls += 1

    else:
        runs = int(ball)
        score += runs
        legal_balls += 1

        if runs == 4:
            fours += 1

        elif runs == 6:
            sixes += 1

# Calculate overs
overs = legal_balls // 6
remaining = legal_balls % 6

# Calculate run rate
run_rate = score / legal_balls * 6

# Calculate boundary runs
boundary_runs = (fours * 4) + (sixes * 6)

# Calculate boundary percentage
boundary_percentage = boundary_runs / score * 100

# Display output
print(f"Score: {score}/{wickets} in {overs}.{remaining} overs")

print(f"Extras {extras}, Fours {fours}, "
      f"Sixes {sixes}, Dot balls {dot_balls}")

print(f"Run rate {run_rate:.2f}, "
      f"Boundary runs {boundary_runs} "
      f"({boundary_percentage:.1f}% of total)")
