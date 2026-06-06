# Problem Statement 
# A batsman's scores in different matches are stored in a list. 
# scores = [45, 78, 12, 100, 67, 8, 90, 55] 
# Write a program to: 
# • Count half-centuries and centuries.  
# • Find the highest score.  
# • Display all scores below 20.  
# • Calculate the average score. 
# Initial list of scores
scores = [45, 78, 12, 100, 67, 8, 90, 55]

# Initialize counters and lists
half_centuries = 0
centuries = 0
scores_below_20 = []
total_score = 0

# Process the scores
for score in scores:
    # Count half-centuries (scores between 50 and 99)
    if 50 <= score < 100:
        half_centuries += 1
    # Count centuries (scores 100 and above)
    elif score >= 100:
        centuries += 1
        
    # Check for scores below 20
    if score < 20:
        scores_below_20.append(score)
        
    # Add to total score for average calculation
    total_score += score

# Find the highest score
highest_score = max(scores)

# Calculate the average score
average_score = total_score / len(scores)

# Display the results without using f-strings
print("--- Cricket Tournament Scorecard Analysis ---")
print("Total Half-Centuries (50-99): " ,half_centuries)
print("Total Centuries (100+): ",centuries)
print("Highest Score: ",highest_score)
print("Scores below 20: ",scores_below_20)
print("Average Score:",average_score)
