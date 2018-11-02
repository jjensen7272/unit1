

##i = "enter"
##while i == "enter":
##    print("looping")
##    x=input("")
##    if x == "yes":
##        continue
##    else:
##        i = " "


print("your hero is surrounded by a massive army of trolls.")
print("you unsheath your sword for you last stand")


health = 10
trolls = 0
damage = 2

while health != 0:
    trolls += 1
    health -= damage
    print("your hero defeats a troll, " \
          "but takes," damage, "damage points.\n")

print("your hero fought faviantly and defeated" , trolls, "trolls.")
print("But alas, your hero is no more.")

input("\n\nPress the enter key to exit")
