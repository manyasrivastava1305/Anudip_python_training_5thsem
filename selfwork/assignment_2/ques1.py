# A cybersecurity company wants to analyze user passwords before allowing account creation. 
# The system should accept at least 15 passwords and generate a security report. 
# Requirements 
# For each password: 
# 1. Count uppercase letters.  
# 2. Count lowercase letters.  
# 3. Count digits.  
# 4. Count special characters.  
# 5. Check minimum length (8 characters).  
# 6. Check if spaces exist.  
# 7. Determine password strength:  
# o Strong  
# o Medium  
# o Weak  
# 8. Display repeated characters.  
# 9. Count vowels and consonants.  
# 10. Identify the most frequently occurring character. 

# Password Analyzer Program

print("--- Password Security Analyzer ---")
print("Please enter at least 15 passwords to generate the report.\n")

passwords = []
counter = 1

# Collect at least 15 passwords
while len(passwords) < 15:
    prompt = "Enter password #" + str(counter) + ": "
    pwd = input(prompt)
    
    # Validation: Ensure the password is not completely empty
    if len(pwd) == 0:
        print("Password cannot be empty. Please try again.")
        continue
        
    passwords.append(pwd)
    counter += 1

print("\n=============================================")
print("             SECURITY REPORT                 ")
print("=============================================\n")

# Process each password
for index, pwd in enumerate(passwords, 1):
    print("---------------------------------------------")
    print("Analyzing Password #", index, ": '", pwd, "'", sep="")
    print("---------------------------------------------")
    
    # Initialize counters
    u_count = 0  # Uppercase
    l_count = 0  # Lowercase
    d_count = 0  # Digits
    s_count = 0  # Special characters
    v_count = 0  # Vowels
    c_count = 0  # Consonants
    
    has_space = False
    
    # Define sets of characters for checking
    vowels = "aeiouAEIOU"
    # Consonants are alphabetic characters that are not vowels
    
    # Track character frequencies for finding duplicates and the most frequent character
    char_frequencies = {}
    
    # Single loop to analyze characters (Highly efficient basic approach)
    for char in pwd:
        # 1 & 2. Count case and find vowels/consonants
        if char.isupper():
            u_count += 1
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
        elif char.islower():
            l_count += 1
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
                
        # 3. Count digits
        elif char.isdigit():
            d_count += 1
            
        # 6. Check if spaces exist
        elif char == " ":
            has_space = True
            s_count += 1  # Spaces are generally treated as special/non-alphanumeric
            
        # 4. Count special characters (anything not a letter or digit)
        else:
            s_count += 1
            
        # Populate frequency dictionary
        if char in char_frequencies:
            char_frequencies[char] += 1
        else:
            char_frequencies[char] = 1

    # 5. Check minimum length
    length = len(pwd)
    meets_length = length >= 8

    # 7. Determine password strength
    # Rule: Strong must be >= 8 chars, have upper, lower, digit, and special, and NO spaces.
    # Medium: >= 8 chars, and has at least two types of characters.
    # Weak: Anything else.
    
    # Count how many distinct character types are present
    types_present = 0
    if u_count > 0: types_present += 1
    if l_count > 0: types_present += 1
    if d_count > 0: types_present += 1
    if s_count > 0: types_present += 1

    if meets_length and types_present == 4 and not has_space:
        strength = "Strong"
    elif meets_length and types_present >= 2:
        strength = "Medium"
    else:
        strength = "Weak"

    # 8. Identify repeated characters
    repeated_chars = []
    for char in char_frequencies:
        if char_frequencies[char] > 1:
            repeated_chars.append(char)

    # 10. Identify the most frequently occurring character
    most_frequent_char = ""
    max_count = 0
    for char in char_frequencies:
        if char_frequencies[char] > max_count:
            max_count = char_frequencies[char]
            most_frequent_char = char

    # --- Print Requirements Output ---
    print("1. Uppercase Letters:", u_count)
    print("2. Lowercase Letters:", l_count)
    print("3. Digits:", d_count)
    print("4. Special Characters:", s_count)
    
    if meets_length:
        print("5. Minimum Length (>= 8): Met (", length, " characters)", sep="")
    else:
        print("5. Minimum Length (>= 8): Failed (Only ", length, " characters)", sep="")
        
    print("6. Contains Spaces:", "Yes" if has_space else "No")
    print("7. Password Strength:", strength)
    
    if len(repeated_chars) > 0:
        print("8. Repeated Characters:", repeated_chars)
    else:
        print("8. Repeated Characters: None")
        
    print("9. Vowels:", v_count, "| Consonants:", c_count)
    print("10. Most Frequent Character: '", most_frequent_char, "' (Appeared ", max_count, " times)", sep="")
    print()

print("=============================================")
print("End of Security Report")
print("=============================================")
