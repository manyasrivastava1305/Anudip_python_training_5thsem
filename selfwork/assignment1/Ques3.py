# library = { 
#     "B101": { 
#         "title": "Python Basics", 
#         "author": "ABC", 
#         "copies": 5 
#     } 
# } 
# Maintain records of at least 30 books. 
# Requirements 
# 1. Add a book.  
# 2. Remove a book.  
# 3. Search a book by ID.  
# 4. Search by title.  
# 5. Update available copies.  
# 6. Issue a book.  
# 7. Return a book.  
# 8. Display books with fewer than 3 copies.  
# 9. Display books that are unavailable.  
# 10. Find the most available book.  
# 11. Generate a restocking report.  
# 12. Create a separate dictionary of books requiring immediate purchase.
# 1. Add a book. (Pre-populated with 30 library records)
library = {
    "B101": {"title": "Python Basics", "author": "ABC", "copies": 5},
    "B102": {"title": "Data Structures", "author": "XYZ", "copies": 2},
    "B103": {"title": "Algorithms", "author": "PQR", "copies": 0},
    "B104": {"title": "Web Development", "author": "John Doe", "copies": 4},
    "B105": {"title": "Machine Learning", "author": "Andrew Ng", "copies": 1},
    "B106": {"title": "Deep Learning", "author": "Goodfellow", "copies": 3},
    "B107": {"title": "Database Systems", "author": "Korth", "copies": 6},
    "B108": {"title": "Operating Systems", "author": "Silberschatz", "copies": 0},
    "B109": {"title": "Computer Networks", "author": "Tanenbaum", "copies": 7},
    "B110": {"title": "Cyber Security", "author": "Stallings", "copies": 2},
    "B111": {"title": "Discrete Mathematics", "author": "Rosen", "copies": 5},
    "B112": {"title": "Digital Electronics", "author": "Mano", "copies": 1},
    "B113": {"title": "Compiler Design", "author": "Ullman", "copies": 4},
    "B114": {"title": "Software Engineering", "author": "Pressman", "copies": 8},
    "B115": {"title": "Cloud Computing", "author": "Buyya", "copies": 0},
    "B116": {"title": "Artificial Intelligence", "author": "Russell", "copies": 3},
    "B117": {"title": "Data Science Intro", "author": "Grus", "copies": 4},
    "B118": {"title": "Linux Command Line", "author": "Shotts", "copies": 10},
    "B119": {"title": "Java Programming", "author": "Schildt", "copies": 2},
    "B120": {"title": "C++ Primer", "author": "Lippman", "copies": 5},
    "B121": {"title": "Design Patterns", "author": "Gamma", "copies": 1},
    "B122": {"title": "Clean Code", "author": "Robert Martin", "copies": 0},
    "B123": {"title": "Automate Boring Stuff", "author": "Al Sweigart", "copies": 6},
    "B124": {"title": "JavaScript Definitive Guide", "author": "Flanagan", "copies": 3},
    "B125": {"title": "SQL Performance Explained", "author": "Winand", "copies": 2},
    "B126": {"title": "Docker in Action", "author": "Nickoloff", "copies": 4},
    "B127": {"title": "Kubernetes Up and Running", "author": "Burns", "copies": 1},
    "B128": {"title": "Rust Programming", "author": "Blandy", "copies": 5},
    "B129": {"title": "Go Programming Language", "author": "Donovan", "copies": 0},
    "B130": {"title": "Introduction to Git", "author": "Chacon", "copies": 12}
}

print("--- System Status: Library Initialized with 30 Books ---")
new_id = input("Enter new Book ID: ")
if new_id not in library:
    new_title = input("Enter book title: ")
    new_author = input("Enter book author: ")
    new_copies = int(input("Enter number of copies: "))
    library[new_id] = {"title": new_title, "author": new_author, "copies": new_copies}
    print("Book added successfully.")
else:
    print("Book ID already exists.")

# 2. Remove a book.
remove_id = input("\nEnter Book ID to remove: ")
if remove_id in library:
    del library[remove_id]
    print("Book removed successfully.")
else:
    print("Book not found.")

# 3. Search a book by ID.
search_id = input("\nEnter Book ID to search: ")
if search_id in library:
    print("Book found:")
    print(f"ID: {search_id} | Title: {library[search_id]['title']} | Author: {library[search_id]['author']} | Copies available: {library[search_id]['copies']}")
else:
    print("Book not found.")

# 4. Search by title.
search_title = input("\nEnter book title to search: ")
found_books = []
for book_id, details in library.items():
    if details["title"].lower() == search_title.lower():
        found_books.append((book_id, details))

if found_books:
    print("Books found:")
    for book_id, details in found_books:
        print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Copies: {details['copies']}")
else:
    print("No books found with that title.")

# 5. Update available copies.       
update_id = input("\nEnter Book ID to update copies: ")
if update_id in library:
    new_copies = int(input("Enter new number of copies: "))
    library[update_id]["copies"] = new_copies
    print("Copies updated successfully.")
else:
    print("Book not found.")

# 6. Issue a book.
issue_id = input("\nEnter Book ID to issue: ")
if issue_id in library:
    if library[issue_id]["copies"] > 0:
        library[issue_id]["copies"] -= 1
        print("Book issued successfully.")
    else:
        print("Book is not available (Out of stock).")
else:
    print("Book not found.")

# 7. Return a book.
return_id = input("\nEnter Book ID to return: ")
if return_id in library:
    library[return_id]["copies"] += 1
    print("Book returned successfully.")
else:
    print("Book not found.")

# 8. Display books with fewer than 3 copies.
print("\nBooks with fewer than 3 copies:")
for book_id, details in library.items():
    if details["copies"] < 3:
        print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Copies: {details['copies']}")    

# 9. Display books that are unavailable.
print("\nUnavailable books:")
for book_id, details in library.items():
    if details["copies"] == 0:
        print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}")

# 10. Find the most available book.
most_available_book = None
max_copies = -1
for book_id, details in library.items():
    if details["copies"] > max_copies:
        max_copies = details["copies"]
        most_available_book = (book_id, details)

if most_available_book:
    print(f"\nThe most available book is: {most_available_book[1]['title']} (ID: {most_available_book[0]}) with {most_available_book[1]['copies']} copies available.")

# 11. Generate a restocking report.
print("\n=== RESTOCKING REPORT ===")
print("The following books require tracking due to low stock counts:")
for book_id, details in library.items():
    if details["copies"] < 3:
        print(f"ALERT -> ID: {book_id} | Title: {details['title']} | Stock remaining: {details['copies']}")

# 12. Create a separate dictionary of books requiring immediate purchase.
immediate_purchase_books = {}
for book_id, details in library.items():
    if details["copies"] < 3:
        immediate_purchase_books[book_id] = details

print("\nBooks requiring immediate purchase (Saved to isolated dictionary):")
for book_id, details in immediate_purchase_books.items():
    print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Copies: {details['copies']}")
