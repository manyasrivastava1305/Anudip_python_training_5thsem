# Available copies of books in a library:
# books = { 
#     "Python": 5, 
#     "Java": 2, 
#     "DBMS": 4, 
#     "Networking": 1, 
#     "OS": 3, 
#     "AI": 6, 
#     "ML": 2, 
#     "Cloud": 5, 
#     "Cyber Security": 1, 
#     "Web Development": 4 
# } 
# Tasks 
# 1. Display books with fewer than 3 copies.  
# 2. Find the book with maximum copies.  
# 3. Find the book with minimum copies.  
# 4. Count total books available.  
# 5. Generate a restocking list. 

books = { 
    "Python": 5, 
    "Java": 2, 
    "DBMS": 4, 
    "Networking": 1, 
    "OS": 3, 
    "AI": 6, 
    "ML": 2, 
    "Cloud": 5, 
    "Cyber Security": 1, 
    "Web Development": 4 
}

# --- Task 1: Display books with fewer than 3 copies ---
print("--- Books with fewer than 3 copies ---")
books_items = list(books.items())
for item in books_items:
    if item[1] < 3:
        print(item[0], ":", item[1])
print("\n" + "-" * 40)

# --- Task 2: Find the book with maximum copies ---
print("--- Book with Maximum Copies ---")
max_copies_book = books_items[0][0]
max_copies_count = books_items[0][1]
for item in books_items:
    if item[1] > max_copies_count:
        max_copies_book = item[0]
        max_copies_count = item[1]
print("Maximum Copies:", max_copies_book, "with", max_copies_count, "copies")
print("\n" + "-" * 40)

# --- Task 3: Find the book with minimum copies ---
print("--- Book with Minimum Copies ---")
min_copies_book = books_items[0][0]
min_copies_count = books_items[0][1]
for item in books_items:
    if item[1] < min_copies_count:
        min_copies_book = item[0]
        min_copies_count = item[1]
print("Minimum Copies:", min_copies_book, "with", min_copies_count, "copies")
print("\n" + "-" * 40)

# --- Task 4: Count total books available ---
print("--- Total Books Available ---")
total_books = 0
for item in books_items:
    total_books += item[1]
print("Total books available in library:", total_books)
print("\n" + "-" * 40)

# --- Task 5: Generate a restocking list ---
print("--- Restocking List ---")
restock_list = []
for item in books_items:
    if item[1] < 3:  # Selecting books with low stock (fewer than 3 copies) to restock
        restock_list.append(item[0])
print("Books requiring restocking:", restock_list)
print("\n" + "-" * 40)
