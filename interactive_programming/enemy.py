#! /usr/bin/env python

import pygame
import basicSprite
import random
from helpers import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos_x,vel_init):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('enemy_plane.png',-1)
        """set initial position"""
        self.pos_x = pos_x
        self.rect.x= pos_x
        self.rect.y= random.randint(-600,50)
        """Initialize the direction"""
        #self.direction = random.randint(1,2)
        self.dist = vel_init
        #self.moves = random.randint(2,5)
        self.moveCount = 0

    def update(self):
        """Called when the Monster sprite should update itself"""
        xMove,yMove = 0,1

        self.rect.move_ip(xMove,yMove) #move the rect
        self.moveCount += 1 #update the move count
        if self.moveCount == 1750+500:
            self.rect.x = self.pos_x
            self.rect.y = random.randint(-1650+600,-45)
            self.moveCount = 0