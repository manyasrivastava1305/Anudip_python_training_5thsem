# Attendance of a student for 15 days is represented as: 
# PPAPPPAAPPPPAPP 
# Where: 
# • P = Present  
# • A = Absent  
# Tasks 
# Write a program to: 
# 1. Count Present and Absent days.  
# 2. Calculate attendance percentage.  
# 3. Find the longest consecutive streak of Presence.  
# 4. Find the longest consecutive streak of Absence.  
# 5. Determine whether attendance is below 75%. 
# Input Attendance String
attendance = "PPAPPPAAPPPPAPP"

print(f"Attendance Record: {attendance}")
print("-" * 45)

# --- Task 1: Count Present and Absent days ---
present_count = 0
absent_count = 0

for day in attendance:
    if day == "P":
        present_count += 1
    elif day == "A":
        absent_count += 1

# Total days tracked
total_days = len(attendance)


# --- Task 2: Calculate attendance percentage ---
# Percentage formula: (Present Days / Total Days) * 100
attendance_percentage = (present_count / total_days) * 100


# --- Tasks 3 & 4: Find Longest Streaks ---
current_p_streak = 0
max_p_streak = 0

current_a_streak = 0
max_a_streak = 0

for day in attendance:
    if day == "P":
        current_p_streak += 1  # Add to present streak
        current_a_streak = 0  # Reset absent streak

        # Check if this is the longest present streak we've seen so far
        if current_p_streak > max_p_streak:
            max_p_streak = current_p_streak

    elif day == "A":
        current_a_streak += 1  # Add to absent streak
        current_p_streak = 0  # Reset present streak

        # Check if this is the longest absent streak we've seen so far
        if current_a_streak > max_a_streak:
            max_a_streak = current_a_streak


# --- Task 5: Determine whether attendance is below 75% ---
if attendance_percentage < 75.0:
    shortage_alert = "YES (Below 75%)"
else:
    shortage_alert = "NO (Attendance is sufficient)"


# --- Output Results ---
print(f"1. Total Present Days       : {present_count}")
print(f"   Total Absent Days        : {absent_count}")
print(f"2. Attendance Percentage    : {attendance_percentage:.2f}%")
print(f"3. Longest Presence Streak  : {max_p_streak} days")
print(f"4. Longest Absence Streak   : {max_a_streak} days")
print(f"5. Low Attendance Alert     : {shortage_alert}")
print("-" * 45)
