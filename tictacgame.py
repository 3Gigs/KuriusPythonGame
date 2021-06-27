import curses
import math

# TODO, this breaks
def drawBoard(gameWin, BOARDCOLS, BOARDLINES):
    for i in range(BOARDCOLS):
        gameWin.addstr(math.floor(BOARDCOLS / 8), i,'-')
        gameWin.addstr(math.floor(BOARDCOLS / 4), i, '-')
    for i in range(BOARDLINES - 2):
        gameWin.addstr(i, math.floor(BOARDCOLS / 3), '|')
        gameWin.addstr(i, math.floor(BOARDCOLS / 1.5), '|')
    gameWin.refresh()
        


def newGame():
    BOARD_COLS = 24;
    BOARD_LINES = 12;

    gameWin = curses.newwin(BOARD_LINES, BOARD_COLS, 0, 0)
    gameWin.keypad(True)
    drawBoard(gameWin, BOARD_COLS, BOARD_LINES)
    gameWin.move(0, 0)
    while True:
        y, x = gameWin.getyx()
        key = gameWin.get_wch()
        if(key == curses.KEY_UP):
            gameWin.move(y - 1, 0)
        elif (key == curses.KEY_DOWN):
            gameWin.move(y + 1, 0)
        elif (key == curses.KEY_RIGHT):
            gameWin.move(0, 1)
        elif (key == curses.KEY_LEFT):
            gameWin.move(0, -1)
        else:
            pass
