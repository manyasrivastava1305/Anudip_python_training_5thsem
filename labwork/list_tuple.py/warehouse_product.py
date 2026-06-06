# Problem Statement 
# Product IDs and quality status: 
# products = [ 
#     (101, "Pass"), 
#     (102, "Fail"), 
#     (103, "Pass"), 
#     (104, "Fail"), 
#     (105, "Pass") 
# ] 
# Write a program to: 
# • Display failed product IDs.  
# • Count passed and failed products.  
# • Calculate pass percentage.  
# • Stop checking if 3 failures are found. 
# Product quality control data stored as tuples (Product ID, Status)
products = [ 
    (101, "Pass"), 
    (102, "Fail"), 
    (103, "Pass"), 
    (104, "Fail"), 
    (105, "Pass") 
] 

# Initialize variables
passed_count = 0
failed_count = 0
failed_product_ids = []

# Scan through the manufacturing data
for product_id, status in products:
    # Check if 3 failures have already been recorded before processing
    if failed_count == 3:
        print("Alert: 3 failures reached. Stopping inspection.")
        break
        
    if status == "Pass":
        passed_count += 1
    elif status == "Fail":
        failed_count += 1
        failed_product_ids.append(product_id)

# Calculate pass percentage
total_checked = passed_count + failed_count
# Prevent DivisionByZero error if the list is empty
if total_checked > 0:
    pass_percentage = (passed_count / total_checked) * 100
else:
    pass_percentage = 0.0

# Display the final report
print("--- Quality Control Report ---")
print("Failed Product IDs:", failed_product_ids)
print("Total Passed Products:", passed_count)
print("Total Failed Products:", failed_count)
print("Pass Percentage:", pass_percentage, "%")
