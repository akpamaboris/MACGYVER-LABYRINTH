import pygame, sys
from pygame.locals import *

#Variable of the dimensions of the Pygame window
screen_width = 400
screen_height = 300

#Loading the window , and converting the background
screen = pygame.display.set_mode((screen_width, screen_height))
fond = pygame.image.load("labyrinthepng.png").convert()
screen.blit(fond,(0,0))

#Refreshing the screen
pygame.display.flip()



pygame.init()




while True:


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


pygame.display.update()