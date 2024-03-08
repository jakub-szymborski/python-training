# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:34:45 2024

@author: Kuba
"""

import matplotlib.pyplot as plt

values = [1,2,3,4,5]
squares = [1,4, 9, 16, 25]

# line plot 
plt.plot(values, squares, linewidth = 5)
plt.title("Square numbers", fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel("Value squared", fontsize = 14)
plt.tick_params(axis = 'both', labelsize =14 )
plt.show()


# scatter plot 
plt.scatter(values, squares, s=50) # s - dot/point size 
plt.plot(values, squares, linewidth = 2)    # add line connecting the points
plt.title("Square numbers", fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel("Value squared", fontsize = 14)
plt.tick_params(axis = 'both', which = 'major',  labelsize =14 )
plt.show()


# using more points


xs = list(range(1,1001))
ys = [x**2 for x in xs]

plt.scatter(xs, ys, s=20, edgecolors='none', c=ys, cmap = plt.cm.Blues_r)
#plt.plot(xs,ys)
plt.axis([0,1100,0,1100**2])
plt.xlabel('Value', fontsize = 14)
plt.ylabel("Value squared", fontsize = 14)
plt.tight_layout()
plt.savefig('squares.png')
plt.show()
