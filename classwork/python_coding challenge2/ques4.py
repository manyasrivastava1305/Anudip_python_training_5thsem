# Online store stock quantities of products: 
# inventory = { 
#     "Laptop": 15, 
#     "Mouse": 45, 
#     "Keyboard": 32, 
#     "Monitor": 12, 
#     "Headphones": 28, 
#     "Printer": 8, 
#     "Webcam": 20, 
#     "Speaker": 18, 
#     "Tablet": 10, 
#     "Router": 25 
# } 
# Tasks 
# 1. Display products with stock below 15 units.  
# 2. Find the product with maximum stock.  
# 3. Find the product with minimum stock.  
# 4. Calculate total stock available.  
# 5. Create a list of products requiring restocking (<10 units). 

inventory = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
}

# --- Task 1: Display products with stock below 15 units ---
print("--- Products with stock below 15 units ---")
inventory_items = list(inventory.items())
for item in inventory_items:
    if item[1] < 15:
        print(item[0], ":", item[1])
print("\n" + "-" * 40)

# --- Task 2: Find the product with maximum stock ---
print("--- Product with Maximum Stock ---")
max_stock_product = inventory_items[0][0]
max_stock_count = inventory_items[0][1]
for item in inventory_items:
    if item[1] > max_stock_count:
        max_stock_product = item[0]
        max_stock_count = item[1]
print("Maximum Stock:", max_stock_product, "with", max_stock_count, "units")
print("\n" + "-" * 40)

# --- Task 3: Find the product with minimum stock ---
print("--- Product with Minimum Stock ---")
min_stock_product = inventory_items[0][0]
min_stock_count = inventory_items[0][1]
for item in inventory_items:
    if item[1] < min_stock_count:
        min_stock_product = item[0]
        min_stock_count = item[1]
print("Minimum Stock:", min_stock_product, "with", min_stock_count, "units")
print("\n" + "-" * 40)

# --- Task 4: Calculate total stock available ---
print("--- Total Stock Available ---")
total_stock = 0
for item in inventory_items:
    total_stock += item[1]
print("Total stock available:", total_stock)
print("\n" + "-" * 40)

# --- Task 5: Create a list of products requiring restocking (<10 units) ---
print("--- Products requiring restocking ---")
restock_list = []
for item in inventory_items:
    if item[1] < 10:
        restock_list.append(item[0])
print("Products requiring restocking (<10 units):", restock_list)
print("\n" + "-" * 40)
