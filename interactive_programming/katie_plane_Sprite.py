"""Sets class that deals with the movement, update, and
loading sprite of the user's plane"""

import pygame
import basicSprite
from helpers import *

PLANE_COLLIDED = pygame.USEREVENT + 1


class MyPlane(pygame.sprite.Sprite):
    """This is our plane that will move around the screen
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('katie_plane.png',-1)
        """set initial position"""
        self.rect.x=480/2
        self.rect.y=550
        """Set the number of pixels to move each time"""
        self.x_dist = 1
        self.y_dist = 1
        """Initialize how much we are moving"""
        self.xMove = 0
        self.yMove = 0


    def MoveKeyDown(self,key):
        """Move your self in one of the 4 directions
        according to key"""
        """key is the pyGame define for either up, down, left,
        or right key
        we will adjust ourselves in that direction"""

        if (key == K_RIGHT):
            self.xMove += self.x_dist
        elif (key == K_LEFT):
            self.xMove += -self.x_dist
        elif (key == K_UP):
            self.yMove += -self.y_dist
        elif (key == K_DOWN):
            self.yMove += self.y_dist

    def MoveKeyUp(self,key):
        if (key == K_RIGHT):
            self.xMove += -self.x_dist
        elif (key == K_LEFT):
            self.xMove += self.x_dist
        elif (key == K_UP):
            self.yMove += self.y_dist
        elif (key == K_DOWN):
            self.yMove += -self.y_dist

    def update(self,enemy_plane_group):
        """Called when the Snake sprit should update itself"""
        
        if (self.xMove == 0) and (self.yMove ==0):
            """f we arent moving just get out of here"""
            return

        """All right we must be moving!"""
        self.rect.move_ip(self.xMove,self.yMove)

        """check if we hit a enemy_plane"""
        lst_enemy_plane = pygame.sprite.spritecollide(self,enemy_plane_group, False)
        if (len(lst_enemy_plane)>0):
            """We've hit enemy"""
            self.EnemyCollide(lst_enemy_plane)
    
    def EnemyCollide(self,lst_enemy_plane):
        """This function is called when katie_plane collides
        with an enemy plane"""
        if (len(lst_enemy_plane)<=0):
            """if list ie empty get out of here"""
            return
        else:
            """Look's like we're dead"""
            pygame.event.post(pygame.event.Event(PLANE_COLLIDED,{}))
