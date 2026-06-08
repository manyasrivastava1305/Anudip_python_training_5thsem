# An e-commerce company stores product sales data as: 
# sales = { 
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
# 1. Display products sold more than 20 times.  
# 2. Find the best-selling product.  
# 3. Find the least-selling product.  
# 4. Calculate total products sold.  
# 5. Create a list of products requiring promotion (sales < 15).  
# 6. Count products having sales between 10 and 30. 
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25,
}
# --- Task 1: Display products sold more than 20 times ---
print("--- Products sold more than 20 times ---")
sales=list(sales.items())
for item in sales:
    if item[1]>20:
        print(item[0],":",item[1])
print(  "\n" + "-" * 40)
# --- Task 2: Find the best-selling product ---
best_selling = sales[0][0]
best_sales = sales[0][1]
for item in sales:
    if item[1]>best_sales:
        best_selling = item[0]
        best_sales = item[1]
print("\nBest-selling product:", best_selling, "with sales of", best_sales)
print(  "\n" + "-" * 40)
# --- Task 3: Find the least-selling product ---    
least_selling = sales[0][0]
least_sales = sales[0][1]
for item in sales:
    if item[1] < least_sales:
        least_selling = item[0]
        least_sales = item[1]
print("Least-selling product:", least_selling, "with sales of", least_sales)
print(  "\n" + "-" * 40)
# --- Task 4: Calculate total products sold ---
total_sales = sum(item[1] for item in sales)
print("\nTotal products sold:", total_sales)
print(  "\n" + "-" * 40)
# --- Task 5: Create a list of products requiring promotion (sales < 15) ---
list_promotion = []
for items in sales:
    if items[1]<15:
        list_promotion.append(items[0])
print("\nProducts requiring promotion (sales < 15):", list_promotion)
print(  "\n" + "-" * 40)
# --- Task 6: Count products having sales between 10 and 30 --- 
count = 0
for items in sales:
    if 10 <= items[1] <= 30:
        count += 1
print("\nNumber of products with sales between 10 and 30:", count)
print(  "\n" + "-" * 40)
