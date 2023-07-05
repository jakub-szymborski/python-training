# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:31:23 2023

@author: Jakub Szymborski
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import imageio

path_unsat = 'dane/unsat/testy_krok_czasowy/dp_1_bar//'

case = 'wyniki_dt_1e-6_dx_1e-3_1ms_wszystkie'
title = 'Wyniki w czasie, ciecz, przekroj L = 50 mm, dp = 1 bar'

# case'y: 
# unsat: wyniki_dp_100_3s.txt, wyniki_dp_400_3s.txt, wyniki_dp_4k_3s.txt, wyniki_dp_40k_3s.txt, wyniki_dp_100k_3s.txt, wyniki_dp_500k_3s.txt, wyniki_dp_1kk_3s.txt

unsat = np.loadtxt(path_unsat+case+'.txt')             
unsat = pd.DataFrame(unsat, columns =['z','t','p','u','v','T','rho','x','xr', 'a'], dtype = 'float')


# konwersja z m na mm 
unsat['z'] = unsat['z']*1e3 

# konwersja z s na ms 
unsat['t'] = unsat['t']*1e3 
t_unit = '[ms]'
#t_unit = '[s]'

# zamiana z bar na Pa, usuniecie cisnienie odniesienia 
unsat['p'] = unsat['p']*1e5 - 20e5

# wybranie konkretnej chwili czasowej 
#unsat_t1 = unsat.loc[unsat[1] == 0.999]

# wybranie konkretnego przekroju 
L1 = 50.0
unsat_L1 = unsat.loc[unsat['z'] == L1]


# ---- Wykresy ------------
xlim = 1
f = plt.figure(figsize=(12,6))
f.suptitle(title, fontsize=12)
ax = f.add_subplot(121)

ax.plot(unsat_L1['t'], unsat_L1['p'], 'm', label = 'p_unsat')

ax.set_xlim(0,xlim)
#ax.set_ylim(0,14)
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

ax.set_xlabel('Czas '+t_unit)
#ax.set_ylabel('Prędkość średnia [m/s]')
ax.set_ylabel('Cisnienie [Pa]')

ax2 = f.add_subplot(122)
ax2.plot(unsat_L1['t'], unsat_L1['v'], 'm', label = 'V_unsat')

ax2.set_xlabel('Czas ' + t_unit)
ax2.set_ylabel('Predkosc [m/s]')
ax2.set_xlim(0,xlim)
#ax2.set_ylim(0, 2000)
ax2.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.05,
                 box.width, box.height * 0.95])
box = ax2.get_position()
ax2.set_position([box.x0, box.y0 + box.height * 0.05,
                 box.width, box.height * 0.95])
     
plt.figlegend( loc = 'lower center', ncol = 7)
#plt.savefig(case+ '_wykres.png',dpi =100, pad_inches =0.4, bbox_inches='tight')

plt.show()

# --------------- wykresy dla 3 czasow ---------------
t1 = 0.01
t2 = 0.1
t3 = 0.15
t4 = 0.175
t5 = 0.2

unsat_t1 = unsat.loc[unsat['t'] == t1]
unsat_t2 = unsat.loc[unsat['t'] == t2]
unsat_t3 = unsat.loc[unsat['t'] == t3]
unsat_t4 = unsat.loc[unsat['t'] == t4]
unsat_t5 = unsat.loc[unsat['t'] == t5]

title = 'Wykresy ciśnienia wzdłuż kanału'
xlim = 100
f = plt.figure(figsize=(12,6))
f.suptitle(title, fontsize=12)
ax = f.add_subplot(111)

ax.plot(unsat_t1['z'], unsat_t1['p'], label = 't= ' + str(t1))
ax.plot(unsat_t2['z'], unsat_t2['p'], label = 't= ' + str(t2))
ax.plot(unsat_t3['z'], unsat_t3['p'], label = 't= ' + str(t3))
ax.plot(unsat_t4['z'], unsat_t4['p'], label = 't= ' + str(t4))
ax.plot(unsat_t5['z'], unsat_t5['p'], label = 't= ' + str(t5))

ax.set_xlim(0,xlim)
#ax.set_ylim(0,14)
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

ax.set_xlabel('Dlugość kanału [mm]')
#ax.set_ylabel('Prędkość średnia [m/s]')
ax.set_ylabel('Ciśnienie [Pa]')

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.05,
                 box.width, box.height * 0.95])
     
plt.figlegend( loc = 'lower center', ncol = 7)
#plt.savefig(case+ '_wykres.png',dpi =100, pad_inches =0.4, bbox_inches='tight')
plt.show()



# robimy gif
xlim = 100
ymax = max(unsat['p'])
ymin = min(unsat['p'])

times = unsat_L1['t']

def create_frame(t):
    f = plt.figure(figsize=(12,6))
    f.suptitle('Przebieg prędkości wzdłuż kanału, t = '+str(round(t,4)) + ' [ms]', fontsize=12)
    
    plt.plot(unsat.loc[unsat['t'] == t]['z'], unsat.loc[unsat['t'] == t]['v'])
    plt.xlim(0,xlim)
    plt.xlabel('Długość kanału [mm]')

    plt.ylim(0,ymax*1.01)
    plt.ylabel('Prędkość [m/s]')
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    
    plt.savefig('gif/' + 't=' +str(t)+'.png', 
                    transparent = False,  
                    facecolor = 'white'
                   )
    plt.close()

if False:
    for t in times:
        create_frame(t)
    
    frames = []
    for t in times:
        image = imageio.imread('gif/' + 't=' +str(t) + '.png')
        frames.append(image)
    
    imageio.mimsave('przebieg_predkosci.gif',  # output gif
                    frames,                     # array of input frames
                    fps = 10,                   # optional: frames per second
                    loop = 1)                  


