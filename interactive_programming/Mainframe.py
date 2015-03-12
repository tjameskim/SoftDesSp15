import os, sys
import pygame
import random
from pygame.locals import *

"""from separately created files we import needed things"""
from helpers import * #will help us get our sprites by loading images
from katie_plane_Sprite import PLANE_COLLIDED 
from katie_plane_Sprite import MyPlane
from enemy import Enemy


if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Mainframe:
	"""The Main class for the game
	This class handles the main initialization
	and creating of the game"""

	def __init__(self, width=480, height = 640):
		"""Initialize"""
		"""Initialize Pygame"""
		pygame.init()
		"""set the window size"""
		self.width = width
		self.height = height
		"""Create the Screen"""
		self.screen = pygame.display.set_mode((self.width, self.height))

	def MainLoop(self):
		"""This is the Main Loop of the Game"""
		"""Load All of our Sprites"""
		self.LoadSprites();

		"""Create the background"""
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((100,100,200))

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
				elif event.type == KEYDOWN:
					if ((event.key == K_RIGHT)
					or (event.key == K_LEFT)
					or (event.key == K_UP)
					or (event.key == K_DOWN)):
						self.katie_plane.MoveKeyDown(event.key)
				elif event.type == KEYUP:
					if ((event.key == K_RIGHT)
					or (event.key == K_LEFT)
					or (event.key == K_UP)
					or (event.key == K_DOWN)):
						self.katie_plane.MoveKeyUp(event.key)
				elif event.type == PLANE_COLLIDED:
					"""plane is dead"""
					"""for now kist quit"""
					sys.exit()

			"""Update the katie_plane sprite"""
			"""create enemy plane group"""
			enemy_plane_group = pygame.sprite.Group(self.enemy_plane_sprites,
						self.enemy_plane_sprites2,self.enemy_plane_sprites3,
						self.enemy_plane_sprites4, self.enemy_plane_sprites5,
						self.enemy_plane_sprites_l, self.enemy_plane_sprites_r)
			
			self.katie_plane_sprites.update(enemy_plane_group)

			"""Update the enemy_plane sprite"""
			self.enemy_plane_sprites.update()
			self.enemy_plane_sprites2.update()
			self.enemy_plane_sprites3.update()
			self.enemy_plane_sprites4.update()
			self.enemy_plane_sprites5.update()
			self.enemy_plane_sprites_l.update()
			self.enemy_plane_sprites_r.update()

			"""Do the drawing"""
			self.screen.blit(self.background, (0, 0))
		
			self.katie_plane_sprites.draw(self.screen)
			
			self.enemy_plane_sprites.draw(self.screen)
			self.enemy_plane_sprites2.draw(self.screen)
			self.enemy_plane_sprites3.draw(self.screen)
			self.enemy_plane_sprites4.draw(self.screen)
			self.enemy_plane_sprites5.draw(self.screen)
			self.enemy_plane_sprites_l.draw(self.screen)
			self.enemy_plane_sprites_r.draw(self.screen)
			
			pygame.display.flip()
			



	def LoadSprites(self):
		"""Load  the sprites that we need"""

		"""Create the Plane group"""
		self.katie_plane = MyPlane()
		self.katie_plane_sprites = pygame.sprite.RenderPlain((self.katie_plane))
		
		self.enemy_plane = Enemy(0,1)
		self.enemy_plane_sprites = pygame.sprite.RenderPlain((self.enemy_plane))

		self.enemy_plane2 = Enemy(110,1)
		self.enemy_plane_sprites2 = pygame.sprite.RenderPlain((self.enemy_plane2))

		self.enemy_plane3 = Enemy(220,1)
		self.enemy_plane_sprites3 = pygame.sprite.RenderPlain((self.enemy_plane3))

		self.enemy_plane4 = Enemy(330,1)
		self.enemy_plane_sprites4 = pygame.sprite.RenderPlain((self.enemy_plane4))

		self.enemy_plane5 = Enemy(440,1)
		self.enemy_plane_sprites5 = pygame.sprite.RenderPlain((self.enemy_plane5))

		self.enemy_plane_l = Enemy(-50,1)
		self.enemy_plane_sprites_l = pygame.sprite.RenderPlain((self.enemy_plane_l))

		self.enemy_plane_r = Enemy(480,1)
		self.enemy_plane_sprites_r = pygame.sprite.RenderPlain((self.enemy_plane_r))		

if __name__ == "__main__":
	MainWindow = Mainframe(480,640)
	MainWindow.MainLoop()