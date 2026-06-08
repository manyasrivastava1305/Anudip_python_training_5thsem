# Daily temperatures of different cities are stored as: 
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
# 1. Display cities having temperature above 40°C.  
# 2. Find the hottest city.  
# 3. Find the coolest city.  
# 4. Calculate average temperature.  
# 5. Create a list of pleasant cities (temperature < 35°C).  
# 6. Count cities with temperature between 35°C and 40°C. 
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
    "Ahmedabad": 43,
}
# --- Task 1: Display cities having temperature above 40°C ---
print("--- Cities with temperature above 40°C ---") 
temperature_items = list(temperature.items())
for item in temperature_items:
    if item[1]>40:
        print(item[0],":",item[1])
print(  "\n" + "-" * 40)
# --- Task 2: Find the hottest city ---
hottest_city = temperature_items[0][0]
hottest_temp = temperature_items[0][1]
for item in temperature_items:
    if item[1]>hottest_temp:
        hottest_city = item[0]
        hottest_temp = item[1]
print("\nHottest city:", hottest_city, "with a temperature of", hottest_temp, "°C")
print(  "\n" + "-" * 40)
# --- Task 3: Find the coolest city ---
coolest_city = temperature_items[0][0]
coolest_temp = temperature_items[0][1]
for item in temperature_items:
    if item[1] < coolest_temp:
        coolest_city = item[0]
        coolest_temp = item[1]
print("Coolest city:", coolest_city, "with a temperature of", coolest_temp, "°C")
print(  "\n" + "-" * 40)
# --- Task 4: Calculate average temperature ---
total_temp = sum(item[1] for item in temperature_items)
average_temp = total_temp / len(temperature_items)
print("\nAverage temperature across cities:", round(average_temp, 2), "°C")
print(  "\n" + "-" * 40)
# --- Task 5: Create a list of pleasant cities (temperature < 35°C)
pleasant_cities = []
for item in temperature_items:
    if item[1] < 35:
        pleasant_cities.append(item[0])
print("Pleasant cities (temperature < 35°C):", pleasant_cities)
print(  "\n" + "-" * 40)
# --- Task 6: Count cities with temperature between 35°C and 40°C ---
count = 0
for item in temperature_items:
    if 35 <= item[1] <= 40:
        count += 1
print("Number of cities with temperature between 35°C and 40°C:", count)
print(  "\n" + "-" * 40)
