# Employee data is stored as tuples: 
# employees = [ 
#     ("Rahul", 35000), 
#     ("Priya", 55000), 
#     ("Amit", 42000), 
#     ("Neha", 65000) 
# ] 
# Write a program to: 
# • Display employees earning above ₹50,000.  
# • Find the highest-paid employee.  
# • Calculate total salary expenditure.  
# • Count employees earning below ₹40,000. 
# Initial employee data stored as tuples (Name, Salary)
employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
] 

# Initialize variables
high_earners = []
highest_paid_employee = None
highest_salary = 0
total_expenditure = 0
below_40k_count = 0

# Loop through the list of employees
for name, salary in employees:
    # 1. Check for employees earning above 50,000
    if salary > 50000:
        high_earners.append(name)
        
    # 2. Tracks the highest-paid employee
    if salary > highest_salary:
        highest_salary = salary
        highest_paid_employee = name
        
    # 3. Add to total salary expenditure
    total_expenditure += salary
    
    # 4. Count employees earning below 40,000
    if salary < 40000:
        below_40k_count += 1

# Display the results
print("--- Employee Data Analysis ---")
print("Employees earning above ₹50,000:", high_earners)
print("Highest-Paid Employee:", highest_paid_employee, "(₹" + str(highest_salary) + ")")
print("Total Salary Expenditure: ₹", total_expenditure)
print("Count of employees earning below ₹40,000:", below_40k_count)
