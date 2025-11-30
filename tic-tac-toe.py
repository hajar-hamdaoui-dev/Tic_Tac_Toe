import random
board = ["-" for _ in range(9)]
def display_board(board):
    print(board[0], "|", board[1],"|", board[2])
    print(board[3], "|", board[4],"|", board[5])
    print(board[6],"|",board[7],"|", board[8])


def player_move():
    while(True) : 
        position = input("Choose a position from 1 to 9 ")
        if(position.isdigit and  int(position) >= 1 and int(position) <= 9):
            position = int(position) - 1
            if(board[position] == "-"):
                board[position]="X"
                break 
            else :
                print("This Position is taken ")
def computer_move():
    while(True) : 
        position = random.randint(0,8)
        if(board[position]=="-"):
            board[position]="O"
            break
def checkIfHumanWon():
    for i in [0, 3, 6]:
        if(board[i] == "X" and  board[i+1] =="X" and board[i+2]== "X"):
            return True 
        if(board[0]=="X" and board[4]=="X" and board[8] =="X"):
            return True
        if(board[2]=="X" and board[4]=="X"and board[6]=="X"):
            return True
    return False
def checkIfComputerWon():
    for i in [0, 3, 6]:
        if(board[i] == "O" and  board[i+1] =="O" and board[i+2]== "O"):
            return True 
        if(board[0]=="O" and board[4]=="O" and board[8] =="O"):
            return True
        if(board[2]=="O" and board[4]=="O"and board[6]=="O"):
            return True
    return False
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score = minimax(False)
                board[i] = "-"
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                score = minimax(True)
                board[i] = "-"
                best_score = min(score, best_score)
        return best_score
        
         


def round():
    while(True) :
        player_move()
        display_board(board)
        print("Computer Move ...") 
        computer_move()
        display_board(board)
        if(checkIfHumanWon()):
            print("Human Won !")
            break
        if(checkIfComputerWon()):
            print("Computer won !")
            break 
round()
    
            
           

            
