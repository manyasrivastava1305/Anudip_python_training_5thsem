resources = {
    "Warehouse1": ["Food", "Medicine", "Blankets"],
    "Warehouse2": ["Water", "Food", "Tents"],
    "Warehouse3": ["Medicine", "Tents", "Clothes"],
    "Warehouse4": ["Food", "Water", "Medicine"]
}

# 1. Unique materials and tracking structures
unique_resources = set()
warehouses_with_medicine = []
resource_counts = {}

for warehouse, items in resources.items():
    if "Medicine" in items:
        warehouses_with_medicine.append(warehouse)
    for item in items:
        unique_resources.add(item)
        resource_counts[item] = resource_counts.get(item, 0) + 1

# 2. Find most widely available resource
max_avail = max(resource_counts.values())
most_widely_available = [item for item, count in resource_counts.items() if count == max_avail]

# 3. Resources available in all warehouses
total_warehouses = len(resources)
all_warehouse_resources = [item for item, count in resource_counts.items() if count == total_warehouses]

# Display Output
print(f"Unique Resources:\n{unique_resources}")
print("\nWarehouses with Medicines:")
for w in warehouses_with_medicine:
    print(w)

print("\nResource Availability:")
for item, count in resource_counts.items():
    print(f"{item}: {count}")

print("\nMost Widely Available Resources:")
for item in most_widely_available:
    print(item)

print("\nResources Available in All Warehouses:")
if all_warehouse_resources:
    for item in all_warehouse_resources:
        print(item)
else:
    print("None")