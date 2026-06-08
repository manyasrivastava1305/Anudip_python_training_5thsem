# Employee performance scores are stored as: 
# performance = { 
#     "EMP101": 92, 
#     "EMP102": 78, 
#     "EMP103": 45, 
#     "EMP104": 88, 
#     "EMP105": 97, 
#     "EMP106": 56, 
#     "EMP107": 81, 
#     "EMP108": 64, 
#     "EMP109": 39, 
#     "EMP110": 73 
# } 
# Tasks 
# 1. Display employees scoring above 80.  
# 2. Count employees needing improvement (score < 60).  
# 3. Find the top performer.  
# 4. Calculate average performance score.  
# 5. Create separate lists:  
# o Excellent (≥ 90)  
# o Good (75–89)  
# o Average (60–74)  
# o Poor (< 60)  
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73,
}
# --- Task 1: Display employees scoring above 80 ---
print("--- Employees scoring above 80 ---")
performance_items = list(performance.items())
for items in performance_items:
    if items[1] > 80:
        print(f"{items[0]}: {items[1]}")
print("-" * 40)
# --- Task 2: Count employees needing improvement (score < 60) ---
count = 0
for items in performance_items:
    if items[1] < 60:
        count = count + 1
print(f"Number of employees needing improvement (score < 60): {count}")
print("-" * 40)
# --- Task 3: Find the top performer ---
top_performer = performance_items[0][0]
top_score = performance_items[0][1]
for items in performance_items:
    if items[1] > top_score:
        top_performer = items[0]
        top_score = items[1]
print(f"Top Performer: {top_performer} with a score of {top_score}")
print("-" * 40)
# --- Task 4: Calculate average performance score ---
total_score = sum(items[1] for items in performance_items)
average_score = total_score / len(performance_items)
print(f"Average Performance Score: {average_score:.2f}")
print("-" * 40)
# --- Task 5: Create separate lists ---
excellent = []
good = []   
average = []
poor = []
for items in performance_items:
    if items[1] >= 90:
        excellent.append(items[0])
    elif 75 <= items[1] < 90:
        good.append(items[0])
    elif 60 <= items[1] < 75:
        average.append(items[0])
    else:
        poor.append(items[0])
print(f"Excellent (≥ 90): {excellent}")
print(f"Good (75–89): {good}")  
print(f"Average (60–74): {average}")
print(f"Poor (< 60): {poor}")
print("-" * 40)
