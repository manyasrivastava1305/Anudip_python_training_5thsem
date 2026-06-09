# A student enters: 
# Rahul Sharma 
# Tasks 
# Generate a username using the rules: 
# 1. Remove spaces.  
# 2. Convert to lowercase.  
# 3. Append current year (2026).  
# 4. If username length exceeds 12, keep only first 12 characters.  
# 5. Count vowels in the generated username.  
# 6. Count consonants.  
# 7. Display username statistics.
# Input Student Name
student_name = "Rahul Sharma"

print(f"Original Name: {student_name}")
print("-" * 40)

# --- Username Generation Steps ---

# 1. Remove spaces
username = student_name.replace(" ", "")

# 2. Convert to lowercase
username = username.lower()

# 3. Append current year (2026)
username = username + "2026"

# 4. If username length exceeds 12, keep only first 12 characters
if len(username) > 12:
    username = username[0:12]


# --- Username Analysis Steps ---

# 5 & 6. Count vowels and consonants in the generated username
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in username:
    # Check if character is a letter (ignore the numbers '2026')
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# 7. Display username statistics
print(f"Generated Username  : {username}")
print(f"Total Length        : {len(username)}")
print(f"Vowels Count        : {vowel_count}")
print(f"Consonants Count    : {consonant_count}")
print("-" * 40)
