# import pygame;

# def main():
#   width = 500
#   hieght = 500

#   window = pygame.display.set_mod((width, hieght))
#   snake = snake( (0,0,0),  (10, 10) )
import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake game by noor')
game_over=False
while not game_over:
    for event in pygame.event.get():
        print(event)   #prints out all the actions that take place on the screen
 
pygame.quit()
quit()