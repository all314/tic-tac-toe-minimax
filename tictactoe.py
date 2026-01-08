import random

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]  #initial empty board

currentPlayer = "X"
game_running = True
turn = 1

# print board

def print_board(board):
    print(board[0]+ ' | ' + board[1] + ' | ' + board[2])
    print("---------")
    print(board[3]+ ' | ' + board[4] + ' | ' + board[5])
    print("---------")
    print(board[6]+ ' | ' + board[7] + ' | ' + board[8])
    print()

    #-----

def available_moves(board):
    return [i for i in range(9) if board[i] == str(i+1)]

#take player input
def win_state(board):
    win_states = [(0,1,2), (3,4,5), (6,7,8),
                  (0,3,6), (1,4,7), (2,5,8),
                  (0,4,8), (2,4,6)]
    for a, b, c in win_states:
        if board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_full(board):
    return len(available_moves(board)) == 0

def input_index(board):
        global turn
        while True:
            inp = int(input("Enter a number 1-9 to place your mark: ")) 
            if inp-1 in available_moves(board):
                board[inp-1] = currentPlayer
                turn += 1
                break

def computer(board):
    global turn
    best_score = -float("inf")
    best_move = available_moves(board)[0]
    
    for i in available_moves(board):
        board[i] = "O"
        score = minimax(board, False)
        board[i] = str(i+1)
        if score > best_score:
            best_score = score
            best_move = i
    
    board[best_move] = "O"
    turn += 1


#check for win or tie

def minimax(board, is_maximizing):
    winner = win_state(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf') #initializes best score to negative infinity so any score is better
        for i in available_moves(board):
            board[i] = "O" #pretend the computer plays here
            score = minimax(board, False) #ohhh this is what makes it recursive!!
            board[i] = str(i+1) #undoes the move so that the board doesn't change
            best_score = max(score, best_score) #updates the best score
        return best_score
    else:
        best_score = float('inf') #so that i wants the lowest score and any score is better
        for i in available_moves(board):
            board[i] = "X"
            score = minimax(board, True)
            board[i] = str(i+1)
            best_score = min(score, best_score)
        return best_score
    

    




#check for win or tie again

while game_running == True:
    print_board(board)
    input_index(board)

    winner = win_state(board)
    if winner or is_full(board):
        break

    computer(board)

    winner = win_state(board)
    if winner or is_full(board):
        break

print_board(board)
if winner:
    print(f"The winner is {winner}!")
else:
    print("It's a tie!")
  






