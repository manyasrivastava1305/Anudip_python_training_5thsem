# Create an ElectricityBill class containing: 
# • Consumer Name  
# • Consumer Number  
# • Units Consumed  
# Implement methods to: 
# • Calculate electricity charges using the following slab:  
# Units Rate 
# First 100 units ₹5/unit 
# Next 100 units ₹7/unit 
# Above 200 units ₹10/unit 
# • Display the final bill.
class ElectricityBill:
    # 1. Constructor: Sets up private attributes correctly
    def __init__(self, consumer_name, consumer_num, units_consumed):
        self.__consumer_name = consumer_name
        self.__consumer_num = consumer_num
        self.__units_consumed = units_consumed

    # 2. Method to calculate electricity charges using a slab rate
    def calculate_bill_amount(self):
        units = self.__units_consumed
        bill_amount = 0

        if units <= 100:
            # First 100 units slab
            bill_amount = units * 5
        elif units <= 200:
            # First 100 units at ₹5 + remainder at ₹7
            bill_amount = (100 * 5) + ((units - 100) * 7)
        else:
            # First 100 units at ₹5 + Next 100 units at ₹7 + remainder at ₹10
            bill_amount = (100 * 5) + (100 * 7) + ((units - 200) * 10)

        return bill_amount

    # 3. Method to display the final bill using comma separation
    def display_bill(self):
        print("Consumer Name :", self.__consumer_name)
        print("Consumer Num  :", self.__consumer_num)
        print("Units Consumed:", self.__units_consumed)
        print("Total Charges : ₹", self.calculate_bill_amount())


# ------------------ Main Code Block ------------------

print("--- Enter Electricity Bill Details ---")

# 1. Input and verify Consumer Name (Alphabet check, spaces allowed for full names)
name_input = input("Enter Consumer Name: ").strip()
if not name_input.replace(" ", "").isalpha():
    print("[Error] Consumer Name must contain letters only!")
    exit()

# 2. Input and verify Consumer Number (Alphanumeric check)
num_input = input("Enter Consumer Number: ").strip()
if not num_input.isalnum():
    print("[Error] Consumer Number must be alphanumeric (letters and numbers only)!")
    exit()

# 3. Input and verify Units Consumed (Positive whole number check)
units_input = input("Enter Units Consumed: ")
if not units_input.isdigit() or int(units_input) < 0:
    print("[Error] Units consumed must be a valid positive whole number!")
    exit()
units = int(units_input)


# Creating the object since all entry values passed validation
ebill = ElectricityBill(name_input, num_input, units)


print("\n--- Final Generated Bill ---")
# Displaying final calculated bill matching the requirement
ebill.display_bill()