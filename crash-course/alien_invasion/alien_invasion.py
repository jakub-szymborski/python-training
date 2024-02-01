# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:10:37 2024

@author: Kuba
"""
import pygame
from settings import Settings 
from ship import Ship
from game_stats import GameStats
from scores import Scores
from button import Button

import game_functions as gf 
from pygame.sprite import Group


def run_game():
    #initialize game and create a screen object 
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    screen.fill(ai_settings.bg_color)   # background color
    play_button = Button(ai_settings, screen, "Play")

    ship = Ship(screen, ai_settings)    # make ship 
    
    stats = GameStats(ai_settings)
    score = Scores(ai_settings, screen, stats)
    
    scoreboard = gf.read_high_score(ai_settings) 
    
    bullets = Group()   # make group for bullets 
    
    aliens = Group()
    # create a fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)
    gf.update_screen(ai_settings, screen, stats,score, ship, aliens, bullets, play_button)
    
    while True: 
        
        gf.check_events(ai_settings, screen, stats, score, scoreboard, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update(ai_settings)
            gf.update_bullets(ai_settings, screen,stats, score, ship, aliens, bullets)
            gf.update_aliens(ai_settings,stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats,score, ship, aliens, bullets, play_button)
            
run_game()

# pygame.quit() 
