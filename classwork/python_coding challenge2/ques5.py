# Daily mobile screen time (in minutes) of a student is recorded for 10 days:
# screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260] 
# Tasks 
# 1. Calculate average screen time.  
# 2. Find the highest and lowest screen time.  
# 3. Count days exceeding 200 minutes.  
# 4. Display days with healthy usage (<180 minutes).  
# 5. Categorize usage:  
# o Healthy (<180)  
# o Moderate (180–240)  
# o Excessive (>240) 

screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]

# Initialize lists for categorizing usage
healthy_usage = []
moderate_usage = []
excessive_usage = []

# Process screen time data
total_time = sum(screen_time)
exceeding_200_count = 0

for time in screen_time:
    # Count days exceeding 200 minutes
    if time > 200:
        exceeding_200_count += 1
        
    # Categorize usage
    if time < 180:
        healthy_usage.append(time)      # Filter into Healthy list
    elif 180 <= time <= 240:
        moderate_usage.append(time)    # Filter into Moderate list
    else:
        excessive_usage.append(time)   # Filter into Excessive list

# 1. Calculate average screen time
average_time = total_time / len(screen_time) if screen_time else 0

# 2. Find the highest and lowest screen time
highest_time = max(screen_time) if screen_time else 0
lowest_time = min(screen_time) if screen_time else 0

# --- Display Results ---
print("## Mobile Screen Time Summary ##")
print(f"1. Average Screen Time: {average_time:.1f} minutes")
print(f"2. Highest Screen Time: {highest_time} minutes")
print(f"   Lowest Screen Time: {lowest_time} minutes")
print(f"3. Days Exceeding 200 Minutes: {exceeding_200_count} days")
print(f"4. Days with Healthy Usage (<180 mins): {healthy_usage}")
print(f"5. Categorized Lists:")
print(f"   - Healthy (<180 mins): {healthy_usage}")
print(f"   - Moderate (180–240 mins): {moderate_usage}")
print(f"   - Excessive (>240 mins): {excessive_usage}")