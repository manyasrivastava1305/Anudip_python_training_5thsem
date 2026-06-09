# Store statistics of at least 30 cricket players. 
# Example Structure 
# players = { 
#     "Virat": { 
#         "runs": 645, 
#         "matches": 12, 
#         "wickets": 0 
#     } 
# } 
# Requirements 
# 1. Display all player statistics.  
# 2. Find highest run scorer.  
# 3. Find lowest run scorer.  
# 4. Calculate average runs.  
# 5. Find player with maximum wickets.  
# 6. Find all-rounders (runs > 300 and wickets > 5).  
# 7. Display players scoring above average.  
# 8. Create categories:  
# o Star Performer  
# o Good Performer  
# o Average Performer  
# o Poor Performer  
# 9. Generate team statistics.  
# 10. Display top 5 batsmen.  
# 11. Display top 5 bowlers.  
# 12. Create a separate dictionary for award winners. 
# ==============================================================================
# CRICKET PLAYER PERFORMANCE ANALYSIS SYSTEM
# Developed using Basic Python Core Constructs (Loops, Conditionals, and Dictionaries)
# ==============================================================================

# 1. Store statistics of at least 30 cricket players in a nested dictionary.
players = {
    "Virat": {"runs": 645, "matches": 12, "wickets": 0},
    "Rohit": {"runs": 550, "matches": 10, "wickets": 0},
    "Jadeja": {"runs": 320, "matches": 15, "wickets": 20},
    "Rahul": {"runs": 410, "matches": 11, "wickets": 0},
    "Hardik": {"runs": 305, "matches": 13, "wickets": 12},
    "Bumrah": {"runs": 45, "matches": 14, "wickets": 28},
    "Shami": {"runs": 25, "matches": 12, "wickets": 24},
    "Ashwin": {"runs": 180, "matches": 10, "wickets": 18},
    "Gill": {"runs": 520, "matches": 12, "wickets": 0},
    "Iyer": {"runs": 460, "matches": 11, "wickets": 0},
    "Pant": {"runs": 390, "matches": 9, "wickets": 0},
    "Axar": {"runs": 210, "matches": 14, "wickets": 15},
    "Siraj": {"runs": 15, "matches": 13, "wickets": 19},
    "Kuldeep": {"runs": 35, "matches": 11, "wickets": 21},
    "Sky": {"runs": 480, "matches": 10, "wickets": 1},
    "Jaiswal": {"runs": 610, "matches": 12, "wickets": 0},
    "Rinku": {"runs": 290, "matches": 8, "wickets": 0},
    "Dube": {"runs": 240, "matches": 9, "wickets": 4},
    "Sundar": {"runs": 130, "matches": 7, "wickets": 8},
    "Chahal": {"runs": 8, "matches": 8, "wickets": 14},
    "Arshdeep": {"runs": 12, "matches": 12, "wickets": 17},
    "Bishnoi": {"runs": 5, "matches": 6, "wickets": 9},
    "Ruturaj": {"runs": 340, "matches": 8, "wickets": 0},
    "Ishan": {"runs": 280, "matches": 9, "wickets": 0},
    "Samson": {"runs": 315, "matches": 7, "wickets": 0},
    "Thakur": {"runs": 110, "matches": 10, "wickets": 11},
    "Krishna": {"runs": 4, "matches": 5, "wickets": 6},
    "Mukesh": {"runs": 9, "matches": 7, "wickets": 8},
    "Deepak": {"runs": 75, "matches": 6, "wickets": 7},
    "Avesh": {"runs": 11, "matches": 6, "wickets": 8}
}

# Displaying all player statistics
print("All Player Statistics:")
for player_name, stats in players.items():
    print(f"Name: {player_name}, Runs: {stats['runs']}, Matches: {stats['matches']}, Wickets: {stats['wickets']}")


# 2. Find highest run scorer.
highest_run_scorer = None
highest_runs = -1  # Starting with an impossibly low score to ensure replacement

for player_name, stats in players.items():
    if stats['runs'] > highest_runs:
        highest_runs = stats['runs']
        highest_run_scorer = player_name

print(f"\nHighest Run Scorer: {highest_run_scorer} with {highest_runs} runs")


# 3. Find lowest run scorer.
lowest_run_scorer = None
lowest_runs = float('inf')  # Starting with infinity so any player's runs will be lower

