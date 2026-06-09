# A company generates employee IDs in the following format: 
# EMP2026ANUJ458 
# Tasks 
# Write a program to: 
# 1. Count the number of uppercase letters.  
# 2. Count the number of digits.  
# 3. Extract the joining year.  
# 4. Extract the employee name.  
# 5. Check whether the ID follows these rules:  
# o Starts with "EMP"  
# o Contains exactly 4 digits for the year  
# o Ends with exactly 3 digits  
# 6. Create a list containing all digits present in the ID.  
# 7. Find the sum of all digits present in the ID.  
# 8. Display whether the ID is valid or invalid. 
# Input Employee ID
emp_id = "EMP2026ANUJ458"

print(f"Analyzing Employee ID: {emp_id}")
print("-" * 40)

# 1. Count uppercase letters
upper_count = 0
for char in emp_id:
    if char.isupper():
        upper_count += 1

# 2. Count digits
digit_count = 0
for char in emp_id:
    if char.isdigit():
        digit_count += 1

# 3. Extract joining year (Digits at positions 3, 4, 5, 6)
joining_year = emp_id[3:7]

# 4. Extract employee name (Letters between the year and final 3 digits)
# We slice from index 7 up to the last 3 characters
emp_name = emp_id[7:-3]

# 5. Check validation rules
starts_with_emp = emp_id.startswith("EMP")
year_is_4_digits = joining_year.isdigit() and len(joining_year) == 4
ends_with_3_digits = emp_id[-3:].isdigit()

# 6. Create a list containing all digits present in the ID
all_digits = []
for char in emp_id:
    if char.isdigit():
        all_digits.append(int(char))

# 7. Find the sum of all digits
digit_sum = sum(all_digits)

# 8. Display whether the ID is valid or invalid
# It must pass all three validation rules checked in step 5
if starts_with_emp and year_is_4_digits and ends_with_3_digits:
    status = "VALID"
else:
    status = "INVALID"

# --- Output Results ---
print(f"1. Number of uppercase letters : {upper_count}")
print(f"2. Number of digits            : {digit_count}")
print(f"3. Joining year                : {joining_year}")
print(f"4. Employee name               : {emp_name}")
print(f"6. List of all digits          : {all_digits}")
print(f"7. Sum of all digits           : {digit_sum}")
print(f"8. Status                      : {status}")
print("-" * 40)
