# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:40:04 2023

@author: Jakub Szymborski
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:31:23 2023

@author: Jakub Szymborski
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'dane\\unsat\\testy_krok_czasowy'

case = '\dp_10_bar_@ 35bar\\'
f1 = 'wyniki_dt_1e-7_dx_1e-3.txt'
f2 = 'wyniki_dt_1e-6_dx_1e-3.txt'
f3 = 'wyniki_dt_1e-5_dx_1e-3.txt'
f4 = 'wyniki_dt_1e-4_dx_1e-3.txt'
f5 = 'wyniki_dt_1e-3_dx_1e-3.txt'

title = 'Predkosc w czasie, ciecz, przekroj L = 50 mm, dp = 10 bar'

dt1 = np.loadtxt(path+case+f1)    # 1e-7
dt2 = np.loadtxt(path+case+f2)    # 1e-6
dt3 = np.loadtxt(path+case+f3)    # 1e-5
dt4 = np.loadtxt(path+case+f4)    # 1e-4
#dt5 = np.loadtxt(path+case+f5)    # 1e-3


dt1 = pd.DataFrame(dt1, columns =['z','t','p','u','v','T','rho','x','xr', 'a'], dtype = 'float')
dt2 = pd.DataFrame(dt2, columns =['z','t','p','u','v','T','rho','x','xr', 'a'], dtype = 'float')
dt3 = pd.DataFrame(dt3, columns =['z','t','p','u','v','T','rho','x','xr', 'a'], dtype = 'float')
dt4 = pd.DataFrame(dt4, columns =['z','t','p','u','v','T','rho','x','xr', 'a'], dtype = 'float')
#dt5 = pd.DataFrame(dt5, columns =['z','t','p','u','v','T','rho','x','xr', 'a'], dtype = 'float')


# konwersja z m na mm 
dt1['z'] = dt1['z']*1e3 
dt2['z'] = dt2['z']*1e3 
dt3['z'] = dt3['z']*1e3 
dt4['z'] = dt4['z']*1e3 
#dt5['z'] = dt5['z']*1e3 

# konwersja z s na ms 
#unsat['t'] = unsat['t']*1e3 
# t_unit = '[ms]'
t_unit = '[s]'

# zamiana z bar na Pa, usuniecie cisnienie odniesienia 
dt1['p'] = dt1['p']*1e5 - 20e5
dt2['p'] = dt2['p']*1e5 - 20e5
dt3['p'] = dt3['p']*1e5 - 20e5
dt4['p'] = dt4['p']*1e5 - 20e5
#dt5['p'] = dt5['p']*1e5 - 20e5

# wybranie konkretnej chwili czasowej 
#unsat_t1 = unsat.loc[unsat[1] == 0.999]

# wybranie konkretnego przekroju 
L1 = 50.0

dt1_L1 = dt1.loc[dt1['z'] == L1]
dt2_L1 = dt2.loc[dt2['z'] == L1]
dt3_L1 = dt3.loc[dt3['z'] == L1]
dt4_L1 = dt4.loc[dt4['z'] == L1]
#dt5_L1 = dt5.loc[dt5['z'] == L1]

# ---- Wykresy ------------
xlim = 1.0

f = plt.figure(figsize=(12,6))
f.suptitle(title, fontsize=12)

plt.plot(dt1_L1['t'], dt1_L1['v'], label = '1e-7')
plt.plot(dt2_L1['t'], dt2_L1['v'], label = '1e-6')
plt.plot(dt3_L1['t'], dt3_L1['v'], label = '1e-5')
plt.plot(dt4_L1['t'], dt4_L1['v'], label = '1e-4')
#plt.plot(dt5_L1['t'], dt5_L1['v'], label = '1e-3')

plt.xlim(0,xlim)
#ax.set_ylim(0,14)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

plt.xlabel('Czas '+t_unit)
plt.ylabel('Predkosc [m/s]')

plt.figlegend( loc = 'lower center', ncol = 7)
#plt.savefig(case+ '_wykres.png',dpi =100, pad_inches =0.4, bbox_inches='tight')
plt.show()


f = plt.figure(figsize=(12,6))
f.suptitle(title, fontsize=12)
ax = f.add_subplot(231)
ax.title.set_text('dt = 1e-7')

ax2 =f.add_subplot(232)
ax2.title.set_text('dt = 1e-6')

ax3 =f.add_subplot(233)
ax3.title.set_text('dt = 1e-5')

ax4 =f.add_subplot(234)
ax4.title.set_text('dt = 1e-4')

#ax5 =f.add_subplot(235)
#ax5.title.set_text('dt = 1e-3')


ax.plot(dt1_L1['t'], dt1_L1['v'], label = '1e-7')
ax2.plot(dt2_L1['t'], dt2_L1['v'], label = '1e-6')
ax3.plot(dt3_L1['t'], dt3_L1['v'], label = '1e-5')
ax4.plot(dt4_L1['t'], dt4_L1['v'], label = '1e-4')
#ax5.plot(dt5_L1['t'], dt5_L1['v'], label = '1e-3')
plt.tight_layout()
plt.subplots_adjust(top=0.92) 
plt.show()