# Sample Input/Data (patients.txt) 
# P101,Anuj,Normal 
# P102,Rahul,Critical 
# P103,Priya,Stable 
# P104,Neha,Critical 
# P105,Amit,Stable 
# P106,Sneha,Normal 
# P107,Karan,Critical 
# P108,Pooja,Stable 
# P109,Rohit,Normal 
# P110,Anjali,Stable 
# Tasks 
# 1. Display all patient records.  
# 2. Display critical patients.  
# 3. Count patients under each status.  
# 4. Search patient details using Patient ID.  
# 5. Save critical patient records to critical_patients.txt.  
# First, let's setup the patients.txt file mock data if it doesn't exist
patient_data = """P101, Anuj, Normal
P102, Rahul, Critical
P103, Priya, Stable
P104, Neha, Critical
P105, Amit, Stable
P106, Sneha, Normal
P107, Karan, Critical
P108, Pooja, Stable
P109, Rohit, Normal
P110, Anjali, Stable"""

with open("patients.txt", "w") as f:
    f.write(patient_data)
    f.close()

# --- Main Program Logic ---

patients = []
# Reading data from patients.txt
with open("patients.txt", "r") as file:
    for line in file:
        if line.strip():
            parts = line.strip().split(",")
            p_id = parts[0].strip()
            name = parts[1].strip()
            status = parts[2].strip()
            patients.append([p_id, name, status])
file.close()

# 1. Display all patient records 
# Validation: Check if there are any patient records loaded in the system
if not patients:
    print("Notification: No patient records found in the database.")
else:
    print(f"\n{'Patient ID':<12} | {'Patient Name':<15} | {'Health Status'}")
    print("-" * 45) # Visual separator for readability
    
    # Iterate through the list and display the records
    for p in patients:
        print(f"{p[0]:<12} | {p[1]:<15} | {p[2]}")
        
    print(f"\nTotal Records Displayed: {len(patients)}")

# 2. Display critical patients
print("Critical Patients:")
for p in patients:
    if p[2] == "Critical":
        print(p[1])
print()

# 3. Count patients under each status
normal_count = 0
stable_count = 0
critical_count = 0

for p in patients:
    if p[2] == "Normal":
        normal_count += 1
    elif p[2] == "Stable":
        stable_count += 1
    elif p[2] == "Critical":
        critical_count += 1

print("Patient Count:")
print(f"Normal: {normal_count}")
print(f"Stable: {stable_count}")
print(f"Critical: {critical_count}")
print()

# 4. Search patient details using Patient ID with user input and validation

# Take input from the user and format it (stripping extra spaces, making it uppercase)
search_id = input("Enter Patient ID to search (e.g., P104): ").strip().upper()

# Validation 1: Check if the user entered an empty string
if not search_id:
    print("Error: Patient ID cannot be empty. Please enter a valid ID.")
else:
    patient_found = False

    # Loop through the records to find a match
    for p in patients:
        if p[0] == search_id:
            print("\nPatient Found:")
            print(f"ID: {p[0]}, Name: {p[1]}, Age/Details: {p[2]}")
            patient_found = True
            break  # Stop searching once the patient is found
    
    # Validation 2: Handle cases where the ID does not exist in the database
    if not patient_found:
        print(f"Error: No patient record found for ID '{search_id}'.")
# 5. Save critical patient records to critical_patients.txt
with open("critical_patients.txt", "w") as out_file:
    for p in patients:
        if p[2] == "Critical":
            out_file.write(f"{p[0]}, {p[1]}, {p[2]}\n")
print("Critical Patient Report Generated Successfully.")
