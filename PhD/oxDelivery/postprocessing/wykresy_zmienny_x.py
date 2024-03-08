# Loading libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

case = 'wykresy'
folder = 'wykresy/'
#wyniki = pd.read_csv(nazwa+roz, sep ='       ', header =None, engine = 'python')

#wyniki = np.loadtxt('wyniki.dta')
wyniki = np.loadtxt('part3/cas3/wyniki.dta')
wyniki = pd.DataFrame(wyniki)

tlum_1 = np.loadtxt('part3/cas3/wyniki.dta')
tlum_2 = np.loadtxt('part3/cas4/wyniki.dta')
#tlum_3 = np.loadtxt('wyniki-tlumienie/cas3/wyniki.dta')

tlum_1 = pd.DataFrame(tlum_1)
tlum_2 = pd.DataFrame(tlum_2)
#tlum_3 = pd.DataFrame(tlum_3)

tlum_1[0] = tlum_1[0]*1000
tlum_1[1] = tlum_1[1]*1000
tlum_2[0] = tlum_2[0]*1000
tlum_2[1] = tlum_2[1]*1000
#tlum_3[0] = tlum_3[0]*1000
#tlum_3[1] = tlum_3[1]*1000

t1 = 600.0

tlum_1_t1 = tlum_1[tlum_1[1]==t1]
tlum_2_t1 = tlum_2[tlum_2[1]==t1]
#tlum_3_pkt1 = tlum_3[tlum_3[0]==0.2]


wyniki[0] = wyniki[0]*1000 # konwersja z m na mm 
wyniki[1] = wyniki[1]*1000 # konwersja z s na ms 

wyniki_wszystkie = wyniki
# ustawianie przerzedzania danych 
n_chciana = 10000      # pozadana liczba punktow 
n = len(wyniki[0])    # aktualna liczba elementow 

if (n_chciana >=n):
    dzielnik = int(1)
else:
    dzielnik = int (n/n_chciana)

wyniki = wyniki[0::dzielnik]   

#p = wyniki[[1,0,2]].pivot(index = 1, columns = 0, values = 2)  # macierz 2x2, z,t,p
z = wyniki[0]
t = wyniki[1]
p= wyniki[2]     # jedna kolumna 
u = wyniki[3]
w = wyniki[4]
T = wyniki[5]
rho = wyniki[6]
x = wyniki[7]
a = wyniki[8]


# statystyki 

print('Predkosc max:', wyniki[4].max())
print('Czas max:', wyniki[1].max())


# ----------------W Y K R E S Y  2 D ----------------------------

t1 = 655.84
t2 = 655.88
t3 = 655.96

# 0 - wsp. wzlud
# 1 - czas
# 2 - cisnienie
# 3 - energia wew
# 4 - predkosc 
# 5 - temperatura 
# 6 - gestosc 
# 7 - stopien suchosci 
# 8 - pr. dzwieku 

pkt_1 = wyniki_wszystkie[wyniki_wszystkie[1]==t1]
pkt_2 = wyniki_wszystkie[wyniki_wszystkie[1]==t2]
pkt_3 = wyniki_wszystkie[wyniki_wszystkie[1]==t3]


# p
plt.figure()
plt.suptitle('Wartosci w czasie: ' + str(t1)+ ', ' + str(t2)+ ', ' + str(t3) + ' ms')
plt.subplot(2,2,1)
#plt.xlim(25,xmax)
#plt.ylim(9.8,10.5)
plt.plot(pkt_1[0],pkt_1[2], 'b', label = 't1')     #pkt 1
plt.plot(pkt_2[0],pkt_2[2], 'g', label = 't2')       #pkt 2
plt.plot(pkt_3[0],pkt_3[2], 'r', label = 't3')    #pkt 3
plt.xlabel('Odlegosc [mm]')
plt.ylabel('Cisnienie [bar]')

#V
plt.subplot(2,2,2)
plt.plot(pkt_1[0],pkt_1[4]/pkt_1[8], 'b')
plt.plot(pkt_2[0],pkt_2[4]/pkt_2[8], 'g')
plt.plot(pkt_3[0],pkt_3[4]/pkt_3[8], 'r')
plt.xlabel('Odlegosc [mm]')
plt.ylabel('Liczba Macha [-]')

# T
plt.subplot(2,2,3)
plt.plot(pkt_1[0], pkt_1[8], 'b')
plt.plot(pkt_2[0], pkt_2[8], 'g')
plt.plot(pkt_3[0], pkt_3[8], 'r')
plt.xlabel('Odlegosc [mm]')
plt.ylabel('Predkosc dzwieku [m/s]')

# rho
plt.subplot(2,2,4)
plt.plot(pkt_1[0], pkt_1[3], 'b')
plt.plot(pkt_2[0], pkt_2[3], 'g')
plt.plot(pkt_3[0], pkt_3[3], 'r')
plt.xlabel('Odlegosc [mm]')
plt.ylabel('Energia [kJ/kg')

plt.figlegend(loc = 'lower center', ncol =3)
plt.show()


# porownanie 2 case'ow
plt.figure()
plt.plot(tlum_1_t1[0], tlum_1_t1[2], 'b',label = 'tarcie 0.1' )
plt.plot(tlum_2_t1[0], tlum_2_t1[2], 'r',label = 'tarcie 0.008' )
#plt.plot(tlum_3_pkt1[1], tlum_3_pkt1[2], 'g',label = 'add_visc = 10' )
#plt.xlim(xmin,10)
#plt.ylim(9.99,10.08)
plt.xlabel('Odlegosc [mm]')
plt.ylabel('Cisnienie [bar]')
plt.tight_layout()
plt.figlegend(loc = 'lower center', ncol = 3)
plt.show()

"""
# --------------- W Y K R E S Y  3 D  MatPlotLib-------------------------

# Wykres cisnienie(czas,polozenie)
fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_trisurf(t,z,p, cmap='viridis', linewidth = 0)  # wykres 3D, powierzchnia z triangulacji punktow
#ax.scatter(t,z,p)             # punkty w 3D, wymaga danych 1D
ax.set_xlabel('Czas[ms]')
ax.set_ylabel('Odleglosc [mm]')
ax.set_zlabel('Cisnienie [bar]')
plt.title('Cisnienie')
plt.tight_layout()
plt.savefig(folder+case+'cisnienie'+ '.png')
plt.show()   
"""
