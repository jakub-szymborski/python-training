# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:49:17 2024

@author: Kuba
"""
import pygame

class Ship():
    
    def __init__(self,screen, ai_settings):
        # initialize the ship and its start position 
        self.screen = screen 
        
        # load ship image 
        self.image = pygame.image.load("images/statek.png")
        # ship coords 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # new ship starts at the bot center
        self.rect.centerx = float(self.screen_rect.centerx)
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        
        self.ai_settings = ai_settings
        
        
        # movement flag 
        self.moving_right = False 
        self.moving_left = False 
        
        
    def update(self,ai_settings):
        # update ship's position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Update rect object 
        self.rect.centerx = self.center

        
    def blit_ship(self):
        # draw ship at rect loc
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        # place the ship at bottom center 
        self.center = self.screen_rect.centerx