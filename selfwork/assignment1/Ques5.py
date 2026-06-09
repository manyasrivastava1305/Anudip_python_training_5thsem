
# The government wants to analyze city data. 
# Store details of at least 30 cities. 
# Example Structure 
# cities = { 
#     "Delhi": { 
#         "population": 32000000, 
#         "area": 1484, 
#         "literacy": 89 
#     } 
# } 
# Requirements:
# 1. Display all city details.   
# 2. Find the most populated city.   
# 3. Find the least populated city.   
# 4. Calculate average population.   
# 5. Display cities with literacy rate above 90%.   
# 6. Display cities with literacy below average.   
# 7. Calculate population density.   
# 8. Find city with highest density.   
# 9. Categorize cities (Small, Medium, Large).   
# 10. Create a development-priority list.   
# 11. Generate separate dictionaries for High/Low Literacy Cities.   
# 12. Generate a national summary report.   
# Challenge: Rank all cities based on population density.
# ==============================================================================

# 1. Initialize data with exactly 30 cities and display details
cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 20000000, "area": 603, "literacy": 88},
    "Bangalore": {"population": 12000000, "area": 709, "literacy": 92},
    "Chennai": {"population": 11000000, "area": 426, "literacy": 90},
    "Kolkata": {"population": 15000000, "area": 205, "literacy": 87},
    "Hyderabad": {"population": 10500000, "area": 650, "literacy": 83},
    "Ahmedabad": {"population": 8500000, "area": 505, "literacy": 89},
    "Pune": {"population": 7000000, "area": 331, "literacy": 91},
    "Surat": {"population": 6000000, "area": 462, "literacy": 87},
    "Jaipur": {"population": 4000000, "area": 484, "literacy": 84},
    "Lucknow": {"population": 3800000, "area": 349, "literacy": 82},
    "Kanpur": {"population": 3200000, "area": 260, "literacy": 79},
    "Nagpur": {"population": 2900000, "area": 228, "literacy": 93},
    "Indore": {"population": 3300000, "area": 530, "literacy": 85},
    "Thane": {"population": 2400000, "area": 147, "literacy": 91},
    "Bhopal": {"population": 2500000, "area": 285, "literacy": 85},
    "Patna": {"population": 2600000, "area": 250, "literacy": 83},
    "Vadodara": {"population": 2200000, "area": 220, "literacy": 91},
    "Ghaziabad": {"population": 2400000, "area": 210, "literacy": 85},
    "Ludhiana": {"population": 1700000, "area": 159, "literacy": 86},
    "Agra": {"population": 1600000, "area": 121, "literacy": 73},
    "Nashik": {"population": 1500000, "area": 259, "literacy": 90},
    "Faridabad": {"population": 1400000, "area": 204, "literacy": 83},
    "Meerut": {"population": 1300000, "area": 141, "literacy": 76},
    "Rajkot": {"population": 1400000, "area": 170, "literacy": 82},
    "Varanasi": {"population": 1200000, "area": 82, "literacy": 77},
    "Srinagar": {"population": 1200000, "area": 294, "literacy": 71},
    "Amritsar": {"population": 1100000, "area": 139, "literacy": 84},
    "Navi Mumbai": {"population": 1100000, "area": 344, "literacy": 96},
    "Ranchi": {"population": 1000000, "area": 175, "literacy": 87}
}

print("All City Details:")
for city, details in cities.items():
    print(f"City: {city}, Population: {details['population']}, Area: {details['area']} sq km, Literacy Rate: {details['literacy']}%")


# 2. Find the most populated city.
most_populated_city = None
max_population = -1

for city, details in cities.items():
    if details['population'] > max_population:
        max_population = details['population']
        most_populated_city = city

print(f"\nMost Populated City: {most_populated_city} with a population of {max_population}")


# 3. Find the least populated city.
least_populated_city = None
min_population = float('inf')

for city, details in cities.items():
    if details['population'] < min_population:
        min_population = details['population']
        least_populated_city = city

print(f"Least Populated City: {least_populated_city} with a population of {min_population}")


# 4. Calculate average population.
total_population = 0
for city, details in cities.items():
    total_population += details['population']

average_population = total_population / len(cities)
print(f"\nAverage Population across cities: {average_population:.2f}")


