pin = int(input("Enter your secret PIN: "))
access = False
i = 1

while not access:
    a = int(input(f"Attempt {i}: "))
    
    if pin == a:
        access = True
        print("Access granted!")
    else:
        access = False
        print("Try again.")
        i += 1
