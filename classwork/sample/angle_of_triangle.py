# --- Angle 1 Validation ---
angle1 = int(input("Enter angle 1 in degrees: "))
if angle1 <= 0 :
    exit("Invalid: A single triangle angle must be between 0 and 180 degrees.")
# --- Angle 2 Validation ---
angle2 = int(input("Enter angle 2 in degrees: "))
if angle2 <= 0 :
    exit("Invalid: A single triangle angle must be between 0 and 180 degrees.")
# --- Angle 3 Validation ---
angle3 = int(input("Enter angle 3 in degrees: "))
if angle3 <= 0 :
    exit("Invalid: A single triangle angle must be between 0 and 180 degrees.")
# --- Total Sum Validation ---
# The sum of all angles must equal exactly 180
total_sum = angle1 + angle2 + angle3
if total_sum != 180:
    exit(f"Invalid: The sum of the angles is {total_sum}°. It must be exactly 180° to form a triangle.")
# --- Success Message ---
print("Success! These angles can successfully form a triangle.")
