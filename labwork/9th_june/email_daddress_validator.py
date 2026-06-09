# A user enters an email address: 
# rahul.sharma2026@gmail.com 
# Tasks 
# Write a program to: 
# 1. Extract username.  
# 2. Extract domain name.  
# 3. Extract extension.  
# 4. Count digits present in username.  
# 5. Count special characters.  
# 6. Check whether:  
# o Exactly one '@' exists.  
# o At least one '.' exists after '@'.  
# 7. Display Valid Email or Invalid Email. 
# Input Email Address
email = "rahul.sharma2026@gmail.com"

print(f"Analyzing Email Address: {email}")
print("-" * 50)

# --- Pre-validation Split ---
# We split the email into two parts using the '@' symbol
# part_1 will be the username, part_2 will be the domain details
email_parts = email.split("@")

# Initialize extraction variables with fallback values if '@' is missing
username = ""
domain_name = ""
extension = ""

if len(email_parts) == 2:
    username = email_parts[0]
    domain_part = email_parts[1]

    # Split the domain part by the last dot to separate domain and extension
    if "." in domain_part:
        # rsplit('.', 1) splits from the right side exactly once
        domain_name, extension = domain_part.rsplit(".", 1)
    else:
        domain_name = domain_part
else:
    # Fallback if the email is completely malformed
    username = email.split("@")[0]

# --- Task 4 & 5: Counting Characters ---
digit_count = 0
special_count = 0

# Count digits specifically in the username
for char in username:
    if char.isdigit():
        digit_count += 1

# Count special characters in the entire email
# Special characters are anything that is NOT a letter and NOT a digit
for char in email:
    if not char.isalnum():
        special_count += 1


# --- Task 6 & 7: Verification and Validity ---
# Rule 1: Exactly one '@' exists
at_count_correct = email.count("@") == 1

# Rule 2: At least one '.' exists after '@'
dot_after_at = False
if at_count_correct:
    # Find the position of '@' and check if a dot exists anywhere after it
    at_index = email.find("@")
    if "." in email[at_index:]:
        dot_after_at = True

# Final Status Check
if at_count_correct and dot_after_at:
    status = "Valid Email"
else:
    status = "Invalid Email"


# --- Output Results ---
print(f"1. Username                  : {username}")
print(f"2. Domain Name               : {domain_name}")
print(f"3. Extension                 : {extension}")
print(f"4. Digits in Username        : {digit_count}")
print(f"5. Total Special Characters  : {special_count}")
print(f"7. Email Status              : {status}")
print("-" * 50)
