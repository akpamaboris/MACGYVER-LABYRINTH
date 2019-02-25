#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame, sys
from pygame.locals import *
from Classes import *
from Constantes import *
import Objects as o

"""

In this file, there is the loop of the game.

"""
#pygame initialization
pygame.init()

#Create a new window
screen = pygame.display.set_mode((side_window, side_window))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

#Title
pygame.display.set_caption(title_window)

# Generating the level
choice = "n1"
level_choice = Level(choice)
level_choice.generate()
level_choice.display(screen)

# Création de Donkey Kong
mac_gyver = Char("ressource/char_down.png", "ressource/char_up.png",
                 "ressource/char_left.png", "ressource/char_right.png", level_choice)

background_image = pygame.image.load(image_fond).convert()





# BOUCLE PRINCIPALE
continue_game = 1
while continue_game :
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()
      elif event.type == KEYDOWN:
            # Si l'utilisateur presse Echap ici, on revient seulement au menu
         if event.key == K_ESCAPE:
            continuer_jeu = 0

            # Touches de déplacement de Donkey Kong
         elif event.key == K_RIGHT:
            mac_gyver.move_char('right')
         elif event.key == K_LEFT:
            mac_gyver.move_char('left')
         elif event.key == K_UP:
            mac_gyver.move_char('up')
         elif event.key == K_DOWN:
            mac_gyver.move_char('down')

      # Affichages aux nouvelles positions

      screen.blit(background_image, (0, 0))
      level_choice.display(screen)
      screen.blit(mac_gyver.direction, (mac_gyver.x, mac_gyver.y))  # dk.direction = l'image dans la bonne direction
      pygame.display.flip()

      # Victoire -> Retour à l'accueil
      if level_choice.structure[mac_gyver.case_y][mac_gyver.case_x] == 'a':
         continuer_jeu = 0



   pygame.display.update()
