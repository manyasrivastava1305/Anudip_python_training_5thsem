# Given list of marks
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# Initialize variables for requirements 2 and 3
failed_count = 0

# Assume the first element is both the highest and lowest initially
highest = marks[0]
lowest = marks[0]

# Lists to store specific categories for display/output
passed_students = []
above_75 = []

# Process the marks using a loop
for score in marks:
    #  Check for passed students (marks >= 40)
    if score >= 40:
        passed_students.append(score)
    else:
        #  Count failed students (marks < 40)
        failed_count += 1
        
    #  Find highest and lowest without max() or min()
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
        
    # 4. Check for marks above 75
    if score > 75:
        above_75.append(score)

# --- Displaying the Results ---
print("1. Passed students (marks >= 40):", passed_students)
print("2. Number of failed students:", failed_count)
print(f"3. Highest mark: {highest} | Lowest mark: {lowest}")
print("4. New list containing marks above 75:", above_75)
