# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:53:02 2024

@author: Kuba
"""
import pygal 
from dice import Dice

# d6 
dice_1 = Dice()
dice_2 = Dice()

n_times = 100000
results = []

for rolls in range(n_times):
    roll_1 = dice_1.roll()
    roll_2 = dice_2.roll()
    results.append(roll_1 + roll_2)

# analyze the results 

counts = []
max_result = dice_1.num_sides + dice_2.num_sides +1
for val in range(2, max_result):
    count = results.count(val)
    counts.append(count)
    
print(counts)

# plots 
hist = pygal.Bar()
hist.title = 'Results of rolling 2 dice ' + str(n_times) + ' times'
hist.x_labels = ['2', '3', '4', '5', '6','7','8','9','10','11','12']
hist.x_title = 'Roll result'
hist.y_title = 'Count of result'

hist.add('D6', counts)
#hist.render_to_file('dice_visual.svg')

# frequencies 
frequencies = []

for val in range(2, max_result):
    freq = results.count(val)/len(results)
    frequencies.append(freq)
    
    
hist = pygal.Bar()
hist.title = 'Results of rolling 2 dice ' + str(n_times) + ' times'
hist.x_labels = ['2', '3', '4', '5', '6','7','8','9','10','11','12']
hist.x_title = 'Roll result'
hist.y_title = 'Result frequency'

hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')
