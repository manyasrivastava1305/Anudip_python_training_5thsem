# Patients arriving at the emergency ward are categorized as: 
# patients = [ 
#     ("P101", "Critical"), 
#     ("P102", "Stable"), 
#     ("P103", "Critical"), 
#     ("P104", "Moderate"), 
#     ("P105", "Stable"), 
#     ("P106", "Critical"), 
#     ("P107", "Moderate"), 
#     ("P108", "Stable"), 
#     ("P109", "Critical"), 
#     ("P110", "Moderate") 
# ] 
# Tasks 
# 1. Count patients in each category.  
# 2. Display IDs of critical patients.  
# 3. Create separate lists for Critical, Moderate, and Stable patients.  
# 4. Determine which category requires maximum attention.  
# 5. Save critical patient IDs to critical_patients.txt. 
patients = [
    ("P101", "Critical"), ("P102", "Stable"), ("P103", "Critical"),
    ("P104", "Moderate"), ("P105", "Stable"), ("P106", "Critical"),
    ("P107", "Moderate"), ("P108", "Stable"), ("P109", "Critical"),
    ("P110", "Moderate")
]

counts = {"Critical": 0, "Moderate": 0, "Stable": 0}
critical_list = []
moderate_list = []
stable_list = []

# Distribute metrics
for pid, status in patients:
    counts[status] += 1
    if status == "Critical":
        critical_list.append(pid)
    elif status == "Moderate":
        moderate_list.append(pid)
    elif status == "Stable":
        stable_list.append(pid)

# Category requiring max attention
max_attn = max(counts, key=counts.get)

# Write to critical_patients.txt
with open("critical_patients.txt", "w") as f:
    for pid in critical_list:
        f.write(f"{pid}\n")

# Display Output
print("Patient Count by Category:")
for k, v in counts.items():
    print(f"{k}: {v}")

print("\nCritical Patients:")
for pid in critical_list:
    print(pid)

print(f"\nCritical Patients List:\n{critical_list}")
print(f"\nModerate Patients List:\n{moderate_list}")
print(f"\nStable Patients List:\n{stable_list}")
print(f"\nCategory Requiring Maximum Attention:\n{max_attn}")
print("\nCritical Patient Report Generated Successfully.")