# Input total number of elements
n = int(input("Enter the number of elements: "))
# Read first number
prev = int(input("Enter number 1: "))
# Current increasing sequence length
current_length = 1
# Longest increasing sequence length
max_length = 1
# Input remaining numbers
for i in range(2, n + 1):
    num = int(input(f"Enter number {i}: "))

    # Check if current number is greater than previous number
    if num > prev:
        current_length += 1
    else:
        # Sequence breaks, start new sequence
        current_length = 1

    # Update maximum length if needed
    if current_length > max_length:
        max_length = current_length

    # Store current number as previous for next comparison
    prev = num

# Display result
print("Longest Sequence Length =", max_length)
