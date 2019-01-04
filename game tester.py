attempts = 0
x = True
print("Python terms")
puzzle = ("QPIJXZUOWEQZYYFLVHMTSUEDEQYNSAFJUOSZYETOCGRULMASRLLDTBADULIFOODLFHHENJOTNEMMOCGVPIDEFJIHTCSRQROHFFPI")
def display_puzzle():
    print()

    print("  0123456789")
    print("0 "+puzzle[0:10])
    print("1 "+puzzle[10:20])
    print("2 "+puzzle[20:30])
    print("3 "+puzzle[30:40])
    print("4 "+puzzle[40:50])
    print("5 "+puzzle[50:60])
    print("6 "+puzzle[60:70])
    print("7 "+puzzle[70:80])
    print("8 "+puzzle[80:90])
    print("9 "+puzzle[90:])
    print()

print()

display_puzzle()
word_list="float, double, if, else, def, comment, loops, string, True, False"
print(word_list)
word1 = "float"
word2 = "double"
word3 = "if"
word4 = "else"
word5 = "def"
word6 = "comment"
word7 = "loops"
word8 = "string"
word9 = "True"
word10 = "False"

print()

##def ():
##		usr_input_

##def score():
##		first_try=input(int("W")) 
##		second_try=
##    thrid_try=
##    fourth_try=
##    final_try=
##    no_point_try=
##    
##    
def quiz1():
    print("Decimal numbers; often represented in computer hardware as base 2 fractions")
    answer = word1
  
    if x == True:
        guess1= input("what is the vocab word?")
        if guess1 == word1:
        
            print("congrats")
            display_puzzle()
            print("find the word in the puzzle")
            finder1 = int(input("what is the position of the first letter in the word: "))
            
            finder2 = int(input("what is the position of the second letter in the word: "))
            finder3 = int(input("what is the position of the third letter in the word: "))
            finder4 = int(input("what is the position of the fourth letter in the word: "))
            finder5 = int(input("what is the position of the fifth letter in the word: "))

            print(puzzle[finder1-1])
            print(puzzle[finder2-1])
            print(puzzle[finder3-1])
            print(puzzle[finder4-1])
            print(puzzle[finder5-1])
            
        
            

        else:
            print("not correct")
quiz1()
