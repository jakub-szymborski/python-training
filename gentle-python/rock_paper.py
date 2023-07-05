# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:29:34 2023

@author: Kuba
Write a rpsWinner() function with parameters player1 and player2. These parameters are
passed one of the strings 'rock', 'paper', or 'scissors' representing that player’s move. If
this results in player 1 winning, the function returns 'player one'. If this results in player 2
winning, the function returns 'player two'. Otherwise, the function returns 'tie'.
"""

def rpsWinner(player1,player2):
    
    if player1 == player2:
        return 'tie'
    
    if player1 == 'paper' and player2 == 'rock':
        return 'player one'
    
    elif player1 == 'rock' and player2 == 'scissors':
        return 'player one'
    
    elif player1 == 'scissors' and player2 == 'paper':
        return 'player one'
    else:
        return 'player two'
    

assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'
