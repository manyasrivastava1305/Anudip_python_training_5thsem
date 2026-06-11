# The parking status of vehicles in a mall is maintained as follows. 
# Sample Data 
# parking_slots = [ 
#     "Occupied", "Vacant", "Occupied", "Vacant", 
#     "Occupied", "Occupied", "Vacant", "Occupied", 
#     "Vacant", "Occupied" 
# ] 
# Tasks 
# 1. Display vacant parking slot numbers.  
# 2. Count occupied and vacant slots.  
# 3. Allocate the first vacant slot to a new vehicle.  
# 4. Calculate parking occupancy percentage.  
# 5. Store updated parking information in parking.txt.  
# Sample Data (Adjusting 0-index conversion to human-readable 1-10 slot indexing)
parking_slots = ["Occupied", "Vacant", "Occupied", "Vacant", "Occupied", "Occupied", "Vacant", "Occupied", "Vacant", "Occupied"]

# 1. Display vacant parking slot numbers
print("Vacant Parking Slots:")
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        print(i + 1, end=" ")
print("\n")

# 2. Count occupied and vacant slots
occupied_count = 0
vacant_count = 0
for slot in parking_slots:
    if slot == "Occupied":
        occupied_count += 1
    elif slot == "Vacant":
        vacant_count += 1

print(f"Occupied Slots: {occupied_count}")
print(f"Vacant Slots: {vacant_count}")

# 3. Allocate the first vacant slot to a new vehicle
allocated_slot = None
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"
        allocated_slot = i + 1
        break
print(f"Vehicle Allocated to Slot {allocated_slot}")

# 4. Calculate parking occupancy percentage
total_slots = len(parking_slots)
current_occupied = 0
for slot in parking_slots:
    if slot == "Occupied":
        current_occupied += 1
occupancy_percentage = (current_occupied / total_slots) * 100
print(f"Occupancy Percentage: {occupancy_percentage}%")

# 5. Store updated parking information in parking.txt
with open("parking.txt", "w") as file:
    for i in range(len(parking_slots)):
        file.write(f"Slot {i+1}: {parking_slots[i]}\n")
print("Parking Details Saved Successfully.")
