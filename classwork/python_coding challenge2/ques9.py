# Patient heart rates are recorded below:
# heart_rate = { 
#     "P101": 72, 
#     "P102": 105, 
#     "P103": 88, 
#     "P104": 120, 
#     "P105": 65, 
#     "P106": 98, 
#     "P107": 110, 
#     "P108": 70, 
#     "P109": 85, 
#     "P110": 130 
# } 
# Tasks 
# 1. Display critical patients (heart rate >100).  
# 2. Find highest and lowest heart rate.  
# 3. Calculate average heart rate.  
# 4. Count stable patients (60–100 bpm).

heart_rate = { 
    "P101": 72, 
    "P102": 105, 
    "P103": 88, 
    "P104": 120, 
    "P105": 65, 
    "P106": 98, 
    "P107": 110, 
    "P108": 70, 
    "P109": 85, 
    "P110": 130 
}

# --- Task 1: Display critical patients (heart rate >100) ---
print("--- Critical Patients (Heart Rate > 100 bpm) ---")
hr_items = list(heart_rate.items())
for item in hr_items:
    if item[1] > 100:
        print(item[0], ":", item[1], "bpm")
print("\n" + "-" * 40)

# --- Task 2: Find highest and lowest heart rate ---
print("--- Highest and Lowest Heart Rates ---")
highest_patient = hr_items[0][0]
highest_hr = hr_items[0][1]
lowest_patient = hr_items[0][0]
lowest_hr = hr_items[0][1]

for item in hr_items:
    # Check for highest heart rate
    if item[1] > highest_hr:
        highest_patient = item[0]
        highest_hr = item[1]
    # Check for lowest heart rate
    if item[1] < lowest_hr:
        lowest_patient = item[0]
        lowest_hr = item[1]

print("Highest Heart Rate:", highest_patient, "with", highest_hr, "bpm")
print("Lowest Heart Rate:", lowest_patient, "with", lowest_hr, "bpm")
print("\n" + "-" * 40)

# --- Task 3: Calculate average heart rate ---
print("--- Average Heart Rate ---")
total_hr = 0
for item in hr_items:
    total_hr += item[1]
average_hr = total_hr / len(hr_items)
print("Average heart rate of all patients:", average_hr, "bpm")
print("\n" + "-" * 40)

# --- Task 4: Count stable patients (60–100 bpm) ---
print("--- Stable Patients Count (60-100 bpm) ---")
stable_count = 0
for item in hr_items:
    if 60 <= item[1] <= 100:
        stable_count += 1
print("Number of stable patients:", stable_count)
print("\n" + "-" * 40)