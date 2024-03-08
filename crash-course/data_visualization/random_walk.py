# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:33:55 2024

@author: Kuba
"""
from random import choice 
from math import dist

class RandomWalk():
    # a class to generate random walks 
    
    def __init__(self, standing_still_allowed = True, num_points = 5000, ThreeD = False):
        # initialize attributes 
        self.num_points = num_points
        self.ThreeD = ThreeD
        
        # walk starting point
        self.xs = [0]
        self.ys = [0]
        self.zs = [0]
        self.standing_still_allowed = standing_still_allowed
        
        
    def fill_walk(self):
        # calc all the points in the walk 
        
        if self.ThreeD:
            self.fill_walk3D()

        while len(self.xs) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            
                
            # reject standing still
            if x_step == 0 and y_step == 0 and not self.standing_still_allowed:
                continue 
            
            # calc next xs and ys 
            next_x = self.xs[-1] + x_step
            next_y = self.ys[-1] + y_step 
            
            self.xs.append(next_x)
            self.ys.append(next_y)

     
    def fill_walk3D(self):
       # calc all the points in the walk in 3D
        while len(self.xs) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            z_step =self.get_step()
 
            if x_step == 0 and y_step == 0 and z_step == 0 and not self.standing_still_allowed:
                continue 
       
            # calc next xs and ys 
            next_x = self.xs[-1] + x_step
            next_y = self.ys[-1] + y_step 
            next_z = self.zs[-1] + z_step
            
            self.xs.append(next_x)
            self.ys.append(next_y)
            self.zs.append(next_z)

       
    def get_step(self):
        # method to calc next step 
        direction = choice([-1,1]) # random direction
        dist = choice([0,1,2,3,4])  # random step size
        step = direction*dist 
        return step  
            
    
    def get_walk_dist(self):
        # calculate total distance from start to finish in a walk
        if self.ThreeD:
            self.get_walk_dist_3D()
        
        last_x = self.xs[-1]
        last_y = self.ys[-1]
        self.dist = dist([0,0], [last_x,last_y])
        return self.dist
    
    def get_walk_dist_3D(self):
        last_x = self.xs[-1]
        last_y = self.ys[-1]
        last_z = self.zs[-1]
        self.dist = dist([0,0,0], [last_x,last_y,last_z])
        return self.dist
    
    
    
"""        
p = [0,0]
q = [1,1]
distance = dist(p,q)
"""