#An inventory manager stores stock quantities as: 
# stock = [25, 5, 0, 12, 3, 18, 0, 30] 
# Write a program to: 
# 1. Display products that are out of stock.  
# 2. Display products that need restocking (quantity less than 10).  
# 3. Count available products.  
# 4. Create a new list containing only products with stock greater than or equal to 15. 
stock = [25, 5, 0, 12, 3, 18, 0, 30] 

# Initialize containers and counters
out_of_stock = []
restock = []
available_count = 0
high_stock = []

# Loop through the stock to evaluate each item
for item in stock:
    # 1. Check for out of stock
    if item == 0:
        out_of_stock.append(item)
    
    # 2. Check if it needs restocking (quantity less than 10)
    if item < 10:
        restock.append(item)
        
    # 3. Count available products (anything with stock greater than 0)
    if item > 0:
        available_count += 1
        
    # 4. Filter products with stock greater than or equal to 15
    if item >= 15:
        high_stock.append(item)

# --- Displaying the Results ---
print(f"1. Products out of stock (quantity 0): {out_of_stock} (Total: {len(out_of_stock)})")
print(f"2. Products that need restocking (< 10): {restock}")
print(f"3. Total number of available products: {available_count}")
print(f"4. Products with high stock (>= 15): {high_stock}")


    
    
