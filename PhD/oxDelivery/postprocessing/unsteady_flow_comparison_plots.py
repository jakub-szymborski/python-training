# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:43:31 2024

@author: Jakub Szymborski
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


import matplotlib.animation as animation

case="testy_stabilnosci/dane/zawor/rozne_dt/"

path1 = "dp_8_tz_0.01_t_0.1_p_30_e_150_dt_1e-7"
case1 = np.loadtxt(case+path1 + '.txt')   
case1 = pd.DataFrame(case1, columns = ['t','j', 'p','u' ,'x','V','rho','xr', 'Mach', 'err' ], dtype ='float')

path2 = "dp_8_tz_0.01_t_0.1_p_30_e_150_dt_5e-7"
case2 = np.loadtxt(case+path2 + '.txt')   
case2 = pd.DataFrame(case2, columns = ['t','j', 'p','u' ,'x','V','rho','xr', 'Mach', 'err' ], dtype ='float')

path3 = "dp_8_tz_0.01_t_0.1_p_30_e_150_dt_1e-6"
case3 = np.loadtxt(case+path3 + '.txt')   
case3 = pd.DataFrame(case3, columns = ['t','j', 'p','u' ,'x','V','rho','xr', 'Mach', 'err' ], dtype ='float')

przypadki = (case1, case2, case3)

for przypadek in przypadki: 
    przypadek.replace([np.inf, -np.inf], np.nan, inplace = True)
    przypadek.dropna(inplace = True)
    przypadek['t'] = przypadek['t']*1000    # konwersja z s na ms 
    przypadek['p'] = przypadek['p']/1e5     # konwersja z Pa na bar 
    przypadek['u'] = przypadek['u']/1e3     # konwersja z J/kg na kJ/kg 



# z badanych przypadkow wybieram nadjdluzsza liste krokow czasowych 
times = max(case1['t'].unique(), case2['t'].unique(), key =len )  # usuwam powtorzenia 


jmax = case1['j'].max()

xmin = 0.95*case1['x'].min()
xmax = 1.05*case1['x'].max()

pmin = 0.99*case1['p'].min()
pmax = 1.01*case1['p'].max()

umin = 0.999*case1['u'].min()
umax = 1.001*case1['u'].max()

Vmin = 0.95*case1['V'].min()
Vmax = 1.05*case1['V'].max()

Machmin = 0
Machmax =  2*case1['Mach'].max()


# animacja parametrow na wtrysku ------------------------------
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize =(12,9))
line1, = ax1.plot([], [], linewidth=2, label=path1)
line2, = ax2.plot([], [], linewidth=2)
line3, = ax3.plot([], [], linewidth=2)
line4, = ax4.plot([], [], linewidth=2)

ax5 = ax4.twinx()
line5, = ax5.plot([], [], linewidth=2, label = 'Mach number, case 1', color = 'gray')

line1a, = ax1.plot([], [], linewidth=2, label = path2)
line2a, = ax2.plot([], [], linewidth=2)
line3a, = ax3.plot([], [], linewidth=2)
line4a, = ax4.plot([], [], linewidth=2)
line5a, = ax5.plot([], [], linewidth=2, label = 'Mach number, case 2', color = 'darkgreen' )

line1b, = ax1.plot([], [], linewidth=2, label=path3)
line2b, = ax2.plot([], [], linewidth=2)
line3b, = ax3.plot([], [], linewidth=2)
line4b, = ax4.plot([], [], linewidth=2)
line5b, = ax5.plot([], [], linewidth=2, label = 'Mach number, case 1', color = 'gray')


fig.legend(ncols = 2, loc = 'lower center')
time_text1 =  ax1.text(0.01, 0.98, '', horizontalalignment='left', verticalalignment='top', transform=ax1.transAxes, backgroundcolor='white') #

for ax in [ax1,ax2,ax3,ax4]:
    ax.grid()
    ax.set_xlim(0,jmax)
    ax.set_xlabel('Cell number [-]')

ax1.set_ylim(xmin, xmax)
ax1.title.set_text('Mass void fraction')
ax1.set_ylabel('Void fraction [kg/kg]')
time_text1 =  ax4.text(0.01, 0.98, '', horizontalalignment='left', verticalalignment='top', transform=ax.transAxes, backgroundcolor='white') #

ax2.set_ylim(pmin, pmax)
ax2.title.set_text('Pressure')
ax2.set_ylabel('Pressure [bar]')

ax3.set_ylim(umin, umax)
ax3.title.set_text('Int. energy')
ax3.set_ylabel('Int. energy [kJ/kg]')

ax4.set_ylim(Vmin, Vmax)
ax4.title.set_text('Velocity')
ax4.set_ylabel('Velocity [m/s]')

ax5.set_ylim(Machmin, Machmax)
ax5.set_ylabel('Mach number')


def animate(t):
    z = case1.loc[case1['t'] == t]['j']
    x = case1.loc[case1['t'] == t]['x']
    p = case1.loc[case1['t'] == t]['p']
    u = case1.loc[case1['t'] == t]['u']
    V = case1.loc[case1['t'] == t]['V']
    Mach = case1.loc[case1['t'] == t]['Mach']
    
    za = case2.loc[case2['t'] == t]['j']
    xa = case2.loc[case2['t'] == t]['x']
    pa = case2.loc[case2['t'] == t]['p']
    ua = case2.loc[case2['t'] == t]['u']
    Va = case2.loc[case2['t'] == t]['V']
    Macha = case2.loc[case2['t'] == t]['Mach']

    zb = case2.loc[case3['t'] == t]['j']
    xb = case2.loc[case3['t'] == t]['x']
    pb = case2.loc[case3['t'] == t]['p']
    ub = case2.loc[case3['t'] == t]['u']
    Vb = case2.loc[case3['t'] == t]['V']
    Machb = case2.loc[case3['t'] == t]['Mach']

    line1.set_data(z,x)
    line2.set_data(z,p)
    line3.set_data(z,u)
    line4.set_data(z,V)
    line5.set_data(z,Mach)
    
    line1a.set_data(za,xa)
    line2a.set_data(za,pa)
    line3a.set_data(za,ua)
    line4a.set_data(za,Va)
    line5a.set_data(z,Macha)
    
    line1b.set_data(zb,xb)
    line2b.set_data(zb,pb)
    line3b.set_data(zb,ub)
    line4b.set_data(zb,Vb)
    line5b.set_data(zb,Machb)

    time_text1.set_text(f't={t:.2f}' +' [ms]')

    return line1, line2, line3, line4, line5, line1a, line2a, line3a, line4a, line5a, line1b, line2b, line3b, line4b, line5b, time_text1

ani = animation.FuncAnimation(
    fig, animate,frames = times, interval=50, blit=True, repeat = False,  repeat_delay = 200)

#ani.save('x_p_u_v_10ms.mp4')

# htlm tworzy osobny obrazek dla kazdej klatki, b. funkcjonalne (przewijanie, stopowanie itd)
#ani.save('animacje/' + path1+'.html', writer="html")

# gif - wolne, ~8MB na 1000 klatek, trzeba by poprawic kadrowanie 
#writergif = animation.PillowWriter(fps=30) 
#ani.save('animacje/' + path1+'.gif', writer=writergif)
plt.show()
