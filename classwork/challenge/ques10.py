traffic = [120, 95, 140, 180, 75, 60, 200, 160, 110, 85]

low_traffic = []
moderate_traffic = []
high_traffic = []

print("Traffic Conditions:")
for count in traffic:
    if count < 80:
        cond = "Low"
        low_traffic.append(count)
    elif count <= 150:
        cond = "Moderate"
        moderate_traffic.append(count)
    else:
        cond = "High"
        high_traffic.append(count)
    print(f"{count} -> {cond}")

peak_count = max(traffic)
manual_control_required = "Yes" if len(high_traffic) > 3 else "No"

# Display Summary
print(f"\nLow Traffic Intervals: {len(low_traffic)}")
print(f"Moderate Traffic Intervals: {len(moderate_traffic)}")
print(f"High Traffic Intervals: {len(high_traffic)}")
print(f"\nPeak Traffic Count:\n{peak_count} vehicles")
print(f"\nLow Traffic List:\n{low_traffic}")
print(f"\nModerate Traffic List:\n{moderate_traffic}")
print(f"\nHigh Traffic List:\n{high_traffic}")
print(f"\nManual Traffic Control Required:\n{manual_control_required}")