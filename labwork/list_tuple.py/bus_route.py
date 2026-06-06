# Passenger count at each stop: 
# passengers = [12, 18, 25, 30, 28, 15, 8] 
# Write a program to: 
# • Find the busiest stop.  
# • Display stops with fewer than 10 passengers.  
# • Calculate average passengers.  
# • Determine whether any stop exceeded 25 passengers. 
# Passenger counts at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# Initialize variables
total_passengers = 0
busiest_count = -1
busiest_stop_number = -1
low_passenger_stops = []
exceeded_25 = False

# Loop through the list using index positions
for index in range(len(passengers)):
    count = passengers[index]
    stop_number = index + 1  # Standardize to Stop 1, Stop 2, etc.
    
    # 1. Track the busiest stop and its count
    if count > busiest_count:
        busiest_count = count
        busiest_stop_number = stop_number
        
    # 2. Check for stops with fewer than 10 passengers
    if count < 10:
        low_passenger_stops.append(stop_number)
        
    # 4. Check if any stop exceeded 25 passengers
    if count > 25:
        exceeded_25 = True
        
    # Accumulate passengers for the average calculation
    total_passengers += count

# 3. Calculate average passengers per stop
average_passengers = total_passengers / len(passengers)

# Display the results
print("--- Passenger Traffic Report ---")
print("Busiest Stop: Stop", busiest_stop_number, "with", busiest_count, "passengers")
print("Stops with fewer than 10 passengers:", low_passenger_stops)
print("Average passengers per stop:", average_passengers)
print("Did any stop exceed 25 passengers?:", exceeded_25)
