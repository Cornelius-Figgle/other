#import functions
from time import sleep
from os import system, name

clearConsole = lambda: system('cls' if name in ('nt', 'dos') else 'clear') #will clear output

#set variables
class forest(): #What this allows us to do is put ``Locations.items`` and it will bring up the relevant list of items no matter what biome we are in
    name = "forest" #for lookup
    items = ["stick", "stone"] #items in the forest
Location = forest #is looking at class
biomes = [forest.name] #the string
inventory = [] #blank
inventoryLimit = 3


#start game
clearConsole()
Username = input("Please choose a username\n")
while Username is None: Username = input("invalid username\n")

#play game
print(f"Welcome {Username}!")


def pickUpItem(item): #called with ``itemToBeThrownOnFloor = pickUpItem(newItem)``
    if len(inventory) < inventoryLimit: #``inventoryLimit`` allows for future expansion
        inventory.append(item) #if it has less that 3 items stick on end
        itemIndex = Location.items.index(item) #looks up index in location's list
        Location.items.pop(itemIndex)#remove items from locations list
        return None #b/c no item was thrown on floor
    else:  #if full inventory
        slot = input("which item do you wish to replace?") #ask for slot
        try: #sees if possible
            try: slot = inventory.index(slot) #if ``slot`` is a word
            except: slot = slot - 1 #assumes ``slot`` is a number
            deprecated = inventory[item] #the items to be thorwn on floor
            inventory.pop(slot) #remove said item
            inventory.insert(slot, item) #add in new item
            itemIndex = Location.items.index(item) #looks up index in location's list
            Location.items.pop(itemIndex)#remove items from locations list
            return deprecated #sets ``itemToBeThrownOnFloor``to be the item we removed
        except:  #if the slot chosen can't be used
            print("please pick 1, 2, 3") #remind them
            sleep(1)
            pickUpItem(item) #go back to start of code

def Location_Details():
    print (f"You are currently in the {Location.name}!")
    print(f"The items in your current location are as follows: {', '.join(Location.items)}")
    print(f"The items in your inventory are as follows: {', '.join(inventory)}")

def Pickup_Options():
    if Location.items is not None: #if you have taken all items from biome
        Chosen_Item = input("Which item would you like to pick up?\n")
        if Chosen_Item in Location.items: 
            floorItem =  pickUpItem(Chosen_Item)
            if floorItem is not None: Location.items.append(floorItem)
            print(f"The items in your inventory are as follows: {', '.join(inventory)}")
            sleep(1)
        else: 
            print("not avaliable")
            sleep(1.5)
            Pickup_Options()
    else: pass

def Game_Loop():
    print(f"The locations are as follows: {', '.join(biomes)}")
    Location = input("Please Choose a new location\n")
    while Location not in biomes: Location = input("Please Choose a valid location\n")
    Location_Details()
    Pickup_Options()
    Game_Loop()

Game_Loop()