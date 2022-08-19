from time import sleep
from random import choice
from os import name, system
from msvcrt import getwch

def clearConsole(): #when called clears the entire terminal
    command = 'clear'
    if name in ('nt', 'dos'): #checks sytem
        command = 'cls'
    system(command)

def enterVillage(InventoryOne, InventoryTwo, InventoryOneAmount):
    clearConsole()
    sleep(1)
    print("You have entered the village")
    sleep(2)
    print("\n\tYour inventory now consists of ",InventoryOne," x" ,InventoryOneAmount, InventoryTwo,"\n")

Wood = "wood"
Body_Parts = ["Chest","Leg","Arm","Cheek","Foot"]
Evil_Synonyms = ["diabolical","evil","wicked","dishonourable","foul"]
Helpless_Synonyms = ["helpless","vulnerable","defenceless","endangered"]
Attacks_Synonyms = ["attacks","slashes","splices","hits"]
Beast_One_Dead = False
Beast_One_Health = 100
where = "woods"
InventoryOneAmount = 0
InventoryOne = ""
InventoryTwo = ""


sleep(0.5)
user = input("\n\tWhat Do You Name Yourself, Brave Warrior? ")
clearConsole()
sleep(1)
print("\n\tWelcome,",user)
sleep(2)
print("\n\tThe",(choice(Evil_Synonyms)),"British Army has invaded the tribe's village and taken the local hunter along with \n\tthe tribal shaman as a prisoner")
sleep(2)
print("\tYour good friend Scott was killed while attempting to protect the village")
sleep(2)
print("\tIt is up to you to free the prisoners and defend this poor," ,(choice(Helpless_Synonyms)), "tribe!\n")
getwch()
clearConsole()

sleep(2)
print("\n\tYou are currently in the woods, about 300m away from the nearest village. Do you: \n\t\ta) go to the village right away or \n\t\tb) try to find resouces in the woods?\n")
Action_One = getwch()
if Action_One == "b" or Action_One == "B":
    InventoryOne = Wood
    InventoryOneAmount = InventoryOneAmount + 1
    print("\n\tYou stayed to gather resources, you gained some wood\n\tYour inventory now consists of ",InventoryOne," x" ,InventoryOneAmount, InventoryTwo,"\n")
    getwch()
    clearConsole()
    sleep(2)
    PossibleNewItem = Wood
    print("\n\tYou find an extra piece of wood on the ground, do you:\n\ta) pick it up or \n\tb) go to the village?\n")
    PickUpExtra1 = getwch()
    if PickUpExtra1 == "a" or PickUpExtra1 == "A":
        if InventoryOne == Wood:
            InventoryOneAmount = InventoryOneAmount + 1
            sleep(0.1)
            print("\n\tYou stayed to gather extra resources, you gained more wood\n\tYour inventory now consists of ",InventoryOne," x" ,InventoryOneAmount, InventoryTwo,"\n")
    elif PickUpExtra1 == "b" or PickUpExtra1 == "B":
        enterVillage("wood", "1", "d")
    else:
        pass
elif Action_One == "a" or Action_One == "A":
    enterVillage(InventoryOne, InventoryTwo, InventoryOneAmount)
else:
    pass

sleep(2)


getwch()

