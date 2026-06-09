# import  shapes area and perimeter functions
import shapes_area_perimeter      
#main function
shape = input("Enter the shape (rectangle/circle/square): ").lower()
if shape == "rectangle":
    #enter length
    length = float(input("Enter the length of the rectangle: "))
    #validate length
    if length < 0:
        exit("Length cannot be negative.")
    #enter width
    width = float(input("Enter the width of the rectangle: "))
    #validate width
    if width < 0:
        exit("Width cannot be negative.")
    area, perimeter = shapes_area_perimeter.rectangle(length, width)
    print("The area of the rectangle is:", area)
    print("The perimeter of the rectangle is:", perimeter)
elif shape == "circle":
    #enter radius
    radius = float(input("Enter the radius of the circle: "))
    #validate radius
    if radius < 0:
        exit("Radius cannot be negative.")
    area, perimeter = shapes_area_perimeter.circle(radius)
    print("The area of the circle is:", area)
    print("The perimeter of the circle is:", perimeter)
elif shape == "square":
    #enter side
    side = float(input("Enter the side of the square: "))
    #validate side
    if side < 0:
        exit("Side cannot be negative.")
    area, perimeter = shapes_area_perimeter.square(side)
    print("The area of the square is:", area)
    print("The perimeter of the square is:", perimeter)
else:
    print("Invalid shape entered.")
