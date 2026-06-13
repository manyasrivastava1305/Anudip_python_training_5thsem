#creating a class to operform various operation for a customer account
class Account:
    #defining a constructor
    def __init__(self,name,acno,balance):
        self.__name=name
        self.__acno=acno
        self.__balance=balance
    #Method to display the account details
    def display_account_info(self):
        print("Name:",self.__name)
        print("Account Number:",self.__acno)
        print("Balance:",self.__balance)
    #---------------------------------------------------
    #Method to deposit money into the account
    def deposit(self,amount):
        self.__balance+=amount
        print("Amount deposited: Rs.",amount)
        print("Available Balance: Rs.",self.__balance)
    #---------------------------------------------------
    #Method to withdraw money from the account
    def withdraw(self,amount):
        if (self.__balance- amount) < 1000:
            print("Insufficient Balance!")
        else:
            self.__balance-=amount
            print("Amount withdrawn: Rs.",amount)
            print("Available Balance: Rs.",self.__balance)
    #---------------------------------------------------
    #method to display available balance
    def display_balance(self):
        print("Available Balance: Rs.",self.__balance)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#------- Main Program ---------------------------------------------------------------
#Ask the user to enter the account details
name=input("Enter the account holder's name: ")
#to validate name input
if name.isspace():
    exit("Name cannot be empty.")
#---------------------------------------------------------------
acno=int(input("Enter six digitaccount number: "))
#validate account number input
if (acno< 100000 or acno>999999):
    exit("Invalid account number.")
balance=float(input("Enter the initial balance(in Rs) at least 1000: "))
#validate balance input
if balance<1000:
    exit("Initial balance must be at least Rs. 1000.")
#-----------------------------------------------------------------
#create an object of the Account class
account=Account(name,acno,balance)
#menu driven program to perform various operations on the account
while True:
    print("\n------- Account Operations -------")
    print("1. Display Account Information")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Display Available Balance")
    print("5. Exit")
    choice=int(input("Select operation: "))
    if choice==1:
        account.display_account_info()
    elif choice==2:
        amount=float(input("Enter the amount to deposit: Rs."))
        #validate deposit amount input
        if amount<=0:
            print("Deposit amount must be greater than zero.")
        else:
            account.deposit(amount)
    elif choice==3:
        amount=float(input("Enter the amount to withdraw: Rs."))
        #validate withdraw amount input
        if amount<=0:
            print("Withdraw amount must be greater than zero.")
        else:
            account.withdraw(amount)
    elif choice==4:
        account.display_balance()
    elif choice==5:
        print("Thank you for using our services!")
        break
    else:
        print("Invalid choice! Please try again.")
    #---------------------------------------------------------------
    #Ask the user if they want to perform another operation
    another_operation=input("Do you want to perform another operation? (yes/no): ")
    if another_operation.lower()!="yes":
        print("Thank you for using our services!")
        break
    print("\n----------------------------------")

            