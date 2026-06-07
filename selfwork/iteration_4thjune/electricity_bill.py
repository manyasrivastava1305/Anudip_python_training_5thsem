# Electricity Bill Simulator

# Input total electricity units consumed
units = int(input("Enter electricity units consumed: "))

# Calculate bill according to slabs
if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Apply 10% surcharge if bill exceeds ₹5000
if bill > 5000:
    surcharge = bill * 0.10
    bill = bill + surcharge

# Display final bill amount
print("Final Payable Amount = ₹", bill)
