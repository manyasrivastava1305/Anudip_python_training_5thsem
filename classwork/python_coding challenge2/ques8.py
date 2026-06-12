# Daily temperatures of different cities:
# temperature = { 
#     "Delhi": 41, 
#     "Mumbai": 33, 
#     "Chennai": 37, 
#     "Kolkata": 39, 
#     "Bengaluru": 28, 
#     "Pune": 30, 
#     "Jaipur": 42, 
#     "Lucknow": 40, 
#     "Hyderabad": 35, 
#     "Ahmedabad": 43 
# } 
# Tasks 
# 1. Display cities with temperature above 40°C.  
# 2. Find the hottest city.  
# 3. Find the coolest city.  
# 4. Calculate average temperature.  
# 5. Create a list of pleasant cities (<35°C). 

temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
}

# --- Task 1: Display cities with temperature above 40°C ---
print("--- Cities with temperature above 40°C ---")
temp_items = list(temperature.items())
for item in temp_items:
    if item[1] > 40:
        print(item[0], ":", item[1], "°C")
print("\n" + "-" * 40)

# --- Task 2: Find the hottest city ---
print("--- Hottest City ---")
hottest_city = temp_items[0][0]
hottest_temp = temp_items[0][1]
for item in temp_items:
    if item[1] > hottest_temp:
        hottest_city = item[0]
        hottest_temp = item[1]
print("Hottest City:", hottest_city, "with", hottest_temp, "°C")
print("\n" + "-" * 40)

# --- Task 3: Find the coolest city ---
print("--- Coolest City ---")
coolest_city = temp_items[0][0]
coolest_temp = temp_items[0][1]
for item in temp_items:
    if item[1] < coolest_temp:
        coolest_city = item[0]
        coolest_temp = item[1]
print("Coolest City:", coolest_city, "with", coolest_temp, "°C")
print("\n" + "-" * 40)

# --- Task 4: Calculate average temperature ---
print("--- Average Temperature ---")
total_temp = 0
for item in temp_items:
    total_temp += item[1]
average_temp = total_temp / len(temp_items)
print("Average temperature of all cities:", average_temp, "°C")
print("\n" + "-" * 40)

# --- Task 5: Create a list of pleasant cities (<35°C) ---
print("--- Pleasant Cities ---")
pleasant_cities = []
for item in temp_items:
    if item[1] < 35:
        pleasant_cities.append(item[0])
print("List of pleasant cities (<35°C):", pleasant_cities)
print("\n" + "-" * 40)