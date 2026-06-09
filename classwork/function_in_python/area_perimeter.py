# Import shapes area and perimeter functions
from shapes_area_perimeter import *

# Main Menu Loop
while True:
    print("---------------------------------")
    print("           MAIN SHAPE MENU           ")
    print("---------------------------------")
    shape = input("Enter the shape (rectangle/circle/square) or 'exit' to quit: ")
    # to exit
    if shape == "exit":
        print("\nExiting the program. Goodbye!")
        break
    # for other choices    
    elif shape not in ["rectangle", "circle", "square"]:
        print("Invalid shape selection. Please try again.")
        continue

    # --------------------------------------------------------------
    # RECTANGLE LOGIC
    # --------------------------------------------------------------
    elif shape == "rectangle":
        while True:
            # Validate input values
            length = float(input("\nEnter the length of the rectangle: "))
            if length < 0:
                print("Length cannot be negative. Please try again.")
                continue
                
            width = float(input("Enter the width of the rectangle: "))
            if width < 0:
                print("Width cannot be negative. Please try again.")
                continue
            
            # Fetch calculations from module
            area, perimeter = rectangle(length, width)
            
            # Ask for operation preference
            operation = input("Calculate area or perimeter?: ")
            if operation == "area":
                print("The area of the rectangle is:" ,area)
            elif operation == "perimeter":
                print("The perimeter of the rectangle is:" ,perimeter)
            else:
                print("Invalid operation.")
            
            # Sub-menu navigation
            choice = input("\nCalculate another rectangle? (yes) or return to Main Menu? (no): ").strip().lower()
            if choice != 'yes':
                break  # Breaks the inner rectangle loop, returns to main menu

    # --------------------------------------------------------------
    # CIRCLE LOGIC
    # --------------------------------------------------------------
    elif shape == "circle":
        while True:
            radius = float(input("\nEnter the radius of the circle: "))
            if radius < 0:
                print("Radius cannot be negative. Please try again.")
                continue
                
            area, perimeter = circle(radius)
            
            operation = input("Calculate area or perimeter?: ")
            if operation == "area":
                print("The area of the circle is:" ,area)
            elif operation == "perimeter":
                print("The perimeter of the circle is:" ,perimeter)
            else:
                print("Invalid operation.")
                
            choice = input("\nCalculate another circle? (yes) or return to Main Menu? (no): ").strip().lower()
            if choice != 'yes':
                break

    # --------------------------------------------------------------
    # SQUARE LOGIC
    # --------------------------------------------------------------
    elif shape == "square":
        while True:
            side = float(input("\nEnter the side of the square: "))
            if side < 0:
                print("Side cannot be negative. Please try again.")
                continue
                
            area, perimeter = square(side)
            
            operation = input("Calculate area or perimeter?: ")
            if operation == "area":
                print("The area of the square is:" ,area)
            elif operation == "perimeter":
                print("The perimeter of the square is:" ,perimeter)
            else:
                print("Invalid operation.")
                
            choice = input("\nCalculate another square? (yes) or return to Main Menu? (no): ").strip().lower()
            if choice != 'yes':
                break
