# Create a Student class to store the student's name, roll number, and marks obtained in three subjects. 
# Implement methods to: 
# • Accept student details.  
# • Calculate the total marks.  
# • Calculate the percentage.  
# • Display the complete student report.  
# Sample Output: 
# Name       : Ananya 
# Roll No    : 101 
# Total Marks: 255 
# Percentage : 85.0% 
class Student:
    # Constructor accepts data directly from the main code
    def __init__(self, name, rollno, marks1, marks2, marks3):
        self.__name = name
        self.__rollno = rollno
        self.__marks1 = marks1
        self.__marks2 = marks2
        self.__marks3 = marks3

    # Method to calculate total marks (no extra parameters needed)
    def calculate_total(self):
        return self.__marks1 + self.__marks2 + self.__marks3

    # Method to calculate percentage
    def calculate_percentage(self):
        # We can call our own class method using self
        total = self.calculate_total()
        return (total / 300)*100

    # Method to display the complete student report
    def display_report(self):
        print(f"Name        : {self.__name}")
        print(f"Roll No     : {self.__rollno}")
        print(f"Total Marks : {self.calculate_total()}")
        print(f"Percentage  : {self.calculate_percentage():.1f}%")


# ------------------ Main Code Block ------------------

print("--- Enter Student Details ---")
# Taking all inputs in the main program block
name_input = input("Enter Name: ")
roll_input = input("Enter Roll No: ")
m1 = float(input("Enter Marks for Subject 1: "))
m2 = float(input("Enter Marks for Subject 2: "))
m3 = float(input("Enter Marks for Subject 3: "))

print("\n-----------------------------")

# Creating the object by passing the inputs into the constructor
s1 = Student(name_input, roll_input, m1, m2, m3)

# Displaying the final report matching your sample output
s1.display_report()