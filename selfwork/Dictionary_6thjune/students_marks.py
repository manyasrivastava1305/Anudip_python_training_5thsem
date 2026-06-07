# Student Marks Analysis 
"""
Sample Data marks = {     
"Aarav": 78,     
"Diya": 92,     
"Rohan": 45,     
"Ishita": 88,     
"Kabir": 56,     
"Meera": 39,     
"Arjun": 95,     
"Saanvi": 67,     
"Vivaan": 82,     
"Anaya": 51 } 
Tasks 
• Display students scoring 80 or above.  
• Count the number of students who failed (marks < 40).  
• Find the highest scorer.  
• Create a list of students scoring between 60 and 75.  
• Assign grades:  
  o A: ≥ 90  
  o B: 75–89  
  o C: 50–74  
  o F: < 50  
"""

# Student Marks Analysis

marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# Task 1: Display students scoring 80 or above
print("Task 1: Students scoring 80 or above")
for student, score in marks.items():
    if score >= 80:
        print(student, ":", score)

# Task 2: Count the number of students who failed
failed_count = 0
for score in marks.values():
    if score < 40:
        failed_count += 1

print("\nTask 2: Number of failed students =", failed_count)

# Task 3: Find the highest scorer
highest_scorer = max(marks, key=marks.get)
print("\nTask 3: Highest Scorer")
print(highest_scorer, ":", marks[highest_scorer])

# Task 4: Create a list of students scoring between 60 and 75
students_60_75 = []

for student, score in marks.items():
    if 60 <= score <= 75:
        students_60_75.append(student)

print("\nTask 4: Students scoring between 60 and 75")
print(students_60_75)

# Task 5: Assign grades
print("\nTask 5: Grades")

for student, score in marks.items():

    if score >= 90:
        grade = "A"

    elif score >= 75:
        grade = "B"

    elif score >= 50:
        grade = "C"

    else:
        grade = "F"

    print(student, ":", grade)
