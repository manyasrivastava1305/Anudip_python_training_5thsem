count = 0
for students in range(1, 31):
    print("student", students)
    attendence = input("attendance (Present/Absent): ")
    
    if attendence == "Present":
        count = count + 1

print("number of present:", count)
print("Number of absentee:", 30 - count)
