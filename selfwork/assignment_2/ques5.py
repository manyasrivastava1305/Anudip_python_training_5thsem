# News Article Content Analyzer Program

print("--- News Article Content Analyzer ---")

# A sample news article paragraph containing over 300 words
article = (
    "The rapid advancement of artificial intelligence technologies has fundamentally changed "
    "how modern global industries operate on a daily basis. Healthcare systems are currently "
    "using smart algorithms to detect anomalies in medical imaging much faster than traditional "
    "methods, allowing doctors to provide treatment early. Financial institutions rely heavily "
    "on machine learning models to detect fraudulent transactions instantly across global networks, "
    "ensuring that customer data remains secure. Meanwhile, the transportation sector is shifting "
    "toward autonomous systems and smart traffic routing to reduce carbon emissions in crowded cities. "
    "However, this sudden digital transformation also introduces significant challenges that society "
    "must address. Data privacy has become a major concern as massive amounts of personal information "
    "are collected every single second. Cybersecurity threats are growing more sophisticated every "
    "day, forcing organizations to invest heavily in advanced protective infrastructure. There is "
    "also an urgent debate about how automation might impact the global workforce over the next "
    "decade. Many fear that automated machines will completely replace human workers in manufacturing "
    "and administrative roles, leading to widespread unemployment. Economists suggest that while "
    "some traditional jobs will disappear, entirely new industries will emerge to create fresh "
    "employment opportunities. Education systems must adapt quickly to teach students the vital digital "
    "skills required for this new technology driven economy. Governments and private organizations "
    "need to collaborate effectively to establish strict ethical guidelines for artificial intelligence "
    "development. Innovation should never come at the cost of basic human rights or societal safety. "
    "As we move forward into this highly automated future, maintaining a proper balance between "
    "technological progress and ethical responsibility will be the ultimate test for humanity."
)

print("Successfully loaded the article paragraph for analysis.\n")

# --- 1. Count total characters ---
total_characters = len(article)

# --- 3. Count total sentences ---
# A basic sentence counter that checks for terminal punctuation marks
total_sentences = 0
for char in article:
    if char == "." or char == "?" or char == "!":
        total_sentences += 1

# --- 4. Count vowels and consonants ---
v_count = 0
c_count = 0
vowels = "aeiouAEIOU"

for char in article:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

# --- Isolate and clean words ---
# Split by spaces to isolate individual word packages
raw_words = article.split()
words = []

for w in raw_words:
    # Remove surrounding punctuation marks to get the exact word
    clean_w = w.strip(".,!?\"'()[]")
    if clean_w: # Keep it if it is not empty
        words.append(clean_w)

# --- 2. Count total words ---
total_words = len(words)

# Ensure there is text present before processing deeper mechanics
if total_words > 0:
    # Initialize extreme values using the first word entry
    longest_word = words[0]
    shortest_word = words[0]
    
    # --- 8. Create a dictionary of word frequencies ---
    word_frequencies = {}
    
    # --- 11. Count words starting with each alphabet ---
    alphabet_counts = {}
    
    for w in words:
        # 5 & 6. Track lengths
        if len(w) > len(longest_word):
            longest_word = w
        if len(w) < len(shortest_word):
            shortest_word = w
            
        # Standardize to lowercase for accurate frequency tracking
        w_lower = w.lower()
        if w_lower in word_frequencies:
            word_frequencies[w_lower] += 1
        else:
            word_frequencies[w_lower] = 1
            
        # Track starting alphabets (case-insensitive)
        first_letter = w_lower[0]
        if first_letter.isalpha():
            if first_letter in alphabet_counts:
                alphabet_counts[first_letter] += 1
            else:
                alphabet_counts[first_letter] = 1

    # --- 7. Find the most frequent word ---
    most_frequent_word = ""
    max_frequency = 0
    
    # --- 9, 10 & 12. Separate specialized word groupings ---
    unique_words = []       # 12. Display all unique words
    appearing_once = []     # 9. Display words appearing only once
    more_than_five = []     # 10. Display words appearing more than 5 times
    
    for word, freq in word_frequencies.items():
        # Update most frequent word values
        if freq > max_frequency:
            max_frequency = freq
            most_frequent_word = word
            
        # Add to unique list (representing every individual word type present)
        unique_words.append(word)
        
        # Frequency conditions
        if freq == 1:
            appearing_once.append(word)
        elif freq > 5:
            more_than_five.append(word)

    # Sort alphabet dictionary keys alphabetically for a cleaner report display
    sorted_alphabets = sorted(alphabet_counts.keys())

    # --- Print Metrics Summary ---
    print("=============================================")
    print("             ARTICLE ANALYSIS REPORT         ")
    print("=============================================\n")
    
    print("1. Total Characters:", total_characters)
    print("2. Total Words Found:", total_words)
    print("3. Total Sentences Found:", total_sentences)
    print("4. Total Vowels:", v_count, "| Total Consonants:", c_count)
    print("5. Longest Word Detected: '", longest_word, "' (Length: ", len(longest_word), ")", sep="")
    print("6. Shortest Word Detected: '", shortest_word, "' (Length: ", len(shortest_word), ")", sep="")
    print("7. Most Frequent Word: '", most_frequent_word, "' (Appeared ", max_frequency, " times)", sep="")
    
    print("\n8. Word Frequencies Dictionary:")
    print(word_frequencies)
    
    print("\n9. Words Appearing Exactly Once (Sample Selection shown):")
    # Displaying a subset or full list depending on size
    print(appearing_once)
    
    print("\n10. Words Appearing More Than 5 Times:")
    if len(more_than_five) > 0:
        print(more_than_five)
    else:
        print("None")
        
    print("\n11. Count of Words Starting with Each Alphabet:")
    for alpha in sorted_alphabets:
        print("   Letter '", alpha, "': ", alphabet_counts[alpha], " words", sep="")
        
    print("\n12. All Unique Words Found in Text:")
    print(unique_words)

else:
    print("The text paragraph processing pool was empty.")

print("\n=============================================")
print("End of Report")
print("=============================================")
