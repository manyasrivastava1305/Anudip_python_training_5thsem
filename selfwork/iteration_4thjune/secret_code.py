#Program for a Secret Code Validator
#given condition:-
# 1. it contains exactly 6 digits.
# 2. sum of first 3 digits equals sum of last three digits

# Accept the secret code as input
code = input("Enter a 6-digit secret code: ")

# Check if the code contains exactly 6 digits
if len(code) == 6 and code.isdigit():

    # Calculate sum of first 3 digits
    first_half_sum = int(code[0]) + int(code[1]) + int(code[2])

    # Calculate sum of last 3 digits
    second_half_sum = int(code[3]) + int(code[4]) + int(code[5])

    # Compare both sums
    if first_half_sum == second_half_sum:
        print("Valid Code")
    else:
        print("Invalid Code")

else:
    print("Code must contain exactly 6 digits")
