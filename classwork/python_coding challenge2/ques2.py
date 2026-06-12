# The marks obtained by students in the final examination are stored as follows: 
# Sample Data 
# marks = { 
#     "Anuj": 92, 
#     "Rahul": 76, 
#     "Priya": 88, 
#     "Neha": 64, 
#     "Amit": 58, 
#     "Sneha": 95, 
#     "Karan": 81, 
#     "Pooja": 73, 
#     "Rohit": 47, 
#     "Anjali": 90 
# } 
# Tasks 
# 1. Display students scoring above 85 marks.  
# 2. Find the topper.  
# 3. Find the student with the lowest marks.  
# 4. Calculate class average marks.  
# 5. Generate grades:  
# o A (90+)  
# o B (75–89)  
# o C (50–74)  
# o F (<50)  
# 6. Create a list of scholarship students (marks ≥ 90). 
marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
}

# Convert dictionary items to a list for iteration
marks_items = list(marks.items())

# 1. Display students scoring above 85 marks.
print("--- Students scoring more than 85 marks ---")
for item in marks_items:
    if item[1] > 85:  # Fixed: Changed from 400 to 85
        print(item[0], ":", item[1])
print("\n" + "-" * 40)

# 2. Find the topper
print("--- The topper's data ---")
topper = marks_items[0][0]
topper_marks = marks_items[0][1]
for item in marks_items:
    if item[1] > topper_marks:
        topper = item[0]
        topper_marks = item[1]
print("Topper:", topper, "with score", topper_marks)
print("\n" + "-" * 40)

# 3. Find the student with the lowest marks
print("--- The lowest scoring student's data ---")
lowest = marks_items[0][0]
lowest_marks = marks_items[0][1]
for item in marks_items:
    if item[1] < lowest_marks:
        lowest = item[0]
        lowest_marks = item[1]
print("Lowest:", lowest, "with score", lowest_marks)  # Fixed: Printed lowest variables instead of topper
print("\n" + "-" * 40)

# 4. Calculate class average marks
print("--- Average marks obtained ---")
total_marks = 0
for item in marks_items:
    total_marks += item[1]
average_marks = total_marks / len(marks_items)  # Fixed: Used len() instead of hardcoded 10
print(f"Class Average: {average_marks:.2f}")
print("\n" + "-" * 40)

# 5. Generate grades
A = []
B = []   
C = []
F = []
for item in marks_items:
    if item[1] >= 90:
        A.append(item[0])
    elif 75 <= item[1] <= 89:
        B.append(item[0])
    elif 50 <= item[1] <= 74:  # Fixed: Changed lower bound from 70 to 50
        C.append(item[0])
    else:
        F.append(item[0])

print("A (90+):", A)
print("B (75–89):", B)  
print("C (50–74):", C)  # Fixed: Label fixed to match prompt rules
print("F (<50):", F)    # Fixed: Label fixed to match prompt rules
print("-" * 40)

# 6. Create a list of scholarship students (marks ≥ 90)
scholars = []
for item in marks_items:  # Fixed: Using singular 'item' to match loop
    if item[1] >= 90:     # Fixed: Changed from 'item' to loop's variable context
        scholars.append(item[0])
print("Scholars:", scholars)