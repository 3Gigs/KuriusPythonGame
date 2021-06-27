import curses

def newGame(stdscr):
    print("xd")

def initGame(stdscr):
    ROWS, COLS = stdscr.getmaxyx()

    stdscr.clear()
    for i in range(COLS):
        if(i % 2):
            stdscr.addstr("X")
        else:
            stdscr.addstr("O")
    stdscr.addstr("Welcome to tic tac toe with Curses!\n")
    stdscr.addstr("Created by Huaxuan Yang (3Gigs)\n")
    stdscr.addstr("Please press ENTER to start game!\n", curses.A_BOLD)
    stdscr.addstr("Press Q to exit game\n", curses.A_BOLD)
    
    while True:
        key = stdscr.getch()
        if key == ord('\n'):
            stdscr.addstr("xd\n")
            stdscr.refresh()
        if key == ord('q'):
            stdscr.endwin()
                
if __name__ == '__main__':
    curses.wrapper(initGame)