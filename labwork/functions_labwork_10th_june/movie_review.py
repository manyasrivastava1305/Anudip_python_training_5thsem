# Movie reviews are stored as follows: 
# reviews = [ 
#     "excellent movie", 
#     "average story", 
#     "excellent acting", 
#     "poor direction", 
#     "excellent visuals", 
#     "poor screenplay", 
#     "good music", 
#     "excellent climax", 
#     "average performance", 
#     "good cinematography" 
# ] 
# Requirements 
# Create the following functions: 
# 1. count_sentiments(reviews) 
# Counts: 
# • Excellent  
# • Good  
# • Average  
# • Poor reviews  
# 2. most_common_word(reviews) 
# Returns the most frequently occurring word. 
# 3. longest_review(reviews) 
# Returns the review containing the maximum number of characters. 
# 4. reviews_with_keyword(reviews, keyword) 
# Displays all reviews containing a given keyword.
# Sample data
reviews = [ 
    "excellent movie", 
    "average story", 
    "excellent acting", 
    "poor direction", 
    "excellent visuals", 
    "poor screenplay", 
    "good music", 
    "excellent climax", 
    "average performance", 
    "good cinematography" 
]

# 1. Count sentiments based on keywords
def count_sentiments(reviews):
    excellent_count = 0
    good_count = 0
    average_count = 0
    poor_count = 0
    
    for r in reviews:
        # Convert to lowercase to make the check case-insensitive
        review_lower = r.lower() 
        
        if "excellent" in review_lower:
            excellent_count = excellent_count + 1
        elif "good" in review_lower:
            good_count = good_count + 1
        elif "average" in review_lower:
            average_count = average_count + 1
        elif "poor" in review_lower:
            poor_count = poor_count + 1
            
    print("Sentiment Counts:")
    print("- Excellent:", excellent_count)
    print("- Good:", good_count)
    print("- Average:", average_count)
    print("- Poor:", poor_count)

# 2. Find the most frequently occurring word
def most_common_word(reviews):
    all_words = []
    
    # Break all reviews down into a single list of individual words
    for r in reviews:
        words = r.lower().split()
        for word in words:
            all_words.append(word)
            
    # Track the word with the highest count
    most_frequent = ""
    max_count = 0
    
    for word in all_words:
        # Count how many times this specific word appears in the whole list
        word_count = 0
        for w in all_words:
            if w == word:
                word_count = word_count + 1
                
        # If it beats the previous record, update our trackers
        if word_count > max_count:
            max_count = word_count
            most_frequent = word
            
    return most_frequent

# 3. Find the review with the maximum number of characters
def longest_review(reviews):
    longest = reviews[0]
    for r in reviews:
        if len(r) > len(longest):
            longest = r
    return longest

# 4. Display all reviews containing a given keyword
def reviews_with_keyword(reviews, keyword):
    print("Reviews containing '" + keyword + "':")
    for r in reviews:
        if keyword.lower() in r.lower():
            print("-", r)


# --- Running the Functions ---

print("1.")
count_sentiments(reviews)
print("---")

print("2. Most common word:", most_common_word(reviews))
print("---")

print("3. Longest review:", longest_review(reviews))
print("---")

print("4.")
reviews_with_keyword(reviews, "acting")
