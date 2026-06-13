# Design a Vehicle class containing: 
# • Vehicle Number  
# • Vehicle Type  
# • Rent per Day  
# Implement methods to: 
# • Accept vehicle details.  
# • Calculate total rental amount based on the number of days rented.  
# • Display the bill.  
# Sample Output: 
# Vehicle Type : Car 
# Days Rented  : 5 
# Total Rent   : ₹10000 
class Vehicle:
    # 1. Constructor: Sets up private attributes correctly
    def __init__(self, vehicle_num, vehicle_type, rent_per_day):
        self.__vehicle_num = vehicle_num
        self.__vehicle_type = vehicle_type
        self.__rent_per_day = rent_per_day

    # 2. Method to calculate total rental amount based on days
    def calculate_total_rent(self, days):
        return self.__rent_per_day * days

    # 3. Method to display the final bill using comma separation
    def display_bill(self, days):
        print("Vehicle Type :", self.__vehicle_type)
        print("Days Rented  :", days)
        print("Total Rent   : ₹", self.calculate_total_rent(days))


# ------------------ Main Code Block ------------------

print("--- Enter Vehicle Details ---")

# 1. Input and verify Vehicle Number (Alphanumeric check)
num_input = input("Enter Vehicle Number: ").strip()
if not num_input.isalnum():
    print("[Error] Vehicle Number must be alphanumeric (letters and numbers only)!")
    exit()

# 2. Input and verify Vehicle Type (Alphabet check)
type_input = input("Enter Vehicle Type (e.g., Car, Bike): ").strip()
if not type_input.isalpha():
    print("[Error] Vehicle Type must contain letters only!")
    exit()

# 3. Input and verify Rent per Day (Positive number check)
rent_input = float(input("Enter Rent per Day: ₹"))
if rent_input <= 0:
    print("[Error] Rent per day must be a positive number greater than zero!")
    exit()

# Creating the object since all vehicle creation details are valid
my_vehicle = Vehicle(num_input, type_input, rent_input)


print("\n--- Rental Booking ---")

# 4. Input and verify Days Rented (Positive whole number check)
days_input = input("Enter Number of Days to Rent: ")
if not days_input.isdigit() or int(days_input) <= 0:
    print("[Error] Number of days must be a positive whole number!")
    exit()
days = int(days_input)


# 5. Displaying the final generated bill
print("\n--- Final Rental Bill ---")
my_vehicle.display_bill(days)