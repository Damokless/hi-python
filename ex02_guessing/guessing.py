import sys
import random

guessingNumber = random.randrange(int(sys.argv[1]), int(sys.argv[2]))
statusGame = False

while statusGame == False :
    userInput = int(input('Guess the number between ' + sys.argv[1] + ' and ' + sys.argv[2] + ':  '))
    if userInput < guessingNumber :
        print("It's more")
    if userInput > guessingNumber :
        print("It's less")
    if userInput == guessingNumber :
        print("You won, " + str(userInput) + " was the right number")
        statusGame = True