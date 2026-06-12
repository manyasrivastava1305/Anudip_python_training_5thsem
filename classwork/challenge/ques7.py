# Crop moisture levels (%) are stored as follows: 
# moisture = { 
#     "Field1": 55, 
#     "Field2": 30, 
#     "Field3": 72, 
#     "Field4": 28, 
#     "Field5": 64, 
#     "Field6": 35, 
#     "Field7": 80, 
#     "Field8": 42, 
#     "Field9": 25, 
#     "Field10": 68 
# } 
# Tasks 
# 1. Identify fields requiring irrigation (< 40%).  
# 2. Classify fields into Low, Moderate, and High moisture categories.  
# 3. Count fields in each category.  
# 4. Find fields with the highest and lowest moisture levels.  
# 5. Generate an irrigation priority list. 
moisture = {
    "Field1": 55, "Field2": 30, "Field3": 72, "Field4": 28, "Field5": 64,
    "Field6": 35, "Field7": 80, "Field8": 42, "Field9": 25, "Field10": 68
}

requires_irrigation = []
low_moisture = []
moderate_moisture = []
high_moisture = []

highest_field = ""
lowest_field = ""
max_m = -1
min_m = 101

# Classify and analyze dictionary
for field, level in moisture.items():
    if level < 40:
        requires_irrigation.append(field)
        low_moisture.append(field)
    elif 40 <= level <= 65:
        moderate_moisture.append(field)
    else:
        high_moisture.append(field)

    if level > max_m:
        max_m = level
        highest_field = field
    if level < min_m:
        min_m = level
        lowest_field = field

# Generate priority list sorted by lowest moisture first
# (Sorting custom items with a basic lambda function)
priority_list = sorted(requires_irrigation, key=lambda x: moisture[x])

# Display Output
print("Fields Requiring Irrigation:")
for f in requires_irrigation:
    print(f)

print(f"\nLow Moisture Fields:\n{low_moisture}")
print(f"\nModerate Moisture Fields:\n{moderate_moisture}")
print(f"\nHigh Moisture Fields:\n{high_moisture}")
print(f"\nField with Highest Moisture:\n{highest_field} ({max_m}%)")
print(f"\nField with Lowest Moisture:\n{lowest_field} ({min_m}%)")
print(f"\nIrrigation Priority List:\n{priority_list}")
