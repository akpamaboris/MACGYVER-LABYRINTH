import random
import pygame
import Constantes as Cs



class Objects:

    """
        The Objects class positions three objects randomly in the labyrinth.


    """

    def __init__(self, labyrinth):
        self.way_map  = labyrinth.way_map
        self.positions = []



        # loading image
        self.object1_sprite = Cs.image.load(Cs.OBJECT1_IMAGE).convert_alpha()
        self.object2_sprite = Cs.image.load(Cs.OBJECT2_IMAGE).convert_alpha()
        self.object3_sprite = Cs.image.load(Cs.OBJECT3_IMAGE).convert_alpha()

        def init_objects_position(self):
            """Choose three positions randomly """
            self.positions = random.sample(self.way_map , 3)

        def update_object_position(self, position):
            """ Update position when an object is collected """
            if self.positions.index(position) == 0:
                self.positions[0] = (0, 15)
                self.objects_collected.append("object1")
            elif self.positions.index(position) == 1:
                self.positions[1] = (1, 15)
                self.objects_collected.append("object2")
            elif self.positions.index(position) == 2:
                self.positions[2] = (2, 15)
                self.objects_collected.append("object3")

        def display(self, window):

            # adding objects to the window
            for obj_num, position in enumerate(self.positions):
                if obj_num == 0:
                    window.blit(self.object1_sprite,
                                (position[0] * Cs.SPRITE_SIZE, position[1] * Cs.SPRITE_SIZE))
                elif obj_num == 1:
                    window.blit(self.object2_sprite,
                                (position[0] * Cs.SPRITE_SIZE, position[1] * Cs.SPRITE_SIZE))
                elif obj_num == 2:
                    window.blit(self.object3_sprite,
                                (position[0] * Cs.SPRITE_SIZE, position[1] * Cs.SPRITE_SIZE))
