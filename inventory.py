# Hero's inventory
# Jacob Jensen
#11/18

import random

player_health = 100
player_armor = 1250
player_attack = 250
player_money = 0

inventory = ["rusty sword","leather armor","wood shield","small healing potion"]
player_stats = ["health",player_health,"armor",player_armor,"attack",player_attack,"money",player_money]
print("player stats: ")
print(player_stats)
print()
print("your items: ")
for item in inventory:
    print(item)


input("\nPress the enter key to continue.")
print("you have", len(inventory), "items in your possession.")

player_health -= 22

input("\nyou have taken damage\n"+
      "your health is at " + str(player_health)+"\n"+
      "you need to use your healing potion \nPress the enter key to continue.")

if "small healing potion" in inventory:
    print("you will live to fight another day")
    player_health += 20
    print(player_stats)
    inventory.remove("small healing potion")
    for item in inventory:
        print(item)

index = int(input("\n Enter the index number for an item in inventory: "))
while index >len(inventory)-1 or index <0:
    print("that number is out of range")
    index = int(input("\n Enter the index number for an item in inventory: "))

print("at index", index, "is", inventory[index])

start = int(input("\n Enter the inde number to begin a slice: "))
finish = int(input("\n Enter the inde number to end a slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\n Press the enter key to continue")

chest_items = ["gold","gems","banana","master ball","dog","non magical glove","elven bows","bow","crossbow","boots","hat"]
chest = []

for i in range (3):
    item = random.choice(chest_items)
    chest.append(item)
print("You find a chest wich contains: ")
print(chest)
print("You add the contens of the chest your inventroy.")
inventory += chest
print(inventory)

input("\n Press the enter key to continue.")
print("you trade your sword for a cross bow")
inventory[0] = "crossbow"
print("your inventory is now: ")
print(inventory)

input("\n Press the enter key to continue.")
print("you use your gold to buy a orb of future telling.")
inventory[4:6] = ["orb of future telling"]
print("your inventory is now: ")
print(inventory)
input("\nPress the enter key to continue.")
print("in a great battle, your shield is destroyed.")
del inventory[2]
print("your inventory is now: ")
print(inventory)


