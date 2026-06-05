# Given list of seat statuses
# 1 -> Booked, 0 -> Available
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# --- 1. Count booked and available seats ---
booked_count = seats.count(1)
available_count = seats.count(0)

print(f"Booked seats: {booked_count}")
print(f"Available seats: {available_count}")
print("-" * 40)


# --- 2. Find the first available seat and stop searching ---
first_available_seat = None

for index, status in enumerate(seats):
    if status == 0:
        first_available_seat = index + 1  # Adding 1 so seat numbering starts from 1
        break  # 'break' stops the loop immediately once found

if first_available_seat is not None:
    print(f"First available seat is seat number: {first_available_seat}")
else:
    print("No available seats found.")
print("-" * 40)


# --- 3. Create a list of all available seat numbers ---
# Adding 1 to each index so seat numbers start from 1
available_seats_list = [index + 1 for index, status in enumerate(seats) if status == 0]

print(f"List of available seat numbers: {available_seats_list}")
print("-" * 40)


# --- 4. Determine if the bus is more than 70% occupied ---
total_seats = len(seats)
occupancy_percentage = (booked_count / total_seats) * 100

print(f"Current Occupancy: {occupancy_percentage}%")

if occupancy_percentage > 70:
    print("Result: Yes, the bus is more than 70% occupied.")
else:
    print("Result: No, the bus is not more than 70% occupied.")
