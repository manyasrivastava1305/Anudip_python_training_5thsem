# Product Price Analysis 
"""
Sample Data prices = {     
"Laptop": 55000,     
"Mouse": 800,     
"Keyboard": 1800,     
"Monitor": 12000,     
"Printer": 9000,     
"Tablet": 28000,     
"Speaker": 3500,     
"Webcam": 2500,     
"Headphones": 4200,     
"Router": 3200 
} 
Tasks 
• Display products costing more than ₹5000.  
• Count products costing less than ₹3000.  
• Find the most expensive product.  
• Create a list of products priced between ₹2000 and ₹10000.  
• Calculate the total value of all products. 
"""

# Product Price Analysis

prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# Task 1: Display products costing more than ₹5000
print("Task 1: Products costing more than ₹5000")

for product, price in prices.items():
    if price > 5000:
        print(product, ":", price)

# Task 2: Count products costing less than ₹3000
count_less_than_3000 = 0

for price in prices.values():
    if price < 3000:
        count_less_than_3000 += 1

print("\nTask 2: Products costing less than ₹3000 =", count_less_than_3000)

# Task 3: Find the most expensive product
most_expensive = max(prices, key=prices.get)

print("\nTask 3: Most expensive product")
print(most_expensive, ":", prices[most_expensive])

# Task 4: Create a list of products priced between ₹2000 and ₹10000
product_list = []

for product, price in prices.items():
    if 2000 <= price <= 10000:
        product_list.append(product)

print("\nTask 4: Products priced between ₹2000 and ₹10000")
print(product_list)

# Task 5: Calculate the total value of all products
total_value = sum(prices.values())

print("\nTask 5: Total value of all products =", total_value)
