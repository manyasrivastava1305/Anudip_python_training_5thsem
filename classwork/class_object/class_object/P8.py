# Create a MobilePhone class to store: 
# • Brand Name  
# • Model Name  
# • Price  
# • Available Stock  
# Implement methods to: 
# • Display phone details.  
# • Sell a specified quantity of phones.  
# • Update stock after sale.  
# Display an appropriate message if sufficient stock is unavailable. 
# Sample Output: 
# Sale Successful. 
# Remaining Stock: 12
class MobilePhone:
    # 1. Constructor: Sets up private attributes correctly
    def __init__(self, brand, model, price, stock):
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__stock = stock

    # 2. Method to sell a specified quantity and update stock
    def sell_phones(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            print("Sale Successful.")
            print("Remaining Stock:", self.__stock)
        else:
            print("[Error] Sufficient stock is unavailable!")
            print("Available Stock is only:", self.__stock)

    # 3. Method to display phone details using comma separation
    def display_details(self):
        print("Brand Name     :", self.__brand)
        print("Model Name     :", self.__model)
        print("Price          : ₹", self.__price)
        print("Available Stock:", self.__stock)


# ------------------ Main Code Block ------------------

print("--- Enter Mobile Phone Details ---")

# 1. Input and verify Brand Name (Alphabet check, spaces allowed for multi-word brands)
brand_input = input("Enter Brand Name: ").strip()
if not brand_input.replace(" ", "").isalpha():
    print("[Error] Brand Name must contain letters only!")
    exit()

# 2. Input and verify Model Name (Alphanumeric check, spaces allowed)
model_input = input("Enter Model Name: ").strip()
if not model_input.replace(" ", "").isalnum():
    print("[Error] Model Name must be alphanumeric!")
    exit()

# 3. Input and verify Price (Positive number check)
price_input = float(input("Enter Price: ₹"))
if price_input <= 0:
    print("[Error] Price must be a positive number greater than zero!")
    exit()

# 4. Input and verify Available Stock (Positive whole number check)
stock_input = input("Enter Available Stock: ")
if not stock_input.isdigit() or int(stock_input) < 0:
    print("[Error] Stock must be a valid positive whole number!")
    exit()
initial_stock = int(stock_input)

# Creating the object since all entry values passed validation
phone = MobilePhone(brand_input, model_input, price_input, initial_stock)


print("\n--- Initial Product Report ---")
# Display details before processing any orders
phone.display_details()


print("\n--------------------------------")
# 5. Input and verify Sale Quantity from the main block
qty_input = input("Enter quantity of phones to sell: ")
if not qty_input.isdigit() or int(qty_input) <= 0:
    print("[Error] Sale quantity must be a positive whole number greater than zero!")
    exit()
sell_quantity = int(qty_input)


print("\n--- Processing Sale ---")
# Execute the sale and show the final remaining stock status
phone.sell_phones(sell_quantity)