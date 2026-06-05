# 1. Initialize an empty list
numbers = []

# 2. Get 20 numbers from the user
print("Please enter 20 numbers:")
for i in range(20):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
element =  int(input("enter any number to remove the duplicate"))
#finding the frequency of given number
frequency = numbers.count(element)
if frequency == 0:
    print("element not found")
elif frequency == 1:
    print("no duplicates present")
else:
    #reversing the list
    numbers.reverse()
    for i in range(1, frequency):
        numbers.remove(element)
    #reversing the list again
    numbers.reverse()
    print("After removing duplicates")
    print(numbers)



