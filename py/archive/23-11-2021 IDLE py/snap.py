import os
import time
import random

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#"""
size = os.get_terminal_size()
columns = size.columns
lines = size.lines
"""
columns = 20
lines = 40
"""
area = columns * lines
console = []
i = area
while i > 0:
    i = i - 1
    console.append("█")
toPrint = "".join(console)
print(toPrint)
time.sleep(2) 
clearConsole()
snapNum = random.randint(0, columns)
    
def fadeReplace():
    snapNum = random.randint(0, columns)
    if snapNum == columns:
        snapNum = snapNum - 6
    else:
        time.sleep(0.001)
    def ifCharsW():
        if console[snapNum] == "█":
            console.pop(snapNum)
            console.insert(snapNum, "▓")
        elif console[snapNum] == "▓":
            console.pop(snapNum)
            console.insert(snapNum, "▒")
        elif console[snapNum] == "▒":
            console.pop(snapNum)
            console.insert(snapNum, "░")
        elif console[snapNum] == "░":
            console.pop(snapNum)
            console.insert(snapNum, " ")
    ifCharsW()
    time.sleep(1)
    toPrint = "".join(console)
    clearConsole()
    print(toPrint)
    i = 1
    while i < 10:
        time.sleep(1)
        ifCharsW()
        snapNum = snapNum - i
        ifCharsW()
        snapNum = snapNum + i + 1
        ifCharsW()
        clearConsole()
        toPrint = "".join(console)
        print(toPrint)
        i = i + 1


fadeReplace()

#█▓▒░
#

input()






