# 5. Display cities with literacy rate above 90%.
print("\nCities with Literacy Rate above 90%:")
for city, details in cities.items():
    if details['literacy'] > 90:
        print(f"  City: {city}, Literacy Rate: {details['literacy']}%")


# 6. Display cities with literacy below average.
total_literacy = 0
for city, details in cities.items():
    total_literacy += details['literacy']

average_literacy = total_literacy / len(cities)
print(f"\nAverage Literacy Rate: {average_literacy:.2f}%")
print("Cities with Literacy Rate below Average:")
for city, details in cities.items():
    if details['literacy'] < average_literacy:
        print(f"  City: {city}, Literacy Rate: {details['literacy']}%")


# 7. Calculate population density.
print("\nPopulation Density of Cities (people per sq km):")
for city, details in cities.items():
    density = details['population'] / details['area']
    print(f"  City: {city}, Population Density: {density:.2f} people/sq km")


# 8. Find city with highest density.
highest_density_city = None
max_density = -1

for city, details in cities.items():
    density = details['population'] / details['area']
    if density > max_density:
        max_density = density
        highest_density_city = city

print(f"\nCity with Highest Population Density: {highest_density_city} with a density of {max_density:.2f} people/sq km")


# 9. Categorize cities.
print("\nCity Categories based on Population:")
for city, details in cities.items():
    if details['population'] < 1500000:
        category = "Small"
    elif details['population'] < 10000000:
        category = "Medium"
    else:
        category = "Large"
    print(f"  City: {city}, Population: {details['population']}, Category: {category}")


# 10. Create a development-priority list (Sorted by highest population, lowest literacy using custom tracking loops).
print("\nDevelopment Priority List (High Population & Lower Literacy = Higher Priority):")
temp_priority = []
for city, details in cities.items():
    temp_priority.append([city, details['population'], details['literacy']])

priority_rank = 1
while len(temp_priority) > 0:
    target_index = 0
    for i in range(len(temp_priority)):
        # Primary check: higher population gets higher development priority
        if temp_priority[i][1] > temp_priority[target_index][1]:
            target_index = i
        # Secondary tie-breaker check: if populations are equal, lower literacy gets higher priority
        elif temp_priority[i][1] == temp_priority[target_index][1]:
            if temp_priority[i][2] < temp_priority[target_index][2]:
                target_index = i
                
    selected_city = temp_priority.pop(target_index)
    print(f"  Priority {priority_rank}: {selected_city[0]} (Population: {selected_city[1]}, Literacy: {selected_city[2]}%)")
    priority_rank += 1


# 11. Generate separate dictionaries for High/Low Literacy.
high_literacy_cities = {}
low_literacy_cities = {}

for city, details in cities.items():
    if details['literacy'] > 90:
        high_literacy_cities[city] = details
    else:
        low_literacy_cities[city] = details

print("\nSaved to 'high_literacy_cities' dictionary.")
print("Saved to 'low_literacy_cities' dictionary.")


# 12. Generate a national summary report.
print("\n" + "="*50)
print("              NATIONAL SUMMARY REPORT             ")
print("="*50)
print(f"Total Evaluated Urban Centers : {len(cities)}")
print(f"Total Combined Population     : {total_population}")
print(f"National Average Literacy Rate: {average_literacy:.2f}%")
print(f"Macro Population Peak         : {most_populated_city} ({max_population})")
print(f"Highest Urban Congestion Zone : {highest_density_city} ({max_density:.2f} people/sq km)")
print("="*50)


# ==============================================================================
# CHALLENGE: Rank all cities based on population density (Basic Selection Sort Method)
# ==============================================================================
print("\nFinal Challenge: Cities Ranked by Population Density (Highest to Lowest):")

# Build a working table calculation using list vectors
density_list = []
for city, details in cities.items():
    calc_density = details['population'] / details['area']
    density_list.append([city, calc_density])

# Process ranks sequentially using selection pop logic
rank = 1
while len(density_list) > 0:
    max_idx = 0
    for i in range(len(density_list)):
        if density_list[i][1] > density_list[max_idx][1]:
            max_idx = i
            
    current_ranker = density_list.pop(max_idx)
    print(f"  Rank {rank:02d}: {current_ranker[0]:<15} | Density: {current_ranker[1]:.2f} people/sq km")
    rank += 1
