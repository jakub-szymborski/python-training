# Loading libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

case = 'wykresy'
folder = 'wykresy/'
#wyniki = pd.read_csv(nazwa+roz, sep ='       ', header =None, engine = 'python')

#wyniki = np.loadtxt('wyniki.dta')
wyniki = np.loadtxt('wyniki.dta')
cfl = np.loadtxt('cfl.dta')

wyniki = pd.DataFrame(wyniki)
cfl = pd.DataFrame(cfl)

tlum_1 = np.loadtxt('part3/cas3/wyniki.dta')
tlum_2 = np.loadtxt('part3/cas3/wyniki.dta')
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


tlum_1_pkt1 = tlum_1[tlum_1[0]==0.2]
tlum_2_pkt1 = tlum_2[tlum_2[0]==0.2]
#tlum_3_pkt1 = tlum_3[tlum_3[0]==0.2]

cfl[0] = cfl[0]*1000    # konwersja m, s na mm, ms 
cfl[1] = cfl[1]*1000

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
max_cfl = cfl[3].max()
print('Liczba Curanta max: ', max_cfl)

print('Predkosc max:', wyniki[4].max())
print('Czas max:', cfl[1].max())


# ----------------W Y K R E S Y  2 D ----------------------------

z1 = 0.2 # uwaga, trzeba wybrac wsp. z taka, ktora faktycznie jest w wynikach (dokladnie)
z2 = 4.2
z3 = 7.8 

# 0 - wsp. wzlud
# 1 - czas
# 2 - cisnienie
# 3 - energia wew
# 4 - predkosc 
# 5 - temperatura 
# 6 - gestosc 
# 7 - stopien suchosci 
# 8 - pr. dzwieku 

pkt_1 = wyniki_wszystkie[wyniki_wszystkie[0]==z1]
pkt_2 = wyniki_wszystkie[wyniki_wszystkie[0]==z2]
pkt_3 = wyniki_wszystkie[wyniki_wszystkie[0]==z3]

xmin = 0
#xmax = (int)(max(wyniki_wszystkie[1]))
xmax = 10

pmax = 1.02*wyniki_wszystkie.loc[wyniki_wszystkie[1]<=xmax].loc[:,2].max()
pmin = 0.98*wyniki_wszystkie.loc[wyniki_wszystkie[1]<=xmax].loc[:,2].min()

vmax = 1.02*wyniki_wszystkie.loc[wyniki_wszystkie[1]<=xmax].loc[:,4].max()
vmin = 0.98*wyniki_wszystkie.loc[wyniki_wszystkie[1]<=xmax].loc[:,4].min()

# p
plt.figure()
plt.suptitle('Wartosci w punktach: ' + str(z1)+ ', ' + str(z2)+ ', ' + str(z3))
plt.subplot(2,2,1)
plt.xlim(xmin,xmax)
plt.ylim(pmin, pmax)
plt.plot(pkt_1[1],pkt_1[2], 'b', label = 'Inlet')     #pkt 1
plt.plot(pkt_2[1],pkt_2[2], 'g', label = 'Mid')       #pkt 2
plt.plot(pkt_3[1],pkt_3[2], 'r', label = 'Outlet')    #pkt 3
plt.xlabel('Czas [ms]')
plt.ylabel('Cisnienie [bar]')

#V
plt.subplot(2,2,2)
plt.xlim(xmin,xmax)
plt.ylim(vmin,vmax)
plt.plot(pkt_1[1],pkt_1[4], 'b')
plt.plot(pkt_2[1],pkt_2[4], 'g')
plt.plot(pkt_3[1],pkt_3[4], 'r')
plt.xlabel('Czas [ms]')
plt.ylabel('Predkosc [m/s]')

# T
plt.subplot(2,2,3)
plt.xlim(xmin,xmax)
plt.plot(pkt_1[1], pkt_1[8], 'b')
plt.plot(pkt_2[1], pkt_2[8], 'g')
plt.plot(pkt_3[1], pkt_3[8], 'r')
plt.xlabel('Czas [ms]')
plt.ylabel('Predkosc dzwieku [m/s]')

# rho
plt.subplot(2,2,4)
plt.xlim(xmin,xmax)
plt.plot(pkt_1[1], pkt_1[6], 'b')
plt.plot(pkt_2[1], pkt_2[6], 'g')
plt.plot(pkt_3[1], pkt_3[6], 'r')
#plt.ylim(85,90)
plt.xlabel('Czas [ms]')
plt.ylabel('Gestosc kg/m3')

plt.figlegend(loc = 'lower center', ncol =3)
plt.show()



# porownanie 2 case'ow
plt.figure()
plt.plot(tlum_1_pkt1[1], tlum_1_pkt1[2], 'b',label = 'tarcie 0.1' )
plt.plot(tlum_2_pkt1[1], tlum_2_pkt1[2], 'r',label = 'tarcie 0.008' )
#plt.plot(tlum_3_pkt1[1], tlum_3_pkt1[2], 'g',label = 'add_visc = 10' )
#plt.xlim(0,10)
#plt.ylim(20.006,20.011)
plt.xlabel('Czas [ms]')
plt.ylabel('Cisnienie [bar]')
plt.tight_layout()
plt.figlegend(loc = 'lower center', ncol = 3)
plt.show()



"""
# predkosc dzwieku i CFL 

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(cfl[1],cfl[2], 'r', label = 'Predkosc dzwieku')
ax2.plot(cfl[1],cfl[3], 'b', label = 'CFL')
plt.xlim(xmin,xmax)
ax1.set_xlabel('Czas [ms]')
ax1.set_ylabel('Predkosc dzwieku [m/s]')
ax2.set_ylabel('CFL')
plt.tight_layout()
plt.figlegend(loc = 'lower center', ncol = 2)
plt.show()


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