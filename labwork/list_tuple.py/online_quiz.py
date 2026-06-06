# Problem Statement 
# Correct answers: 
# correct = ['A', 'C', 'B', 'D', 'A'] 
# Student answers: 
# student = ['A', 'B', 'B', 'D', 'C'] 
# Write a program to: 
# • Calculate score.  
# • Display incorrectly answered question numbers.  
# • Count correct and wrong answers.  
# • Determine pass/fail (minimum 60%).  
# Answer keys
correct = ['A', 'C', 'B', 'D', 'A'] 
student = ['A', 'B', 'B', 'D', 'C'] 

# Initialize trackers
correct_count = 0
wrong_count = 0
incorrect_questions = []

# Loop through the questions using the index
for index in range(len(correct)):
    question_number = index + 1  # Convert 0-index to Question 1, 2, 3...
    
    # Check if the student's answer matches the correct answer
    if student[index] == correct[index]:
        correct_count += 1
    else:
        wrong_count += 1
        incorrect_questions.append(question_number)

# Calculate final score and percentage
# Assuming 1 mark per correct answer
total_questions = len(correct)
score_percentage = (correct_count / total_questions) * 100

# Determine pass/fail status (minimum 60% required)
passed = score_percentage >= 60

# Display the results
print("--- Student Exam Evaluation ---")
print("Total Correct Answers:", correct_count)
print("Total Wrong Answers:", wrong_count)
print("Final Score:", correct_count, "/", total_questions)
print("Incorrectly Answered Question Numbers:", incorrect_questions)
print("Score Percentage:", score_percentage, "%")
print("Exam Passed?:", passed)
