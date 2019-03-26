#! /usr/bin/env python3
# coding: utf-8

import sys
from pygame.locals import *
from classes import *
from constants import WINDOW_SIZE, START_PICTURE, VICTORY, DEFEAT, PIC_BACKGROUND,\
    PIC_ETHER, PIC_NEEDLE, PIC_TUBE, MCGYVER_UP, MCGYVER_DOWN, MCGYVER_RIGHT,\
    MCGYVER_LEFT

"""
Main file of the game

"""

pygame.init()

# Open the Pygame window
WINDOW_GAME = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# Chargement et collage du fond


# Title of the window
pygame.display.set_caption("Maze of Mac Gyver")

# Initialization of the program loop
PROG_GAME = 0

# Initilization of the game loop
GAME_LOOP = 0


# Menu loop
CONTINUE_HOME = 1
while CONTINUE_HOME:
    # Loading and displaying the home picture
    HOME_GAME = pygame.image.load(START_PICTURE).convert()
    WINDOW_GAME.blit(HOME_GAME, (0, -17))

    # Refresh
    pygame.display.flip()

    # Setting the variables
    START_GAME = 1

    # Loop Home
    while CONTINUE_HOME:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            if event.type == QUIT:
                CONTINUE_HOME = 0
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                # Lauching the game
                if event.key == K_RETURN:

                    CONTINUE_HOME = 0
                    PROG_GAME = 1
                    GAME_LOOP = 1


# Initialization of the program loop
PROG_GAME = 1

# Initilization of the game loop
GAME_LOOP = 1


# Program loop
while PROG_GAME:

    # Initialization of the lvl
    LEVEL_DESIGN = Map()
    LEVEL_DESIGN.create()

    # Initilization of the lvl design
    LEVEL_DESIGN.display(WINDOW_GAME)
    BACKGROUND_GAME = pygame.image.load(PIC_BACKGROUND).convert()

    # Initialization of the character
    MCGYVER_CHAR = Character(MCGYVER_RIGHT, MCGYVER_LEFT, MCGYVER_UP, MCGYVER_DOWN, LEVEL_DESIGN)

    # Initialization of objects
    ETHER_OBJECT = Object(LEVEL_DESIGN, PIC_ETHER)
    NEEDLE_OBJECT = Object(LEVEL_DESIGN, PIC_NEEDLE)
    TUBE_OBJECT = Object(LEVEL_DESIGN, PIC_TUBE)

    # Loop

    OBJ_LIST = [ETHER_OBJECT, NEEDLE_OBJECT, TUBE_OBJECT]


    # Game loop
    while GAME_LOOP:

        # Limitation of the number of loop per second
        pygame.time.Clock().tick(30)

        # Detection of events
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    MCGYVER_CHAR.move('right')
                elif event.key == K_LEFT:
                    MCGYVER_CHAR.move('left')
                elif event.key == K_UP:
                    MCGYVER_CHAR.move('up')
                elif event.key == K_DOWN:
                    MCGYVER_CHAR.move('down')

        # Display the lvl and objects
        WINDOW_GAME.blit(BACKGROUND_GAME, (0, 0))
        LEVEL_DESIGN.display(WINDOW_GAME)
        for obj in OBJ_LIST:
            WINDOW_GAME.blit(obj.design, (obj.obj_sprite_x, obj.obj_sprite_y))

            # Test if an object have been taken
            # if obj.taken is False:
            MCGYVER_CHAR.take_obj(obj)

        # Display a counter
        MYFONT_GAME = pygame.font.SysFont("monospace", 32)
        MYFONT_GAME.set_bold(True)
        COUNTER_DISPLAY = MYFONT_GAME.render("x " + str(MCGYVER_CHAR.nb_object), False,
        (255, 255, 0))
        WINDOW_GAME.blit(COUNTER_DISPLAY, (0, 30 * (NB_SPRITE - 1)))

        # Update the character direction
        WINDOW_GAME.blit(MCGYVER_CHAR.direction, (MCGYVER_CHAR.sprite_x, MCGYVER_CHAR.sprite_y))
        # Update the window
        pygame.display.flip()

        # Test if the game is finish
        if LEVEL_DESIGN.structure[MCGYVER_CHAR.y][MCGYVER_CHAR.x] == 'a':
            GAME_LOOP = 0

        # Test of victory
        if MCGYVER_CHAR.nb_object == 3:
            FINAL_BACKGROUND = pygame.image.load(VICTORY).convert()
                                
        else:
            FINAL_BACKGROUND = pygame.image.load(DEFEAT).convert()

    WINDOW_GAME.blit(FINAL_BACKGROUND, (0, 0))
    pygame.display.flip()

    # New game or quit the program
    for event in pygame.event.get():
        if event.type == QUIT:
            PROG_GAME = 0
        elif event.type == KEYDOWN:
            if event.key == K_r:
                GAME_LOOP = 1
            elif event.key == K_ESCAPE:
                PROG_GAME = 0
