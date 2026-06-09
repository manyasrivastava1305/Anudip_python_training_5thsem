# A chat application stores a message: 
# Python is awesome and Python is easy to learn 
# Tasks 
# Write a program to: 
# 1. Count total characters.  
# 2. Count total words.  
# 3. Find the longest word.  
# 4. Find the shortest word.  
# 5. Count how many times the word "Python" appears.  
# 6. Create a list of words having more than 4 characters.  
# 7. Display all words starting with a vowel.  
# 8. Count the number of vowels and consonants. 
# Input Message
message = "Python is awesome and Python is easy to learn"

print(f"Analyzing Message: '{message}'")
print("-" * 50)

# --- Task 1: Count total characters ---
# This includes spaces and letters
total_characters = len(message)

# Prepare the words list for the next tasks
# .split() splits the string by spaces into a list of words
words = message.split()

# --- Task 2: Count total words ---
total_words = len(words)

# --- Tasks 3 & 4: Find longest and shortest words ---
# Initialize with the first word
longest_word = words[0]
shortest_word = words[0]

for word in words:
    # If current word is longer than our recorded longest, update it
    if len(word) > len(longest_word):
        longest_word = word
    # If current word is shorter than our recorded shortest, update it
    if len(word) < len(shortest_word):
        shortest_word = word

# --- Task 5: Count occurrences of "Python" ---
python_count = 0
for word in words:
    if word == "Python":
        python_count += 1

# --- Task 6: List of words with more than 4 characters ---
long_words = []
for word in words:
    if len(word) > 4:
        # Avoid adding duplicate words to the list
        if word not in long_words:
            long_words.append(word)

# --- Task 7: Display all words starting with a vowel ---
vowel_words = []
vowels = "aeiouAEIOU"
for word in words:
    # Check if the first character of the word is in the vowels string
    if word[0] in vowels:
        if word not in vowel_words:
            vowel_words.append(word)

# --- Task 8: Count total vowels and consonants ---
vowel_count = 0
consonant_count = 0

for char in message:
    # Check only alphabetic characters (ignore spaces)
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# --- Output Results ---
print(f"1. Total characters                  : {total_characters}")
print(f"2. Total words                       : {total_words}")
print(f"3. Longest word                      : {longest_word}")
print(f"4. Shortest word                     : {shortest_word}")
print(f"5. Occurrences of 'Python'           : {python_count}")
print(f"6. Words with > 4 characters        : {long_words}")
print(f"7. Words starting with a vowel       : {vowel_words}")
print(f"8. Total Vowels: {vowel_count} | Total Consonants: {consonant_count}")
print("-" * 50)
