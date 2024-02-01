# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:21:25 2024

@author: Kuba
"""

class Settings():
    # settings for Alien Invasion 
    
    def __init__(self):
        # Initialize game's settings
        # screen settings: 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (130,130,130)
        
        # bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (255,255,153)
        self.bullets_allowed = 13
        
        # aliens
        self.alien_spacing = 2
        self.fleet_drop = 100
        
        # ship settings 
        self.ship_limit = 1
        
        # difficulty 
        self.speedup = 2
        self.initialize_dynamic_settings()
        
        # high score file 
        self.hs_filename ='high_scores.txt'

        
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        self.fleet_direction = 1 # 1 -> right, -1 left
        
        # scoring 
        self.alien_points = 10

    def increase_speed(self):
        # increase game speed
        self.ship_speed_factor *= self.speedup
        self.bullet_speed_factor *= self.speedup
        self.alien_speed_factor *= self.speedup
        self.alien_points *= 2