# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:31:23 2023

@author: Jakub Szymborski
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path_unsat = 'dane/unsat/'
path_sat = 'dane/sat/'

case = 'wyniki_dp_1kk_3s'
title = 'Wyniki w czasie, przekroj L = 50 mm, dp = 1 MPa'
# case'y: 
# sat: wyniki_dp_100_3s.txt, wyniki_dp_400_3s.txt, wyniki_dp_4k_3s.txt, wyniki_dp_40k_3s.txt, wyniki_dp_100k_3s.txt
# unsat: wyniki_dp_100_3s.txt, wyniki_dp_400_3s.txt, wyniki_dp_4k_3s.txt, wyniki_dp_40k_3s.txt, wyniki_dp_100k_3s.txt, wyniki_dp_500k_3s.txt, wyniki_dp_1kk_3s.txt

unsat = np.loadtxt(path_unsat+case+'.txt')             
unsat = pd.DataFrame(unsat, columns =['z','t','p','u','v','T','rho','x','xr'], dtype = 'float')

#sat = np.loadtxt(path_sat + case+'.dta')    
sat = np.loadtxt(path_sat + 'dummy.txt')    
sat = pd.DataFrame(sat,columns =['z','t','p','u','v','T','rho','x','xr'],  dtype = 'float')

# konwersja z m na mm 
sat['z'] = sat['z']*1e3
unsat['z'] = unsat['z']*1e3 

# konwersja z s na ms 
#unsat['t']  = unsat['t']*1e3
#sat['t']    = sat['t']*1e3

# zamiana z bar na Pa, usuniecie cisnienie odniesienia 
sat['p'] = sat['p']*1e5 - 20e5 
unsat['p'] = unsat['p']*1e5 - 20e5

# wybranie konkretnej chwili czasowej 
#unsat_t1 = unsat.loc[unsat[1] == 0.999]

# wybranie konkretnego przekroju 
L1 = 50.0

unsat_L1 = unsat.loc[unsat['z'] == L1]
sat_L1   = sat.loc[sat['z'] == L1 ]


# ---- Wykresy ------------

f = plt.figure(figsize=(12,6))
f.suptitle(title, fontsize=12)
ax = f.add_subplot(121)

#ax.plot(sat_L1['t'], sat_L1['p'], 'c', label = 'p_sat')
ax.plot(unsat_L1['t'], unsat_L1['p'], 'm', label = 'p_unsat')

#ax.set_xlim(0,xlim)
#ax.set_ylim(0,14)
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

ax.set_xlabel('Czas [s]')
#ax.set_ylabel('Prędkość średnia [m/s]')
ax.set_ylabel('Cisnienie [Pa]')

ax2 = f.add_subplot(122)
#ax2.plot(sat_L1['t'], sat_L1['v'], 'c', label = 'V_sat')
ax2.plot(unsat_L1['t'], unsat_L1['v'], 'm', label = 'V_unsat')

ax2.set_xlabel('Czas [s]')
ax2.set_ylabel('Predkosc [m/s]')
  #  ax2.set_xlim(0,xlim)
#ax2.set_ylim(0, 2000)
ax2.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.05,
                 box.width, box.height * 0.95])
box = ax2.get_position()
ax2.set_position([box.x0, box.y0 + box.height * 0.05,
                 box.width, box.height * 0.95])
     
plt.figlegend( loc = 'lower center', ncol = 7)
plt.savefig('dane/wykresy/relax-vs-no-relax/' + case+ '_wykres.png',dpi =100, pad_inches =0.4, bbox_inches='tight')

plt.show()