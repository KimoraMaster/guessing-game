import random

#number = random.randint(1, 10)
print("Welcome to Anthony's Guessing Game BRU")
print("choose a difficulty")
print("1: 1-10")
print("2: 1-30")
print("3: 1-99")

diff = int(input("enter a diffculty between 1-3"))

if diff == 1:
    number = random.randint(1, 10)
elif diff == 2:
    number = random.randint(1, 30)
elif diff == 3:
    number = random.randint(1, 992)
else:
    print ("invalid option")
    number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and max "))

# give the user a hint.
if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")


## Check if the guess is correct
if guess == number:
    print("You got it!")
else:

#if the user is wrong, let them try again
    #tell the user they have 2 more tries
    print("2 more tries !")
    guess = int(input("Try again! Guess a number between 1 and 10: "))
    if guess == number:
        print("You got it!")
    else:

        # give the user a hint.
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")

        #tell the user they have 1 more tries
        print("last try!!!! !")
        guess = int(input("Try again! Guess a number between 1 and 10: "))
        if guess == number:
            print("You got it!")
        else:

            print("Sorry, the number was", number)
            print("Better luck next time!")

