import math

num = int(input("Enter any Number: "))
num_str = str(num)

sum_of_factorials = 0

for digit in num_str:
    sum_of_factorials += math.factorial(int(digit))

if sum_of_factorials == num:
    print("Number is a Strong number")
else:
    print("Number is not a Strong number")
