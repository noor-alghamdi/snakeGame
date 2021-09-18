import curses
from random import randint 

# setup window
curses.initscr()
window = curses.newwin(20, 60, 0, 0)
window.keypad(1)
curses.noecho()
curses.curs_set(0)
window.border(0)
window.nodelay(1) #-1 means user didn't hit any arrow key!

#food and snake
snake = [(4, 4), (4, 3), (4, 2)]
food = (6, 6)

window.addch(food[0], food[1], "*")
# game logic 
score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    window.addstr(0, 2, 'Score ' + str(score) + ' ')
    window.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120) # increase speed

    prev_key = key
    event = window.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key
  
  # calculate the next coordenate
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x)) # append O(n)

  # check if we hit the boarder

    if y == 0: break
    if y == 20-1: break
    if x == 0: break
    if x == 60-1: break


  # if snake run over itself then it means it eats itself
    if snake[0] in snake[1:]: break

  # otherwise snake should eat the food and grow
    if snake[0] == food:
    #eat he food
      score += 1
      food = ()
      while food == ():
          food = (randint(1,20-2), randint(1,60-2))
          if food in snake:
            food = ()
      
      window.addch(food[0], food[1], '*')
    else:
        # move snake
        last = snake.pop()
        window.addch(last[0], last[1], ' ')

    window.addch(snake[0][0], snake[0][1], '=')
  
curses.endwin()
print(f"Final score = {score}")