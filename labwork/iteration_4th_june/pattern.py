rows = int(input("Enter the number of rows: "))

print("Forward Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nReverse Pattern:")
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
