num = int(input("Enter any Number: "))
num_str = str(num)
num_digits = len(num_str)

sum_of_powers = 0

for digit in num_str:
    sum_of_powers += int(digit) ** num_digits

if sum_of_powers == num:
    print("Number is an Armstrong number")
else:
    print("Number is not an Armstrong number")
