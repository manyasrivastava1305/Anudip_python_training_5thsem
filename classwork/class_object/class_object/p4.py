class Employee:
    # 1. Constructor: Sets up private attributes correctly
    def __init__(self, emp_id, name, monthly_sal):
        self.__id = emp_id
        self.__name = name
        self.__monthly_sal = monthly_sal

    # 2. Method to display employee details using comma separation
    def display_details(self):
        print("Employee ID   :", self.__id)
        print("Employee Name :", self.__name)
        print("Monthly Salary: ₹", self.__monthly_sal)

    # 3. Method to calculate and return annual salary
    def calculate_annual_salary(self):
        return self.__monthly_sal * 12

    # 4. Method to increase salary by accepting percentage as an argument
    def increase_salary(self, percentage):
        self.__monthly_sal += self.__monthly_sal * (percentage / 100)


# ------------------ Main Code Block ------------------

print("--- Enter Employee Details ---")

# 1. Input and verify Employee ID (Alphanumeric check)
id_input = input("Enter Employee ID: ")
if not id_input.isalnum():
    print("[Error] Employee ID must be alphanumeric (letters and numbers only)!")
    exit()

# 2. Input and verify Name (Full name check - checks for at least one space)
name_input = input("Enter Employee Name (First Last): ").strip()
if " " not in name_input:
    print("[Error] Please enter a full name (First Name and Last Name)!")
    exit()

# 3. Input and verify Monthly Salary (Positive number check)
sal_input = float(input("Enter Monthly Salary: ₹"))
if sal_input <= 0:
    print("[Error] Salary must be a positive number greater than zero!")
    exit()

# Creating the object since all data passed verification
emp = Employee(id_input, name_input, sal_input)

print("\n--- Employee Report ---")
# 1. Display initial details
emp.display_details()

# 2. Calculate and display annual salary using commas
annual_salary = emp.calculate_annual_salary()
print("Annual Salary : ₹", annual_salary)

# 3. Get the percentage increase from user in main code
inc_percent = float(input("\nEnter percentage to increase salary: "))
if inc_percent < 0:
    print("[Error] Percentage increase cannot be negative!")
    exit()

# 4. Increase the salary and show updated details
emp.increase_salary(inc_percent)
print("--- Salary Updated Successfully ---")
emp.display_details()  # Shows the updated monthly salary seamlessly