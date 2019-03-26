"""
Classes Of The Game Mac Gyver

"""

#! /usr/bin/env python3
# coding: utf-8

import random
import pygame
from constants import NB_SPRITE, SIZE_SPRITE, LVL_DESIGN, PIC_WALL, PIC_START, PIC_END, OBJECT_TAKEN




class Map:

    """
            This class generates a level from the file

    """

    def __init__(self):

        # The map's file
        self.file = LVL_DESIGN
        # The map in the form of list
        self.structure = 0




    def create(self):

        """
                This class scan a level from the file

        """

        # Open the lvl file
        with open(self.file, 'r') as file:
            # Create a list of list
            structure_file = []

            for lign in file:
                lign_lvl = []

                # Each caracter will be a case of the grid
                for caracter in lign:
                    if caracter != "\n":
                        lign_lvl.append(caracter)

                structure_file.append(lign_lvl)

            self.structure = structure_file

    def display(self, window):
        """
                This class generates the level design

        """


        # Different sprite of the lvl design
        wall = pygame.image.load(PIC_WALL).convert()
        start = pygame.image.load(PIC_START).convert()
        end = pygame.image.load(PIC_END).convert()

        lign_number = 0
        for lign in self.structure:

            case_number = 0
            for sprite in lign:
                # Add the corresponding sprite at the good place
                x_case = case_number * SIZE_SPRITE
                y_case = lign_number * SIZE_SPRITE
                if sprite == 'm':
                    window.blit(wall, (x_case, y_case))
                elif sprite == 'd':
                    window.blit(start, (x_case, y_case))
                elif sprite == 'a':
                    window.blit(end, (x_case, y_case))
                case_number += 1
            lign_number += 1


class Character:

    """
    This class generates the character

    """

    def __init__(self, right_char, left_char, up_char, down_char, lvl):

        # Character's sprite
        self.right = pygame.image.load(right_char).convert_alpha()
        self.left = pygame.image.load(left_char).convert_alpha()
        self.up = pygame.image.load(up_char).convert_alpha()
        self.down = pygame.image.load(down_char).convert_alpha()

        # Initialization of the direction
        self.direction = self.right

        # Initialization of the position on the grid
        self.x = 0
        self.y = 0

        # Initialization of the position on the design
        self.sprite_x = 0
        self.sprite_y = 0

        # LVL where the character is
        self.lvl = lvl

        # Number of object taken
        self.nb_object = 0


    def move(self, direction):

        """

         Character's deplacement

        """

        if direction == 'right':
            # Test if the character will not go out of the screen
            if self.x < (NB_SPRITE - 1):
                # Test if the destination is not a wall
                if self.lvl.structure[self.y][self.x + 1] != 'm':
                    # Incrementing self.x by 1
                    self.x += 1
                    # Update the position on the interface
                    self.sprite_x = self.x * SIZE_SPRITE
            # Update the direction on the interface
            self.direction = self.right

        if direction == 'left':
            if self.x > 0:
                if self.lvl.structure[self.y][self.x - 1] != 'm':
                    self.x -= 1
                    self.sprite_x = self.x * SIZE_SPRITE
            self.direction = self.left

        if direction == 'up':
            if self.y > 0:
                if self.lvl.structure[self.y - 1][self.x] != 'm':
                    self.y -= 1
                    self.sprite_y = self.y * SIZE_SPRITE
            self.direction = self.up

        if direction == 'down':
            if self.y < (NB_SPRITE - 1):
                if self.lvl.structure[self.y + 1][self.x] != 'm':
                    self.y += 1
                    self.sprite_y = self.y * SIZE_SPRITE
            self.direction = self.down

    def take_obj(self, obj):
        """

        Get the object


        """

        if (self.x == obj.obj_x) and (self.y ==
                                      obj.obj_y) and (obj.taken is False):
            self.nb_object += 1
            obj.taken = True
            obj.design = pygame.image.load(OBJECT_TAKEN).convert_alpha()


class Object:

    """
    Class that generate objects

    """

    # Create an object and place him in random position
    def __init__(self, lvl, design):

        # Object's position on the grid
        self.obj_x = 0
        self.obj_y = 0

        # Object's position on the design
        self.obj_sprite_x = 0
        self.obj_sprite_y = 0

        # Bool if the object has been picked up
        self.taken = False
        self.lvl = lvl
        self.design = pygame.image.load(design).convert_alpha()

        # Place the object on a sprite o
        while self.lvl.structure[self.obj_y][self.obj_x] != 'o':
            # Update the position on the grid
            self.obj_x = random.randint(0, NB_SPRITE - 1)
            self.obj_y = random.randint(0, NB_SPRITE - 1)
            # Update the position on the design
            self.obj_sprite_x = self.obj_x * SIZE_SPRITE
            self.obj_sprite_y = self.obj_y * SIZE_SPRITE
