# Create a Product class containing product name, quantity, and price per unit. 
# Implement methods to: 
# • Calculate total price.  
# • Update quantity.  
# • Display product details.  
# Sample Output: 
# Product Name : Laptop 
# Quantity     : 2 
# Unit Price   : ₹45000 
# Total Price  : ₹90000 
class Product:
    # 1. Constructor: Sets up private attributes correctly
    def __init__(self, name, quantity, price_per_unit):
        self.__name = name
        self.__quantity = quantity
        self.__price_per_unit = price_per_unit

    # 2. Method to calculate total price
    def calculate_total_price(self):
        return self.__quantity * self.__price_per_unit

    # 3. Method to update quantity directly
    def update_quantity(self, new_quantity):
        self.__quantity = new_quantity

    # 4. Method to display product details using comma separation
    def display_details(self):
        print("Product Name :", self.__name)
        print("Quantity     :", self.__quantity)
        print("Unit Price   : ₹", self.__price_per_unit)
        print("Total Price  : ₹", self.calculate_total_price())


# ------------------ Main Code Block ------------------

print("--- Enter Product Details ---")

# 1. Input and verify Product Name (Alphabet check, spaces allowed for multi-word items)
name_input = input("Enter Product Name: ").strip()
if not name_input.replace(" ", "").isalpha():
    print("[Error] Product Name must contain letters only!")
    exit()

# 2. Input and verify Quantity (Positive whole number check)
qty_input = input("Enter Quantity: ")
if not qty_input.isdigit() or int(qty_input) <= 0:
    print("[Error] Quantity must be a positive whole number greater than zero!")
    exit()
quantity = int(qty_input)

# 3. Input and verify Price per Unit (Positive number check)
price_input = float(input("Enter Price per Unit: ₹"))
if price_input <= 0:
    print("[Error] Price must be a positive number greater than zero!")
    exit()

# Creating the object since all inputs passed verification
prod = Product(name_input, quantity, price_input)

print("\n--- Initial Product Report ---")
# Display initial details
prod.display_details()

print("\n--------------------------------")
# 4. Updating the quantity from the main block
new_qty_input = input("Enter new quantity to update inventory: ")
if not new_qty_input.isdigit() or int(new_qty_input) <= 0:
    print("[Error] Updated quantity must be a positive whole number!")
    exit()
new_quantity = int(new_qty_input)

# Apply update and show revised details
prod.update_quantity(new_quantity)
print("--- Inventory Updated Successfully ---")
prod.display_details()