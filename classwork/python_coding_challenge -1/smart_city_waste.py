# Problem Statement 
# The amount of waste collected (in kilograms) from different sectors of a city is stored below. 
# Sample Data 
# waste = { 
# "Sector1": 320, 
#     "Sector2": 180, 
#     "Sector3": 510, 
#     "Sector4": 275, 
#     "Sector5": 150, 
#     "Sector6": 430, 
#     "Sector7": 220, 
#     "Sector8": 390, 
#     "Sector9": 145, 
#     "Sector10": 600 
# } 
# Tasks 
# 1. Display sectors generating more than 400 kg of waste.  
# 2. Find the sector generating maximum waste.  
# 3. Find the sector generating minimum waste.  
# 4. Calculate the total waste collected.  
# 5. Categorize sectors:  
# o Low Waste (<200 kg)  
# o Medium Waste (200–400 kg)  
# o High Waste (>400 kg)  
# 6. Count sectors requiring awareness campaigns (waste generation >300 kg).  
# 7. Save the awareness campaign list to campaign_sectors.txt.  
# Sample Data 
waste = { 
    "Sector1": 320, 
    "Sector2": 180, 
    "Sector3": 510, 
    "Sector4": 275, 
    "Sector5": 150, 
    "Sector6": 430, 
    "Sector7": 220, 
    "Sector8": 390, 
    "Sector9": 145, 
    "Sector10": 600 
}

# --- Validation: Ensure the data dictionary contains records ---
if not waste:
    print("Error: Waste management database is empty!")
else:
    # 1. Display sectors generating more than 400 kg of waste
    print("Sectors generating more than 400 kg of waste:")
    has_high_waste = False
    for sector, kg in waste.items():
        if kg > 400:
            print(sector, "-", kg, "kg")
            has_high_waste = True
            
    if not has_high_waste:
        print("None")
    print("-" * 45)

    # 2. Find the sector generating maximum waste
    max_sector = max(waste, key=waste.get)
    print("Sector generating Maximum Waste:", max_sector, "with", waste[max_sector], "kg")

    # 3. Find the sector generating minimum waste
    min_sector = min(waste, key=waste.get)
    print("Sector generating Minimum Waste:", min_sector, "with", waste[min_sector], "kg")
    print("-" * 45)

    # 4. Calculate the total waste collected
    total_waste = sum(waste.values())
    print("Total Waste Collected from all sectors:", total_waste, "kg")
    print("-" * 45)

    # 5. Categorize sectors
    print("Sector Waste Categorization:")
    for sector, kg in waste.items():
        # Input Validation: Skip invalid or negative data entries if they exist
        if kg < 0:
            print(sector, "- Invalid negative data entry skipped")
            continue
            
        if kg < 200:
            category = "Low Waste"
        elif kg <= 400:
            category = "Medium Waste"
        else:
            category = "High Waste"
            
        print(sector, ":", category)
    print("-" * 45)

    # 6. Count sectors requiring awareness campaigns (waste generation >300 kg)
    # We will gather the names into a list to fulfill both Task 6 and Task 7 cleanly
    campaign_list = []
    for sector, kg in waste.items():
        if kg > 300:
            campaign_list.append(sector)
            
    print("Number of sectors requiring awareness campaigns:", len(campaign_list))
    print("-" * 45)

    # 7. Save the awareness campaign list to campaign_sectors.txt
    with open("campaign_sectors.txt", "w") as file:
        for sector in campaign_list:
            file.write(sector + "\n")
            
    print("Success: Awareness campaign sector list saved to 'campaign_sectors.txt'.")
