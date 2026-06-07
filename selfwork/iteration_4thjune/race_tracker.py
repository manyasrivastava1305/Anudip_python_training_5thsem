#Program for Race Leader Tracker
# Input number of racers
n = int(input("Enter number of racers: "))

# Input lap time of first racer
lap_time = float(input("Enter lap time of Racer 1: "))

# Assume first racer is both fastest and slowest initially
fastest_time = lap_time
slowest_time = lap_time

fastest_position = 1
slowest_position = 1

# Input remaining racers' lap times
for i in range(2, n + 1):
    lap_time = float(input(f"Enter lap time of Racer {i}: "))

    # Check for fastest racer
    if lap_time < fastest_time:
        fastest_time = lap_time
        fastest_position = i

    # Check for slowest racer
    if lap_time > slowest_time:
        slowest_time = lap_time
        slowest_position = i

# Calculate difference
difference = slowest_time - fastest_time

# Display results
print("\n----- Race Result -----")
print("Fastest Racer Position :", fastest_position)
print("Slowest Racer Position :", slowest_position)
print("Time Difference        :", difference)
