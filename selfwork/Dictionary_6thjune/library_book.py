#  Library Book Availability 
"""
Sample Data books = {     
"Python Basics": 5,     
"Data Structures": 0,     
"Machine Learning": 3,     
"Java Programming": 2,     
"DBMS": 0,     
"Operating Systems": 6,     
"Networking": 4,     
"Cloud Computing": 1,     
"Cyber Security": 0,     
"Web Development": 7 
} 
Tasks 
• Display books that are currently unavailable.  
• Count the number of available books.  
• Find the book with the maximum copies.  
• Create a list of books having less than 3 copies.  
• Calculate the total number of books available.
"""

# Library Book Availability

books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Task 1: Display books that are currently unavailable
print("Task 1: Unavailable Books")

for book, copies in books.items():
    if copies == 0:
        print(book)

# Task 2: Count the number of available books
available_count = 0

for copies in books.values():
    if copies > 0:
        available_count += 1

print("\nTask 2: Number of available books =", available_count)

# Task 3: Find the book with maximum copies
max_book = max(books, key=books.get)

print("\nTask 3: Book with maximum copies")
print(max_book, ":", books[max_book])

# Task 4: Create a list of books having less than 3 copies
less_than_3 = []

for book, copies in books.items():
    if copies < 3:
        less_than_3.append(book)

print("\nTask 4: Books having less than 3 copies")
print(less_than_3)

# Task 5: Calculate the total number of books available
total_books = sum(books.values())

print("\nTask 5: Total number of books available =", total_books)
