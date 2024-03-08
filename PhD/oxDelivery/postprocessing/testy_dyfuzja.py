# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:01:17 2023

@author: Jakub Szymborski
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


import matplotlib.animation as animation

case="testy_stabilnosci/dane/zawor/"

path_diff = "dp_8_tz_0.1_t_0.00001_p_30_e_50"
diff = np.loadtxt(case+path_diff + '.txt')   
diff = pd.DataFrame(diff, columns = ['t','j', 'p','u' ,'x','V','rho','xr', 'Mach', 'err' ], dtype ='float')

path_relax = "dp_8_tz_0.1_t_0.000001_p_30_e_50"
relax = np.loadtxt(case+path_relax + '.txt')   
relax = pd.DataFrame(relax, columns = ['t','j', 'p','u' ,'x','V','rho','xr', 'Mach', 'err' ], dtype ='float')

path_equil = "dp_8_tz_0.1_t_0.0000001_p_30_e_50"
equil = np.loadtxt(case+path_equil + '.txt')   
equil = pd.DataFrame(equil, columns = ['t','j', 'p','u' ,'x','V','rho','xr', 'Mach', 'err' ], dtype ='float')

przypadki = (diff, relax, equil)

for przypadek in przypadki: 
    przypadek.dropna(inplace = True)
    przypadek['t'] = przypadek['t']*1000    # konwersja z s na ms 
    przypadek['p'] = przypadek['p']/1e5     # konwersja z Pa na bar 
    przypadek['u'] = przypadek['u']/1e3     # konwersja z J/kg na kJ/kg 


# z badanych przypadkow wybieram nadjdluzsza liste krokow czasowych 
times = max(diff['t'].unique(), relax['t'].unique(), equil['t'].unique(), key =len )  # usuwam powtorzenia 

jmax = diff['j'].max()

xmin = 0.95*diff['x'].min()
xmax = 1.05*diff['x'].max()

pmin = 0.99*diff['p'].min()
pmax = 1.01*diff['p'].max()

umin = 0.999*diff['u'].min()
umax = 1.001*diff['u'].max()

Vmin = 0.95*diff['V'].min()
Vmax = 1.05*diff['V'].max()


topka = 11
# dane z jednego kroku czasowego 
diff_t1 = diff.loc[diff['t']==times[0]]
#diff_t1 = diff.head(21)
diff_t1 = diff_t1.drop('t', axis=1)
diff_t1 = diff_t1.head(topka)

diff_t2 = diff.loc[diff['t']==times[1]]
#diff_t1 = diff.head(21)
diff_t2 = diff_t2.drop('t', axis=1)
diff_t2 = diff_t2.head(topka)

diff_t3 = diff.loc[diff['t']==times[2]]
#diff_t1 = diff.head(21)
diff_t3 = diff_t3.drop('t', axis=1)
diff_t3 = diff_t3.head(topka)

if False:
    f1 = plt.figure()
    f1ax = f1.add_subplot(221)
    f1ax2= f1.add_subplot(222)
    f1ax3 = f1.add_subplot(223)
    f1ax4 = f1.add_subplot(224)
    f1ax.plot(diff_t1['j'], diff_t1['p'], label = 't0')
    f1ax.plot(diff_t2['j'], diff_t2['p'], label = 't1')
    f1ax.plot(diff_t3['j'], diff_t3['p'], label = 't2')
    
    
    f1ax2.plot(diff_t1['j'], diff_t1['u'])
    f1ax2.plot(diff_t2['j'], diff_t2['u'])
    f1ax2.plot(diff_t3['j'], diff_t3['u'])
    f1ax2.set_ylim(umin,umax)
    
    f1ax3.plot(diff_t1['j'], diff_t1['V'])
    f1ax3.plot(diff_t2['j'], diff_t2['V'])
    f1ax3.plot(diff_t3['j'], diff_t3['V'])
    
    f1ax4.plot(diff_t1['j'], diff_t1['err'])
    f1ax4.plot(diff_t2['j'], diff_t2['err'])
    f1ax4.plot(diff_t3['j'], diff_t3['err'])
    
    for axs in [f1ax,f1ax2,f1ax3, f1ax4]:
        axs.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        axs.set_xlabel('j [-]')
        axs.set_xlim(diff_t1['j'].min(),diff_t1['j'].max())
        xticks = range(0,topka,int(topka/10))
        xlabels = [f'{x}' for x in xticks]
        axs.set_xticks(xticks, xlabels)
    
    f1ax.set_ylabel('Cisnienie [bar]')
    f1ax2.set_ylabel('Energia [kJ/kg]')
    f1ax3.set_ylabel('Predkosc [m/s]')
    f1ax4.set_ylabel('Blad gestosci [-]')
    
    plt.figlegend( loc = 'lower center', ncol = 3)
    plt.tight_layout()
plt.show()


# test stabilnosci -----------------------

