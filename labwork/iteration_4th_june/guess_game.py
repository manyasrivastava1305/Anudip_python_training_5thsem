import random

secret_number = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-50): "))
    attempts += 1
    
    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Correct Guess")
        break

print("Total number of attempts:", attempts)
