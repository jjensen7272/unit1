#jacob jensen
#1/4/19
#




import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "\nEnding program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the data file, formatted."""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

def next_block(the_file):
    category = next_line(the_file)
    questions = next_line(the_file)
    answers = []
    for i in range(4):
        answer = category + questions
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation - next_line(the_file)

    return category, question, answers, correct, explanation

def welcome(title):
    """welcome the player and get their name"""
    print("\t\twelcome to trvia challenge!")
    print("\t\t", title, "\n")


def main():
    open_file(the_file, mode)
    next_line(the_file)
    welcome(title)
    score = 0
    while category:
        print(category)
        print(question)

    for i in range(4):
        answer = input("what is the answer")
        print("for question", question,"you put", answer)
        if answer == correct:
            print("congrats you are right")
            points += 1
        else:
            print("you are wrong")

        print(explenation)
        print(score)
        
main()       
        

        


##file_name = "test_data.txt"
##the_file = open_file(file_name, "r")
##line = next_line(the_file)
##print(line)




