# Vehicle Registration Analyzer Program

print("--- Vehicle Registration Analyzer ---")

# Predefined list containing 20 vehicle numbers (including some invalid ones for testing)
vehicles = [
    "MH12AB4589", "DL05XY9988", "KA03PQ1234", "HR26BM7788", "UP16CD1122",
    "MH02XY5555", "DL01AA0001", "GJ01ZZ9999", "KA51ME4321", "TN07BY1111",
    "INVALID123", "MH14A4567",  "AP09BC8822", "WB02AA5566", "HR12XX3456",
    "DL3CXY8899", "KA045PQ123", "UP32HA9000", "MH011A1234", "GJ03BC7711"
]

print("Successfully loaded ", len(vehicles), " registration numbers for analysis.\n", sep="")

invalid_registrations = []
state_counts = {}

print("=============================================")
print("          VEHICLE ANALYSIS REPORT            ")
print("=============================================\n")

# Process each vehicle registration number
for index, reg in enumerate(vehicles, 1):
    print("---------------------------------------------")
    print("Analyzing Vehicle #", index, ": '", reg, "'", sep="")
    print("---------------------------------------------")
    
    # --- 5. Count letters and digits ---
    letter_count = 0
    digit_count = 0
    
    for char in reg:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1

    # --- 6. Validate format ---
    # Total length must be exactly 10 characters based on the rule: 2 + 2 + 2 + 4 = 10
    is_valid = True
    
    if len(reg) != 10:
        is_valid = False
    else:
        # Extract segments to check their specific character types
        part1 = reg[0:2]  # State code
        part2 = reg[2:4]  # District code
        part3 = reg[4:6]  # Series
        part4 = reg[6:10] # Vehicle number
        
        # Check matching types for each segment
        if not part1.isalpha():
            is_valid = False
        if not part2.isdigit():
            is_valid = False
        if not part3.isalpha():
            is_valid = False
        if not part4.isdigit():
            is_valid = False

    # Handle invalid registration numbers
    if not is_valid:
        # 7. Track invalid registrations
        invalid_registrations.append(reg)
        print("Status: INVALID FORMAT")
        print("5. Total Letters:", letter_count, "| Total Digits:", digit_count)
        print("Reason: Does not match standard structure (AA DD AA DDDD).")
        print()
        continue # Skip data extraction for invalid numbers
        
    print("Status: VALID FORMAT")
    
    # --- 1, 2, 3, & 4. Extract Components (Safe to do since format is verified) ---
    state_code = reg[0:2]
    district_code = reg[2:4]
    series = reg[4:6]
    vehicle_num = reg[6:10]
    
    # --- 8. Count vehicles state-wise ---
    if state_code in state_counts:
        state_counts[state_code] += 1
    else:
        state_counts[state_code] = 1

    # --- Print individual results ---
    print("1. State Code:", state_code)
    print("2. District Code:", district_code)
    print("3. Series:", series)
    print("4. Vehicle Number:", vehicle_num)
    print("5. Total Letters:", letter_count, "| Total Digits:", digit_count)
    print()

print("=============================================")
print("             DEPARTMENT SUMMARY              ")
print("=============================================\n")

# 7. Display invalid registrations accumulated
print("--- 7. Invalid Registration Numbers ---")
if len(invalid_registrations) > 0:
    for inv_reg in invalid_registrations:
        print("-", inv_reg)
else:
    print("None! All tracked numbers matched the required template format.")

print()

# 8. Display state-wise breakdown counts
print("--- 8. State-Wise Vehicle Metrics ---")
if len(state_counts) > 0:
    for state, count in state_counts.items():
        print("State: '", state, "' -> Total Verified Vehicles: ", count, sep="")
else:
    print("No valid state registrations were found.")

print("\n=============================================")
print("End of Report")
print("=============================================")
