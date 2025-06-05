import random

print("Welcome to Anthony's Guessing Game BRU")
print("Choose a difficulty")
print("1: 1-10")
print("2: 1-30")
print("3: 1-99")

diff = int(input("Enter a difficulty between 1-3: "))

if diff == 1:
    max_num = 10
elif diff == 2:
    max_num = 30
elif diff == 3:
    max_num = 99
else:
    print("Invalid option, defaulting to 1-10")
    max_num = 10

number = random.randint(1, max_num)

guess = int(input(f"Guess a number between 1 and {max_num}: "))

# First guess
if guess == number:
    print("You got it!")
else:
    if guess < number:
        print("Too low!")
    else:
        print("Too high!")

    print("2 more tries!")

    # Second guess
    guess = int(input(f"Try again! Guess a number between 1 and {max_num}: "))
    if guess == number:
        print("You got it!")
    else:
        if guess < number:
            print("Too low!")
        else:
            print("Too high!")

        print("Last try!!!")

        # Third guess
        guess = int(input(f"Try again! Guess a number between 1 and {max_num}: "))
        if guess == number:
            print("You got it!")
        else:
            print(f"Sorry, the number was {number}")
            print("Better luck next time!")
