#
#
import random
win=0


mHealth = 100
pHealth = 100
choice = input("attack or run")
while choice == "attack":
    
    playerDamage = random.randrange(0, 25)
    monsterDamage = random.randrange(0, 50)
    print("you attack the monster", playerDamage)
    mHealth -= playerDamage
    if mHealth > 0:

        pHealth -= monsterDamage
        print("the monster attacks you for", monsterDamage )
    if pHealth <= 0:
        win = 0
        print ("you have died")
        break
    elif mHealth <= 0:
        win = 1
        print("you have killed the monster")
        break
    elif pHealth >=0 and mHealth >=0:
        print ("you have " ,pHealth,"health")
        print ("the monster has ", mHealth,"health")
        choice = input("attack or run")
        if choice != "attack" or choice != "run":
            print("im not sure what that command is")
            choice = "attack"
            continue
        else:
            continue

if choice == "run":
    print("you are a coward")
if win == 0:
    print("game over")
else:
    print("you win")
