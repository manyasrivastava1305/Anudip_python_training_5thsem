# A flight reservation system stores passenger records as tuples: 
# bookings = ( 
#     ("P101", "Delhi", "Confirmed"), 
#     ("P102", "Mumbai", "Waiting"), 
#     ("P103", "Delhi", "Confirmed"), 
#     ("P104", "Chennai", "Cancelled"), 
#     ("P105", "Mumbai", "Confirmed"), 
#     ("P106", "Delhi", "Waiting") 
# ) 
# Where: 
# • Passenger ID  
# • Destination  
# • Booking Status  
# Tasks 
# Write a Python program to: 
# 1. Display all passengers whose booking status is Confirmed.  
# 2. Count the number of passengers travelling to Delhi.  
# 3. Count Confirmed, Waiting, and Cancelled bookings separately.  
# 4. Create a list containing passenger IDs with Waiting status.  
# 5. Determine which destination has the highest number of bookings. 
# Initial data given in the problem
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# --- Task 1: Display all passengers whose booking status is Confirmed ---
print("Confirmed Passengers:")
for p_id, dest, status in bookings:
    if status == "Confirmed":
        print(f"{p_id} {dest}")

# --- Task 2: Count the number of passengers travelling to Delhi ---
delhi_count = 0
for p_id, dest, status in bookings:
    if dest == "Delhi":
        delhi_count += 1
print(f"\nPassengers Travelling to Delhi: {delhi_count}")

# --- Task 3: Count Confirmed, Waiting, and Cancelled bookings separately ---
confirmed_count = 0
waiting_count = 0
cancelled_count = 0

for p_id, dest, status in bookings:
    if status == "Confirmed":
        confirmed_count += 1
    elif status == "Waiting":
        waiting_count += 1
    elif status == "Cancelled":
        cancelled_count += 1

print(f"\nConfirmed: {confirmed_count}")
print(f"Waiting: {waiting_count}")
print(f"Cancelled: {cancelled_count}")

# --- Task 4: Create a list containing passenger IDs with Waiting status ---
waiting_list = []
for p_id, dest, status in bookings:
    if status == "Waiting":
        waiting_list.append(p_id)
print(f"\nWaiting List:\n{waiting_list}")

# --- Task 5: Determine which destination has the highest number of bookings ---
# We use a dictionary to dynamically count bookings per destination
dest_counts = {}
for p_id, dest, status in bookings:
    if dest in dest_counts:
        dest_counts[dest] += 1
    else:
        dest_counts[dest] = 1
# Find the key with the maximum value in the dictionary
most_booked = max(dest_counts, key=dest_counts.get)
print(f"\nMost Booked Destination:\n{most_booked}")









