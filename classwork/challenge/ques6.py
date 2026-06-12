# 1. Create telemetry.txt data file
with open("telemetry.txt", "w") as f:
    readings = [101, 98, 105, 110, 112, 95, 90, 88, 120, 102]
    for r in readings:
        f.write(f"{r}\n")

# 2. Track metrics
all_readings = []
abnormal_readings = []
normal_count = 0
abnormal_count = 0

with open("telemetry.txt", "r") as f:
    for line in f:
        val = line.strip()
        if val:
            num = int(val)
            all_readings.append(num)
            if num < 90 or num > 110:
                abnormal_readings.append(num)
                abnormal_count += 1
            else:
                normal_count += 1

avg_value = sum(all_readings) / len(all_readings)

# 3. Store to alerts.txt
with open("alerts.txt", "w") as f:
    for num in abnormal_readings:
        f.write(f"{num}\n")

# Display Output
print("Abnormal Sensor Readings:")
for num in abnormal_readings:
    print(num)

print(f"\nAverage Sensor Value:\n{avg_value:.1f}")
print(f"\nNormal Readings: {normal_count}")
print(f"Abnormal Readings: {abnormal_count}")
print("\nAlert File Generated Successfully.")