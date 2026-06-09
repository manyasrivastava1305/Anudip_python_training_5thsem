# An online store wants to manage products and sales. 
# Example Structure 
# products = { 
#     "P101": { 
#         "name": "Laptop", 
#         "price": 55000, 
#         "stock": 12, 
#         "sold": 25 
#     } 
# } 
# Maintain records of at least 30 products. 
# Requirements 
# 1. Display all products.  
# 2. Add a new product.  
# 3. Update stock after sales.  
# 4. Find out-of-stock products.  
# 5. Find products with stock less than 5.  
# 6. Calculate total inventory value.  
# 7. Find best-selling product.  
# 8. Find least-selling product.  
# 9. Calculate total revenue generated.  
# 10. Generate a low-stock report.  
# 11. Display products whose sales exceed the average sales.  
# 12. Create a dictionary of products eligible for promotion (sales < 10).  
# Challenge 
# Generate a complete business report.
# 1. Display all products (Pre-populated with 30 items)
products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
    "P102": {"name": "Smartphone", "price": 20000, "stock": 30, "sold": 50},
    "P103": {"name": "Headphones", "price": 1500, "stock": 100, "sold": 200},
    "P104": {"name": "Smartwatch", "price": 5000, "stock": 20, "sold": 15},
    "P105": {"name": "Keyboard", "price": 1200, "stock": 45, "sold": 80},
    "P106": {"name": "Mouse", "price": 800, "stock": 0, "sold": 120},
    "P107": {"name": "Monitor", "price": 12000, "stock": 8, "sold": 22},
    "P108": {"name": "External HDD", "price": 4500, "stock": 15, "sold": 35},
    "P109": {"name": "SSD", "price": 6000, "stock": 3, "sold": 65},
    "P110": {"name": "Router", "price": 2500, "stock": 18, "sold": 40},
    "P111": {"name": "USB Flash Drive", "price": 600, "stock": 150, "sold": 310},
    "P112": {"name": "Webcam", "price": 3500, "stock": 2, "sold": 18},
    "P113": {"name": "Gaming Chair", "price": 18000, "stock": 4, "sold": 8},
    "P114": {"name": "Desk Lamp", "price": 1100, "stock": 25, "sold": 14},
    "P115": {"name": "Microphone", "price": 5500, "stock": 7, "sold": 29},
    "P116": {"name": "Bluetooth Speaker", "price": 3000, "stock": 40, "sold": 85},
    "P117": {"name": "Graphic Tablet", "price": 8500, "stock": 5, "sold": 12},
    "P118": {"name": "HDMI Cable", "price": 400, "stock": 200, "sold": 450},
    "P119": {"name": "Power Bank", "price": 1800, "stock": 35, "sold": 95},
    "P120": {"name": "Laptop Stand", "price": 1500, "stock": 0, "sold": 42},
    "P121": {"name": "Printer", "price": 14000, "stock": 6, "sold": 11},
    "P122": {"name": "Ink Cartridge", "price": 2200, "stock": 50, "sold": 130},
    "P123": {"name": "Projector", "price": 35000, "stock": 3, "sold": 4},
    "P124": {"name": "VR Headset", "price": 40000, "stock": 8, "sold": 3},
    "P125": {"name": "Case Fan", "price": 900, "stock": 60, "sold": 75},
    "P126": {"name": "Thermal Paste", "price": 500, "stock": 120, "sold": 190},
    "P127": {"name": "CPU Cooler", "price": 4200, "stock": 14, "sold": 28},
    "P128": {"name": "Motherboard", "price": 11500, "stock": 9, "sold": 31},
    "P129": {"name": "RAM Stick 8GB", "price": 3200, "stock": 22, "sold": 115},
    "P130": {"name": "Graphics Card", "price": 45000, "stock": 1, "sold": 19}
}

print("All Products:")
for product_id, details in products.items():
    print(f"ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Stock: {details['stock']}, Sold: {details['sold']}")

# 2. Add a new product.
print("\n--- Add New Product ---")
new_id = input("Enter new Product ID: ")
if new_id not in products:
    new_name = input("Enter new product's name: ")
    new_price = float(input("Enter new product's price: "))
    new_stock = int(input("Enter new product's stock: "))
    new_sold = int(input("Enter new product's sold: "))
    products[new_id] = {"name": new_name, "price": new_price, "stock": new_stock, "sold": new_sold}
    print("Product added successfully.")
else:
    print("Product ID already exists.")

