import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

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

