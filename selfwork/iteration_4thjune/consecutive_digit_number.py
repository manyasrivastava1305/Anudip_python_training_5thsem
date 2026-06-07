# Program to check whether a number is a Consecutive Digit Number
# A Consecutive Digit Number is one in which every digit is exactly 1 greater than the previous digit.
# Example: 12345, -4567 
# Accept number from user
num = input("Enter a number: ")
# Check if the number is negative
# If yes, remove the '-' sign before processing
if num[0] == '-':
    num = num[1:]
# Assume the number is consecutive initially
is_consecutive = True
# Traverse through all digits of the number
for i in range(len(num) - 1):
    # Check whether the next digit is exactly
    # 1 greater than the current digit
    if int(num[i + 1]) != int(num[i]) + 1:
        is_consecutive = False
        break   # Stop checking if condition fails
# Display result
if is_consecutive:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")
