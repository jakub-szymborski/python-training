# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:11:16 2024

@author: Kuba
"""

from random_walk import RandomWalk 
from statistics import fmean
import matplotlib.pyplot as plt

if False:
    rw = RandomWalk(True)
    rw.fill_walk()
    #plt.scatter(rw.xs, rw.ys)
    plt.plot(rw.xs, rw.ys)
    plt.show

running = False
while running:
    rw = RandomWalk(False)
    rw.fill_walk()
    #plt.scatter(rw.xs, rw.ys)
    plt.plot(rw.xs, rw.ys, alpha = 0.5)
    plt.show

    keep_running = input("make another walk? y/n:")
    if keep_running == 'n':
        running = False


# checking numerical impact of standing still option on total displacement  
dist_w_standing  = []
dist_no_standing = []

for i in range(11):
    walk1 = RandomWalk(True)
    walk1.fill_walk()
    d1 = walk1.get_walk_dist()
    dist_w_standing.append(d1)

    walk2 = RandomWalk(False)
    walk2.fill_walk()
    d2 = walk2.get_walk_dist()
    dist_no_standing.append(d2)

mean_dist_w_standing = fmean(dist_w_standing)
mean_dist_no_standing = fmean(dist_no_standing) 
diff = mean_dist_no_standing/mean_dist_w_standing

print(str((diff-1)*100) +'%')
# 1000 x2 tries     -> no standing has 1.9% more disp
# 10000 x2 tries    -> 1.4% more disp
# 100k x2 tries     -> 1.87% more disp
f4 = plt.figure().add_subplot(111)
plt.title('Total displacement ')
f4.hist(dist_w_standing, bins =40, color ='r', alpha = 0.5, label = 'with standing allowed')
f4.hist(dist_no_standing, bins =40, color ='b', alpha = 0.5, label = 'with no standing allowed')
f4.axvline(mean_dist_w_standing, color ='r', linestyle='dashed')
f4.axvline(mean_dist_no_standing, color ='b', linestyle='dashed')
f4.set_xlabel('Displacement value')
f4.set_ylabel('Count of occurances')
plt.legend(loc ='lower center', ncol =2)
plt.show()


if True:
    # plot n random walks from each variant
    f3 = plt.figure().add_subplot(111)
    
    # first, make one each to produce 2 labels for the legend
    rw = RandomWalk(True)
    rw.fill_walk()
    f3.plot(rw.xs, rw.ys, label = 'standing still allowed', color = 'r')
    
    rw = RandomWalk(False)
    rw.fill_walk()
    f3.plot(rw.xs, rw.ys, label = 'no standing still', color ='b')
    
    # generate 2 x n random walks without creating new variables
    for i in range(11):
    
        rw = RandomWalk(True)
        rw.fill_walk()
        plt.plot(rw.xs, rw.ys, color ='r', alpha = 0.5)
        
        rw = RandomWalk(False)
        rw.fill_walk()
        plt.plot(rw.xs, rw.ys, color ='b', alpha = 0.5)
        
    plt.legend(loc ='lower center', ncol =2)
    plt.show


"""
# make 10 walks each 
if True:
    rw0 = RandomWalk(False)
    rw1 = RandomWalk(False)
    rw2 = RandomWalk(False)
    rw3 = RandomWalk(False)
    rw4 = RandomWalk(False)
    rw5 = RandomWalk(False)
    rw6 = RandomWalk(False)
    rw7 = RandomWalk(False)
    rw8 = RandomWalk(False)
    rw9 = RandomWalk(False)
    
    rw10 = RandomWalk(True)
    rw11 = RandomWalk(True)
    rw12 = RandomWalk(True)
    rw13 = RandomWalk(True)
    rw14 = RandomWalk(True)
    rw15 = RandomWalk(True)
    rw16 = RandomWalk(True)
    rw17 = RandomWalk(True)
    rw18 = RandomWalk(True)
    rw19 = RandomWalk(True)
    
#rw0, rw1, rw2, rw3, rw4, rw5, rw6, rw7, rw8, rw9 = RandomWalk(False)
#rw10, rw11, rw12, rw13, rw14, rw15, rw16, rw17, rw18, rw19 = RandomWalk(True)

standing_still =(rw1, rw2, rw3, rw4, rw5,rw6, rw7, rw8, rw9) 
no_standing_still = (rw11, rw12, rw13, rw14, rw15, rw16, rw17, rw18, rw19)

f0 = plt.figure().add_subplot(111)
f1 = plt.figure().add_subplot(111)

f2 = plt.figure().add_subplot(111)

rw0.fill_walk()
f2.plot(rw0.xs, rw0.ys, label = 'standing still allowed', color = 'r')

rw10.fill_walk()
f2.plot(rw10.xs, rw0.ys, label = 'no standing still', color ='b')

for walk in no_standing_still: 
    walk.fill_walk()
    f2.plot(walk.xs, walk.ys, color ='b')
    plt.show
 
for walk in standing_still: 
    walk.fill_walk()
    f2.plot(walk.xs, walk.ys, color='r')
    
   # f2.annotate('10 walks each \n Blue: no standing still \n Red: standing still allowed', 
   #             xy =(200,-400))  
plt.legend(loc ='lower center', ncol =2)
plt.show
"""