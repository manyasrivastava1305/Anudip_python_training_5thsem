# Program to check whether a number is a Mountain Number
num = input("Enter a number: ")
increasing = False
decreasing = False
i = 0
# Check increasing part
while i < len(num) - 1 and num[i] < num[i + 1]:
    increasing = True
    i += 1
# Check decreasing part
while i < len(num) - 1 and num[i] > num[i + 1]:
    decreasing = True
    i += 1
# If both increasing and decreasing parts exist and all digits are processed, it is a Mountain Number
if increasing and decreasing and i == len(num) - 1:
    print("Mountain Number")
else:
    print("Not a Mountain Number")
