from msvcrt import getwch
from qol_mth import clearConsole, sleep
#from colorama import Fore
from shutil import get_terminal_size

input()

#________________________________________________________________________________________________________________________________

def moveChoice():
    button = getwch() #takes a single character input and saves it as button

    if button.islower():
        if button == keyMap[0]: left()
        elif button == keyMap[1]: right()
        elif button == keyMap[2]: jump()
        elif button == keyMap[3]: attack()
        elif button == keyMap[4]: use()
        elif button == keyMap[5]: return not paused

def left():
    global startCordX
    global startCordY
    for y in range(0, 54):
        playArea.pop(startCordX + y * columns - 1)
        playArea.insert(startCordX + y * columns + 48, "@") 
    startCordX = startCordX - 1
def right(): 
    global startCordX
    global startCordY
    for y in range(0, 54):
        playArea.pop(startCordX + y * columns + 48)
        playArea.insert(startCordX + y * columns, "@") 
    startCordX = startCordX + 1
def jump():
    global startCordX
    global startCordY
    for x in range(0, 48):
        playArea.pop(startCordY * columns + startCordX + x - columns)
        #playArea.insert(, "@") 
    #startCordY = startCordY - 1

def attack():
    pass
def use():
    pass

#________________________________________________________________________________________________________________________________

idleOne = "            ████                                          ████████                                        ████████                                        ████████                                        ████████                                        ████████            ██████████                  ████████        ████████████████                ████████        ████████████████                ████████      ████████████████                  ████████      ████████████████                  ████████████  ████████████████            ██████████████████████████████████            ██████████████████████████████████████          ████████████████████████████████████████          ████████████████████████████████████████          ████████████████████████████████████████          ██████████████████████████████████████            ████████████████████████████████████            ██████████████████████████████████                ██████████████████████████████                    ██████████████████████████                      ████████████████████████                          ██████████████████████                          ████████████████████                            ████████████████████                          ██████████████████████                          ██████████████████████                          ██████████████████████████                      ████████████████████████████                  ████████████████████████████████                ████████████████████████████████                ██████████████  ██████████████████            ████████████████    ████████████████            ██████████████        ██████████████            ██████████████          ████████████        ████████████████            ████████████      ████████████████            ██████████████      ██████████████              ████████████        ████████████                ████████████      ████████████                  ██████████        ██████████                    ██████████      ██████████                        ██████        ████████                          ██████        ██████                            ██████        ██████                            ██████        ██████                          ██████████      ██████                          ██████████████  ████████                        ████████████████"

pausedScreen = "\n\tPaused"

#________________________________________________________________________________________________________________________________

keyMap = ["a", "d", "w", " ", "e", "p"]
paused = False

#________________________________________________________________________________________________________________________________

columns = get_terminal_size()[0] #extracts amount of columns
lines = get_terminal_size()[1] #extracts amount of lines
area = columns * lines #works out chars on screen

startCordY = lines // 10
startCordX = columns // 10

playArea = [] #blank list
for i in range(0, area): playArea.append("@") #playArea.append(baackgroundOne[i]) #etc u get the idea

#________________________________________________________________________________________________________________________________

for y in range(0, 48):
    for x in range(0, 48): 
        playArea.pop(startCordY * columns + startCordX + x + columns * y)
        playArea.insert(startCordY * columns + startCordX + x + columns * y, idleOne[x + 48 * y])

#________________________________________________________________________________________________________________________________

while True:
    paused = moveChoice()
    #clearConsole() #seizure warning!!!
    if not paused: print("".join(playArea))
    elif paused: 
        clearConsole()
        print(pausedScreen)