# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:55:17 2024

@author: Kuba
"""

from random_walk import RandomWalk 
from statistics import fmean
import matplotlib.pyplot as plt

rw = RandomWalk(True, ThreeD = True)
rw.fill_walk()

xs = rw.xs
ys = rw.ys
zs = rw.zs

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.scatter(xs, ys, zs)
plt.show()


fig2 = plt.figure()
ax2 = fig2.add_subplot(projection = '3d')
ax2.plot(xs,ys,zs)
plt.show()

fig3 = plt.figure()
ax3 = fig3.add_subplot(projection = '3d')

for i in range(10):
    rw = RandomWalk(standing_still_allowed = True, ThreeD = True)
    rw.fill_walk()
    plt.plot(rw.xs, rw.ys, rw.zs, alpha = 0.5)

    
plt.legend(loc ='lower center', ncol =2)
plt.show