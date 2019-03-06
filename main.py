#! /usr/bin/env python3
# coding: utf-8

import pygame,sys
from pygame.locals import *
from classes import *
from constants import *

pygame.init()

# Open the Pygame window
window = pygame.display.set_mode((window_size, window_size))

# Chargement et collage du fond


# Title of the window
pygame.display.set_caption("Maze of Mac Gyver")

# Initialization of the program loop
prog = 0

# Initilization of the game loop
game = 0


# Menu loop
continue_home =  1
while continue_home :
        #Loading and displaying the home picture
        home_game = pygame.image.load(START_PICTURE).convert()
        window.blit(home_game,(0,-17))

        #Refresh
        pygame.display.flip()

        #Setting the variables
        start_game =1

        #Loop Home
        while continue_home:
                pygame.time.Clock().tick(30)

                for event in pygame.event.get():

                        if event.type == QUIT :
                                continue_home =0
                                pygame.quit()
                                sys.exit()

                        elif event.type == KEYDOWN:
                                #Lauching the game
                                if event.key ==  K_RETURN:

                                        continue_home =0
                                        prog =1
                                        game =1







# Initialization of the program loop
prog = 1

# Initilization of the game loop
game = 1


# Program loop
while prog:

        # Initialization of the lvl
        lvl = Map()
        lvl.create()
        # Initilization of the lvl design
        lvl.display(window)
        background = pygame.image.load(pic_background).convert()

        # Initialization of the character
        mcGyver = Character(mcGyver_right, mcGyver_left,
                            mcGyver_up, mcGyver_down, lvl)

        # Initialization of objects
        ether = Object(lvl, pic_ether)
        needle = Object(lvl, pic_needle)
        tube = Object(lvl, pic_tube)
## Boucle
##
##
##        
        obj_list = [ether, needle, tube]





        # Game loop
        while game:

                # Limitation of the number of loop per second
                pygame.time.Clock().tick(30)

                # Detection of events
                for event in pygame.event.get():

                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()

                        if event.type == KEYDOWN:
                                if event.key == K_RIGHT:
                                        mcGyver.move('right')
                                elif event.key == K_LEFT:
                                        mcGyver.move('left')
                                elif event.key == K_UP:
                                        mcGyver.move('up')
                                elif event.key == K_DOWN:
                                        mcGyver.move('down')

                # Display the lvl and objects
                window.blit(background, (0, 0))
                lvl.display(window)
                for obj in obj_list:
                        window.blit(obj.design, (obj.obj_sprite_x,
                                                 obj.obj_sprite_y))
                        # Test if an object have been taken
                        #if obj.taken is False:
                        mcGyver.take_obj(obj)


                #Display a counter
                myfont = pygame.font.SysFont("monospace", 32)
                myfont.set_bold(True)
                counter_display = myfont.render("x " + str(mcGyver.nb_object), False, (255, 255, 0))
                window.blit(counter_display, (0, 30 * (nb_sprite - 1)))


                # Update the character direction
                window.blit(mcGyver.direction, (mcGyver.sprite_x,
                                                mcGyver.sprite_y))
                # Update the window
                pygame.display.flip()

                # Test if the game is finish
                if (lvl.structure[mcGyver.y][mcGyver.x] == 'a'):
                        game = 0

                # Test of victory
                        if mcGyver.nb_object == 3:
                                final_background = \
                                        pygame.image.load(victory).convert()
                                
                        else:
                                final_background = \
                                        pygame.image.load(defeat).convert()

                        
        window.blit(final_background, (0, 0))
        pygame.display.flip()

        # New game or quit the program
        for event in pygame.event.get():
                if event.type == QUIT:
                        prog = 0
                elif event.type == KEYDOWN:
                    if event.key == K_r:
                        game = 1
                    elif event.key == K_ESCAPE:
                        prog = 0
