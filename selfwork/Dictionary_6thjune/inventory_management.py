# Inventory Management System 
"""
Sample Data inventory = {     
"Notebook": 45,     
"Pen": 120,     
"Pencil": 80,     
"Eraser": 25,     
"Marker": 15,     
"Stapler": 8,     
"Glue": 12,     
"Scale": 30,     
"Folder": 5,     
"Calculator": 3 }
Tasks 
• Display products with stock less than 10.  
• Count products having stock more than 50.  
• Find the product with the minimum stock.  
• Create a list of products that require restocking (stock < 20).  
• Calculate the total inventory count.  
"""

# Inventory Management System

inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# Task 1: Display products with stock less than 10
print("Task 1: Products with stock less than 10")

for product, stock in inventory.items():
    if stock < 10:
        print(product, ":", stock)

# Task 2: Count products having stock more than 50
count_more_than_50 = 0

for stock in inventory.values():
    if stock > 50:
        count_more_than_50 += 1

print("\nTask 2: Products having stock more than 50 =", count_more_than_50)

# Task 3: Find the product with minimum stock
min_product = min(inventory, key=inventory.get)

print("\nTask 3: Product with minimum stock")
print(min_product, ":", inventory[min_product])

# Task 4: Create a list of products that require restocking
restock_list = []

for product, stock in inventory.items():
    if stock < 20:
        restock_list.append(product)

print("\nTask 4: Products requiring restocking")
print(restock_list)

# Task 5: Calculate the total inventory count
total_inventory = sum(inventory.values())

print("\nTask 5: Total inventory count =", total_inventory)
