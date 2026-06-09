# A compressed message is given: 
# AAABBBCCCDDDAAA 
# Tasks 
# Write a program to: 
# 1. Count occurrences of each character.  
# 2. Create a dictionary of character frequencies.  
# 3. Display unique characters.  
# 4. Find the most frequent character.  
# 5. Create a compressed output:  
# A3B3C3D3A3 
# 6. Calculate compression ratio.  
# Input Compressed Message
message = "AAABBBCCCDDDAAA"

print(f"Original Message: {message}")
print("-" * 45)

# --- Tasks 1 & 2: Count occurrences & Create Frequency Dictionary ---
# (This tracks overall counts throughout the whole string)
frequency_dict = {}
for char in message:
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1


# --- Task 3: Unique Characters ---
# Dictionary keys are automatically unique
unique_characters = list(frequency_dict.keys())


# --- Task 4: Find the Most Frequent Character ---
most_frequent_char = ""
highest_count = 0
for char, count in frequency_dict.items():
    if count > highest_count:
        highest_count = count
        most_frequent_char = char


# --- Task 5: Create a Compressed Output (Run-Length Encoding) ---
# We loop through the string and count consecutive matching characters
compressed_output = ""

if len(message) > 0:
    current_char = message[0]
    consecutive_count = 1

    # Loop starting from the second character
    for i in range(1, len(message)):
        if message[i] == current_char:
            consecutive_count += 1
        else:
            # Character changed! Append the old character and its count
            compressed_output += current_char + str(consecutive_count)
            # Reset for the new character
            current_char = message[i]
            consecutive_count = 1

    # Don't forget to append the final character group after the loop ends
    compressed_output += current_char + str(consecutive_count)


# --- Task 6: Calculate Compression Ratio ---
# Formula: (Compressed Length / Original Length)
# Lower ratio means better compression!
original_length = len(message)
compressed_length = len(compressed_output)
compression_ratio = compressed_length / original_length


# --- Output Results ---
print(f"1 & 2. Character Frequencies : {frequency_dict}")
print(f"3. Unique Characters        : {unique_characters}")
print(
    f"4. Most Frequent Character  : '{most_frequent_char}' ({highest_count} times)"
)
print(f"5. Compressed Output        : {compressed_output}")
print(f"6. Original Length          : {original_length}")
print(f"   Compressed Length        : {compressed_length}")
print(f"   Compression Ratio        : {compression_ratio:.2f}")
print("-" * 45)
