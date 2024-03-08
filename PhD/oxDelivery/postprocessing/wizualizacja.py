# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:57:33 2023

@author: Jakub Szymborski
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import imageio


path_tank = "wyniki_tank"
path_inj  = "wyniki_wtrysk_basic" 
path_inj_full = "wyniki_wtrysk_full"

case = "dane/5bar_4.25kg_dt_inj1e-6_0.1s/"

tank = np.loadtxt(case+path_tank + '.txt')             
tank = pd.DataFrame(tank, columns =['t','alfa','p','hg','hd','T_wall','x_inj','m_ox_tank','m_out_dyer' ], dtype = 'float')

inj = np.loadtxt(case+path_inj + '.txt')             
inj = pd.DataFrame(inj, columns =['t','dt_inj', 'delta_p', 'delta_x', 'm_ox_out', 'T_out', 'rho_out'], dtype = 'float')

inj_full = np.loadtxt(case+path_inj_full + '.txt')   
inj_full = pd.DataFrame(inj_full, columns = ['t','j', 'p','u' ,'x','V','rho','xr', 'Mach' ], dtype ='float')

inj_full['t'] = inj_full['t']*1000 # konwersja z s na ms
inj_full['p'] = inj_full['p']/1e5
inj_full['u'] = inj_full['u']/1e3

strumienie = pd.DataFrame(columns = ['t','Model', 'Dyer'])
strumienie ['t'] = tank['t']
strumienie['Model'] = inj['m_ox_out']/inj['dt_inj']

strumienie['Dyer'] = tank['m_out_dyer']
#strumienie.loc[:,'Dyer'] = tank['m_out_dyer']

xlim = 2.0
t_unit = 's'

# ---------------------------------------------------
f = plt.figure(figsize=(12,6))
f.suptitle('Parametry zbiornika', fontsize=12)
ax = f.add_subplot(221)
ax2 = f.add_subplot(222)
ax3 = f.add_subplot(223)
ax4 = f.add_subplot(224)

ax.plot(tank['t'], tank['alfa'], label = 'alfa')
ax2.plot(tank['t'], tank['p'], label = 'p')
ax3.plot(tank['t'], tank['T_wall'], label = 'T_wall')
ax4.plot(tank['t'], tank['m_ox_tank'], label = 'm_ox_tank')

ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
ax2.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
ax3.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
ax4.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

ax.set_xlabel('Czas [s]')
ax2.set_xlabel('Czas [s]')
ax3.set_xlabel('Czas [s]')
ax4.set_xlabel('Czas [s]')

ax.set_ylabel('Udzial gornej czesci [m3/m3]')
ax2.set_ylabel('Cisnienie [Pa]')
ax3.set_ylabel('Temp. scianki [K]')
ax4.set_ylabel('Masa w zbiorniku [kg]')

#plt.xlabel('Czas '+t_unit)
#plt.ylabel('Predkosc [m/s]')

plt.figlegend( loc = 'lower center', ncol = 7)
#plt.savefig(case+ '_wykres.png',dpi =100, pad_inches =0.4, bbox_inches='tight')
plt.show()

# ----------------------------------------
f = plt.figure(figsize=(12,6))
f.suptitle('Parametry wtrysku', fontsize=12)
ax = f.add_subplot(221)
ax2 = f.add_subplot(222)
ax3 = f.add_subplot(223)
ax4 = f.add_subplot(224)

ax.plot(inj['t'], inj['delta_p'], label = 'delta_p')
ax2.plot(inj['t'], inj['delta_x'], label = 'delta_x')
ax3.plot(inj['t'], inj['m_ox_out'], label = 'm_ox_out')
ax4.plot(inj['t'], inj['rho_out'], label = 'rho_out')

ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
ax2.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
ax3.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
ax4.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

ax.set_xlabel('Czas [s]')
ax2.set_xlabel('Czas [s]')
ax3.set_xlabel('Czas [s]')
ax4.set_xlabel('Czas [s]')

ax.set_ylabel('Spadek ciśnienia [bar]')
ax2.set_ylabel('Zmiana st. suchości [kg/kg]')
ax3.set_ylabel('Masa strumienia na krok  [kg]')
ax4.set_ylabel('Gęstość wylotowa [kg/m3]')

#plt.xlabel('Czas '+t_unit)
#plt.ylabel('Predkosc [m/s]')

plt.figlegend( loc = 'lower center', ncol = 7)
#plt.savefig(case+ '_wykres.png',dpi =100, pad_inches =0.4, bbox_inches='tight')
plt.show()

# ---------------------------------------------------


# ---------------------------------------------------
f = plt.figure()
f.suptitle('Model wtrysku vs Model Dyera', fontsize=12)
ax = f.add_subplot(111)
ax.plot(strumienie['t'], strumienie['Model'], label = 'Model')
ax.plot(strumienie['t'], strumienie['Dyer'], label = 'Dyer')
plt.xlabel('Czas '+t_unit)
plt.ylabel('Strumien masy [kg/s]')
#plt.xlim(0,xlim)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

#plt.xlabel('Czas '+t_unit)
#plt.ylabel('Predkosc [m/s]')

