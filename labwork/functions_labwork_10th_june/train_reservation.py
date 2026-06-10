# A railway coach has seats represented as follows: 
# seats = [ 
#     "Booked", "Available", "Booked", "Booked", 
#     "Available", "Available", "Booked", "Available", 
#     "Booked", "Booked", "Available", "Booked" 
# ] 
# Requirements 
# Create the following functions: 
# 1. count_seats(seats) 
# Returns the number of booked and available seats. 
# 2. first_available(seats) 
# Returns the seat number of the first available seat. 
# 3. occupancy_percentage(seats) 
# Returns the percentage of occupied seats. 
# 4. display_available_seats(seats) 
# Displays all available seat numbers.
# Provided seats list from the problem statement
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# 1. Function to count booked and available seats
def count_seats(seats):
    booked = seats.count("Booked")
    available = seats.count("Available")
    return booked, available

# 2. Function to find the seat number of the first available seat
def first_available(seats):
    for index in range(len(seats)):
        if seats[index] == "Available":
            # Adding 1 to convert 0-based list index to 1-based seat number
            return index + 1
    return 0  # Return None if no seats are available

# 3. Function to calculate the occupancy percentage
def occupancy_percentage(seats):
    booked = seats.count("Booked")
    total_seats = len(seats)
    
    if total_seats == 0:
        return 0.0
        
    percentage = (booked / total_seats) * 100
    return percentage

# 4. Function to display all available seat numbers
def display_available_seats(seats):
    available_numbers = []
    for index in range(len(seats)):
        if seats[index] == "Available":
            # Adding 1 to convert to 1-based seat number
            available_numbers.append(str(index + 1))
            
    # Joining the seat numbers with a space to match sample output format
    print(" ".join(available_numbers))


# --- Executing and Formatting the Output ---

# Get counts
booked_count, available_count = count_seats(seats)
print("Booked Seats:",booked_count)
print("Available Seats: ",available_count)
print()  # Empty line for formatting

# Get first available seat
first_seat = first_available(seats)
print("First Available Seat:",first_seat)
print()

# Get occupancy percentage
occupancy = occupancy_percentage(seats)
# Using :.2f to format the percentage to 2 decimal places
print("Occupancy Percentage: occupancy:.2f}%")
print()

# Display all available seats
print("Available Seat Numbers:")
display_available_seats(seats)
    
