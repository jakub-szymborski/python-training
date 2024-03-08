# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:13:02 2024

@author: Jakub Szymborski
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

case = 'mapa_wtrysk_steady_dp_2bar'
ext = '.txt'
path= case + ext
ss = np.loadtxt(path)            
ss = pd.DataFrame(ss, dtype = 'float', columns = ['p_A', 'u_A','p_avg','e_avg','x_avg','v_avg','rho_avg','mdot'])

p_A = ss['p_A']
u_A = ss['u_A']
v_avg = ss['v_avg']
mdot = ss['mdot']
rho_avg = ss['rho_avg']

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

surf = ax.plot_trisurf(p_A,u_A,v_avg, cmap = 'viridis')  # wykres 3D, powierzchnia z triangulacji punktow
#ax.scatter(t,z,w)             # punkty w 3D, wymaga danych 1D
ax.set_xlabel('Ciśnienie [bar]')
ax.set_ylabel('Energia [kJ/kg]')
ax.set_zlabel('Prędkość [m/s]')
plt.title('Mapa prędkości dla dp = 2bar ')
plt.tight_layout()
plt.savefig(case+'_predkosc'+ '.png')
plt.show()


fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

surf = ax.plot_trisurf(p_A, u_A, mdot, cmap = 'viridis')  # wykres 3D, powierzchnia z triangulacji punktow
#ax.scatter(t,z,w)             # punkty w 3D, wymaga danych 1D
ax.set_xlabel('Ciśnienie [bar]')
ax.set_ylabel('Energia [kJ/kg]')
ax.set_zlabel('Strumień [kg/s]')
plt.title('Mapa strumieni dla dp = 2bar ')
plt.tight_layout()
plt.savefig(case+'_strumienie'+ '.png')
plt.show()


fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

surf = ax.plot_trisurf(p_A, u_A, rho_avg, cmap = 'viridis')  # wykres 3D, powierzchnia z triangulacji punktow
#ax.scatter(t,z,w)             # punkty w 3D, wymaga danych 1D
ax.set_xlabel('Ciśnienie [bar]')
ax.set_ylabel('Energia [kJ/kg]')
ax.set_zlabel('Gęstość [kg/m3]')
plt.title('Mapa gęstości dla dp = 2bar ')
plt.tight_layout()
plt.savefig(case+'_gęstości'+ '.png')
plt.show()