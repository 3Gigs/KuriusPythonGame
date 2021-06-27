import curses
from tictacgame import newGame

def initGame(stdscr):
    LINES, COLS = stdscr.getmaxyx()

    stdscr.clear()
    for i in range(COLS):
        if(i % 2):
            stdscr.addstr("X")
        else:
            stdscr.addstr("O")
    stdscr.addstr("Welcome to tic tac toe with Curses!\n")
    stdscr.addstr(str(LINES) + "\n")
    stdscr.addstr(str(COLS) + "\n")
    stdscr.addstr("Created by Huaxuan Yang (3Gigs)\n")
    stdscr.addstr("Please press ENTER to start game!\n", curses.A_BOLD)
    stdscr.addstr("Press Q to exit game\n", curses.A_BOLD)
    
    while True:
        key = stdscr.getch()
        if key == ord('\n' or '\r'):
            stdscr.clear()
            stdscr.refresh()
            newGame()
        if key == ord('q'):
            break
                
if __name__ == '__main__':
    curses.wrapper(initGame)