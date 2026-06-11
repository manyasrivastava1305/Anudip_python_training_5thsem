# The prices of products added to a shopping cart are stored below. 
# Sample Data 
# cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
# Tasks 
# 1. Calculate the total cart value.  
# 2. Find the most expensive and cheapest products.  
# 3. Count products eligible for premium shipping (price > ₹1000).  
# 4. Generate a discount list (products above ₹1500).  
# 5. Calculate the average product price. 
# Sample Data
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

# --- Validation: Ensure the cart is not empty before processing ---
if not cart:
    print("Error: The shopping cart is empty! Cannot perform calculations.")
else:
    # 1. Calculate the total cart value
    total_val = sum(cart)
    print("Total Cart Value: ₹", total_val)

    # 2. Find the most expensive and cheapest products
    most_expensive = max(cart)
    cheapest = min(cart)
    print("Most Expensive Product: ₹", most_expensive)
    print("Cheapest Product: ₹", cheapest)

    # 3. Count products eligible for premium shipping (price > 1000)
    premium_count = 0
    for price in cart:
        if price < 0:
            continue
        if price > 1000:
            premium_count += 1
    print("Premium Shipping Eligible Products:", premium_count)

    # 4. Generate a discount list (products above 1500)
    discount_list = []
    for price in cart:
        if price > 1500:
            discount_list.append(price)
            
    # Validation: Handle the case where no items qualify for a discount
    print("Discount Eligible Products:")
    if not discount_list:
        print("No products qualify for a discount.")
    else:
        print(discount_list)

    # 5. Calculate the average product price
    avg_price = total_val / len(cart)
    # Using round() to keep the decimal output clean without using f-strings
    print("Average Product Price: ₹", round(avg_price, 2))