#test
t = 0.9039999999999999
vmax = max(unsat['v'])
f = plt.figure(figsize=(12,6))
f.suptitle('Przebieg prędkości wzdłuż kanału, t = '+str(round(t,4)), fontsize=12)

plt.plot(unsat.loc[unsat['t'] == t]['z'], unsat.loc[unsat['t'] == t]['v'], label = 't= ' + str(t))
plt.xlim(0,xlim)
plt.xlabel('Długość kanału [mm]')

plt.ylim(0.99*ymin,ymax*1.01)
plt.ylabel('Prędkość [m/s]')

plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

plt.show()


vmax    = max(unsat['v'])
pmin    = min(unsat['p'])
pmax    = max(unsat['p'])
rhomin  = min(unsat['rho'])
rhomax  = max(unsat['rho'])
xmin    = min(unsat['x'])
xmax    = max(unsat['x'])


def create_frame(t):
    
# -------- multiplot -----------
    f = plt.figure(figsize=(12,6))
    f.suptitle('t=' + str(round(t,4))+' [ms]' , fontsize=12)
    ax = f.add_subplot(221)
    ax.title.set_text('Nadciśnienie')
    ax.set_xlabel('Czas [ms]')
    ax.set_xlim(0,100)
    ax.set_ylabel('Nadciśnienie [Pa]')
    ax.set_ylim(0.99*pmin, 1.01*pmax)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    
    
    ax2 =f.add_subplot(222)
    ax2.title.set_text('Prędkość')
    ax2.set_xlabel('Czas [ms]')
    ax2.set_xlim(0,100)
    ax2.set_ylabel('Prędkość [m/s]')
    ax2.set_ylim(0, 1.01*vmax)
    ax2.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    
    ax3 =f.add_subplot(223)
    ax3.title.set_text('Masowy stopień suchości')
    ax3.set_xlabel('Czas [ms]')
    ax3.set_xlim(0,100)
    ax3.set_ylabel('Stopień suchości [kg/kg]')
    ax3.set_ylim(-0.05, -0.04994)
    ax3.tick_params(axis = 'y', labelrotation = 30)
    ax3.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    
    
    ax4 =f.add_subplot(224)
    ax4.title.set_text('Gęstość')
    ax4.set_xlabel('Czas [ms]')
    ax4.set_xlim(0,100)
    ax4.set_ylabel('Gęstość [kg/m3]')
    ax4.set_ylim(1004, 1010)
    ax4.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    
    ax.plot(unsat.loc[unsat['t'] == t]['z'], unsat.loc[unsat['t'] == t]['p'],    'b')
    ax2.plot(unsat.loc[unsat['t'] == t]['z'], unsat.loc[unsat['t'] == t]['v'],   'g')
    ax3.plot(unsat.loc[unsat['t'] == t]['z'], unsat.loc[unsat['t'] == t]['x'],   'r' )
    ax4.plot(unsat.loc[unsat['t'] == t]['z'], unsat.loc[unsat['t'] == t]['rho'], 'k' )
    
    plt.tight_layout()
    plt.savefig('gif/' + 't=' +str(t)+'.png', 
                    transparent = False,  
                    facecolor = 'white'
                   )
    plt.close()

if True:
    for t in times:
        create_frame(t)
    
    frames = []
    for t in times:
        image = imageio.imread('gif/' + 't=' +str(t) + '.png')
        frames.append(image)
    
    imageio.mimsave('multiplot.gif',  # output gif
                    frames,                     # array of input frames
                    fps = 10,                   # optional: frames per second
                    loop = 1)                  


f = plt.figure(figsize=(12,6))
f.suptitle('t=' + str(round(t,4))+'[ms]' , fontsize=12)
ax = f.add_subplot(221)
ax.title.set_text('Nadciśnienie')
ax.set_xlabel('Czas [ms]')
ax.set_xlim(0,100)
ax.set_ylabel('Nadciśnienie [Pa]')
ax.set_ylim(0.99*pmin, 1.01*pmax)
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)


ax2 =f.add_subplot(222)
ax2.title.set_text('Prędkość')
ax2.set_xlabel('Czas [ms]')
ax2.set_xlim(0,100)
ax2.set_ylabel('Prędkość [m/s]')
ax2.set_ylim(0, 1.01*vmax)
ax2.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

ax3 =f.add_subplot(223)
ax3.title.set_text('Masowy stopień suchości')
ax3.set_xlabel('Czas [ms]')
ax3.set_xlim(0,100)
ax3.set_ylabel('Stopień suchości [kg/kg]')
ax3.set_ylim(-0.05, -0.04994)
ax3.tick_params(axis = 'y', labelrotation = 30)
ax3.grid(color = 'gray', linestyle = '--', linewidth = 0.5)


ax4 =f.add_subplot(224)
ax4.title.set_text('Gęstość')
ax4.set_xlabel('Czas [ms]')
ax4.set_xlim(0,100)
ax4.set_ylabel('Gęstość [kg/m3]')
ax4.set_ylim(0.999*rhomin, 1.001*rhomax)
ax4.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

ax.plot(unsat.loc[unsat['t'] == t]['z'], unsat.loc[unsat['t'] == t]['p'],    'b')
ax2.plot(unsat.loc[unsat['t'] == t]['z'], unsat.loc[unsat['t'] == t]['v'],   'g')
ax3.plot(unsat.loc[unsat['t'] == t]['z'], unsat.loc[unsat['t'] == t]['x'],   'r' )
ax4.plot(unsat.loc[unsat['t'] == t]['z'], unsat.loc[unsat['t'] == t]['rho'], 'k' )

plt.tight_layout()
plt.show()

