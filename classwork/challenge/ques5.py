abstract1 = "Artificial intelligence is transforming education and healthcare."
abstract2 = "Healthcare and education are rapidly transforming through artificial intelligence."

# Clean up punctuation and convert to standard lower-case word lists
words1 = abstract1.lower().replace(".", "").split()
words2 = abstract2.lower().replace(".", "").split()

# 1. Convert to sets
set1 = set(words1)
set2 = set(words2)

# 2. Logic processing
common_words = set1.intersection(set2)
unique_in_1 = set1 - set2
unique_in_2 = set2 - set1

# 3. Calculate percentage similarity
total_unique_words = len(set1.union(set2))
similarity_percentage = (len(common_words) / total_unique_words) * 100

# Display Output
print(f"Common Words:\n{common_words}")
print(f"\nUnique Words in Abstract 1:\n{unique_in_1}")
print(f"\nUnique Words in Abstract 2:\n{unique_in_2}")
print(f"\nSimilarity Percentage:\n{similarity_percentage:.1f}%")
print("\nPlagiarism Review Required:")
print("Yes" if similarity_percentage > 50 else "No")