class Rectangle:
    # Constructor only needs length and breadth
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
        self.__area = 0
        self.__perimeter = 0

    # Method to calculate and display area
    def calculate_area(self):
        self.__area = self.__length * self.__breadth
        print(f"\n-> Area of the Rectangle: {self.__area}")

    # Method to calculate and display perimeter
    def calculate_perimeter(self):
        self.__perimeter = 2 * (self.__length + self.__breadth)
        print(f"\n-> Perimeter of the Rectangle: {self.__perimeter}")


# Helper function to validate if a string input is a valid positive number
def is_valid_number(user_input):
    # Remove a single decimal point to check for float numbers
    clean_input = user_input.replace('.', '', 1)
    
    if clean_input.isdigit():
        return True
    else:
        print("\n[Error] Invalid input! Please enter a valid positive number.")
        return False


# ------------------ Main Menu Driven Program ------------------

print("--- Welcome to the Rectangle Calculator ---")
    
# Get initial inputs as strings
l_input = input("Enter the length of the rectangle: ")
b_input = input("Enter the breadth of the rectangle: ")
    
# Validate inputs using if-else
if is_valid_number(l_input) and is_valid_number(b_input):
    l = float(l_input)
    b = float(b_input)
    # Create the rectangle object
    rect = Rectangle(l, b)
else:
    print("Program terminated due to invalid dimensions.")
    exit() # Stop execution if initial dimensions are wrong

# Menu loop
while True:
    print("\n" + "="*30)
    print("             MENU             ")
    print("="*30)
    print("1. Calculate Area")
    print("2. Calculate Perimeter")
    print("3. Change Dimensions")
    print("4. Exit")
    print("-"*30)
        
    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        rect.calculate_area()
            
    elif choice == '2':
        rect.calculate_perimeter()
            
    elif choice == '3':
        new_l_input = input("Enter new length: ")
        new_b_input = input("Enter new breadth: ")
        
        if is_valid_number(new_l_input) and is_valid_number(new_b_input):
            l = float(new_l_input)
            b = float(new_b_input)
            rect = Rectangle(l, b)
            print("\nDimensions updated successfully!")
                
    elif choice == '4':
        print("\nThank you for using the program. Goodbye!")
        break
            
    else:
        print("\nInvalid choice! Please select a valid option (1-4).")









