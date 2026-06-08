# Monthly electricity consumption (units) is stored as: 
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
# 4. Calculate total units consumed.  
# 5. Create lists:  
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
    "House110": 600 
}
# 1. Display houses consuming more than 400 units.
print("Houses consuming more than 400 units:")
units_items =list(units.items())
for item in units_items:
    if item[1] > 400:
        print(item[0])
print("-" * 40)
# 2. Find the highest-consuming house.
highest_consuming_house = units_items[0][0]
for item in units_items:
    if item[1] > units[highest_consuming_house]:
        highest_consuming_house = item[0]
print("Highest-consuming house:", highest_consuming_house)
print("-" * 40)
# 3. Find the lowest-consuming house.
lowest_consuming_house = units_items[0][0]
for item in units_items:
    if item[1] < units[lowest_consuming_house]:
        lowest_consuming_house = item[0]
print("Lowest-consuming house:", lowest_consuming_house)
print("-" * 40)
# 4. Calculate total units consumed.
total_units = 0
for item in units_items:
    total_units += item[1]
print("Total units consumed:", total_units) 
print("-" * 40)
# 5. Create lists:
low_consumption = []
medium_consumption = []
high_consumption = []

for item in units_items:
    if item[1] < 200:
        low_consumption.append(item[0])
    elif 200 <= item[1] <= 400:
        medium_consumption.append(item[0])
    else:
        high_consumption.append(item[0])

print("Low consumption houses (< 200):", low_consumption)
print("Medium consumption houses (200–400):", medium_consumption)
print("High consumption houses (> 400):", high_consumption)
print("-" * 40)
# 6. Count houses eligible for an energy-saving campaign (consumption > 300).
eligible_houses = 0
for item in units_items:
    if item[1] > 300:
        eligible_houses += 1
print("Number of houses eligible for energy-saving campaign:", eligible_houses)
print("-" * 40)
