# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 12:53:12 2023

@author: Kuba
Write a drawRectangle() function with two integer parameters: width and height. The
function doesn’t return any values but rather prints a rectangle with the given number of hashtags in
the horizontal and vertical directions.
If either the width or height parameter is 0 or a negative number, the function should print
nothing.
"""


def drawRectangle(width,height):
    
    if width < 1 or height < 1: 
        print('')
        
    else:
        for i in range(height):
            for j in range(width):
                print('*', end='')
            print('')
            
drawRectangle('zupa',-2)

"""
Similar to the solid, filled-in ASCII art rectangles our code generated in Exercise #27, ―Rectangle
Drawing,‖ this exercise draws only the border of a rectangle. The + plus character is used for the
corners, the - dash character for horizontal lines, and the | pipe character for vertical lines. (This is
the similar style as the lines in Exercise #25’s multiplication table.

+-------+
|       |
+-------+
"""

def drawBorder(width, height):
    if width < 2 or height < 2: 
        print('')
        
    else:
        borderLines = '+' + (width-2) * '-'  + '+'
        regularLines = '|' +(width-2) * ' '  + '|'
        print(borderLines)
        for i in range(height-2):
            print(regularLines)
        print(borderLines)
        
drawBorder(3,3)

    
"""
Write a drawPyramid() function with a height parameter. The top of the pyramid has one
centered hashtag character, and the subsequent rows have two more hashtags than the previous row.
The number of rows matches the height integer   
"""
   
   
    
    
    