# 3. Update stock after sales.
print("\n--- Update Stock Process ---")
update_id = input("Enter Product ID to update stock after sales: ")
if update_id in products:
    sales = int(input("Enter the number of units sold: "))
    if sales <= products[update_id]["stock"]:
        products[update_id]["stock"] -= sales
        products[update_id]["sold"] += sales
        print("Stock updated successfully.")
    else:
        print("Not enough stock available.")
else:
    print("Product not found.")

# 4. Find out-of-stock products.
print("\n--- Out-of-Stock Products ---")
out_of_stock_count = 0
for product_id, details in products.items():
    if details["stock"] == 0:
        print(f"ID: {product_id}, Name: {details['name']}")
        out_of_stock_count += 1
if out_of_stock_count == 0:
    print("No products are completely out of stock.")

# 5. Find products with stock less than 5.
print("\n--- Products with Stock Less Than 5 ---")
for product_id, details in products.items():
    if details["stock"] < 5:
        print(f"ID: {product_id}, Name: {details['name']}, Stock: {details['stock']}")

# 6. Calculate total inventory value.
total_inventory_value = 0
for product_id, details in products.items():
    total_inventory_value += details["stock"] * details["price"]
print(f"\nTotal Inventory Value: {total_inventory_value}")

# 7. Find best-selling product.
best_selling_product = None
max_sales = -1
for product_id, details in products.items():
    if details["sold"] > max_sales:
        max_sales = details["sold"]
        best_selling_product = details["name"]
print(f"\nBest-Selling Product: {best_selling_product} with {max_sales} units sold")

# 8. Find least-selling product.
least_selling_product = None
min_sales = float('inf')
for product_id, details in products.items():
    if details["sold"] < min_sales:
        min_sales = details["sold"]
        least_selling_product = details["name"]
print(f"Least-Selling Product: {least_selling_product} with {min_sales} units sold")

# 9. Calculate total revenue generated.
total_revenue = 0
for product_id, details in products.items():
    total_revenue += details["sold"] * details["price"]
print(f"\nTotal Revenue Generated: {total_revenue}")

# 10. Generate a low-stock report.
print("\n=== LOW-STOCK REPORT ===")
low_stock_items = 0
for product_id, details in products.items():
    if details["stock"] < 5:
        print(f"WARNING -> ID: {product_id} | Name: {details['name']} | Current Stock: {details['stock']}")
        low_stock_items += 1
print(f"Total items needing immediate reorder: {low_stock_items}")

# 11. Display products whose sales exceed the average sales.
total_sales = 0
for product_id, details in products.items():
    total_sales += details["sold"]
average_sales = total_sales / len(products)
print(f"\nClass Average Units Sold: {average_sales:.2f}")

print("Products with Sales Exceeding Average Sales:")
for product_id, details in products.items():
    if details["sold"] > average_sales:
        print(f"ID: {product_id}, Name: {details['name']}, Sold: {details['sold']}")

# 12. Create a dictionary of products eligible for promotion (sales < 10).
promotional_products = {}
for product_id, details in products.items():
    if details["sold"] < 10:
        promotional_products[product_id] = details

print("\nProducts Eligible for Promotion (Sales < 10):")
for product_id, details in promotional_products.items():
    print(f"ID: {product_id}, Name: {details['name']}, Sold: {details['sold']}")


# ==========================================
# CHALLENGE: Generate a Complete Business Report
# ==========================================
print("\n" + "="*50)
print("             COMPLETE BUSINESS REPORT            ")
print("="*50)

# Aggregating metrics manually via basic loops
total_items_in_catalog = len(products)
total_units_sold = 0
most_profitable_product = None
highest_product_revenue = -1

for product_id, details in products.items():
    total_units_sold += details["sold"]
    product_revenue = details["sold"] * details["price"]
    if product_revenue > highest_product_revenue:
        highest_product_revenue = product_revenue
        most_profitable_product = details["name"]

print(f"1. Overall Portfolio Size   : {total_items_in_catalog} unique items")
print(f"2. Current Inventory Value  : {total_inventory_value} INR")
print(f"3. Total Revenue Generated  : {total_revenue} INR")
print(f"4. Total Volume Sold        : {total_units_sold} units")
print(f"5. Store Star Performer     : {best_selling_product} ({max_sales} units shipped)")
print(f"6. Primary Financial Driver : {most_profitable_product} (Brought in {highest_product_revenue} INR)")
print(f"7. Marketing Focus Group    : {len(promotional_products)} products designated for promo strategies")
print("="*50)
