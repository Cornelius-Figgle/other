#importing things
from random import randint
from msvcrt import getwch, getwche
from time import sleep

def start():
    #username and intro screen
    print("Hey! Welcome to my game!")
    username = input("Please choose a username: ")

    #explanation of the game
    print(f"Well, {username} guess as many numbers on the dice roll as possible! \nWe will roll 1 dice, and if you guess the number you win!")

#we show the computer how to roll a dice now
def RollDice(): 
    print("Rolling Dice...")
    sleep(1)
    return randint(1, 6)

#now we show the computer how to ask for guesses
def AskGuess(): 
    print("Please guess a number: ")
    sleep(1)
    return getwche() #single charakter input but it echoes to comsole

#now we show the computer how to check if that answer is right
def CheckGuess(roll, guess):
    if guess == roll: print(f"You guessed it! The number was {roll}!")
    elif guess != roll: print(f"Wrong! The number was {roll}!")
    else: print("Error In Roll Check")

if __name__ == '__main__':
    #now we tell it to do all that in order :D
    start()
    roll = RollDice()
    guess = AskGuess()
    CheckGuess(roll, guess)

    getwch() #to stop autoclose, waits for you to press anykey

quit()

var = True
print(var) #True

def myfunc():
    var = False
    print(var) #False

myfunc()
print(var) #True



var = True
print(var) #True

def myfunc(var):
    var = False
    print(var) #False
    return var #False

var = myfunc(var)
print(var) #False