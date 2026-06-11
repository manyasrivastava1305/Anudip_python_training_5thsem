import os

FILENAME = "employees.txt"

def load_employees():
    employees = []
    if not os.path.exists(FILENAME):
        return employees
    with open(FILENAME, "r") as f:
        for line in f:
            if line.strip():
                emp_id, name, salary = line.strip().split(",")
                employees.append({
                    "id": emp_id.strip(),
                    "name": name.strip(),
                    "salary": float(salary.strip())
                })
    return employees

def save_employee(emp_id, name, salary):
    with open(FILENAME, "a") as f:
        f.write(f"{emp_id}, {name}, {salary}\n")

def display_all():
    employees = load_employees()
    if not employees:
        print("No employee records found.")
        return
    print("\n--- Employee Records ---")
    for emp in employees:
        print(f"ID: {emp['id']} | Name: {emp['name']} | Salary: {emp['salary']}")

def search_employee():
    emp_id = input("Enter Employee ID to search: ").strip()
    employees = load_employees()
    for emp in employees:
        if emp['id'].lower() == emp_id.lower():
            print(f"\nEmployee Found:\nID: {emp['id']}\nName: {emp['name']}\nSalary: {emp['salary']}")
            return
    print("Employee not found.")

def calculate_average_salary():
    employees = load_employees()
    if not employees:
        print("No employee records available.")
        return
    total_salary = sum(emp['salary'] for emp in employees)
    avg_salary = total_salary / len(employees)
    print(f"\nAverage Salary: {avg_salary:.2f}")

def find_highest_lowest_paid():
    employees = load_employees()
    if not employees:
        print("No employee records available.")
        return
    highest = max(employees, key=lambda x: x['salary'])
    lowest = min(employees, key=lambda x: x['salary'])
    print(f"\nHighest Paid: {highest['name']} (ID: {highest['id']}) - {highest['salary']}")
    print(f"Lowest Paid: {lowest['name']} (ID: {lowest['id']}) - {lowest['salary']}")

def display_high_earners():
    employees = load_employees()
    print("\n--- Employees Earning Above 50,000 ---")
    found = False
    for emp in employees:
        if emp['salary'] > 50000:
            print(f"ID: {emp['id']} | Name: {emp['name']} | Salary: {emp['salary']}")
            found = True
    if not found:
        print("No employees found earning above 50,000.")

def add_employee():
    emp_id = input("Enter Employee ID: ").strip()
    name = input("Enter Employee Name: ").strip()
    try:
        salary = float(input("Enter Salary: ").strip())
    except ValueError:
        print("Invalid salary amount.")
        return
    
    # Check for duplicate ID
    employees = load_employees()
    if any(emp['id'].lower() == emp_id.lower() for emp in employees):
        print("Error: Employee ID already exists.")
        return
        
    save_employee(emp_id, name, salary)
    print("Employee record added successfully.")

def generate_salary_categories():
    employees = load_employees()
    if not employees:
        print("No employee records available.")
        return
    print("\n--- Salary Categories ---")
    for emp in employees:
        sal = emp['salary']
        if sal >= 60000:
            cat = "High"
        elif 40000 <= sal <= 59999:
            cat = "Medium"
        else:
            cat = "Low"
        print(f"ID: {emp['id']} | Name: {emp['name']} | Category: {cat} ({sal})")

def menu():
    while True:
        print("\n===== Employee Payroll Management System =====")
        print("1. Display all employee records")
        print("2. Search employee details using Employee ID")
        print("3. Calculate average salary")
        print("4. Find highest-paid and lowest-paid employee")
        print("5. Display employees earning above 50,000")
        print("6. Add a new employee record")
        print("7. Generate salary categories")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1': display_all()
        elif choice == '2': search_employee()
        elif choice == '3': calculate_average_salary()
        elif choice == '4': find_highest_lowest_paid()
        elif choice == '5': display_high_earners()
        elif choice == '6': add_employee()
        elif choice == '7': generate_salary_categories()
        elif choice == '8': 
            print("Exiting application...")
            break
        else: 
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()