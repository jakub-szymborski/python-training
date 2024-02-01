# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:14:21 2024

@author: Kuba
"""

import sys
import pygame 
from time import sleep
from settings import Settings 
from ship import Ship
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, score, scoreboard, ship, aliens, bullets, play_button):
    # respond to key and mouse press
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quitting 
            quit_game(ai_settings,stats, scoreboard)
            
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_settings, screen, stats, score, scoreboard, play_button,ship, aliens, bullets)
                
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats,score, play_button,ship, aliens, bullets, mouse_x, mouse_y)
        
   
def check_keydown(event, ai_settings, screen, stats, score, scoreboard, play_button,ship, aliens, bullets):
    # respond to keydown events 
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # move right 
        ship.moving_right = True
        
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a: # move left 
        ship.moving_left = True
        
    elif event.key == pygame.K_SPACE:
        # create new bullet and add it to the group
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        quit_game(ai_settings,stats, scoreboard)

    elif event.key == pygame.K_RETURN: 
        reset_game(ai_settings, screen, stats,score, play_button,ship, aliens, bullets)

def check_keyup(event, ship):
    # respond to keyUp events 
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
        
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False

      
def update_screen(ai_settings, screen, stats,score, ship, aliens, bullets, play_button): # 
    # update screen and flip to the new screen
    # Redraw screen for each loop pass 
    screen.fill(ai_settings.bg_color)   # background color
    ship.blit_ship()
    aliens.draw(screen)    
    score.show_score()
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    if not stats.game_active:
        play_button.draw_button()
    
    # make the most recently drawn screen visible 
    pygame.display.flip()
    
    
def update_bullets(ai_settings, screen, stats, score, ship, aliens, bullets):
    # update bullets position, remove old bullets 
    bullets.update()
    # remove bullets above top screen edge 
    for bullet in bullets.copy(): 
    # we use copy because we shouldnt remove elements of a list we're looping through
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_hit(ai_settings, screen,stats, score, ship, aliens, bullets)
    
            
def fire_bullet(ai_settings, screen, ship, bullets):
    # fire a bullet 
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen,ship)
        bullets.add(new_bullet)
 
    
# aliens     
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width  
    # add shift to even rows, to create a chessboard pattern
    alien.x = alien_width + ai_settings.alien_spacing*alien_width*alien_number + alien_width*(row_number%2) 
    alien.rect.x = alien.x
    alien.rect.y = 0.5*alien.rect.height + 0.75*ai_settings.alien_spacing*alien.rect.height*row_number
    aliens.add(alien)
     
    
def get_number_aliens_x(ai_settings, alien_width):
    # calculate number of columns and rows of aliens
    available_space_x = ai_settings.screen_width - ai_settings.alien_spacing*alien_width
    number_aliens_x  = int(available_space_x / (ai_settings.alien_spacing*alien_width))
    return number_aliens_x


def get_number_aliens_y(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    number_rows = int(available_space_y/(ai_settings.alien_spacing*alien_height))
    return number_rows  
    
    
def create_fleet(ai_settings, screen, ship, aliens):
    # create a fleet of aliens 
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_aliens_y(ai_settings, ship.rect.height, alien.rect.height)
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_aliens(ai_settings,stats, screen, ship, aliens, bullets):
    # update all aliens in the fleet
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    check_fleet_bottom(ai_settings, stats, screen, ship, aliens, bullets)

    # look for alien - ship collision\
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
 
    
def check_fleet_edges(ai_settings, aliens):
    # check if any alien reached edge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_fleet_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    # check if any alien reached bottom of the screen
    screen_rect = screen.get_rect()
    for alien in aliens.sprites(): 
        if alien.rect.bottom >= screen_rect.bottom:  
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
        
        
def change_fleet_direction(ai_settings, aliens):
    # drop fleet, change direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop
        
    ai_settings.fleet_direction *= -1
    
    
def check_bullet_hit(ai_settings, screen,stats, score, ship, aliens, bullets):
    # check for hits, remove hit alien, spawn new fleet if needed 
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions: 
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points*len(aliens)
            score.prep_score()
            check_high_score(ai_settings, stats, score)
    if len(aliens) == 0:
        next_level(ai_settings, screen,stats, score, ship, aliens, bullets)
       
  
def next_level(ai_settings, screen,stats, score, ship, aliens, bullets):
    # handle setting up new level        
    stats.level += 1
    score.prep_level()
    bullets.empty()
    ai_settings.increase_speed()
    
    # whole fleet is destroyed, create a new one 
    create_fleet(ai_settings, screen, ship, aliens)
        
    
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    # handle ship being hit
    stats.ships_left += -1
    
    if stats.ships_left >= 0:
        # remove old fleet and bullets 
        aliens.empty()
        bullets.empty()
        
        # create new ship and fleet
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        print("BLACK HAWK DOWN")
        print(f"ships left:{stats.ships_left}")
    
        # pause 
        sleep(0.5)
    else: 
        stats.game_active = False 
        pygame.mouse.set_visible(False)
        # write_high_score(ai_settings, stats, scoreboard)

        
def check_play_button(ai_settings, screen, stats, score, play_button,ship, aliens, bullets, mouse_x, mouse_y):
    # check if button is clicked 
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        reset_game(ai_settings, screen, stats,score, play_button,ship, aliens, bullets)
        
        
def reset_game(ai_settings, screen, stats,score, play_button,ship, aliens, bullets):
    ai_settings.initialize_dynamic_settings()
    stats.reset_stats()
    stats.game_active = True
    pygame.mouse.set_visible(False)
    
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    
    # reset scoreboard
    score.prep_score()
    score.prep_high_score()
    score.prep_level()
    
    
def check_high_score(ai_settings, stats, score):
    # check if new high score is reached
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()
     
        
def read_high_score(ai_settings):
    # open high score file, if not present, create one
    # return scoreboard
    filename = ai_settings.hs_filename
    try:
        with open (filename) as file_object:
            scoreboard = file_object.readlines()
            scoreboard = list(map(int, scoreboard))
            scoreboard.sort(reverse=True)           
        
    except FileNotFoundError:
        high_score_file = open(filename, "w")
        high_score_file.write('0 \n')
        scoreboard = [0]
    return scoreboard        

    
def write_high_score(ai_settings, stats, scoreboard):
    # append new high score to a scoreboard
    if stats.high_score > 0:
        scoreboard.append(stats.high_score)


def write_scoreboard(ai_settings,stats, scoreboard):
    # take prepared scoreboard and save it to a file
    write_high_score(ai_settings, stats, scoreboard)
    scoreboard.sort(reverse=True)
    filename = ai_settings.hs_filename
    high_score_file = open(filename, "w")

    for score in scoreboard:
        high_score_file.write(str(score) + '\n')
  

def quit_game(ai_settings,stats, scoreboard):
    write_scoreboard(ai_settings,stats, scoreboard)
    print('See you again, space cowboy')
    pygame.quit()
    sys.exit(0)
    
    
"""
    filename = ai_settings.hs_filename

    if stats.high_score > 0:
        try: # try appending high score to a file 
            high_score_file = open(filename, "a")
            high_score_file.write(str(stats.high_score) + '\n')
            print(str(stats.high_score) + '\n')
            
        except FileNotFoundError:
            high_score_file.write(str(stats.high_score) + '\n')
            print(str(stats.high_score) + '\n')
"""