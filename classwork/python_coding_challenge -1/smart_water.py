# #Monthly water consumption (in litres) of households is recorded below. 
# Sample Data 
# water_usage = { 
#     "House101": 1800, 
#     "House102": 2200, 
#     "House103": 3500, 
#     "House104": 2800, 
#     "House105": 1600, 
#     "House106": 4100, 
#     "House107": 2400, 
#     "House108": 3900, 
#     "House109": 1500, 
#     "House110": 4500 
# } 
# Tasks 
# 1. Display houses consuming more than 3000 litres.  
# 2. Find the highest and lowest consumers.  
# 3. Calculate total water consumption.  
# 4. Categorize houses:  
# o Low (<2000 litres)  
# o Medium (2000–3500 litres)  
# o High (>3500 litres)  
# 5. Count households eligible for conservation awareness programs (>2500 litres).  
# Sample Data
water_usage = { 
    "House101": 1800, 
    "House102": 2200, 
    "House103": 3500, 
    "House104": 2800, 
    "House105": 1600, 
    "House106": 4100, 
    "House107": 2400, 
    "House108": 3900, 
    "House109": 1500, 
    "House110": 4500 
}

# --- Validation: Ensure dataset is not empty before processing ---
if not water_usage:
    print("Error: No water consumption records found!")
else:
    # 1. Display houses consuming more than 3000 litres
    print("Houses consuming more than 3000 litres:")
    found_high_consumers = False
    for house, litres in water_usage.items():
        if litres > 3000:
            print(house, "-", litres, "litres")
            found_high_consumers = True
            
    if not found_high_consumers:
        print("None")
    print("-" * 40)

    # 2. Find the highest and lowest consumers
    # Finding the keys (House IDs) corresponding to the max and min values safely
    highest_house = max(water_usage, key=water_usage.get)
    lowest_house = min(water_usage, key=water_usage.get)
    
    print("Highest Water Consumer:", highest_house, "with", water_usage[highest_house], "litres")
    print("Lowest Water Consumer:", lowest_house, "with", water_usage[lowest_house], "litres")
    print("-" * 40)

    # 3. Calculate total water consumption
    total_consumption = sum(water_usage.values())
    print("Total Water Consumption of all households:", total_consumption, "litres")
    print("-" * 40)

    # 4. Categorize houses
    print("Household Categorization:")
    for house, litres in water_usage.items():
        # Input Validation: Skip invalid or negative consumption readings
        if litres < 0:
            print(house, "- Invalid Reading skipped")
            continue
            
        if litres < 2000:
            category = "Low"
        elif litres <= 3500:
            category = "Medium"
        else:
            category = "High"
            
        print(house, ": Category -", category)
    print("-" * 40)

    # 5. Count households eligible for conservation awareness programs (>2500 litres)
    awareness_count = 0
    for litres in water_usage.values():
        if litres > 2500:
            awareness_count += 1
            
    print("Households eligible for conservation awareness programs:", awareness_count)
