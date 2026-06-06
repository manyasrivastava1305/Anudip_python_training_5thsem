#An online store records orders as: 
# orders = [ 
#     ("Laptop", 55000), 
#     ("Mouse", 800), 
#     ("Keyboard", 1500), 
#     ("Monitor", 12000), 
#     ("Pen Drive", 600) 
# ] 
# Write a program to: 
# • Display all products costing more than ₹1000.  
# • Find the most expensive product.  
# • Calculate the total order value.  
# • Count products costing below ₹1000. 
# Initial data
orders = [
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
]

# Initializing variables for tracking data
expensive_product = orders[0]  # Assume the first item is the most expensive initially
total_order_value = 0
below_1000_count = 0

print("--- Products costing more than ₹1000 ---")

# Processing the orders
for product, price in orders:
    # 1. Display products costing more than ₹1000
    if price > 1000:
        print(f"- {product}: ₹{price}")
        
    # 2. Track the most expensive product
    if price > expensive_product[1]:
        expensive_product = (product, price)
        
    # 3. Add to total order value
    total_order_value += price
    
    # 4. Count products costing below ₹1000
    if price < 1000:
        below_1000_count += 1

print("\n--- Summary Statistics ---")
print(f"Most expensive product: {expensive_product[0]} (₹{expensive_product[1]})")
print(f"Total order value: ₹{total_order_value}")
print(f"Number of products below ₹1000: {below_1000_count}")
