# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:09:20 2024

@author: Kuba
"""

import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite):
    # Class for managing bullets

    def __init__(self, ai_settings, screen,ship):
        # create bullet at current ship position
        super().__init__()
        self.screen = screen
        
        # create bullet at (0,0) and then set correct pos.
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # save bullet pos. as float
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        # move the bullet 
        
        self.y -= self.speed_factor # bullet go up, so negative height(y)
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)