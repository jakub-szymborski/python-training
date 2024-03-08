# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:59:36 2022

@author: Jakub Szymborski
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

zmienne_p = np.loadtxt('wlasnosci_1zmienna.dta')
zmienne_pu = np.loadtxt('wlasnosci_2zmienna.dta')

zmienne_p = pd.DataFrame(zmienne_p)
zmienne_pu = pd.DataFrame(zmienne_pu)

zmienne_p[0] = zmienne_p[0]/1e5 # zamiana na bar

zmienne_pu[0] = zmienne_pu[0]/1e5    # zamiana na bar
zmienne_pu[1] = zmienne_pu[1]/1e3    # zamiana na kJ/kg


plt.subplot(2,2,1)
plt.plot(zmienne_p[0],zmienne_p[1], 'b', label = 'esat_p_vap')     #pkt 1
plt.plot(zmienne_p[0],zmienne_p[2], 'r', label = 'esat_p_lqd')     #pkt 1
plt.xlabel('Cisnienie [bar]')
plt.ylabel('Energia wew. [kJ/kg]')

plt.subplot(2,2,2)
plt.plot(zmienne_p[0],zmienne_p[3], 'b', label = 'dT/dp')     #pkt 1
plt.xlabel('Cisnienie [bar]')
plt.ylabel('dT dp [K/Pa]')

plt.subplot(2,2,3)
plt.plot(zmienne_p[0],zmienne_p[4], 'b', label = 'Temp')     #pkt 1
plt.xlabel('Cisnienie [bar]')
plt.ylabel('Temp [K]')

plt.tight_layout()
plt.show()



 
    

"""
    
# Gestosc (p,u)   
fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_trisurf(zmienne_pu[0], zmienne_pu[1], zmienne_pu[2], 
                       cmap='viridis', linewidth = 0)  # wykres 3D, powierzchnia z triangulacji punktow
#ax.scatter(t,z,p)             # punkty w 3D, wymaga danych 1D
ax.set_xlabel('Cisnienie[bar]')
ax.set_ylabel('Energia wew [kJ/kg]')
ax.set_zlabel('Gestosc [kg/m3]')
plt.title('Gestosc')
plt.tight_layout()
plt.show()   
    
 # d_rho/dp
fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_trisurf(zmienne_pu[0], zmienne_pu[1], zmienne_pu[3], 
                       cmap='viridis', linewidth = 0)  # wykres 3D, powierzchnia z triangulacji punktow
#ax.scatter(t,z,p)             # punkty w 3D, wymaga danych 1D
ax.set_xlabel('Cisnienie[bar]')
ax.set_ylabel('Energia wew [kJ/kg]')
ax.set_zlabel('d rho dp [kg/m3/Pa]')
plt.title('d rho dp')
plt.tight_layout()
plt.show()   
   
# d_rho/de
fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_trisurf(zmienne_pu[0], zmienne_pu[1], -zmienne_pu[4], 
                       cmap='viridis', linewidth = 0)  # wykres 3D, powierzchnia z triangulacji punktow
#ax.scatter(t,z,p)             # punkty w 3D, wymaga danych 1D
ax.set_xlabel('Cisnienie[bar]')
ax.set_ylabel('Energia wew [kJ/kg]')
ax.set_zlabel('d rho de [kg/m3/kJ]')
plt.title('minus d rho de')
plt.tight_layout()
plt.show()   

    