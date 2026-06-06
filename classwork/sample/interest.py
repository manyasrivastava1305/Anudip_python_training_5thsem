import sys

p = float(input("Enter principal amount: "))
if p < 0:
    print("invalid")
    sys.exit()

r = float(input("Enter rate of interest: ")) 
if r < 0:
    print("invalid")
    sys.exit()

t = float(input("Enter time period in years: "))
if t < 0:
    print("invalid")
    sys.exit()

s: float = (p * r * t) / 100
print("Simple interest:", s)
