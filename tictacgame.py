import curses
import math

def drawBoard(gameWin, BOARDCOLS, BOARDLINES):
    for i in range(BOARDCOLS):
        gameWin.addstr(math.floor(BOARDLINES / 3), i, "-")
        gameWin.addstr(math.floor(BOARDLINES / 1.5), i, "-")
        
    for i in range(BOARDLINES):
        gameWin.addstr(i, math.floor(BOARDCOLS / 3), "|")
        gameWin.addstr(i, math.floor(BOARDCOLS / 1.5), "|")
    



def newGame(LINES, COLS):
    gameWin = curses.newwin(LINES, COLS, 0, 0)
    BOARDCOLS = math.floor(COLS / 2)
    BOARDLINES = LINES - 4
    
    drawBoard(gameWin, BOARDCOLS, BOARDLINES)
    
    gameWin.addstr(BOARDLINES, 0, "XD")
    gameWin.refresh()
