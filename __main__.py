def drawBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2] + "|")
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print(board[6] + "|" + board[7] + "|" + board[8] + "|")

def newGame(board):
    players = ('X', 'O')
    turn = 0
    while True:
        drawBoard(board)
        if(turn == 2):
            turn = 0
        print(f"It is {players[turn]}'s turn")
        gridNumber = int(input("Enter grid number (left to right order 0-8): "))
        if(gridNumber < 0 or gridNumber > 8):
            print("Enter a valid grid")
        board[gridNumber] = players[turn]
        print("")
        turn += 1

if __name__ == '__main__':
    print("Welcome to tic-tac-toe terminal edition!")
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    newGame(board)
