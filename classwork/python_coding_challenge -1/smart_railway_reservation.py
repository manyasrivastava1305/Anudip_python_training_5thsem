# A railway reservation system stores the booking status of seats in a train coach. 
# Sample Data 
# seats = { 
#     1: "Booked", 
#     2: "Available", 
#     3: "Booked", 
#     4: "Available", 
#     5: "Booked", 
#     6: "Booked", 
#     7: "Available", 
#     8: "Booked", 
#     9: "Available", 
#     10: "Booked" 
# } 
# Tasks 
# 1. Display all available seat numbers.  
# 2. Count booked and available seats.  
# 3. Reserve the first available seat.  
# 4. Cancel booking for a given seat number.  
# 5. Store the updated reservation status in reservations.txt.  
# 6. Display occupancy percentage. 
# Sample Data
seats = {
    1: "Booked", 2: "Available", 3: "Booked", 4: "Available", 5: "Booked",
    6: "Booked", 7: "Available", 8: "Booked", 9: "Available", 10: "Booked"
}

# 1. Display all available seat numbers
print("Available Seats:")
for seat, status in seats.items():
    if status == "Available":
        print(seat, end=" ")
print("\n")

# 2. Count booked and available seats
booked_count = 0
available_count = 0
for status in seats.values():
    if status == "Booked":
        booked_count += 1
    elif status == "Available":
        available_count += 1

print(f"Booked Seats: {booked_count}")
print(f"Available Seats: {available_count}")

# 3. Reserve the first available seat
reserved_seat = None
for seat in sorted(seats.keys()):
    if seats[seat] == "Available":
        seats[seat] = "Booked"
        reserved_seat = seat
        break

if reserved_seat:
    print(f"Seat {reserved_seat} Reserved Successfully.")
else:
    print("No seats available.")

# 4. Cancel booking for a given seat number with user input and validation
try:
    cancel_seat = int(input("\nEnter the seat number you want to cancel: "))
    
    # Validation 1: Check if the seat number exists in the train coach
    if cancel_seat not in seats:
        print(f"Error: Seat {cancel_seat} does not exist in this coach.")
        
    # Validation 2: Check if the seat is actually booked before trying to cancel
    elif seats[cancel_seat] == "Available":
        print(f"Notification: Seat {cancel_seat} is already available. No cancellation needed.")
        
    # If validations pass, cancel the booking
    else:
        seats[cancel_seat] = "Available"
        print(f"Success: Booking for Seat {cancel_seat} has been cancelled.")
        
except ValueError:
    # Validation 3: Handle cases where the user inputs text instead of a number
    print("Error: Invalid input! Please enter a valid numerical seat number.")

# 6. Display occupancy percentage
# Recalculate counts after the reservation update
total_seats = len(seats)
current_booked = 0
for status in seats.values():
    if status == "Booked":
        current_booked += 1
occupancy_percentage = (current_booked / total_seats) * 100
print(f"Occupancy Percentage: {occupancy_percentage}%")

# 5. Store the updated reservation status in reservations.txt
with open("reservations.txt", "w") as file:
    for seat, status in seats.items():
        file.write(f"{seat}: {status}\n")
print("Reservation Details Saved Successfully.")