for player_name, stats in players.items():
    if stats['runs'] < lowest_runs:
        lowest_runs = stats['runs']
        lowest_run_scorer = player_name

print(f"Lowest Run Scorer: {lowest_run_scorer} with {lowest_runs} runs")


# 4. Calculate average runs.
total_runs = 0
for player_name, stats in players.items():
    total_runs += stats['runs']

average_runs = total_runs / len(players)
print(f"\nAverage Runs scored per player: {average_runs:.2f}")


# 5. Find player with maximum wickets.
max_wicket_taker = None
max_wickets = -1  # Initializing to find the absolute highest value

for player_name, stats in players.items():
    if stats['wickets'] > max_wickets:
        max_wickets = stats['wickets']
        max_wicket_taker = player_name

print(f"\nPlayer with Maximum Wickets: {max_wicket_taker} with {max_wickets} wickets")


# 6. Find all-rounders (runs > 300 and wickets > 5).
print("\nAll-Rounders (Runs > 300 and Wickets > 5):")
for player_name, stats in players.items():
    if stats['runs'] > 300 and stats['wickets'] > 5:
        print(f"Name: {player_name}, Runs: {stats['runs']}, Wickets: {stats['wickets']}")


# 7. Display players scoring above average.
print("\nPlayers Scoring Above Average Runs:")
for player_name, stats in players.items():
    if stats['runs'] > average_runs:
        print(f"Name: {player_name}, Runs: {stats['runs']}")


# 8. Create performance categories.
print("\nPlayer Categories:")
for player_name, stats in players.items():
    if stats['runs'] > 500:
        category = "Star Performer"
    elif stats['runs'] > 300:
        category = "Good Performer"
    elif stats['runs'] > 100:
        category = "Average Performer"
    else:
        category = "Poor Performer"
    print(f"Name: {player_name}, Category: {category}")


# 9. Generate team statistics.
total_matches = 0
total_wickets = 0

for player_name, stats in players.items():
    total_matches += stats['matches']
    total_wickets += stats['wickets']

print("\n=== TEAM STATISTICS ===")
print(f"Total Runs Scored by Team: {total_runs}")
print(f"Total Wickets Taken by Team: {total_wickets}")
print(f"Total Collective Matches Played: {total_matches}")


# 10. Display top 5 batsmen (Using basic loops and temporary variables only).
print("\nTop 5 Batsmen:")
# We convert our dictionary items into a working list copy to protect our original data
temp_batsmen = []
for player_name, stats in players.items():
    temp_batsmen.append([player_name, stats['runs']])

# Run an external loop exactly 5 times to peel away the highest scorer round-by-round
for rank in range(1, 6):
    if not temp_batsmen:
        break
    
    # Track the best individual batsman inside this processing round
    best_idx = 0
    for idx in range(len(temp_batsmen)):
        if temp_batsmen[idx][1] > temp_batsmen[best_idx][1]:
            best_idx = idx
            
    # Pop out the selected best player from our loop variables and present them
    top_player = temp_batsmen.pop(best_idx)
    print(f"Rank {rank}: {top_player[0]} - Runs: {top_player[1]}")


# 11. Display top 5 bowlers (Using basic loops and temporary variables only).
print("\nTop 5 Bowlers:")
temp_bowlers = []
for player_name, stats in players.items():
    temp_bowlers.append([player_name, stats['wickets']])

# Run an external loop exactly 5 times to peel away the highest wicket taker round-by-round
for rank in range(1, 6):
    if not temp_bowlers:
        break
        
    # Track the best individual bowler inside this processing round
    best_idx = 0
    for idx in range(len(temp_bowlers)):
        if temp_bowlers[idx][1] > temp_bowlers[best_idx][1]:
            best_idx = idx
            
    # Pop out the selected best bowler from our loop variables and present them
    top_bowler = temp_bowlers.pop(best_idx)
    print(f"Rank {rank}: {top_bowler[0]} - Wickets: {top_bowler[1]}")


# 12. Create a separate dictionary for award winners.
award_winners = {}
for player_name, stats in players.items():
    # If a player hits either landmark criterion, they match the requirement
    if stats['runs'] > 500 or stats['wickets'] > 10:
        award_winners[player_name] = stats

print("\nAward Winners Dictionary Contents:")
for player_name, stats in award_winners.items():
    print(f"Name: {player_name}, Runs: {stats['runs']}, Wickets: {stats['wickets']}")
