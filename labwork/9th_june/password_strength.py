# A user enters a password. 
# Python@2026! 
# Tasks 
# Write a program to determine whether the password is Strong, Medium, or Weak. 
# Rules: 
# • Minimum length 8  
# • Contains at least:  
# o 1 uppercase letter  
# o 1 lowercase letter  
# o 1 digit  
# o 1 special character  
# Additionally: 
# 1. Count uppercase letters.  
# 2. Count lowercase letters.  
# 3. Count digits.  
# 4. Count special characters.  
# 5. Display all digits separately.  
# 6. Display all special characters separately. 
# Input Password
password = "Python@2026!"

print(f"Analyzing Password: {password}")
print("-" * 40)

# Initialize counters
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

# Lists to store individual characters
digits_list = []
special_list = []

# Loop through each character in the password
for char in password:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
        digits_list.append(char)  # Store the digit
    else:
        # If it's not a letter or a digit, it's a special character
        special_count += 1
        special_list.append(char)  # Store the special character

# Determine total length
password_length = len(password)

# Determine Password Strength
# Rule check variables (True or False)
has_min_length = password_length >= 8
has_upper = upper_count >= 1
has_lower = lower_count >= 1
has_digit = digit_count >= 1
has_special = special_count >= 1

# Check criteria met count
criteria_met = 0
if has_upper:
    criteria_met += 1
if has_lower:
    criteria_met += 1
if has_digit:
    criteria_met += 1
if has_special:
    criteria_met += 1

# Strength logic:
# Strong: Meets minimum length AND all 4 character type rules
# Medium: Meets minimum length AND at least 2 or 3 character type rules
# Weak: Anything less
if has_min_length and criteria_met == 4:
    strength = "Strong"
elif has_min_length and criteria_met >= 2:
    strength = "Medium"
else:
    strength = "Weak"

# --- Output Results ---
print(f"Password Length            : {password_length}")
print(f"1. Uppercase letters       : {upper_count}")
print(f"2. Lowercase letters       : {lower_count}")
print(f"3. Digits count            : {digit_count}")
print(f"4. Special characters count: {special_count}")
print(f"5. Digits found            : {digits_list}")
print(f"6. Special characters found: {special_list}")
print(f"Password Strength          : {strength.upper()}")
print("-" * 40)
