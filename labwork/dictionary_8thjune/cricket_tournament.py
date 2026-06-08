# Runs scored by players in a tournament: 
# runs = { 
#     "Virat": 645, 
#     "Rohit": 512, 
#     "Gill": 698, 
#     "Rahul": 435, 
#     "Hardik": 278, 
#     "Pant": 534, 
#     "Surya": 389, 
#     "Jadeja": 301, 
#     "Iyer": 455, 
#     "KL": 410 
# } 
# Tasks 
# 1. Display players scoring more than 500 runs.  
# 2. Find the Orange Cap winner.  
# 3. Find the lowest scorer.  
# 4. Calculate total runs scored.  
# 5. Create a list of players scoring below 400.  
# 6. Count players scoring between 400 and 600 runs. 
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410,
}
# --- Task 1: Display players scoring more than 500 runs ---
print("--- Players scoring more than 500 runs ---")
runs_items = list(runs.items())
for item in runs_items:
    if item[1] > 500:
        print(item[0], ":", item[1])
print("\n" + "-" * 40)
# --- Task 2: Find the Orange Cap winner ---
print("--- Orange Cap Winner ---")
orange_cap_winner = runs_items[0][0]
orange_cap_score = runs_items[0][1]
for item in runs_items:
    if item[1] > orange_cap_score:
        orange_cap_winner = item[0]
        orange_cap_score = item[1]
print("Orange Cap Winner:", orange_cap_winner, "with", orange_cap_score, "runs")
print("\n" + "-" * 40)
# --- Task 3: Find the lowest scorer ---
print("--- Lowest Scorer ---")
lowest_scorer = runs_items[0][0]
lowest_score = runs_items[0][1]
for item in runs_items:
    if item[1] < lowest_score:
        lowest_scorer = item[0]
        lowest_score = item[1]
print("Lowest Scorer:", lowest_scorer, "with", lowest_score, "runs")
print("\n" + "-" * 40)
# --- Task 4: Calculate total runs scored ---
print("--- Total Runs Scored ---")
total_runs = 0
for item in runs_items:
    total_runs += item[1]
print("Total runs scored:", total_runs)
print("\n" + "-" * 40)
# --- Task 5: Create a list of players scoring below 400 ---
print("--- Players scoring below 400 runs ---")
below_400 = []
for item in runs_items:
    if item[1] < 400:
        below_400.append(item[0])
print("Players scoring below 400 runs:", below_400)
print("\n" + "-" * 40)
# --- Task 6: Count players scoring between 400 and 600 runs ---
print("--- Players scoring between 400 and 600 runs ---")
count = 0
for item in runs_items:
    if 400 <= item[1] <= 600:
        count += 1
print("Number of players scoring between 400 and 600 runs:", count)
print("\n" + "-" * 40)