plt.figlegend( loc = 'lower center', ncol = 7)
#plt.savefig(case+ '_wykres.png',dpi =100, pad_inches =0.4, bbox_inches='tight')
plt.show()
# ---------------------------------------------------

# rozrzedzanie wynikow 
unikalneRekordy = len(inj_full['t'].unique())
chciane = 100  # ile rekordow chcemy  
odrzuc = int(round((unikalneRekordy/chciane),0))    # okresla co ktory wynik pozostanie - 1 = kazdy

if odrzuc < 1.0: 
    odrzuc = 1.0

#inj_full = inj_full.iloc[::odrzuc, :]    

# wizualizacja kanalu wtryskowego 
times = inj_full['t'].unique()  # usuwam powtorzenia 
times = np.delete(times, np.arange(0, times.size, odrzuc))

jmax = inj_full['j'].max()

pmin = 0.95*inj_full['p'].min()
pmax = 1.05*inj_full['p'].max()

umin = 0.95*inj_full['u'].min()
umax = 1.05*inj_full['u'].max()

vmin = 0.95*inj_full['V'].min()
vmax = 1.05*inj_full['V'].max()

rhomin= 0.95*inj_full['rho'].min()
rhomax= 1.05*inj_full['rho'].max()

xmin = 0.95*inj_full['x'].min()
xmax = 1.05*inj_full['x'].max()

machmin = 0.95*inj_full['Mach'].min()
machmax = 1.05*inj_full['Mach'].max()

def create_frame(t):
   # -------- multiplot -----------
    f = plt.figure(figsize=(12,6))
    f.suptitle('t=' + str(round(t,4))+' [ms]' , fontsize=12)
    ax = f.add_subplot(321)
    ax.title.set_text('Ciśnienie')
    ax.set_xlabel('Długość [-]')
    ax.set_ylabel('Ciśnienie [bar]')
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax.set_xlim(0,jmax)
    ax.set_ylim(pmin, pmax)
    
    ax2 =f.add_subplot(322)
    ax2.title.set_text('Energia')
    ax2.set_xlabel('Długość [-]')
    ax2.set_ylabel('Energia [kJ/kg]')
    ax2.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax2.set_xlim(0,jmax)
    ax2.set_ylim(umin,umax)
    
    ax3 =f.add_subplot(323)
    ax3.title.set_text('Masowy stopień suchości')
    ax3.set_xlabel('Długość [-]')
    ax3.set_ylabel('Stopień suchości [kg/kg]')
    ax3.tick_params(axis = 'y', labelrotation = 30)
    ax3.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax3.set_xlim(0,jmax)
    ax3.set_ylim(xmin, xmax)
    
    ax4 =f.add_subplot(324)
    ax4.title.set_text('Prędkość')
    ax4.set_xlabel('Długość [-]')
    ax4.set_ylabel('Prędkość [m/s]')
    ax4.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax4.set_xlim(0,jmax)
    ax4.set_ylim(vmin, vmax)
    
    ax5 =f.add_subplot(325)
    ax5.title.set_text('Gęstość')
    ax5.set_xlabel('Długość [-]')
    ax5.set_ylabel('Gęstość [kg/m3]')
    ax5.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax5.set_xlim(0,jmax)
    ax5.set_ylim(rhomin, rhomax)
    
    ax6 =f.add_subplot(326)
    ax6.title.set_text('Liczba Macha')
    ax6.set_xlabel('Długość [-]')
    ax6.set_ylabel('Liczba Macha [-]')
    ax6.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax6.set_xlim(0,jmax)
    ax6.set_ylim(machmin, machmax)
    
    # ['t', 'p','u' ,'x','V','ro','xr' ]
    ax.plot(inj_full.loc[inj_full['t'] == t]['j'], inj_full.loc[inj_full['t'] == t]['p'], 'k')
    ax2.plot(inj_full.loc[inj_full['t'] == t]['j'], inj_full.loc[inj_full['t'] == t]['u'], 'k')
    ax3.plot(inj_full.loc[inj_full['t'] == t]['j'], inj_full.loc[inj_full['t'] == t]['x'], 'k')
    ax4.plot(inj_full.loc[inj_full['t'] == t]['j'], inj_full.loc[inj_full['t'] == t]['V'], 'k')
    ax5.plot(inj_full.loc[inj_full['t'] == t]['j'], inj_full.loc[inj_full['t'] == t]['rho'], 'k')
    ax6.plot(inj_full.loc[inj_full['t'] == t]['j'], inj_full.loc[inj_full['t'] == t]['Mach'], 'k')

    plt.tight_layout()
    plt.savefig(case+'wyniki_wtrysk/' + 't=' +str(t)+'.png', 
                    transparent = False,  
                    facecolor = 'white'
                   )
    plt.close() 

create_frame(2.7)
 
if True:
    for t in times:
        create_frame(t)
            
    frames = []
    for t in times:
            image = imageio.imread(case+'wyniki_wtrysk/' + 't=' +str(t) + '.png')
            frames.append(image)
        
            imageio.mimsave(case+'przebiegi.gif',  # output gif
                                frames,                     # array of input frames
                            fps = 10,                   # optional: frames per second
                            loop = 1)                  
            



