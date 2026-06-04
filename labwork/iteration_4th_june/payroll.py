def employee_payroll_system():
    try:
        emp_name = input("Enter Employee Name: ")
        basic_salary = float(input("Enter Basic Salary: ₹"))
        
        if basic_salary < 0:
            print("Salary cannot be negative.")
            return

        hra = 0.20 * basic_salary
        da = 0.10 * basic_salary
        pf_deduction = 0.12 * basic_salary

        gross_salary = basic_salary + hra + da
        net_salary = gross_salary - pf_deduction

        if net_salary > 50000:
            grade = "Senior Grade"
        elif net_salary > 30000:
            grade = "Mid Grade"
        else:
            grade = "Junior Grade"

        print("\n=== Payroll Details ===")
        print(f"Employee Name : {emp_name}")
        print(f"Basic Salary  : ₹{basic_salary:,.2f}")
        print(f"HRA (20%)     : ₹{hra:,.2f}")
        print(f"DA (10%)      : ₹{da:,.2f}")
        print(f"PF Deduction  : ₹{pf_deduction:,.2f}")
        print("-----------------------")
        print(f"Gross Salary  : ₹{gross_salary:,.2f}")
        print(f"Net Salary    : ₹{net_salary:,.2f}")
        print(f"Grade         : {grade}")
        
    except ValueError:
        print("Invalid input! Please enter a valid numeric value for salary.")

if __name__ == "__main__":
    employee_payroll_system()
