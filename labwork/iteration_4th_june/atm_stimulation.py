def atm_simulation():
    balance = 10000.0
    
    print("=== Welcome to the ATM Simulation System ===")
    
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        try:
            choice = int(input("Please select an option (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
            
        if choice == 1:
            print(f"Your current balance is: ₹{balance:,.2f}")
            
        elif choice == 2:
            try:
                deposit_amount = float(input("Enter the amount to deposit: ₹"))
                if deposit_amount > 0:
                    balance += deposit_amount
                    print(f"Successfully deposited ₹{deposit_amount:,.2f}. New Balance: ₹{balance:,.2f}")
                else:
                    print("Invalid amount. Deposit must be greater than zero.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                
        elif choice == 3:
            try:
                withdraw_amount = float(input("Enter the amount to withdraw: ₹"))
                if withdraw_amount <= 0:
                    print("Invalid amount. Withdrawal must be greater than zero.")
                elif withdraw_amount > balance:
                    print("Transaction Failed: Insufficient funds.")
                    print(f"Your current balance is only ₹{balance:,.2f}")
                else:
                    balance -= withdraw_amount
                    print(f"Successfully withdrew ₹{withdraw_amount:,.2f}. Remaining Balance: ₹{balance:,.2f}")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                
        elif choice == 4:
            print("Thank you for using our ATM service. Goodbye!")
            break
            
        else:
            print("Invalid option! Please select a valid option from the menu.")

if __name__ == "__main__":
    atm_simulation()
