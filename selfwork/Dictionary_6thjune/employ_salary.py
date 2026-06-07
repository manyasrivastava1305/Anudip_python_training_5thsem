# Electricity Consumption Report 
"""
Sample Data units = {     
"House101": 320,     
"House102": 180,     
"House103": 450,     
"House104": 290,     
"House105": 150,     
"House106": 510,     
"House107": 220,     
"House108": 390,     
"House109": 170,     
"House110": 260 
} 
Tasks 
• Display houses consuming more than 300 units.  
• Count houses consuming less than 200 units.  
• Find the house with the highest consumption.  
• Create a list of houses eligible for an energy-saving awareness campaign (consumption > 400 units).  
• Categorize houses as:  
 o Low: < 200 units  
 o Medium: 200–350 units  
 o High: > 350 units
 """

 # Electricity Consumption Report

units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# Task 1: Display houses consuming more than 300 units
print("Task 1: Houses consuming more than 300 units")

for house, unit in units.items():
    if unit > 300:
        print(house, ":", unit)

# Task 2: Count houses consuming less than 200 units
count_less_than_200 = 0

for unit in units.values():
    if unit < 200:
        count_less_than_200 += 1

print("\nTask 2: Houses consuming less than 200 units =", count_less_than_200)

# Task 3: Find the house with the highest consumption
highest_house = max(units, key=units.get)

print("\nTask 3: House with highest consumption")
print(highest_house, ":", units[highest_house])

# Task 4: Create a list of houses eligible for energy-saving awareness campaign
campaign_list = []

for house, unit in units.items():
    if unit > 400:
        campaign_list.append(house)

print("\nTask 4: Houses eligible for awareness campaign")
print(campaign_list)

# Task 5: Categorize houses
print("\nTask 5: House Categories")

for house, unit in units.items():

    if unit < 200:
        category = "Low"

    elif unit <= 350:
        category = "Medium"

    else:
        category = "High"

    print(house, ":", category)
