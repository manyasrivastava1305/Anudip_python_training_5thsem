units = int(input("Enter the total units consumed: "))
bill = 0
category = ""

# Calculate bill based on slab rates
if units <= 100:
    bill = units * 5
    category = "Low Consumption"
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    category = "Medium Consumption"
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    category = "High Consumption"

# Display the required outputs
print("--- Electricity Bill Receipt ---")
print("Units Consumed:", units)
print("Total Bill: ₹" + str(bill))
print("Category:", category)
