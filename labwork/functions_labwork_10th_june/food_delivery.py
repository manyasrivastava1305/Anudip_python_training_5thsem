# Delivery times (in minutes) for diDisplays order categories: fferent orders are given below: 
# delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
# Requirements 
# Create the following functions: 
# 1. fastest_delivery(times) 
# Returns the shortest delivery time. 
# 2. delayed_orders(times) 
# Returns a list of orders taking more than 45 minutes. 
# 3. average_delivery_time(times) 
# Returns the average delivery time. 
# 4. delivery_category(times) 
# 
# • Fast → ≤ 30 minutes  
# • Normal → 31–45 minutes  
# • Delayed → > 45 minutes 
# Fixed variable name to match what you use at the bottom
times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Fixed the typo in the function name here ('fastest')
def fastest_delivery(times):
    shortest = times[0] 
    for t in times:
        if t < shortest:
            shortest = t
    return shortest

# 2. Fixed the argument to 'times', and made the loop variables consistent (using 't')
def delayed_orders(times):
    delayed = []
    for t in times:        # Changed 'i' to 't'
        if t > 45:
            delayed.append(t) # Changed 'i' to 't'
    return delayed

# 3. This function was perfect!
def average_delivery_time(times):
    total_time = 0
    count = 0
    for t in times:
        total_time = total_time + t
        count = count + 1
    return total_time / count

# 4. This function was perfect too!
def delivery_category(times):
    for t in times:
        if t <= 30:
           category = "fast" 
        elif t <= 45:  
            category = "Normal"
        else:          
            category = "Delayed"
        print(t, "mins ->", category)

# --- Running the Functions ---
# These will all run perfectly now because 'times' is defined at the top.

print("1. Fastest Delivery:", fastest_delivery(times), "minutes")
print("---")
print("2. Delayed Orders:", delayed_orders(times))
print("---")
print("3. Average Delivery Time:", average_delivery_time(times), "minutes")
print("---")
print("4. Delivery Categories:")
delivery_category(times)
