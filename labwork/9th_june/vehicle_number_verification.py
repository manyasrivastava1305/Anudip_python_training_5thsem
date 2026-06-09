
# Input Vehicle Number Plate
plate = "MH12AB4589"

print(f"Analyzing Number Plate: {plate}")
print("-" * 40)

# --- Parsing Tasks (Slicing) ---
# 1. Extract state code (First 2 characters)
state_code = plate[0:2]

# 2. Extract district code (Next 2 characters)
district_code = plate[2:4]

# 3. Extract vehicle series (Next 2 characters)
series = plate[4:6]

# 4. Extract vehicle number (Last 4 characters)
vehicle_number = plate[6:10]


# --- Task 5: Count letters and digits separately ---
letter_count = 0
digit_count = 0

for char in plate:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1


# --- Task 6 & 7: Verification and Validity ---
# Check total length first (Must be exactly 10 characters)
correct_length = len(plate) == 10

# Rule checks based on position
rule_1 = state_code.isalpha()  # First 2 must be alphabets
rule_2 = district_code.isdigit()  # Next 2 must be digits
rule_3 = series.isalpha()  # Next 2 must be alphabets
rule_4 = vehicle_number.isdigit()  # Last 4 must be digits

# Determine validity
if correct_length and rule_1 and rule_2 and rule_3 and rule_4:
    status = "VALID"
else:
    status = "INVALID"


# --- Output Results ---
print(f"1. State Code        : {state_code}")
print(f"2. District Code     : {district_code}")
print(f"3. Vehicle Series    : {series}")
print(f"4. Vehicle Number    : {vehicle_number}")
print(f"5. Total Letters     : {letter_count}")
print(f"   Total Digits      : {digit_count}")
print(f"7. Status            : {status}")
print("-" * 40)
