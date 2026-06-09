# A customer submits a review: 
# This product is excellent excellent excellent and very useful 
# Tasks 
# Write a program to: 
# 1. Count total words.  
# 2. Create a dictionary containing word frequencies.  
# 3. Find the most frequently used word.  
# 4. Find all words appearing only once.  
# 5. Count words having more than 5 characters.  
# 6. Display words in reverse order.  
# 7. Create a list of unique words. 
# Input Review
review = "This product is excellent excellent excellent and very useful"

print(f"Analyzing Review: '{review}'")
print("-" * 50)

# Clean and split the text into a list of words
# .lower() ensures "This" and "this" would be counted as the same word
words = review.lower().split()


# --- Task 1: Count total words ---
total_words = len(words)


# --- Task 2: Create a dictionary containing word frequencies ---
word_frequencies = {}
for word in words:
    if word in word_frequencies:
        word_frequencies[word] += 1
    else:
        word_frequencies[word] = 1


# --- Task 3: Find the most frequently used word ---
most_frequent_word = ""
highest_count = 0

for word, count in word_frequencies.items():
    if count > highest_count:
        highest_count = count
        most_frequent_word = word


# --- Task 4: Find all words appearing only once ---
unique_appearing_once = []
for word, count in word_frequencies.items():
    if count == 1:
        unique_appearing_once.append(word)


# --- Task 5: Count words having more than 5 characters ---
# Note: We check the clean list of words
words_over_5_chars = 0
for word in words:
    if len(word) > 5:
        words_over_5_chars += 1


# --- Task 6: Display words in reverse order ---
# We make a copy of the words list and reverse it
reversed_words = words.copy()
reversed_words.reverse()


# --- Task 7: Create a list of unique words ---
# Convert the dictionary keys directly to a list, as dictionary keys are always unique
unique_words_list = list(word_frequencies.keys())


# --- Output Results ---
print(f"1. Total words                   : {total_words}")
print(f"2. Word frequencies dictionary   : {word_frequencies}")
print(
    f"3. Most frequent word            : '{most_frequent_word}' ({highest_count} times)"
)
print(f"4. Words appearing only once     : {unique_appearing_once}")
print(f"5. Count of words > 5 characters : {words_over_5_chars}")
print(f"6. Words in reverse order        : {reversed_words}")
print(f"7. List of unique words          : {unique_words_list}")
print("-" * 50)
