import os

FILENAME = "books.txt"

def load_books():
    books = []
    if not os.path.exists(FILENAME):
        return books
    with open(FILENAME, "r") as f:
        for line in f:
            if line.strip():
                b_id, title, qty = line.strip().split(",")
                books.append({
                    "id": b_id.strip(),
                    "title": title.strip(),
                    "qty": int(qty.strip())
                })
    return books

def save_all_books(books):
    with open(FILENAME, "w") as f:
        for b in books:
            f.write(f"{b['id']}, {b['title']}, {b['qty']}\n")

def display_all_books():
    books = load_books()
    if not books:
        print("No books available in the library library.")
        return
    print("\n--- Library Catalogue ---")
    for b in books:
        print(f"Book ID: {b['id']} | Title: {b['title']} | Available Copies: {b['qty']}")

def search_book():
    b_id = input("Enter Book ID to search: ").strip()
    books = load_books()
    for b in books:
        if b['id'].lower() == b_id.lower():
            print(f"\nBook Found:\nID: {b['id']}\nTitle: {b['title']}\nAvailable Copies: {b['qty']}")
            return
    print("Book not found.")

def issue_book():
    b_id = input("Enter Book ID to issue: ").strip()
    books = load_books()
    for b in books:
        if b['id'].lower() == b_id.lower():
            if b['qty'] > 0:
                b['qty'] -= 1
                save_all_books(books)
                print(f"Book '{b['title']}' issued successfully. Remaining copies: {b['qty']}")
            else:
                print("Sorry, this book is currently out of stock.")
            return
    print("Book ID not found.")

def return_book():
    b_id = input("Enter Book ID to return: ").strip()
    books = load_books()
    for b in books:
        if b['id'].lower() == b_id.lower():
            b['qty'] += 1
            save_all_books(books)
            print(f"Book '{b['title']}' returned successfully. New quantity: {b['qty']}")
            return
    print("Book ID not matching library database records.")

def display_unavailable_books():
    books = load_books()
    print("\n--- Out of Stock / Unavailable Books ---")
    found = False
    for b in books:
        if b['qty'] == 0:
            print(f"Book ID: {b['id']} | Title: {b['title']}")
            found = True
    if not found:
        print("All books are currently available.")

def display_restock_suggestions():
    books = load_books()
    print("\n--- Books Requiring Restocking (< 2 copies) ---")
    found = False
    for b in books:
        if b['qty'] < 2:
            print(f"Book ID: {b['id']} | Title: {b['title']} | Copies: {b['qty']}")
            found = True
    if not found:
        print("No books require urgent restocking.")

def menu():
    while True:
        print("\n===== Library Book Issue System =====")
        print("1. Display all books")
        print("2. Search a book using Book ID")
        print("3. Issue a book (decrease quantity)")
        print("4. Return a book (increase quantity)")
        print("5. Display unavailable books")
        print("6. Display books requiring restocking")
        print("7. Exit")
        choice = input("Enter choice (1-7): ").strip()

        if choice == '1': display_all_books()
        elif choice == '2': search_book()
        elif choice == '3': issue_book()
        elif choice == '4': return_book()
        elif choice == '5': display_unavailable_books()
        elif choice == '6': display_restock_suggestions()
        elif choice == '7':
            print("Exiting application...")
            break
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    menu()