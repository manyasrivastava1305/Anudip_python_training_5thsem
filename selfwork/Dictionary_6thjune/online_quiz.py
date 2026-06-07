# Online Quiz Performance 
"""
Sample Data quiz_scores = {     
"S001": 18,     
"S002": 12,     
"S003": 9,     
"S004": 20,     
"S005": 14,     
"S006": 7,     
"S007": 16,     
"S008": 10,     
"S009": 19,     
"S010": 13 
} 
(Quiz is out of 20 marks.) 
Tasks 
• Display students scoring 15 or above.  
• Count students scoring below 10.  
• Find the top performer.  
• Create a list of students who passed (≥ 10 marks).  
• Calculate the class average.  
"""

# Online Quiz Performance

quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Task 1: Display students scoring 15 or above
print("Task 1: Students scoring 15 or above")

for student, score in quiz_scores.items():
    if score >= 15:
        print(student, ":", score)

# Task 2: Count students scoring below 10
count_below_10 = 0

for score in quiz_scores.values():
    if score < 10:
        count_below_10 += 1

print("\nTask 2: Students scoring below 10 =", count_below_10)

# Task 3: Find the top performer
top_performer = max(quiz_scores, key=quiz_scores.get)

print("\nTask 3: Top Performer")
print(top_performer, ":", quiz_scores[top_performer])

# Task 4: Create a list of students who passed (>= 10 marks)
passed_students = []

for student, score in quiz_scores.items():
    if score >= 10:
        passed_students.append(student)

print("\nTask 4: Students who passed")
print(passed_students)

# Task 5: Calculate the class average
average_score = sum(quiz_scores.values()) / len(quiz_scores)

print("\nTask 5: Class Average =", average_score)
