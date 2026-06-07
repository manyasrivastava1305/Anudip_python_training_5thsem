#Check whether the left half of a number is identical to the right half
#example:-
# Input: 123123
# Output: Mirror Number
# Input: 123456
# Output: Not a Mirror Number

# Number Mirror Check

# Accept a number from the user
num = input("Enter a number: ")

# Check if the number has even digits
if len(num) % 2 != 0:
    print("Mirror check is possible only for even-digit numbers.")
else:
    # Find the middle position
    mid = len(num) // 2

    # Extract left half and right half
    left_half = num[:mid]
    right_half = num[mid:]

    # Compare both halves
    if left_half == right_half:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")
