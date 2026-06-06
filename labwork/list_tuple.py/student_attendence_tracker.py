# Attendance for 15 days is recorded as: 
# attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P'] 
# Write a program to: 
# • Count present and absent days.  
# • Calculate attendance percentage.  
# • Determine eligibility (minimum 75% attendance).  
# • Display positions where the student was absent. 
# Initial 15-day attendance record ('P' = Present, 'A' = Absent)
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# Initialize counters and list for absent days
present_count = 0
absent_count = 0
absent_days = []

# Loop through the list using index to track the days
for index in range(len(attendance)):
    status = attendance[index]
    day_number = index + 1  # Human-readable day numbers (1 to 15)
    
    if status == 'P':
        present_count += 1
    elif status == 'A':
        absent_count += 1
        absent_days.append(day_number)

# Calculate attendance percentage
total_days = len(attendance)
attendance_percentage = (present_count / total_days) * 100

# Determine eligibility (minimum 75% attendance required)
is_eligible = attendance_percentage >= 75

# Display the results
print("--- Attendance Analysis Report ---")
print("Total Present Days:", present_count)
print("Total Absent Days:", absent_count)
print("Positions (Days) when absent:", absent_days)
print("Attendance Percentage:", attendance_percentage, "%")
print("Is the student eligible for exams?:", is_eligible)
