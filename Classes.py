"""Classes of the game """

import pygame
from pygame.locals import *
from Constantes import *

class Level:
	"""Classes to create the level """
	def __init__(self, file):
		self.file = file
		self.structure = 0


	def generate(self):
		"""Method allowing us to create a level with a file.
		"""
		#We open the file
		with open(self.file, "r") as file:
			structure_level = []
			#Scan the file line by line
			for line in file:
				line_level = []
				#We scan the sprites in the file
				for sprite in line:
					#We are ignoring the "\n" at the end of lines
					if sprite != '\n':
						#We add sprite to the list
						line_level.append(sprite)
				#We add a sprite to the line of the level
				structure_level.append(line_level)
			#We save the structure
			self.structure = structure_level


	def display(self, window):
		"""Méthode permettant d'afficher le niveau en fonction
		de la liste de structure renvoyée par generer()"""
		#Chargement des images (seule celle d'arrivée contient de la transparence)

		wall = pygame.image.load(image_mur).convert()
		start = pygame.image.load(image_depart).convert()
		end = pygame.image.load(image_arrivee).convert_alpha()



		#On parcourt la liste du niveau
		num_line = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_line * taille_sprite
				if sprite == 'm':		   #m = Mur
					window.blit(wall, (x,y))
				elif sprite == 'd':		   #d = Départ
					window.blit(start, (x,y))
				elif sprite == 'a':		   #a = Arrivée
					window.blit(end, (x,y))
				num_case += 1
			num_line += 1




class Char:
	"""Class to create the character"""
	def __init__(self, right, left, up, down, level):
		#Sprites du personnage
		self.droite = pygame.image.load(right).convert_alpha()
		self.gauche = pygame.image.load(left).convert_alpha()
		self.haut = pygame.image.load(up).convert_alpha()
		self.bas = pygame.image.load(down).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.droite
		#Niveau dans lequel le personnage se trouve
		self.niveau = level


	def move_char(self, direction):
		"""Methode permettant de déplacer le personnage"""

		#Déplacement vers la droite
		if direction == 'right':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.droite

		#Déplacement vers la gauche
		if direction == 'left':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche

		#Déplacement vers le haut
		if direction == 'up':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut

		#Déplacement vers le bas
		if direction == 'down':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas
