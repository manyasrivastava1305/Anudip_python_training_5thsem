i = int(input("Enter any Number: "))
factors = []

for n in range(1, i + 1):
    if i % n == 0:
        factors.append(n)

if len(factors) == 2:
    print("Number is prime")
else:
    print("Number is not prime")
    print("Factors:", factors)
