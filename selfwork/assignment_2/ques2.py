# Email Address Analyzer Program

print("--- Email Address Analyzer ---")
print("Please enter exactly 20 email addresses to generate the report.\n")

emails = []
counter = 1

# Collect exactly 20 email addresses
while len(emails) < 20:
    prompt = "Enter email address #" + str(counter) + ": "
    email_input = input(prompt)
    
    # Validation: Ensure the user doesn't pass a completely empty input
    if len(email_input.strip()) == 0:
        print("Email cannot be empty. Please try again.")
        continue
        
    emails.append(email_input)
    counter += 1

# Dictionaries/Lists to keep track of global organization data
invalid_emails = []
domain_counts = {}

print("\n=============================================")
print("             EMAIL ANALYSIS REPORT            ")
print("=============================================\n")

# Process each email
for index, email in enumerate(emails, 1):
    print("---------------------------------------------")
    print("Analyzing Email #", index, ": '", email, "'", sep="")
    print("---------------------------------------------")
    
    # --- 6. Check if email is valid ---
    # Rule A: Exactly one '@'
    at_count = 0
    for char in email:
        if char == "@":
            at_count += 1
            
    # Rule B: Contains '.'
    has_dot = "." in email
    
    # Rule C: No spaces
    has_space = " " in email
    
    # Determine overall validity
    is_valid = (at_count == 1) and has_dot and (not has_space)
    
    if not is_valid:
        # 7. Add to invalid tracker
        invalid_emails.append(email)
        print("Status: INVALID EMAIL")
        print("Reason: Fails basic structure rules (Check @, spaces, or dots).")
        print()
        continue # Skip extraction for invalid emails to prevent program crashes
        
    print("Status: VALID EMAIL")
    
    # --- 1, 2, & 3. Extract Username, Domain, and Extension ---
    # Split username and the rest using the '@' symbol
    at_index = email.find("@")
    username = email[:at_index]
    domain_part = email[at_index + 1:] # Everything after '@'
    
    # Split domain and extension using the last '.' found in the domain part
    dot_index = domain_part.rfind(".")
    domain = domain_part[:dot_index]
    extension = domain_part[dot_index + 1:]
    
    # --- 4. Count digits in username ---
    digit_count = 0
    for char in username:
        if char.isdigit():
            digit_count += 1
            
    # --- 5. Count special characters in entire email ---
    # Special characters are anything that is NOT a letter or a digit
    special_count = 0
    for char in email:
        if not char.isalnum():
            special_count += 1
            
    # --- 8. Track domain counts globally ---
    # We combine domain and extension to properly identify unique entities (e.g., gmail.com)
    full_domain = domain + "." + extension
    if full_domain in domain_counts:
        domain_counts[full_domain] += 1
    else:
        domain_counts[full_domain] = 1
        
    # --- Print individual results ---
    print("1. Username Extracted:", username)
    print("2. Domain Extracted:", domain)
    print("3. Extension Extracted:", extension)
    print("4. Digits in Username:", digit_count)
    print("5. Special Characters Total:", special_count)
    print()

print("=============================================")
print("             ORGANIZATION SUMMARY            ")
print("=============================================\n")

# 7. Display all invalid emails accumulated
print("--- 7. Invalid Emails List ---")
if len(invalid_emails) > 0:
    for inv_email in invalid_emails:
        print("-", inv_email)
else:
    print("None! All entered emails were structurally valid.")

print()

# 8. Display accumulated count for each domain
print("--- 8. Domain Distribution Count ---")
if len(domain_counts) > 0:
    for dom, count in domain_counts.items():
        print("Domain: '", dom, "' -> Total Emails: ", count, sep="")
else:
    print("No valid domains processed.")

print("\n=============================================")
print("End of Report")
print("=============================================")
