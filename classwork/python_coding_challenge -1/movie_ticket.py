# Seat booking status in a cinema hall is stored as follows. 
# Sample Data 
# tickets = { 
#     "A1": "Booked", 
#     "A2": "Available", 
#     "A3": "Booked", 
#     "A4": "Available", 
#     "B1": "Booked", 
#     "B2": "Available", 
#     "B3": "Booked", 
#     "B4": "Available", 
#     "C1": "Booked", 
#     "C2": "Available" 
# } 
# Tasks 
# 1. Display available seats.  
# 2. Count booked and available seats.  
# 3. Reserve the first available seat.  
# 4. Save updated booking details to tickets.txt.  
# 5. Calculate hall occupancy percentage.  
# Sample Data
tickets = { 
    "A1": "Booked", 
    "A2": "Available", 
    "A3": "Booked", 
    "A4": "Available", 
    "B1": "Booked", 
    "B2": "Available", 
    "B3": "Booked", 
    "B4": "Available", 
    "C1": "Booked", 
    "C2": "Available" 
}

# --- Validation: Ensure the system has data before executing ---
if not tickets:
    print("Error: Cinema hall seating data is empty!")
else:
    # 1. Display available seats
    print("Available Seats:")
    has_available = False
    for seat, status in tickets.items():
        if status == "Available":
            print(seat, end=" ")
            has_available = True
    print("\n")
    
    # Validation if no seats are available at all
    if not has_available:
        print("Notification: No available seats found.")

    # 2. Count booked and available seats
    booked_count = 0
    available_count = 0
    for status in tickets.values():
        if status == "Booked":
            booked_count += 1
        elif status == "Available":
            available_count += 1

    print("Total Booked Seats:", booked_count)
    print("Total Available Seats:", available_count)

    # 3. Reserve the first available seat
    reserved_seat = None
    # Sorting ensures we check rows alphabetically (A1, A2, B1...)
    for seat in sorted(tickets.keys()):
        if tickets[seat] == "Available":
            tickets[seat] = "Booked"
            reserved_seat = seat
            break  # Stop as soon as the first one is booked

    print("\nReserving Seat...")
    if reserved_seat:
        print("Success: Seat", reserved_seat, "has been successfully reserved.")
        # Update our counters because a seat status changed
        booked_count += 1
        available_count -= 1
    else:
        print("Notice: House Full! No available seats to reserve.")

    # 4. Save updated booking details to tickets.txt (Creates file automatically)
    with open("tickets.txt", "w") as file:
        for seat, status in tickets.items():
            # Standard string joining to write clean lines: A1,Booked
            file.write(seat + "," + status + "\n")
    print("Success: Updated booking details saved to 'tickets.txt'.")

    # 5. Calculate hall occupancy percentage
    total_seats = len(tickets)
    
    # Validation to prevent division by zero if the data dictionary is corrupted
    if total_seats == 0:
        print("Error: Cannot calculate occupancy because total seats equal zero.")
    else:
        occupancy_pct = (booked_count / total_seats) * 100
        print("Hall Occupancy Percentage:", round(occupancy_pct, 2), "%")
