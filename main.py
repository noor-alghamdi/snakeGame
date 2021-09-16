import curses

# setup window
curses.initscr()
window = curses.newwin(20, 60, 0, 0)
window.keypad(1)
curses.noecho()
curses.curs_set(0)
window.border(0)
window.nodelay(1) #-1 means user didn't hit any arrow key!

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
    prev_key = key
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
      key = prev_key
  
  # calculate the next coordenate
  y = sanke [0][0]
  x = snake [0][1]

  if key == curses.KEY_UP:
    y += 1
  if key == curses.KEY_DOWN:
    y -= 1

  if key == curses.KEY_LEFT:
    x -= 1
  if key == curses.KEY_RIGHT:
    x += 1 
  
    for c in snake:
      window.addch(c[0], c[1], "-")

    window.addch(food[0], food[1], "*")
curses.endwin()
print("Final score is = " + score)