from time import sleep
from os import name, system
from shutil import get_terminal_size


def clearConsole(): #stuff from webto clear
    command = 'clear'
    if name in ('nt', 'dos'):
        command = 'cls'
    system(command)

sleep(2)
temp = get_terminal_size() #wrokout size
columns = temp[0]
lines = temp[1]
area = columns * lines #work ourthe amount of chars on screen
charsOnScreen = [] # blank list
for i in range(1, area): #adds square for amount of chars
    charsOnScreen.append("█")

toPrint = "".join(charsOnScreen) # join the list into one string
print("", end=f"\r{toPrint}") #print it with the carrage return
clearConsole() #runs clear
snapNum = (lines // 2) * (columns // 2) #floor divides the lines & the columns, then times by eachover to get rough center

def addInChar():
    if charsOnScreen[snapNum] == "█":
        charsOnScreen.pop(snapNum)
        charsOnScreen.insert(snapNum, "▓") #removes that number then adds in lower one
    elif charsOnScreen[snapNum] == "▓":
        charsOnScreen.pop(snapNum)
        charsOnScreen.insert(snapNum, "▒")
    elif charsOnScreen[snapNum] == "▒":
        charsOnScreen.pop(snapNum)
        charsOnScreen.insert(snapNum, "░")
    elif charsOnScreen[snapNum] == "░":
        charsOnScreen.pop(snapNum)
        charsOnScreen.insert(snapNum, " ")


sleep(0.1) #so u can see
toPrint = "".join(charsOnScreen) #joins list to one string
clearConsole() #clears everythibg
print("", end=f"\r{toPrint}") #prints with return

for i in range(1, 10): # repeat 9 times (odd num)
    for a in range(1, i + 1): #adds chars to list at vcaring spaces from centre - repeat i times 
        addInChar()
        snapNum = snapNum - a
        addInChar()
        snapNum = snapNum + 2 * a
        addInChar()

    sleep(0.1) #so u can see
    toPrint = "".join(charsOnScreen) #joins list to one string
    clearConsole() #clears everythibg
    print("", end=f"\r{toPrint}") #prints with return
    snapNum = (lines // 2) * (columns // 2) #floor divides the lines & the columns, then times by eachover to get rough center

#█▓▒░
input()
