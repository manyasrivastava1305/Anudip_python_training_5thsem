# Employee attendance records are stored in attendance.txt. 
# Sample Input/Data (attendance.txt) 
# EMP101,P 
# EMP102,A 
# EMP103,P 
# EMP104,P 
# EMP105,A 
# EMP106,P 
# EMP107,P 
# EMP108,A 
# EMP109,P 
# EMP110,P 
# Tasks 
# 1. Count present and absent employees.  
# 2. Display absent employee IDs.  
# 3. Calculate attendance percentage.  
# 4. Generate an absentee report in absent_report.txt.  
# 5. Display employees eligible for attendance awards (100% attendance).  
# Mock Setup for attendance.txt
attendance_data = """EMP101,P
EMP102,A
EMP103,P
EMP104,P
EMP105,A
EMP106,P
EMP107,P
EMP108,A
EMP109,P
EMP110,P"""

with open("attendance.txt", "w") as f:
    f.write(attendance_data)

# --- Main Program Logic ---

attendance = []
with open("attendance.txt", "r") as file:
    for line in file:
        if line.strip():
            # Basic structural validation: ensure the line contains a comma
            if "," in line:
                emp_id, status = line.strip().split(",")
                attendance.append([emp_id.strip(), status.strip()])

# --- Validation: Ensure records exist before performing calculations ---
if not attendance:
    print("Error: No attendance data found in the file.")
else:
    # 1. Count present and absent employees
    present_count = 0
    absent_count = 0
    for emp in attendance:
        if emp[1] == "P":
            present_count += 1
        elif emp[1] == "A":
            absent_count += 1

    print("Present Employees:", present_count)
    print("Absent Employees:", absent_count)

    # 2. Display absent employee IDs
    print("\nAbsent Employee IDs:")
    # Check if there are actually any absentees to display
    if absent_count == 0:
        print("None")
    else:
        for emp in attendance:
            if emp[1] == "A":
                print(emp[0])

    # 3. Calculate attendance percentage
    # The 'if not attendance' check above safely prevents a ZeroDivisionError here
    attendance_pct = (present_count / len(attendance)) * 100
    print("\nAttendance Percentage:", round(attendance_pct, 1), "%")

    # 4. Generate an absentee report in absent_report.txt
    with open("absent_report.txt", "w") as out_file:
        for emp in attendance:
            if emp[1] == "A":
                # Writing to a file still requires standard string joining or creation
                out_file.write(emp[0] + "\n")
    print("Absentee Report Generated Successfully.")

    # 5. Display employees eligible for attendance awards
    print("\nAttendance Award Eligibility:")
    if attendance_pct == 100.0:
        for emp in attendance:
            print(emp[0])
    else:
        print("Not Applicable")
