# Passenger baggage weights dataset
baggage = (
    ("P101", 18),
    ("P102", 32),
    ("P103", 24),
    ("P104", 36),
    ("P105", 28),
    ("P106", 20),
    ("P107", 41),
    ("P108", 26),
    ("P109", 19),
    ("P110", 34)
)

within_limit = 0
exceeding_limit = 0
exceeding_passengers = []
excess_charges = {}
manual_inspection = []
heaviest_passenger = None
max_weight = -1

# Process baggage data
for pid, weight in baggage:
    if weight > 30:
        exceeding_limit += 1
        exceeding_passengers.append(pid)
        excess_charges[pid] = (weight - 30) * 500
        manual_inspection.append(pid)
    else:
        within_limit += 1
        
    if weight > max_weight:
        max_weight = weight
        heaviest_passenger = (pid, weight)

# Display Output
print("Passengers Exceeding 30 kg Limit:")
for pid in exceeding_passengers:
    print(pid)

print(f"\nPassengers Within Limit: {within_limit}")
print(f"Passengers Exceeding Limit: {exceeding_limit}")

print("\nExcess Baggage Charges:")
for pid, charge in excess_charges.items():
    print(f"{pid}: ₹{charge}")

print(f"\nPassenger with Heaviest Baggage:\n{heaviest_passenger[0]} ({heaviest_passenger[1]} kg)")
print(f"\nPassengers Requiring Manual Inspection:\n{manual_inspection}")