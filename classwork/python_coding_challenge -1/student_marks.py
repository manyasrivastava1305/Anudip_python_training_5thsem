# Student marks are stored in marks.txt. 
# Sample Input/Data (marks.txt) 
# S101,Anuj,92 
# S102,Rahul,76 
# S103,Priya,88 
# S104,Neha,45 
# S105,Amit,58 
# S106,Sneha,95 
# S107,Karan,81 
# S108,Pooja,73 
# S109,Rohit,39 
# S110,Anjali,90 
# Tasks 
# 1. Calculate grades for all students.  
# Passed Students: 9 
# Failed Students: 1 
# 2. Generate a report card file report_card.txt.  
# 3. Display topper details.  
# 4. Count pass and fail students.  
# 5. Display students eligible for merit certificates (marks ≥ 90). 
# Mock Setup for marks.txt
marks_data = """S101,Anuj, 92
S102, Rahul, 76
S103, Priya, 88
S104, Neha, 45
S105,Amit,58
S106, Sneha, 95
S107, Karan, 81
S108, Pooja, 73
S109, Rohit, 39
S110, Anjali, 90"""

with open("marks.txt", "w") as f:
    f.write(marks_data)

# --- Main Program Logic ---

students = []
with open("marks.txt", "r") as file:
    for line in file:
        if line.strip():
            parts = line.strip().split(",")
            s_id = parts[0].strip()
            name = parts[1].strip()
            score = int(parts[2].strip())
            students.append([s_id, name, score])

# 3. Display topper details
topper_name = ""
topper_score = -1
for s in students:
    if s[2] > topper_score:
        topper_score = s[2]
        topper_name = s[1]

print("Topper:")
print(f"{topper_name} ({topper_score})\n")

# 4. Count pass and fail students (Assuming 40 is the passing mark based on sample output)
pass_count = 0
fail_count = 0
for s in students:
    if s[2] >= 40:
        pass_count += 1
    else:
        fail_count += 1

print(f"Passed Students: {pass_count}")
print(f"Failed Students: {fail_count}\n")

# 5. Display students eligible for merit certificates (marks >= 90)
print("Merit Certificate Holders:")
for s in students:
    if s[2] >= 90:
        print(s[1])
print()

# 1 & 2. Calculate grades and generate report_card.txt
with open("report_card.txt", "w") as out_file:
    for s in students:
        mark = s[2]
        if mark >= 90: grade = "A"
        elif mark >= 75: grade = "B"
        elif mark >= 50: grade = "C"
        elif mark >= 40: grade = "D"
        else: grade = "F"
        out_file.write(f"{s[0]}, {s[1]}, Marks: {mark}, Grade: {grade}\n")

print("Report Cards Generated Successfully.")
