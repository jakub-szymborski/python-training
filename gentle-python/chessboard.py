# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:30:29 2023

@author: Kuba
Write a getChessSquareColor() function that has parameters column and row. 
The function either returns 'black' or 'white' depending on the color at the specified column and
row. 
Chess boards are 8 x 8 spaces in size, and the columns and rows in this program begin at 0 and
end at 7 like in Figure 9-1. 
If the arguments for column or row are outside the 0 to 7 range, the
function returns a blank string.
Note that chess boards always have a white square in the top left corner.
"""

chessboard = [[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0]]

def getChessSquareColor(col,row):
    col = col - 1
    row = row - 1
    
    if col in range(0,8) and row in range(0,8):
        color = chessboard[row][col]
    
        if color == 1:
            return 'black'
        else:
            return 'white'
    else:
        return ''
    

assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''


# alternative
# oba parzyste - bialy 
# oba nieparzyste - bialy 
# reszta czarne 
 
def getChessSquareColor2(col,row):
    if col not in range(1,9) or row not in range(1,9):
        return ''
    else:
        if col % 2 == 0 and row % 2 == 0 or col % 2 !=0 and row % 2 != 0:
            return 'white'
        else:
            return 'black'
            

assert getChessSquareColor2(1, 1) == 'white'
assert getChessSquareColor2(2, 1) == 'black'
assert getChessSquareColor2(1, 2) == 'black'
assert getChessSquareColor2(8, 8) == 'white'
assert getChessSquareColor2(0, 8) == ''
assert getChessSquareColor2(2, 9) == ''


