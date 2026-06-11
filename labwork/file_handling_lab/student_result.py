import os

FILENAME = "results.txt"
GRADES_FILENAME = "grades.txt"

def load_students():
    students = []
    if not os.path.exists(FILENAME):
        return students
    with open(FILENAME, "r") as f:
        for line in f:
            if line.strip():
                s_id, name, marks = line.strip().split(",")
                students.append({
                    "id": s_id.strip(),
                    "name": name.strip(),
                    "marks": int(marks.strip())
                })
    return students

def display_all_students():
    students = load_students()
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Marks: {s['marks']}")

def search_student():
    s_id = input("Enter Student ID to search: ").strip()
    students = load_students()
    for s in students:
        if s['id'].lower() == s_id.lower():
            print(f"\nStudent Found:\nID: {s['id']}\nName: {s['name']}\nMarks: {s['marks']}")
            return
    print("Student record not found.")

def find_topper_and_lowest():
    students = load_students()
    if not students:
        print("No student data.")
        return
    topper = max(students, key=lambda x: x['marks'])
    lowest = min(students, key=lambda x: x['marks'])
    print(f"\nTopper: {topper['name']} ({topper['id']}) - Score: {topper['marks']}")
    print(f"Lowest Scorer: {lowest['name']} ({lowest['id']}) - Score: {lowest['marks']}")

def calculate_class_average():
    students = load_students()
    if not students:
        print("No student data available.")
        return
    total_marks = sum(s['marks'] for s in students)
    avg = total_marks / len(students)
    print(f"\nClass Average Marks: {avg:.2f}")

def count_pass_fail():
    students = load_students()
    if not students:
        print("No student data available.")
        return
    pass_count = sum(1 for s in students if s['marks'] >= 40)
    fail_count = len(students) - pass_count
    print(f"\nPass Students: {pass_count}")
    print(f"Fail Students: {fail_count}")

def get_grade(marks):
    if marks >= 90: return 'A'
    elif 75 <= marks <= 89: return 'B'
    elif 40 <= marks <= 74: return 'C'
    else: return 'F'

def generate_grades_and_report():
    students = load_students()
    if not students:
        print("No student data to process.")
        return
    
    print("\n--- Live Grade Preview ---")
    with open(GRADES_FILENAME, "w") as f:
        for s in students:
            grade = get_grade(s['marks'])
            record = f"ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}, Grade: {grade}"
            print(record)
            f.write(record + "\n")
    print(f"\nGrade reports have been completely compiled and saved into '{GRADES_FILENAME}'.")

def menu():
    while True:
        print("\n===== Student Result Processing System =====")
        print("1. Display all student records")
        print("2. Search a student using Student ID")
        print("3. Find topper and lowest scorer")
        print("4. Calculate class average")
        print("5. Count pass and fail students")
        print("6. Generate grades and write reports to file")
        print("7. Exit")
        choice = input("Enter option (1-7): ").strip()

        if choice == '1': display_all_students()
        elif choice == '2': search_student()
        elif choice == '3': find_topper_and_lowest()
        elif choice == '4': calculate_class_average()
        elif choice == '5': count_pass_fail()
        elif choice == '6': generate_grades_and_report()
        elif choice == '7':
            print("Exiting application...")
            break
        else:
            print("Invalid option chosen, please try again.")

if __name__ == "__main__":
    menu()