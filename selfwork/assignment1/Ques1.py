# A coaching institute wants to analyze student performance. 
# Store details of at least 30 students in a dictionary. 
# Example Structure 
# students = { 
#     "S101": {"name": "Anuj", "marks": 85}, 
#     "S102": {"name": "Rahul", "marks": 72} 
# } 
# Requirements 
# 1. Display all student records.  
# 2. Search a student using Student ID.  
# 3. Add a new student.  
# 4. Update marks of an existing student.  
# 5. Delete a student.  
# 6. Find topper and lowest scorer.  
# 7. Calculate class average.  
# 8. Count pass and fail students.  
# 9. Generate grades:  
# o A (90+)  
# o B (75–89)  
# o C (50–74)  
# o F (<50)  
# 10. Display students scoring above average.  
# 11. Display top 5 performers.  
# 12. Create a separate dictionary for scholarship students (marks > 85).  
# Expected Learning 
# • Nested Dictionaries  
# • Dictionary Traversal  
# • Searching  
# • Aggregation  
# • Report Generation 
#1. Display all student records.
students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Priya", "marks": 90},
    "S104": {"name": "Amit", "marks": 65},
    "S105": {"name": "Sneha", "marks": 78},
    "S106": {"name": "Vikram", "marks": 55},
    "S107": {"name": "Riya", "marks": 92},
    "S108": {"name": "Karan", "marks": 80},
    "S109": {"name": "Neha", "marks": 68},
    "S110": {"name": "Aditya", "marks": 74},
    # Add more students to reach at least 30
}
# Display all student records
print("All Student Records:")
for student_id, details in students.items():
    print(f"ID: {student_id}, Name: {details['name']}, Marks: {details['marks']}")  
#2. Search a student using Student ID.
search_id = input("\nEnter Student ID to search: ")
if search_id in students:
    print(f"Student found: ID: {search_id}, Name: {students[search_id]['name']}, Marks: {students[search_id]['marks']}")
else:
    print("Student not found.")
#3. Add a new student.
new_id = input("\nEnter new Student ID: ")
if new_id not in students:
    new_name = input("Enter new student's name: ")
    new_marks = float(input("Enter new student's marks: "))
    students[new_id] = {"name": new_name, "marks": new_marks}
    print("Student added successfully.")
else:
    print("Student ID already exists.")
#4. Update marks of an existing student.
update_id = input("\nEnter Student ID to update marks: ")
if update_id in students:
    new_marks = float(input("Enter new marks: "))
    students[update_id]["marks"] = new_marks
    print("Marks updated successfully.")
else:
    print("Student not found.")
#5. Delete a student.
delete_id = input("\nEnter Student ID to delete: ")
if delete_id in students:
    del students[delete_id]
    print("Student deleted successfully.")
else:
    print("Student not found.")
#6. Find topper and lowest scorer.
students_list = list(students.values())
topper_name = students_list[0]['name']
lowest_scorer = students_list[0]['name'] 
topper_marks = students_list[0]['marks']
lowest_marks = students_list[0]['marks']
for student in students_list:
    if student['marks'] > topper_marks:
        topper_marks = student['marks']
        topper_name = student['name']
    if student['marks'] < lowest_marks:
        lowest_marks = student['marks']
        lowest_scorer = student['name']
print(f"\nTopper: {topper_name} with marks {topper_marks}")
print(f"Lowest Scorer: {lowest_scorer} with marks {lowest_marks}")
#7. Calculate class average.
total_marks = 0
for student in students_list:
    total_marks += student['marks']
average_marks = total_marks / len(students_list)
print(f"\nClass Average: {average_marks}")  
#8. Count pass and fail students.
pass_count = 0
fail_count = 0
for student in students_list:
    if student['marks'] >= 50:
        pass_count += 1
    else:
        fail_count += 1
print(f"\nPass Students: {pass_count}")
print(f"Fail Students: {fail_count}")
#9. Generate grades:
grades = {}
for student in students_list:
    marks = student['marks']
    if marks >= 90:
        grades[student['name']] = 'A'
    elif marks >= 75:
        grades[student['name']] = 'B'
    elif marks >= 50:
        grades[student['name']] = 'C'
    else:
        grades[student['name']] = 'F'
print("\nGrades:")
for name, grade in grades.items():
    print(f"{name}: {grade}")
#10. Display students scoring above average.
print("\nStudents scoring above average:")
for student in students_list:
    if student['marks'] > average_marks:
        print(f"{student['name']}: {student['marks']}")
#11. Display top 5 performers.
print("\nTop 5 Performers:")
temp_students = list(students_list)

for i in range(1, 6):
    if not temp_students:
        break
    highest_student = temp_students[0]
    for student in temp_students:
        if student['marks'] > highest_student['marks']:
            highest_student = student
            
    print(f"{i}. {highest_student['name']} - Marks: {highest_student['marks']}")
    temp_students.remove(highest_student)
#12. Create a separate dictionary for scholarship students (marks > 85).
scholarship_students = {}
for student in students_list:
    if student['marks'] > 85:
        scholarship_students[student['name']] = student['marks']
print("\nScholarship Students:")
for name, marks in scholarship_students.items():
    print(f"{name}: {marks}")
    #------------------------------------------
