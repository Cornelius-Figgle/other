from qol_mth import checkEven, sleep, sleep as wait


x=0
while True:
    x=x+1
    if checkEven(x) == True:
        wait(1000)
        print (x)
    elif checkEven(x) == False:
        wait(1000)
        print (x)
    



input()





var = "How Long Will You Watch For?\n"

var2 = 0

while len(var) < 10000:
    var = var + str(var2) + " "
    print("", end=f"\r{var}")
    var2 = var2 + 1
    sleep(50)

input()