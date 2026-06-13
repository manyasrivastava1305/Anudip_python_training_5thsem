# Create a Book class with attributes: 
# • Book ID  
# • Title  
# • Author  
# • Availability Status  
# Implement methods to: 
# • Issue a book.  
# • Return a book.  
# • Display book details.  
# Prevent issuing a book that is already issued. 
# Sample Output: 
# Book Issued Successfully. 
# Availability Status: Not Available
class BookBank:
    # 1. Constructor: Defaults the availability status to "Available"
    def __init__(self, bookid, title, author):
        self.__bookid = bookid
        self.__title = title
        self.__author = author
        self.__status = "Available"

    # 2. Method to Issue a Book
    def issue_book(self):
        if self.__status == "Available":
            self.__status = "Not Available"
            print("Book Issued Successfully.")
            print("Availability Status:", self.__status)
        else:
            print("[Error] This book is already issued and currently not available!")

    # 3. Method to Return a Book
    def return_book(self):
        if self.__status == "Not Available":
            self.__status = "Available"
            print("Book Returned Successfully.")
            print("Availability Status:", self.__status)
        else:
            print("[Warning] This book is already in the library!")

    # 4. Method to Display Book Details
    def display_details(self):
        print("\n--- Book Details ---")
        print("Book ID            :", self.__bookid)
        print("Title              :", self.__title)
        print("Author             :", self.__author)
        print("Availability Status:", self.__status)


# ------------------ Main Code Block ------------------

print("--- Register New Book ---")

# Input and verify Book ID (Alphanumeric check)
id_input = input("Enter Book ID: ")
if not id_input.isalnum():
    print("[Error] Book ID must be alphanumeric (letters and numbers only, no spaces)!")
    exit()

# Get other book details
title_input = input("Enter Book Title: ")
author_input = input("Enter Author Name: ")

# Create the book object
book = BookBank(id_input, title_input, author_input)

# Menu Loop to test functionality
while True:
    print("\n==============================")
    print("          LIBRARY MENU        ")
    print("==============================")
    print("1. Issue Book")
    print("2. Return Book")
    print("3. Display Book Details")
    print("4. Exit")
    print("------------------------------")
    
    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        book.issue_book()
    elif choice == '2':
        book.return_book()
    elif choice == '3':
        book.display_details()
    elif choice == '4':
        print("\nExiting library system. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please select an option between 1 and 4.")