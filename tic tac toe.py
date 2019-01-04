#jacob jensen
#12/15/18
#tic tac toe
#global constants

X = "X"
O = "O"
EMPTY = ""
TIE = "TIE"
NUM_SQUARES = 9

def display():
    print("welcome chalenger")
    print("to play tic tac toe you first place your piece on the board\nThen the A.I. will make its move\nYou will continue untill someone wins")

    print("""
                          |            |
                          |            |
                          |            |
                   1      |     2      |       3
                          |            |
                          |            |
             _____________|____________|_______________
                          |            |
                          |            |
                          |            |
                   4      |     5      |       6
                          |            |
                          |            |
             _____________|____________|_______________
                          |            |
                          |            |
                          |            |
                   7      |      8     |      9 
                          |            |
                          |            |
                          |            |

""")

##################################################################################################################################
def start():
    x = True

    while x == True:
        responce = input("do you want to play y/n: ")
        if responce == "y":
            print("you choose to go play")
            break
        elif responce == "n":
            print("you choose to not play")
            break
        else:
            print("enter a valid input")


##################################################################################################################################
def pieces():
    print("do you want to go first?")
    choice = input("y/n: ")

    if choice == "y":
        print("your piece is X")
        human = X
        computer = O
    
    else:
        print("your piece is O")
        human = X
        computer = O

    return human, computer


##################################################################################################################################
def new_board():
    ##new game board
    board = []

    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return(board)



##################################################################################################################################
def display_board(board):
    """display game board on screen."""
    print("\n\t ", board[0], "|",board[1], "|",board[2])
    print("\t","--------")
    print("\t " ,board[3], "|",board[4], "|",board[5])
    print("\t","--------")
    print("\t ", board[6], "|", board[7], "|", board[8], "\n")


##################################################################################################################################
def legal_moves(board):
    moves = []
    for square in range(len(board)):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

##################################################################################################################################
def ask_number(question,low,high):
    """Ask for a number within a range."""
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            else:
                print("you must enter a number")
                response = input(question)
            return int(response)


##################################################################################################################################

def winner(board):
    """determine the game winner"""
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None


##################################################################################################################################
def human_move(board,human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("you are an idiot, that is not a legal move")
    print("fine")
    return move

##################################################################################################################################
def next_turn(turn):
    if turn == X:
        return X
    else:
        return O


##################################################################################################################################
def congrat_winner(winner,human,computer):
    if winner != TIE:
        print(winner,"won!")
        if winner != computer:
            print("this is impossible you must have cheated!")
            
        else:
            print("this proves you are inferior human")
    else:
        print(TIE)
        print("ha looser")
h=X
c=O
w=O
##################################################################################################################################
def computer_move(board, computer, human):
    """make computer move"""
    board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("I shall take the square numbered", end="")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
    
















































    


