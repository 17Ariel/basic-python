import random

guessNumber=random.randint(0,1000)
# print(guessNumber)
userGuess=int(input('Guess the number :'))
if(userGuess==guessNumber):
    print(guessNumber)
    print("Your guess is correct!")
else:
    print(guessNumber)
    print("Your guess is wrong!")

