# Mobile Contact Directory 
"""
Sample Data contacts = {     
"Amit": "9876543210",     
"Priya": "9876543211",     
"Rohan": "9876543212",     
"Neha": "9876543213",     
"Anjali": "9876543214",     
"Karan": "9876543215",     
"Pooja": "9876543216",     
"Arjun": "9876543217",     
"Sneha": "9876543218",     
"Rahul": "9876543219" 
} 
Tasks 
• Display all contact names in alphabetical order.  
• Count the total number of contacts.  
• Search for a given contact name.  
• Create a list of contacts whose names start with a vowel.  
• Stop the search using break once the required contact is found.
"""


# Mobile Contact Directory

contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# Task 1: Display all contact names in alphabetical order
print("Task 1: Contacts in alphabetical order")

for name in sorted(contacts.keys()):
    print(name)

# Task 2: Count the total number of contacts
total_contacts = len(contacts)

print("\nTask 2: Total number of contacts =", total_contacts)

# Task 3: Search for a given contact name
search_name = input("\nEnter contact name to search: ")

found = False

for name, number in contacts.items():
    if name.lower() == search_name.lower():
        print("Contact Found")
        print("Name :", name)
        print("Number :", number)
        found = True
        break

if not found:
    print("Contact not found")

# Task 4: Create a list of contacts whose names start with a vowel
vowel_contacts = []

for name in contacts.keys():
    if name[0].lower() in "aeiou":
        vowel_contacts.append(name)

print("\nTask 4: Contacts starting with a vowel")
print(vowel_contacts)

# Task 5: Stop the search using break once the required contact is found
print("\nTask 5: Demonstration of break")

search_name = input("Enter contact name: ")

for name, number in contacts.items():
    if name.lower() == search_name.lower():
        print("Found:", name, "-", number)
        break
