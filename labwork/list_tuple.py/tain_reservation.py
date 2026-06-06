# Passenger records: 
# passengers = [ 
#     ("Anuj", "Confirmed"), 
#     ("Rahul", "Waiting"), 
#     ("Priya", "Confirmed"), 
#     ("Amit", "Waiting"), 
#     ("Neha", "Confirmed") 
# ] 
# Write a program to: 
# • Display all waiting-list passengers.  
# • Count confirmed and waiting passengers.  
# • Find whether a specific passenger has a confirmed ticket.  
# • Create separate lists for confirmed and waiting passengers.
# Initial passenger records
passengers = [ 
    ("Anuj", "Confirmed"), 
    ("Rahul", "Waiting"), 
    ("Priya", "Confirmed"), 
    ("Amit", "Waiting"), 
    ("Neha", "Confirmed") 
]

# 1. Create separate lists for confirmed and waiting passengers
# (Doing this first makes the other tasks much easier!)
confirmed_passengers = [name for name, status in passengers if status == "Confirmed"]
waiting_passengers = [name for name, status in passengers if status == "Waiting"]

# 2. Display all waiting-list passengers
print("--- Waiting-List Passengers ---")
for name in waiting_passengers:
    print(f"- {name}")

print("\n--- Passenger Counts ---")
# 3. Count confirmed and waiting passengers
print(f"Total Confirmed: {len(confirmed_passengers)}")
print(f"Total Waiting: {len(waiting_passengers)}")

print("\n--- Ticket Status Check ---")
# 4. Find whether a specific passenger has a confirmed ticket
def check_status(passenger_name):
    if passenger_name in confirmed_passengers:
        return f"{passenger_name} has a Confirmed ticket."
    elif passenger_name in waiting_passengers:
        return f"{passenger_name} is on the Waiting list."
    else:
        return f"{passenger_name} not found in the passenger records."

# Example checks
print(check_status("Priya"))
print(check_status("Amit"))
print(check_status("Vikram"))
