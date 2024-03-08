# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:51:07 2024

@author: Kuba
"""

import pygal 

americas = pygal.maps.world.World()
americas.title = 'North, Central and South America'

americas.add('North America', ['ca', 'mx', 'us'])
americas.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
americas.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
'gy', 'pe', 'py', 'sr', 'uy', 've'])

americas.render_in_browser()
americas.render_to_file('americas.svg')
