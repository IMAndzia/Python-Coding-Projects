# track how many times it takes the user to guess the number correctly

import random

print("Welcome to the number guessing game! ")

while True:
    answer = input("Do you want to play? ")
    if answer.lower() == "no":
        print("Thank you for playing! Goodbye!")
        quit()



    while True:
        r = random.randrange(-5, 11)  # generates a random number between -5 and 10
        attempts = 0
        guess = int(input("Please enter a number between -5 and 10: "))
        attempts = attempts + 1
        print(r)

        if r == guess:
            print("You guessed it right! It took you " + str(attempts) + " attempt(s) to guess the number correctly.")
            break
        else:
            print("Sorry, you guessed it wrong! The correct number was " + str(r) + ".")
