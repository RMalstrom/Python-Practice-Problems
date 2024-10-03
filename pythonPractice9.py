"""
R. Malstrom

Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

Last modified: 10.3.2024
"""
import random


randomNumber = random.randint(1,9)
continuePlaying = True
guessCount = 0

while continuePlaying:
    userGuess = int(input("Please enter your guess for the number or enter -99 to exit. "))
    if userGuess == -99:
        continuePlaying = False
        break
    elif userGuess > randomNumber:
        print("You guess is too high")
        guessCount = guessCount + 1
    elif userGuess < randomNumber:
        print("Your guess is too low")
        guessCount = guessCount + 1
    else:
        print(f"Your guess was correct the number was {randomNumber}")
        playAgain = input("Would you like to play again? Y/N ")
        if playAgain.upper() == "N":
            continuePlaying = False
            break
        else:
            randomNumber = random.randint(1,9)
print(f"You took {guessCount} guesses.")