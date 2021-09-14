import curses

# setup window
curses.initscr()
window = curses.newwin(20, 60, 0, 0)
window.keypad(1)
curses.noecho()
curses.curs_set(0)
window.border(0)
window.nodelay(1)

#food and snake
snake = [(4,10), (4, 9 ), (4, 8)]
food = (10, 20)

window.addch(food[0], food[1], "*")
key = curses.KEY_RIGHT
ESC = 27



# game logic 
score = 0

while key != ESC:
    window.addstr(0, 2, 'Score ' + str(score) + " ")

    #  increase the spead of the snake
    window.timeout(150 - len(snake) // 5 + len(snake) // 10 % 120 )
    
    event = window.getch() # waiting for the next user input (getch())means get the next character
    pev_key = key
    key = event  
  
    for c in snake:
      window.addch(c[0], c[1], "-")

    window.addch(food[0], food[1], "*")
curses.endwin()
print("Final score is = " + score)