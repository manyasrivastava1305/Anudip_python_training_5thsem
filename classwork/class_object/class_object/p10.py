# Design a MovieTicket class containing: 
# • Movie Name  
# • Ticket Price  
# • Number of Seats Available  
# Implement methods to: 
# • Book tickets.  
# • Cancel tickets.  
# • Display booking details.  
# • Update seat availability.  
# Do not allow booking if requested seats exceed availability. 
# Sample Output: 
# Booking Successful. 
# Tickets Booked : 4 
# Amount Payable : ₹800 
# Seats Remaining: 46
class MovieTicket:
    # 1. Constructor: Sets up private attributes correctly
    def __init__(self, movie_name, ticket_price, total_seats):
        self.__movie_name = movie_name
        self.__ticket_price = ticket_price
        self.__seats_available = total_seats

    # 2. Method to book tickets
    def book_tickets(self, count):
        if count <= self.__seats_available:
            self.__seats_available -= count
            amount_payable = count * self.__ticket_price
            print("Booking Successful.")
            print("Tickets Booked :", count)
            print("Amount Payable : ₹", amount_payable)
            print("Seats Remaining:", self.__seats_available)
        else:
            print("[Error] Booking failed! Requested seats exceed availability.")
            print("Seats Available:", self.__seats_available)

    # 3. Method to cancel tickets
    def cancel_tickets(self, count):
        self.__seats_available += count
        print("Cancellation Successful.")
        print("Tickets Cancelled:", count)
        print("Seats Remaining  :", self.__seats_available)

    # 4. Method to display complete booking details
    def display_details(self):
        print("Movie Name     :", self.__movie_name)
        print("Ticket Price   : ₹", self.__ticket_price)
        print("Seats Remaining:", self.__seats_available)


# ------------------ Main Code Block ------------------

print("--- Enter Movie System Details ---")

# 1. Input and verify Movie Name (Alphanumeric check, spaces/colons allowed for movie titles)
name_input = input("Enter Movie Name: ").strip()
if not name_input.replace(" ", "").replace(":", "").replace("-", "").isalnum():
    print("[Error] Movie Name contains invalid characters!")
    exit()

# 2. Input and verify Ticket Price (Positive number check)
price_input = float(input("Enter Ticket Price: ₹"))
if price_input <= 0:
    print("[Error] Ticket price must be a positive number greater than zero!")
    exit()

# 3. Input and verify Total Number of Seats Available (Positive whole number check)
seats_input = input("Enter Number of Seats Available: ")
if not seats_input.isdigit() or int(seats_input) <= 0:
    print("[Error] Seats must be a positive whole number!")
    exit()
initial_seats = int(seats_input)

# Creating the movie ticket object since setup inputs are valid
movie = MovieTicket(name_input, price_input, initial_seats)


# Menu Loop to manage Bookings, Cancellations, and Inquiries
while True:
    print("\n==============================")
    print("      MOVIE TICKET MENU       ")
    print("==============================")
    print("1. Book Tickets")
    print("2. Cancel Tickets")
    print("3. Display Movie Details")
    print("4. Exit")
    print("------------------------------")
    
    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        count_input = input("Enter number of seats to book: ")
        if not count_input.isdigit() or int(count_input) <= 0:
            print("[Error] Booking count must be a positive whole number!")
        else:
            print("\n--- Processing Booking ---")
            movie.book_tickets(int(count_input))
            
    elif choice == '2':
        count_input = input("Enter number of seats to cancel: ")
        if not count_input.isdigit() or int(count_input) <= 0:
            print("[Error] Cancellation count must be a positive whole number!")
        else:
            print("\n--- Processing Cancellation ---")
            movie.cancel_tickets(int(count_input))
            
    elif choice == '3':
        print("\n--- Current Show Status ---")
        movie.display_details()
        
    elif choice == '4':
        print("\nExiting ticketing system. Enjoy your movie!")
        break
        
    else:
        print("\nInvalid choice! Please select an option between 1 and 4.")