# szacowanie roznic miedzy kolejnymi krokami czasowymi 
if False:
    stab = diff[['t','j','p','u', 'err']]
    # ramka z danymi dla wszystkich t dla jednego j, np j = 10
    stab = stab.loc[stab['j']== 5]
    stab = stab.drop('j', axis =1)
    stab['u_diff'] = stab.diff()['u']
    stab['p_diff'] = stab.diff()['p']
    
    stab['u_diff'] = stab['u_diff'].abs()
    stab['p_diff'] = stab['p_diff'].abs()
    
    # case2
    stab2 = relax[['t','j','p','u', 'err']]
    # ramka z danymi dla wszystkich t dla jednego j, np j = 10
    stab2 = stab2.loc[stab2['j']== 5]
    stab2 = stab2.drop('j', axis =1)
    stab2['u_diff'] = stab2.diff()['u']
    stab2['p_diff'] = stab2.diff()['p']
    
    stab2['u_diff'] = stab2['u_diff'].abs()
    stab2['p_diff'] = stab2['p_diff'].abs()
    
    # case 3
    stab3 = equil[['t','j','p','u', 'err']]
    # ramka z danymi dla wszystkich t dla jednego j, np j = 10
    stab3 = stab3.loc[stab3['j']== 5]
    stab3 = stab3.drop('j', axis =1)
    stab3['u_diff'] = stab3.diff()['u']
    stab3['p_diff'] = stab3.diff()['p']
    
    stab3['u_diff'] = stab3['u_diff'].abs()
    stab3['p_diff'] = stab3['p_diff'].abs()
    
    
    f = plt.figure()
    ax = f.add_subplot(221)
    ax2= f.add_subplot(222)
    ax3 = f.add_subplot(223)
    
    ax.plot(stab['t'], stab['u_diff'], label = path_diff)
    ax.plot(stab2['t'], stab2['u_diff'], label = path_relax)
    ax.plot(stab3['t'], stab3['u_diff'], label = path_equil)
    
    ax2.plot(stab['t'], stab['p_diff'])
    ax2.plot(stab2['t'], stab2['p_diff'])
    ax2.plot(stab3['t'], stab3['p_diff'])
    
    ax3.plot(stab['t'], stab['err'])
    ax3.plot(stab2['t'], stab2['err'])
    ax3.plot(stab3['t'], stab3['err'])
    
    ax.set_xlabel('Czas [ms]')
    ax.set_ylabel('U_diff [kJ/kg]')
    ax.set_yscale('log')
    
    ax2.set_xlabel('Czas [ms]')
    ax2.set_ylabel('p_diff [bar]')
    ax2.set_yscale('log')
    
    ax3.set_xlabel('Czas [ms]')
    ax3.set_ylabel('Err []')
    #ax2.set_yscale('log')
    
    plt.figlegend( loc = 'lower center', ncol = 7)
    
    plt.show()

# test stabilnosci ----------------------- koniec 



# animacja parametrow na wtrysku ------------------------------
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)
line1, = ax1.plot([], [], linewidth=2, label=path_diff)
line2, = ax2.plot([], [], linewidth=2)
line3, = ax3.plot([], [], linewidth=2)
line4, = ax4.plot([], [], linewidth=2)

line1a, = ax1.plot([], [], linewidth=2, label = path_relax)
line2a, = ax2.plot([], [], linewidth=2)
line3a, = ax3.plot([], [], linewidth=2)
line4a, = ax4.plot([], [], linewidth=2)

line1b, = ax1.plot([], [], linewidth=2, label = path_equil)
line2b, = ax2.plot([], [], linewidth=2)
line3b, = ax3.plot([], [], linewidth=2)
line4b, = ax4.plot([], [], linewidth=2)

fig.legend()
time_text1 =  ax1.text(0.01, 0.98, '', horizontalalignment='left', verticalalignment='top', transform=ax1.transAxes, backgroundcolor='white') #


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
    z = diff.loc[diff['t'] == t]['j']
    x = diff.loc[diff['t'] == t]['x']
    p = diff.loc[diff['t'] == t]['p']
    u = diff.loc[diff['t'] == t]['u']
    V = diff.loc[diff['t'] == t]['V']
    
    za = relax.loc[relax['t'] == t]['j']
    xa = relax.loc[relax['t'] == t]['x']
    pa = relax.loc[relax['t'] == t]['p']
    ua = relax.loc[relax['t'] == t]['u']
    Va = relax.loc[relax['t'] == t]['V']
        
    zb = equil.loc[equil['t'] == t]['j']
    xb = equil.loc[equil['t'] == t]['x']
    pb = equil.loc[equil['t'] == t]['p']
    ub = equil.loc[equil['t'] == t]['u']
    Vb = equil.loc[equil['t'] == t]['V']
        
    line1.set_data(z,x)
    line2.set_data(z,p)
    line3.set_data(z,u)
    line4.set_data(z,V)
    
    line1a.set_data(za,xa)
    line2a.set_data(za,pa)
    line3a.set_data(za,ua)
    line4a.set_data(za,Va)
    
    line1b.set_data(zb,xb)
    line2b.set_data(zb,pb)
    line3b.set_data(zb,ub)
    line4b.set_data(zb,Vb)
    
    time_text1.set_text(f't={t:.2f}' +' [ms]')

    return line1, line2, line3, line4,line1a, line2a, line3a, line4a, line1b, line2b, line3b, line4b, time_text1

ani = animation.FuncAnimation(
    fig, animate,frames = times[:100], interval=300, blit=True, repeat = False,  repeat_delay = 200)
#ani.save('x_p_u_v_10ms.mp4')
plt.show()
