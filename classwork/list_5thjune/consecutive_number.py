# Given list of numbers
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# List to store consecutive pairs (Additional Challenge)
consecutive_pairs = []

# Loop through the list up to the second-to-last element
for i in range(len(numbers) - 1):
    # Check if the next number is exactly 1 greater than the current number
    if numbers[i + 1] == numbers[i] + 1:
        # Print the output as expected
        print(f"{numbers[i]} and {numbers[i + 1]} are consecutive")
        
        # Store the pair as a tuple in the challenge list
        consecutive_pairs.append((numbers[i], numbers[i + 1]))

---
# Additional Challenge Output Verification
print("\n--- Additional Challenge List ---")
print(consecutive_pairs)
