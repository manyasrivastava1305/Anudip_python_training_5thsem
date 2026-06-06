# Problem Statement 
# A company stores employee details in a tuple. Each employee record contains: 
# employees = ( 
#     ("E101", "Anuj", 92), 
#     ("E102", "Rahul", 76), 
#     ("E103", "Priya", 58), 
#     ("E104", "Neha", 88), 
#     ("E105", "Amit", 45) 
# ) 
# Where: 
# • First value = Employee ID  
# • Second value = Employee Name  
# • Third value = Performance Score  
# Tasks 
# Write a Python program to: 
# 1. Display details of employees scoring 80 or above.  
# 2. Count the number of employees who need improvement (score below 60).  
# 3. Find the employee with the highest score.  
# 4. Create a list containing the names of all employees scoring above 75.  
# 5. Display the performance category for each employee:  
# o 90 and above → Excellent  
# o 75 to 89 → Good  
# o 60 to 74 → Average  
# o Below 60 → Needs Improvement 

# Initial data given in the problem
employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# --- Task 1: Display details of employees scoring 80 or above ---
print("Employees Scoring 80 or Above:")
for emp_id, name, score in employees:
    if score >= 80:
        print(f"{emp_id} {name} {score}")

# --- Task 2: Count the number of employees who need improvement (score below 60) ---
needs_improvement_count = 0
for emp in employees:
    if emp[2] < 60:
        needs_improvement_count += 1
print(f"\nEmployees Needing Improvement: {needs_improvement_count}")

# --- Task 3: Find the employee with the highest score ---
# We initialize with the first employee's details
highest_performer = employees[0] 
for emp in employees:
    if emp[2] > highest_performer[2]:
        highest_performer = emp
        
print("\nHighest Performer:")
print(f"{highest_performer[0]} {highest_performer[1]} {highest_performer[2]}")

# --- Task 4: Create a list containing the names of all employees scoring above 75 ---
high_performers = []
for emp in employees:
    if emp[2] > 75:
        high_performers.append(emp[1])
print(f"\nHigh Performers:\n{high_performers}")

# --- Task 5: Display the performance category for each employee ---
print("\nPerformance Categories:")
for emp_id, name, score in employees:
    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"
    print(f"{name} -> {category}")
