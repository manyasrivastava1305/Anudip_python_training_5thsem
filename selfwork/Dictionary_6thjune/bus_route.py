# Bus Route Passenger Analysis 
"""
Sample Data passengers = {     
"Stop1": 12,     
"Stop2": 25,     
"Stop3": 18,     
"Stop4": 32,     
"Stop5": 9,     
"Stop6": 28,     
"Stop7": 14,     
"Stop8": 7,     
"Stop9": 21,     
"Stop10": 16 
} 
Tasks 
• Display stops having more than 20 passengers.  
• Count stops with fewer than 10 passengers.  
• Find the busiest stop.  
• Create a list of stops requiring an extra bus (passengers > 25).  
• Calculate the average number of passengers.
"""

# Bus Route Passenger Analysis

passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# Task 1: Display stops having more than 20 passengers
print("Task 1: Stops having more than 20 passengers")

for stop, count in passengers.items():
    if count > 20:
        print(stop, ":", count)

# Task 2: Count stops with fewer than 10 passengers
count_less_than_10 = 0

for count in passengers.values():
    if count < 10:
        count_less_than_10 += 1

print("\nTask 2: Stops with fewer than 10 passengers =", count_less_than_10)

# Task 3: Find the busiest stop
busiest_stop = max(passengers, key=passengers.get)

print("\nTask 3: Busiest Stop")
print(busiest_stop, ":", passengers[busiest_stop])

# Task 4: Create a list of stops requiring an extra bus
extra_bus_stops = []

for stop, count in passengers.items():
    if count > 25:
        extra_bus_stops.append(stop)

print("\nTask 4: Stops requiring an extra bus")
print(extra_bus_stops)

# Task 5: Calculate the average number of passengers
average_passengers = sum(passengers.values()) / len(passengers)

print("\nTask 5: Average number of passengers =", average_passengers)
