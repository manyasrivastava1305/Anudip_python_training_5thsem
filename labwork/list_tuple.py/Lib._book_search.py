# Books available in a library: 
# books = [ 
#     ("Python Basics", 5), 
#     ("Data Science", 0), 
#     ("Java Programming", 3), 
#     ("Machine Learning", 0) 
# ] 
# Write a program to: 
# • Display unavailable books.  
# • Find all books with more than 2 copies.  
# • Count available books.  
# • Stop searching once a requested book is found. 
# Initial library data stored as tuples (Book Name, Copies Available)
books = [ 
    ("Python Basics", 5), 
    ("Data Science", 0), 
    ("Java Programming", 3), 
    ("Machine Learning", 0) 
] 

# Set the book you want to look for
requested_book = "Java Programming"

# Initialize trackers
unavailable_books = []
more_than_2_copies = []
available_books_count = 0
book_found_status = False

# 1, 2, & 3: Scan through the library inventory
for title, copies in books:
    # Check for unavailable books (0 copies)
    if copies == 0:
        unavailable_books.append(title)
    else:
        # Count books that have at least 1 copy available
        available_books_count += 1
        
    # Check for books with more than 2 copies
    if copies > 2:
        more_than_2_copies.append(title)

# 4: Search for the requested book and stop immediately when found
for title, copies in books:
    print("Checking catalog for:", title)  # Shows the search progress
    if title == requested_book:
        book_found_status = True
        break  # Stops the loop immediately

# Display the results
print("\n--- Library Inventory Report ---")
print("Unavailable Books:", unavailable_books)
print("Books with more than 2 copies:", more_than_2_copies)
print("Total number of unique titles available:", available_books_count)
print("Was '" + requested_book + "' found?:", book_found_status)
