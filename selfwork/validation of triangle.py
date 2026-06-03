# --- Side 1 Validation ---
side1 = int(input("Enter side 1 in cm: "))
if side1 <= 0:
    exit("Invalid: Side must be greater than 0.")

# --- Side 2 Validation ---
side2 = int(input("Enter side 2 in cm: "))
if side2 <= 0:
    exit("Invalid: Side must be greater than 0.")

# --- Side 3 Validation ---
side3 = int(input("Enter side 3 in cm: "))
if side3 <= 0:
    exit("Invalid: Side must be greater than 0.")

# --- Triangle Inequality Validation ---
# The sum of any two sides must be strictly greater than the third side
if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
    exit("Invalid: These side lengths cannot form a real triangle.")
    if side1 == side2 == side3:
        print("Yes, it is a valid Equilateral triangle.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        if ((side1 **2) + (side2 **2) == (side3 **2) or (side2 **2) + (side3 **2) == (side1 **2) or (side1 **2) + (side3 **3) == (side2 **2)):
            print("triangle is right angled Isosceles")
        else:
            print("Yes, it is a valid Isosceles triangle.")
    else:
        if ((side1 **2) + (side2 **2) == (side3 **2) or (side2 **2) + (side3 **2) == (side1 **2) or (side1 **2) + (side3 **3) == (side2 **2)):
            print("triangle is right angled Scalene")
        else:
            print("Yes, it is a valid Scalene triangle.")
    s = (side1 + side2 + side3) / 2 
    area= (s * (s- side1) * (s- side2) * (s- side3))**0.5
    perimeter = s * 2
    print("area",area, "sq. cm") 
    print("perimeter",perimeter, "cm")
else:
    print("no triangle is not possible ")  
