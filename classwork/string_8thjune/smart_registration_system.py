'''
---------------Smart User Registration System ----------------------------------------------
A company is creating a registration portal for new employees. 
The system asks the user to enter the following information: 
Enter Full Name:   anuj kumar 
Enter Email ID:    anuj.kumar@company.com 
The HR team wants the system to automatically validate and process the entered information. 
Tasks 
1. Display the employee's name in uppercase.  
2. Display the employee's name in title case.  
3. Count the total number of characters in the name.  
4. Count the number of spaces in the name.  
5. Check whether the email contains "@".  
6. Check whether the email ends with ".com".  
7. Extract and displays the company name from the email.  
8. Replace all spaces in the employee name with underscores (_).  
9. Check whether the employee's name starts with the letter "A".  
10. Count how many times the letter "a" appears in the employee's name.  
Sample Input 
Name: anuj kumar 
Email: anuj.kumar@company.com 
Sample Output 
ANUJ KUMAR 
Anuj Kumar 
Total Characters: 10 
Spaces: 1 
Valid Email: Yes 
Ends With .com: Yes 
Company Name: company 
Name with Underscore: anuj_kumar 
Starts With A: True 
Count of 'a': 2
------------------------------------------------------------'''
#to ask user to enter name
name = input("Enter Full Name: ").strip()
#validating name of employee
if name.isspace():
    exit("Name cannot be empty.")
#if name cotains digits then exit
for char in name:
    if char.isdigit():
        exit("Name cannot contain digits.")
#------------------------------------------------
#to ask user to enter email
email = input("Enter Email ID: ").strip()
#validating email of employee
if email.isspace():
    exit("Email cannot be empty.")
#------------------------------------------------
#to check @ in email and validate if it is only one @
if email.count("@") != 1:
    exit("Email must contain exactly one '@' symbol.")  
#-----------------------------------------------------------
#1. Display the employee's name in uppercase.
print("-----------------------------------------")
print("Name in Uppercase : ", name.upper())
#2. Display the employee's name in title case.
print("Name in Title Case : ", name.title())
#3. Count the total number of characters in the name.
print("Total Characters: ", len(name))
#4. Count the number of spaces in the name.
print("Spaces: ", name.count(" "))
#5. Check whether the email contains "@".
print("Valid Email: ", "@" in email)
#6. Check whether the email ends with ".com".
print("Ends With .com: ", email.endswith(".com"))
#7. Extract and display the company name from the email.
email_extract = email.split("@")
company_name = email_extract[1].split(".")[0]
print("Company Name: ", company_name)
#8. Replace all spaces in the employee name with underscores (_).
name_with_underscore = name.replace(" ", "_")
print("Name with Underscore: ", name_with_underscore)
#9. Check whether the employee's name starts with the letter "A".
print("Starts With A: ", name.startswith("A"))
#10. Count how many times the letter "a" appears in the employee's name.
print("Count of 'a': ", name.lower().count("a"))
