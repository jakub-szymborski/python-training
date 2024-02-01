# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:36:39 2024

@author: Kuba
"""
from game_functions import read_high_score
class GameStats():
    # statistics for Alan invasion 
    
    def __init__(self, ai_settings):
        # initialize 
        
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False 
        self.high_score = 0
       # self.all_time_high_score = read_high_score(self.ai_settings)
        
      #  if self.all_time_high_score > self.high_score:
       #     self.high_score = self.all_time_high_score 
        
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1