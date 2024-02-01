# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 12:29:48 2024

@author: Kuba
"""

import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
    # class for a single alien

    def __init__(self, ai_settings, screen):
        # init alien and set its starting pos. 
        
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # load img 
        self.image = pygame.image.load("images/alien-ciastko.png")
        self.image = pygame.transform.scale(self.image, (120,60))
        
        self.rect = self.image.get_rect()
        
        # start each new alien near top leaft
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # store exact pos.
        self.x = float(self.rect.x)
        
    def blitme(self):
        # draw alien at its pos
        self.screen.blit(self.image, self.rect)

    def update(self):
        # move alien
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.rect.x = self.x
        
    def check_edges(self):
        # return True if alien is at the edge 
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True 

#picture = pygame.image.load(filename)
#picture = pygame.transform.scale(picture, (1280, 720))

