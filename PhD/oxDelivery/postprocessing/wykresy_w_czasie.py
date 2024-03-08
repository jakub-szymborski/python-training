# -*- coding: utf-8 -*-
"""
Created on Mon May  9 13:18:36 2022
# Porownanie wynikow zaleznych od czasu 
    
@author: Jakub Szymborski
"""

# Loading libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#from matplotlib import rcParams
plt.rcParams.update({'figure.autolayout': True})

case = 'kanaly_zmienna_geometria/prosty/'

unstd_10 = np.loadtxt(case+'wyniki_2s.dta')            # wyniki dt = 5e-5
unstd_10 = pd.DataFrame(unstd_10, dtype = 'float')

unstd_100 = np.loadtxt(case+'wyniki_widmo.dta')       # wyniki z dt = 5e-6
unstd_100 = pd.DataFrame(unstd_100, dtype = 'float')

visc_100 = np.loadtxt(case+'wyniki_widmo.dta')      # wyniki z dt = 5e-7
visc_100 = pd.DataFrame(visc_100, dtype = 'float')


# zamiana z bar na Pa, usuniecie cisnienie odniesienia 
unstd_10[0] = unstd_10[0]*1000 
unstd_10[2] = unstd_10[2]*1e5 - 10e5 

unstd_100[0] = unstd_100[0]*1000 
unstd_100[2] = unstd_100[2]*1e5 - 10e5 


# zmiana z s na ms 
unstd_10[1] = unstd_10[1]*1000 
unstd_100[1] = unstd_100[1]*1000 
visc_100[1] = visc_100[1]*1000

visc_100[0] = visc_100[0]*1000 
visc_100[2] = visc_100[2]*1e5 - 10e5

# wybranie konkretnego punktu  
z1 = 98.5
unstd_t1_10 = unstd_10.loc[unstd_10[0] == z1 ]          
unstd_t1_100 = unstd_100.loc[unstd_100[0] == z1]
visc_100_t1 = visc_100.loc[visc_100[0] == z1]



# do wykresu 3D
wyniki = unstd_10
# ustawianie przerzedzania danych 
n_chciana = 10000      # pozadana liczba punktow 
n = len(wyniki[0])    # aktualna liczba elementow 

if (n_chciana >=n):
    dzielnik = int(1)
else:
    dzielnik = int (n/n_chciana)

wyniki = wyniki[0::dzielnik]  

t = wyniki[1]
z = wyniki[0]
v = wyniki[4]
p = wyniki[2]


xlim = 2000

f = plt.figure(figsize=(12,6))
ax = f.add_subplot(121)
ax2 = f.add_subplot(122)

ax.plot(unstd_t1_10[1], unstd_t1_10[4], 'c', label = 'dt = 1e-6')
#ax.plot(unstd_t1_100[1], unstd_t1_100[4], 'm', label = 'dt = 1e-7')
#ax.plot(visc_100_t1[1], visc_100_t1[4], 'r', label = 'dt = 1e-6 n=1000')

ax.set_xlim(0,xlim)
#ax.set_ylim(0,14)
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

ax.set_xlabel('Czas [ms]')
ax.set_ylabel('Prędkość średnia [m/s]')

#ax2.plot(pressure_avg, 'k')
ax2.plot(unstd_t1_10[1], unstd_t1_10[2], 'c')
#ax2.plot(unstd_t1_100[1], unstd_t1_100[2], 'm')
#ax2.plot(visc_100_t1[1], visc_100_t1[2], 'r')

ax2.set_xlabel('Czas [ms]')
ax2.set_ylabel('Ciśnienie [Pa]')
ax2.set_xlim(0,xlim)
#ax2.set_ylim(0, 2000)
ax2.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
    
plt.figlegend( loc = 'lower center', ncol = 7)
plt.savefig(case+ 'wykres.png',dpi =100, pad_inches =0.4, bbox_inches='tight')

plt.show()



# --------------- W Y K R E S Y  3 D  MatPlotLib-------------------------
# Wykres cisnienie(czas,polozenie)
fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_trisurf(t,z,v, cmap='viridis', linewidth = 0)  # wykres 3D, powierzchnia z triangulacji punktow
#ax.scatter(t,z,p)             # punkty w 3D, wymaga danych 1D
ax.set_xlabel('Czas[ms]')
ax.set_ylabel('Odleglosc [mm]')
#ax.set_zlabel('Cisnienie [Pa]')
ax.set_zlabel('Predkosc [m/s]')

ax.set_xlim(0,xlim)
#plt.title('Cisnienie')
plt.tight_layout()
#plt.savefig(folder+case+'cisnienie'+ '.png')
plt.show()   
