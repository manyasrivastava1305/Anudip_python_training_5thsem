import os

FILENAME = "expenses.txt"
REPORT_FILENAME = "report.txt"

def load_expenses():
    expenses = []
    if not os.path.exists(FILENAME):
        return expenses
    with open(FILENAME, "r") as f:
        for line in f:
            if line.strip():
                category, amount = line.strip().split(",")
                expenses.append({
                    "category": category.strip(),
                    "amount": float(amount.strip())
                })
    return expenses

def save_all_expenses(expenses):
    with open(FILENAME, "w") as f:
        for e in expenses:
            f.write(f"{e['category']}, {e['amount']}\n")

def display_all():
    expenses = load_expenses()
    if not expenses:
        print("No recorded tracking metrics.")
        return
    print("\n--- Daily Tracker Budget Matrix ---")
    for e in expenses:
        print(f"Category: {e['category']} | Amount: {e['amount']}")

def calculate_total():
    expenses = load_expenses()
    total = sum(e['amount'] for e in expenses)
    print(f"\nTotal Expenditure: {total:.2f}")
    return total

def find_extremes():
    expenses = load_expenses()
    if not expenses:
        print("No items recorded.")
        return None, None
    highest = max(expenses, key=lambda x: x['amount'])
    lowest = min(expenses, key=lambda x: x['amount'])
    print(f"\nHighest spending: Category '{highest['category']}' ({highest['amount']})")
    print(f"Lowest spending: Category '{lowest['category']}' ({lowest['amount']})")
    return highest, lowest

def display_expensive_items():
    expenses = load_expenses()
    print("\n--- Expenses Greater Than 800 ---")
    found = False
    for e in expenses:
        if e['amount'] > 800:
            print(f"Category: {e['category']} | Amount: {e['amount']}")
            found = True
    if not found:
        print("No category balances cross the threshold of 800.")

def add_expense():
    category = input("Enter new expense category name: ").strip()
    try:
        amount = float(input("Enter amount spent: ").strip())
    except ValueError:
        print("Invalid value entered for amount.")
        return
    
    expenses = load_expenses()
    # Check for category redundancy
    for e in expenses:
        if e['category'].lower() == category.lower():
            print("Category already exists. Use the update parameter instead.")
            return

    expenses.append({"category": category, "amount": amount})
    save_all_expenses(expenses)
    print("New category tracked and file updated securely.")

def update_expense_amount():
    category = input("Enter expense category to update: ").strip()
    expenses = load_expenses()
    for e in expenses:
        if e['category'].lower() == category.lower():
            try:
                new_amount = float(input(f"Enter new amount spent for {e['category']}: ").strip())
            except ValueError:
                print("Invalid input value.")
                return
            e['amount'] = new_amount
            save_all_expenses(expenses)
            print("Value updated in base architecture config successfully.")
            return
    print("Expense Category tracking mismatch.")

def generate_summary_report():
    expenses = load_expenses()
    if not expenses:
        print("No analytical variables to parse.")
        return
        
    total = sum(e['amount'] for e in expenses)
    highest = max(expenses, key=lambda x: x['amount'])
    lowest = min(expenses, key=lambda x: x['amount'])
    high_spending_categories = [e['category'] for e in expenses if e['amount'] > 800]

    report_lines = [
        "===== EXPENSE SUMMARY REPORT =====",
        f"Total Expenses: {total:.2f}",
        f"Highest Expense Category: {highest['category']} ({highest['amount']})",
        f"Lowest Expense Category: {lowest['category']} ({lowest['amount']})",
        "Categories spending more than 800: " + (", ".join(high_spending_categories) if high_spending_categories else "None"),
        "=================================="
    ]
    
    # Output to File
    with open(REPORT_FILENAME, "w") as f:
        for line in report_lines:
            f.write(line + "\n")
            
    # Output to console for user validation
    print("\nReport Generated Successfully!")
    print("\n".join(report_lines))

def menu():
    while True:
        print("\n===== Daily Expense Tracker Framework =====")
        print("1. Display all expenses")
        print("2. Calculate total expenditure")
        print("3. Find highest and lowest spending category")
        print("4. Display expenses greater than 800")
        print("5. Add a new expense category")
        print("6. Update an existing expense amount")
        print("7. Generate a summary report to file")
        print("8. Exit")
        choice = input("Enter parameter choice (1-8): ").strip()

        if choice == '1': display_all()
        elif choice == '2': calculate_total()
        elif choice == '3': find_extremes()
        elif choice == '4': display_expensive_items()
        elif choice == '5': add_expense()
        elif choice == '6': update_expense_amount()
        elif choice == '7': generate_summary_report()
        elif choice == '8':
            print("Exiting application logs...")
            break
        else:
            print("Wrong execution parameter, try again.")

if __name__ == "__main__":
    menu()