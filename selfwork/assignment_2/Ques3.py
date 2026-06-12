# A messaging application wants to analyze chat messages. 
# Store at least 20 chat messages in a list. 
# Requirements 
# For each message: 
# 1. Count total words.  
# 2. Count total characters.  
# 3. Count vowels and consonants.  
# 4. Find longest word.  
# 5. Find shortest word.  
# 6. Count occurrence of each word.  
# 7. Display repeated words.  
# 8. Display words starting with vowels.  
# 9. Display words longer than 5 characters.  
# 10. Create a dictionary containing word frequencies.
# Chat Message Analyzer Program

print("--- Chat Message Analyzer ---")

# Predefined list containing 20 chat messages
messages = [
    "Hello everyone welcome to the group chat",
    "Are you coming to the office today",
    "Please send the updated project report ASAP",
    "The quick brown fox jumps over the lazy dog",
    "Let us schedule a quick meeting tomorrow morning",
    "I will be late for the call today",
    "Can you share the link for the document",
    "That is an excellent idea for our application",
    "Do not forget to complete your assignment",
    "Happy birthday have an amazing day ahead",
    "Python is an awesome programming language to learn",
    "We need to optimize this backend code immediately",
    "Is anyone available to help me with this bug",
    "Please review my pull request when you get time",
    "The weather today is absolutely beautiful and sunny",
    "Let us grab some hot coffee during the break",
    "Remember to update your status on the tracker",
    "Great job on completing the task ahead of schedule",
    "Can we discuss this issue over a quick voice call",
    "See you all at the venue tomorrow evening"
]

print("Successfully loaded ", len(messages), " chat messages for analysis.\n", sep="")

print("=============================================")
print("             CHAT ANALYSIS REPORT            ")
print("=============================================\n")

# Process each chat message
for index, msg in enumerate(messages, 1):
    print("---------------------------------------------")
    print("Analyzing Message #", index, ": '", msg, "'", sep="")
    print("---------------------------------------------")
    
    # --- 2. Count total characters ---
    total_chars = len(msg)
    
    # --- 3. Count vowels and consonants ---
    v_count = 0
    c_count = 0
    vowels = "aeiouAEIOU"
    
    for char in msg:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
                
    # Split message into words using standard spaces
    # We also clean punctuation to get clean words for counting
    raw_words = msg.split()
    words = []
    for w in raw_words:
        # Strip simple punctuation from ends of words if any exist
        clean_w = w.strip(".,!?\"'")
        if clean_w: # Ensure word is not empty after stripping
            words.append(clean_w)
            
    # --- 1. Count total words ---
    total_words = len(words)
    
    # Check if message contains words before continuing analysis
    if total_words == 0:
        print("This message does not contain any valid words.")
        print()
        continue
        
    # Initialize logic variables with the first word
    longest_word = words[0]
    shortest_word = words[0]
    
    # --- 6 & 10. Create a dictionary containing word frequencies ---
    word_frequencies = {}
    
    # Lists for conditional classification
    vowel_starters = []
    longer_than_five = []
    
    for w in words:
        # 4 & 5. Find longest and shortest word
        if len(w) > len(longest_word):
            longest_word = w
        if len(w) < len(shortest_word):
            shortest_word = w
            
        # 6 & 10. Build word frequency dictionary (case-insensitive for accuracy)
        w_lower = w.lower()
        if w_lower in word_frequencies:
            word_frequencies[w_lower] += 1
        else:
            word_frequencies[w_lower] = 1
            
        # 8. Identify words starting with vowels
        if w[0] in vowels:
            # Avoid adding duplicate exact words to the display list
            if w break not in vowel_starters:
                vowel_starters.append(w)
                
        # 9. Identify words longer than 5 characters
        if len(w) > 5:
            if w not in longer_than_five:
                longer_than_five.append(w)

    # --- 7. Display repeated words ---
    repeated_words = []
    for item in word_frequencies:
        if word_frequencies[item] > 1:
            repeated_words.append(item)

    # --- Print individual results ---
    print("1. Total Words:", total_words)
    print("2. Total Characters:", total_chars)
    print("3. Vowels:", v_count, "| Consonants:", c_count)
    print("4. Longest Word: '", longest_word, "' (Length: ", len(longest_word), ")", sep="")
    print("5. Shortest Word: '", shortest_word, "' (Length: ", len(shortest_word), ")", sep="")
    print("6 & 10. Word Frequencies Dictionary:")
    print("   ", word_frequencies)
    
    if len(repeated_words) > 0:
        print("7. Repeated Words:", repeated_words)
    else:
        print("7. Repeated Words: None")
        
    if len(vowel_starters) > 0:
        print("8. Words Starting with Vowels:", vowel_starters)
    else:
        print("8. Words Starting with Vowels: None")
        
    if len(longer_than_five) > 0:
        print("9. Words Longer than 5 Characters:", longer_than_five)
    else:
        print("9. Words Longer than 5 Characters: None")
    print()

print("=============================================")
print("End of Report")
print("=============================================")
