import os

FILENAME = "contacts.txt"

def load_contacts():
    contacts = []
    if not os.path.exists(FILENAME):
        return contacts
    with open(FILENAME, "r") as f:
        for line in f:
            if line.strip():
                name, number = line.strip().split(",")
                contacts.append({
                    "name": name.strip(),
                    "number": number.strip()
                })
    return contacts

def save_all_contacts(contacts):
    with open(FILENAME, "w") as f:
        for c in contacts:
            f.write(f"{c['name']}, {c['number']}\n")

def display_all():
    contacts = load_contacts()
    if not contacts:
        print("Directory is empty.")
        return
    print("\n--- Contact List ---")
    for c in contacts:
        print(f"Name: {c['name']} | Phone: {c['number']}")

def search_contact():
    name = input("Enter contact name to search: ").strip()
    contacts = load_contacts()
    for c in contacts:
        if c['name'].lower() == name.lower():
            print(f"Contact Found -> Name: {c['name']} | Phone: {c['number']}")
            return
    print("Contact details not found.")

def add_contact():
    name = input("Enter Contact Name: ").strip()
    number = input("Enter Contact Number: ").strip()
    contacts = load_contacts()
    
    # Validation against identical matching names
    for c in contacts:
        if c['name'].lower() == name.lower():
            print("Contact name already exists! Use the update function to change numbers.")
            return

    contacts.append({"name": name, "number": number})
    save_all_contacts(contacts)
    print("Contact added and saved successfully.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    contacts = load_contacts()
    for c in contacts:
        if c['name'].lower() == name.lower():
            new_number = input(f"Enter new phone number for {c['name']}: ").strip()
            c['number'] = new_number
            save_all_contacts(contacts)
            print("Contact number updated and saved successfully.")
            return
    print("Contact name not found.")

def delete_contact():
    name = input("Enter the contact name to delete: ").strip()
    contacts = load_contacts()
    original_length = len(contacts)
    contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    
    if len(contacts) < original_length:
        save_all_contacts(contacts)
        print("Contact removed and modifications successfully written to disk.")
    else:
        print("Contact not found.")

def display_vowel_names():
    contacts = load_contacts()
    print("\n--- Contacts Starting with a Vowel ---")
    found = False
    vowels = ('a', 'e', 'i', 'o', 'u')
    for c in contacts:
        if c['name'] and c['name'][0].lower() in vowels:
            print(f"Name: {c['name']} | Phone: {c['number']}")
            found = True
    if not found:
        print("No contacts found starting with a vowel.")

def menu():
    while True:
        print("\n===== Mobile Contact Directory System =====")
        print("1. Display all contacts")
        print("2. Search a contact by name")
        print("3. Add a new contact")
        print("4. Update an existing contact number")
        print("5. Delete a contact")
        print("6. Display contacts whose names start with a vowel")
        print("7. Exit")
        choice = input("Enter choice (1-7): ").strip()

        if choice == '1': display_all()
        elif choice == '2': search_contact()
        elif choice == '3': add_contact()
        elif choice == '4': update_contact()
        elif choice == '5': delete_contact()
        elif choice == '6': display_vowel_names()
        elif choice == '7':
            print("Exiting Application... Modifications are permanently saved.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()