# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 15:25:02 2024

@author: Kuba
"""

import pygame.font 

class Scores():
    # class for storing high scores
    
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats 
        
        # font settings 
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        
        # prep initial score img 
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        
        
    def prep_score(self):
        # turn score into rendered img 
        rounded_score = int(round(self.stats.score,-1)) # round to tens
        score_str = "{:,}".format(rounded_score).replace(',', ' ')
        self.score_img = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        
        # display score at the top right of the screen 
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top = 20
        
        
    def prep_high_score(self):
        # prep high score as an img
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score).replace(',', ' ')
        self.high_score_img = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # display score at the center right of the screen 
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx 
        self.high_score_rect.top = self.score_rect.top


    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)

        
    def prep_level(self):
        # turn lvl into img
        self.level_img = self.font.render(str(self.stats.level),
                                          True, self.text_color,
                                          self.ai_settings.bg_color)
        # pos. lvl below score
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        