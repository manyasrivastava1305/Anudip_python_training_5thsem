# A coaching institute wants to store student information in a way that prevents accidental modification of 
# records. 
# Each student's record should contain: 
# • Student ID  
# • Student Name  
# • Course Name  
# • Fees Paid  
# Store the details of 5 students using tuples and perform the following operations: 
# 1. Display all student records.  
# 2. Display the first student's details.  
# 3. Display the last student's details using negative indexing.  
# 4. Display only Student ID and Name for all students.  
# 5. Count the total number of students.  
# 6. Check whether a student named "Rahul" exists in the records.

#creating students data
students = (
    (101,"Rahul","java",3000),
    (102,"priya","data science",45000),
    (103,"Amit","Python",2500),
    (104,"sneha","Python",2500),
    (105,"Rohan","MERN", 40000),
)
#to display
print("------student record--------")
for record in students:
    print("student id:",record[0])
    print("Name:",record[1])
    print("Course",record[2])
    print("Fees paid",record[3])
    print("-------------------------")
#first student record
print("record of first student")
print("student id:",students[0][0])
print("Name:",students[0][1])
print("Course",students[0][2])
print("Fees paid",students[0][3])
print("-------------------------")
#last student record
print("record of last student")
print("student id:",students[-1][0])
print("Name:",students[-1][1])
print("Course",students[-1][2])
print("Fees paid",students[-1][3])
print("-------------------------")
#only id and name
for record in students:
    print("student id:",record[0])
    print("Name:",record[1])
    print("-------------------------")
#task 5
print("Total count:",len(students))
print("-------------------------")
count =0
for record in students:
    if (record[1] == "Rahul"):
        count+=1
        break
if (count == 0):
    print("record not found")
else:
    print("record found")
