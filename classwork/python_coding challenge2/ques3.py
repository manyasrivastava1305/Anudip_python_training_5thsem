# --- Delivery Times Data ---
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Initialize lists for categorizing deliveries
fast_deliveries = []
normal_deliveries = []
delayed_orders = []

# Process delivery data
total_time = sum(delivery_times)

for time in delivery_times:
    if time <= 30:
        fast_deliveries.append(time)      # Filter into Fast list
    elif 31 <= time <= 45:
        normal_deliveries.append(time)    # Filter into Normal list
    else:
        delayed_orders.append(time)       # Filter into Delayed list

# 1. & 2. Find the fastest and slowest delivery times
fastest_time = min(delivery_times) if delivery_times else 0
slowest_time = max(delivery_times) if delivery_times else 0

# 3. Calculate average delivery time
average_time = total_time / len(delivery_times) if delivery_times else 0

# --- Display Results ---
print("## Delivery Performance Summary ##")
print(f"1. Fastest Delivery Time: {fastest_time} minutes")
print(f"2. Slowest Delivery Time: {slowest_time} minutes")
print(f"3. Average Delivery Time: {average_time:.1f} minutes")
print(f"4. Delayed Orders (>45 mins): {delayed_orders}")
print(f"5. Categorized Lists:")
print(f"   - Fast (≤30 mins): {fast_deliveries}")
print(f"   - Normal (31–45 mins): {normal_deliveries}")
print(f"   - Delayed (>45 mins): {delayed_orders}")