# Monthly electricity consumption (units) of different houses in a residential society is stored as follows: 
# Sample Data 
# units = { 
#     "House101": 320, 
#     "House102": 180, 
#     "House103": 510, 
#     "House104": 275, 
#     "House105": 150, 
#     "House106": 430, 
#     "House107": 220, 
#     "House108": 390, 
#     "House109": 145, 
#     "House110": 600 
# } 
# Tasks 
# 1. Display houses consuming more than 400 units.  
# 2. Find the highest-consuming house.  
# 3. Find the lowest-consuming house.  
# 4. Calculate the total units consumed.  
# 5. Create separate lists for:  
# o Low Consumption (< 200)  
# o Medium Consumption (200–400)  
# o High Consumption (> 400)  
# 6. Count houses eligible for an energy-saving campaign (consumption > 300). 
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600,
}

# --- Task 1: Display houses consuming more than 400 units ---
print("--- Houses consuming more than 400 units ---")
units_items = list(units.items())
for item in units_items:
    if item[1] > 400:
        print(item[0], ":", item[1])
print("\n" + "-" * 40)

# --- Task 2: Find the highest-consuming house ---
print("--- Highest Consuming House ---")
highest_house = units_items[0][0]
highest_units = units_items[0][1]
for item in units_items:
    if item[1] > highest_units:
        highest_house = item[0]
        highest_units = item[1]
print("Highest Consuming House:", highest_house, "with", highest_units, "units")
print("\n" + "-" * 40)

# --- Task 3: Find the lowest-consuming house ---
print("--- Lowest Consuming House ---")
lowest_house = units_items[0][0]
lowest_units = units_items[0][1]
for item in units_items:
    if item[1] < lowest_units:
        lowest_house = item[0]
        lowest_units = item[1]
print("Lowest Consuming House:", lowest_house, "with", lowest_units, "units")
print("\n" + "-" * 40)

# --- Task 4: Calculate total units consumed ---
print("--- Total Units Consumed ---")
total_units = 0
for item in units_items:
    total_units += item[1]
print("Total units consumed:", total_units)
print("\n" + "-" * 40)

# --- Task 5: Create separate lists for low, medium, and high consumption ---
print("--- House Consumption Categories ---")
low_consumption = []
medium_consumption = []
high_consumption = []
for item in units_items:
    if item[1] < 200:
        low_consumption.append(item[0])
    elif 200 <= item[1] <= 400:
        medium_consumption.append(item[0])
    elif item[1] > 400:
        high_consumption.append(item[0])

print("Low Consumption (< 200):", low_consumption)
print("Medium Consumption (200-400):", medium_consumption)
print("High Consumption (> 400):", high_consumption)
print("\n" + "-" * 40)

# --- Task 6: Count houses eligible for energy-saving campaign ---
print("--- Houses eligible for energy-saving campaign ---")
count = 0
for item in units_items:
    if item[1] > 300:
        count += 1
print("Number of houses eligible for energy-saving campaign:", count)
print("\n" + "-" * 40)