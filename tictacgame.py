import curses
import math

def newGame(LINES, COLS):
    win = curses.newwin(LINES, COLS, 0, 0)
    win.refresh()
    
    BOARDCOLS = math.floor(COLS / 2)
    BOARDLINES = LINES - 4
    
    for i in range(BOARDCOLS):
        win.addstr(math.floor(BOARDLINES / 3), i, "-")
        win.addstr(math.floor(BOARDLINES / 1.5), i, "-")
        
    for i in range(BOARDLINES):
        win.addstr(i, math.floor(BOARDCOLS / 3), "|")
        win.addstr(i, math.floor(BOARDCOLS / 1.5), "|")
    
    win.addstr(BOARDLINES, BOARDCOLS, "XD")
    win.refresh()