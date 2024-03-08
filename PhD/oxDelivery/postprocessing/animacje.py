# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:38:15 2023

@author: Jakub Szymborski
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


import matplotlib.animation as animation

case=''

path_tank = "wyniki_tank"
tank = np.loadtxt(case+path_tank + '.txt')             
tank = pd.DataFrame(tank, columns =['t','alfa','p','hg','hd','T_wall','x_inj','m_ox_tank','m_out_dyer' ], dtype = 'float')

path_inj_full = "wyniki_wtrysk_full"
inj_full = np.loadtxt(case+path_inj_full + '.txt')   
inj_full = pd.DataFrame(inj_full, columns = ['t','j', 'p','u' ,'x','V','rho','xr', 'Mach' ], dtype ='float')

# drop NaNs 
inj_full.dropna(inplace = True)
tank.dropna(inplace = True)

inj_full['t'] = inj_full['t']*1000 # konwersja z s na ms
tank['t'] = tank['t']*1000 # konwersja z s na ms

inj_full['p'] = inj_full['p']/1e5
inj_full['u'] = inj_full['u']/1e3


# szacowanie roznic miedzy kolejnymi krokami czasowymi 
stab = inj_full[['t','j','p','u']]
# ramka z danymi dla wszystkich t dla jednego j, np j = 10
stab = stab.loc[stab['j']== 10]
stab = stab.drop('j', axis =1)
stab['u_diff'] = stab.diff()['u']
stab['p_diff'] = stab.diff()['p']

stab['u_diff'] = stab['u_diff'].abs()
stab['p_diff'] = stab['p_diff'].abs()


f = plt.figure()
ax = f.add_subplot(121)
ax2= f.add_subplot(122)

ax.plot(stab['t'], stab['u_diff'])
ax2.plot(stab['t'], stab['p_diff'])

ax.set_xlabel('Czas [s]')
ax.set_ylabel('U_diff [kJ/kg]')
ax.set_yscale('log')

ax2.set_xlabel('Czas [s]')
ax2.set_ylabel('p_diff [bar]')
ax2.set_yscale('log')
plt.show()



jmax = inj_full['j'].max()

xmin = 0.95*inj_full['x'].min()
xmax = 1.05*inj_full['x'].max()

pmin = 0.99*inj_full['p'].min()
pmax = 1.01*inj_full['p'].max()

umin = 0.99*inj_full['u'].min()
umax = 1.01*inj_full['u'].max()

Vmin = 0.95*inj_full['V'].min()
Vmax = 1.05*inj_full['V'].max()

times = inj_full['t'].unique()  # usuwam powtorzenia 


# ---------------------------------------------------
f = plt.figure(figsize=(12,6))
f.suptitle('Parametry zbiornika', fontsize=12)
ax1 = f.add_subplot(221)
ax2 = f.add_subplot(222)
ax3 = f.add_subplot(223)
ax4 = f.add_subplot(224)

ax1.plot(tank['t'], tank['alfa'], label = 'alfa')
ax2.plot(tank['t'], tank['p'], label = 'p')
ax3.plot(tank['t'], tank['T_wall'], label = 'T_wall')
ax4.plot(tank['t'], tank['m_ox_tank'], label = 'm_ox_tank')


for ax in [ax1,ax2,ax3,ax4]:
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax.set_xlabel('Czas [ms]')
    ax.set_xlim(0,tank['t'].max())
    
ax1.set_ylabel('Udzial gornej czesci [m3/m3]')
ax2.set_ylabel('Cisnienie [bar]')
ax3.set_ylabel('Temp. scianki [K]')
ax4.set_ylabel('Masa w zbiorniku [kg]')


#plt.figlegend( loc = 'lower center', ncol = 7)
#plt.savefig(case+ '_wykres.png',dpi =100, pad_inches =0.4, bbox_inches='tight')
plt.show()



# animacja parametrow na wtrysku ------------------------------
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)
line1, = ax1.plot([], [], linewidth=2)
line2, = ax2.plot([], [], linewidth=2)
line3, = ax3.plot([], [], linewidth=2)
line4, = ax4.plot([], [], linewidth=2)
dot,   = ax2.plot([], [],  'or', markersize=6, label = 'Ptank')
time_text1 =  ax1.text(0.01, 0.98, '', horizontalalignment='left', verticalalignment='top', transform=ax.transAxes, backgroundcolor='white') #


for ax in [ax1,ax2,ax3,ax4]:
    ax.grid()
    ax.set_xlim(0,jmax)
    ax.set_xlabel('Długość [-]')

ax1.set_ylim(xmin, xmax)
ax1.title.set_text('Masowy stopień suchości')
ax1.set_ylabel('Stopień suchości [kg/kg]')
time_text1 =  ax4.text(0.01, 0.98, '', horizontalalignment='left', verticalalignment='top', transform=ax.transAxes, backgroundcolor='white') #

ax2.set_ylim(pmin, pmax)
ax2.title.set_text('Ciśnienie')
ax2.set_ylabel('Ciśnienie [bar]')

ax3.set_ylim(umin, umax)
ax3.title.set_text('Energia wew.')
ax3.set_ylabel('Energia wew. [kJ/kg]')

ax4.set_ylim(Vmin, Vmax)
ax4.title.set_text('Prędkość')
ax4.set_ylabel('Prędkość [m/s]')

def animate(t):
    z = inj_full.loc[inj_full['t'] == t]['j']
    x = inj_full.loc[inj_full['t'] == t]['x']
    p = inj_full.loc[inj_full['t'] == t]['p']
    u = inj_full.loc[inj_full['t'] == t]['u']
    V = inj_full.loc[inj_full['t'] == t]['V']
    ptank = tank.loc[tank['t'] == t]['p']
    
    line1.set_data(z,x)
    line2.set_data(z,p)
    dot.set_data(1,ptank)
    line3.set_data(z,u)
    line4.set_data(z,V)
    time_text1.set_text(f't={t:.2f}' +' [ms]')

    return line1, line2,dot, line3, line4, time_text1

ani = animation.FuncAnimation(
    fig, animate,frames = times, interval=10, blit=True, repeat = False,  repeat_delay = 100)
#ani.save('x_p_u_v_10ms.mp4')
plt.show()

