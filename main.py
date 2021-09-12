import curses

# setup window
curses.initscr()
window = curses.newwin(20, 60, 0, 0)
window.keypad(1)
curses.noecho()
curses.curs_set(0)
window.border(0)
window.nodelay(1)

# game logic 
score = 0

while True:
    event = window.getch() # waiting for the next user input (getch())means get the next character
     

    # ...
curses.endwin()
print("Final score is = " + score)