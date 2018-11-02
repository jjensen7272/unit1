import random

menu = input("what would you like to do, play, options, credits, or exit")

if menu == ("play"):
    num1 = random.randrange(1, 100)
    print (num1)
    guess1 = int(input("guess a number between 1 - 100 : "))

elif menu == ("options"):
    ("")
    
elif menu == ("credits"):
    print("made possible by viewers like you, thank you \n and Jacob Jensen and Hayden Whitney")


elif menu.startswith("e"):
    break
