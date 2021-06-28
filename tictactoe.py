def drawBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2] + "|")
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print(board[6] + "|" + board[7] + "|" + board[8] + "|")

def checkWinner(board, players):
    player1, player2 = players
    row1 = [board[0], board[1], board[2]]
    row2 = [board[3], board[4], board[5]]
    row3 = [board[6], board[7], board[8]]
    col1 = [board[0], board[3], board[6]]
    col2 = [board[1], board[4], board[7]]
    col3 = [board[2], board[5], board[8]]
    diag1 = [board[0], board[4], board[8]]
    diag2 = [board[2], board[4], board[6]]
    solutions = [row1, row2, row3, col1, col2, col3, diag1, diag2]
    for i in solutions:
        if(''.join(i) == player1 * 3):
            print("Player 1 wins")
            return True
        elif(''.join(i) == player2 * 3):
            print("Player 2 wins")
            return True

def newGame(board):
    players = ('X', 'O')
    playerTurn = 0
    while True:
        drawBoard(board)
        if(checkWinner(board, players) == True):
            break
        if(playerTurn == 2):
            playerTurn = 0
        print(f"It is {players[playerTurn]}'s turn")
        gridNumber = int(input("Enter grid number (left to right order 0-8): "))
        if(gridNumber < 0 or gridNumber > 8):
            print("Enter a valid grid")
        if(board[gridNumber] == '-'):
            board[gridNumber] = players[playerTurn]
        else:
            print("Grid already taken")
        print("")
        playerTurn += 1