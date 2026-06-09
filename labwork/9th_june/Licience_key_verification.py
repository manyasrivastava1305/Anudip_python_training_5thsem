# A software license key is entered: 
# ABCD-EFGH-IJKL-MNOP 
# Tasks 
# Write a program to: 
# 1. Verify there are exactly 4 groups.  
# 2. Verify each group contains exactly 4 characters.  
# 3. Count total letters.  
# 4. Count vowels.  
# 5. Remove hyphens and display the merged key.  
# 6. Create a list containing all groups.  
# 7. Display whether the key format is valid.
# Input License Key
license_key = "ABCD-EFGH-IJKL-MNOP"

print(f"Analyzing License Key: {license_key}")
print("-" * 45)

# --- Parsing & Grouping ---
# 6. Create a list containing all groups by splitting at the hyphens
groups = license_key.split("-")


# --- Verification and Character Counting ---
# 1. Verify there are exactly 4 groups
has_four_groups = len(groups) == 4

# 2. Verify each group contains exactly 4 characters
each_group_has_four_chars = True
for group in groups:
    if len(group) != 4:
        each_group_has_four_chars = False

# 3 & 4. Count total letters and vowels
total_letters = 0
vowel_count = 0
vowels = "AEIOUaeiou"

for char in license_key:
    if char.isalpha():
        total_letters += 1
        if char in vowels:
            vowel_count += 1


# --- Merging & Validity Check ---
# 5. Remove hyphens and display the merged key
# We can rebuild it using an empty string and a loop
merged_key = ""
for group in groups:
    merged_key += group

# 7. Display whether the key format is valid
# It must pass both group count and character length rules
if has_four_groups and each_group_has_four_chars:
    status = "VALID"
else:
    status = "INVALID"


# --- Output Results ---
print(f"1. Exactly 4 groups found?   : {has_four_groups} ({len(groups)} found)")
print(f"2. Each group has 4 chars?   : {each_group_has_four_chars}")
print(f"3. Total letters in key      : {total_letters}")
print(f"4. Total vowels in key       : {vowel_count}")
print(f"5. Merged Key (No hyphens)   : {merged_key}")
print(f"6. List of groups            : {groups}")
print(f"7. Key Format Status         : {status}")
print("-" * 45)
