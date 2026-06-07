# Program for Coin Change Counter 
# Problem Statement: 
# Given an amount, 
# determine the minimum number of notes required using: ₹500, ₹200, ₹100, ₹50, ₹20, ₹10 

# Input the amount
amount = int(input("Enter the amount: "))

# List of available note denominations
notes = [500, 200, 100, 50, 20, 10]

print("\nMinimum notes required:")

# Calculate notes one by one
for note in notes:
    count = amount // note  # Number of notes of current denomination

    if count > 0:
        print(note, "x", count)

    amount = amount % note  # Remaining amount
