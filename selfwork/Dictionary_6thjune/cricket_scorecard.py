# Cricket Scoreboard Analysis 
"""
Sample Data scores = {     
"Virat": 78,     
"Rohit": 112,     
"Gill": 45,     
"Rahul": 89,     
"Hardik": 32,     
"Jadeja": 61,     
"Surya": 105,     
"Pant": 95,     
"Bumrah": 18,     
"Shami": 25 
} 
Tasks 
• Display players who scored 50 or more runs.  
• Count the number of centuries.  
• Find the player with the highest score.  
• Create a list of players scoring below 30 runs.  
• Determine how many players scored between 50 and 99. 
"""

# Cricket Scoreboard Analysis

scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# Task 1: Display players who scored 50 or more runs
print("Task 1: Players who scored 50 or more runs")

for player, score in scores.items():
    if score >= 50:
        print(player, ":", score)

# Task 2: Count the number of centuries
century_count = 0

for score in scores.values():
    if score >= 100:
        century_count += 1

print("\nTask 2: Number of centuries =", century_count)

# Task 3: Find the player with the highest score
highest_scorer = max(scores, key=scores.get)

print("\nTask 3: Player with the highest score")
print(highest_scorer, ":", scores[highest_scorer])

# Task 4: Create a list of players scoring below 30 runs
below_30 = []

for player, score in scores.items():
    if score < 30:
        below_30.append(player)

print("\nTask 4: Players scoring below 30 runs")
print(below_30)

# Task 5: Determine how many players scored between 50 and 99
count_50_99 = 0

for score in scores.values():
    if 50 <= score <= 99:
        count_50_99 += 1

print("\nTask 5: Players scoring between 50 and 99 =", count_50_99)
