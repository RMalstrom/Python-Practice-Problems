"""
R. Malstrom

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

Last modified: 9.24.2024
"""
from random import randint

game = True
while game:
    userPlay = input("Please input your play: R/P/S: ")
    randomNum = randint(1, 3)
    if randomNum == 1:
        computerChoice = "R"
    elif randomNum == 2:
        computerChoice = "P"
    else:
        computerChoice = "S"

    if computerChoice != userPlay:
        if computerChoice == "R" and userPlay.upper() == "P":
            print("User wins! Paper covers Rock")
        elif computerChoice == "R" and userPlay.upper() == "S":
            print("Computer wins! Rock crushes Scissors")
        if computerChoice == "P" and userPlay.upper() == "R":
            print("Computer wins! Paper covers Rock")
        elif computerChoice == "P" and userPlay.upper() == "S":
            print("User wins! Scissors cuts Paper")
        if computerChoice == "S" and userPlay.upper() == "P":
            print("Computer wins! Scissors cuts Paper")
        elif computerChoice == "S" and userPlay.upper() == "R":
            print("User wins! Rock crushes Scissors")
    else:
        print("Its a tie")

    replay = input("Do you want to play again: Y/N ")
    if replay.upper() != "Y":
        game = False
