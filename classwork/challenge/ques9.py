# 1. Setup sample source file
with open("hashtags.txt", "w") as f:
    tags = ["#AI", "#Python", "#AI", "#MachineLearning", "#DataScience", "#Python", "#AI", "#Coding", "#DataScience", "#Python"]
    for tag in tags:
        f.write(tag + "\n")

hashtag_counts = {}
unique_hashtags = set()

with open("hashtags.txt", "r") as f:
    for line in f:
        tag = line.strip()
        if tag:
            # Handle text variance if needed, sample matches exact string cases
            hashtag_counts[tag] = hashtag_counts.get(tag, 0) + 1
            unique_hashtags.add(tag)

# Find top trends & filtering tags > 2 occurrences
max_votes = max(hashtag_counts.values())
top_trending = [tag for tag, count in hashtag_counts.items() if count == max_votes]
more_than_twice = [tag for tag, count in hashtag_counts.items() if count > 2]

# 2. Write trend report
with open("trend_report.txt", "w") as f:
    f.write("Trend Report\n")
    for tag, count in hashtag_counts.items():
        f.write(f"{tag}: {count}\n")

# Display Output
print("Hashtag Frequency:")
for tag, count in hashtag_counts.items():
    print(f"{tag}: {count}")

print("\nTop Trending Hashtags:")
for tag in top_trending:
    print(tag)

print(f"\nUnique Hashtags:\n{unique_hashtags}")
print("\nHashtags Used More Than Twice:")
for tag in more_than_twice:
    print(tag)
print("\nTrend Report Generated Successfully.")