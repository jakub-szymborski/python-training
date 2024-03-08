# Loading libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

nazwa = 'wyniki-w-czasie'
roz = '.dta'
case = 'wykresy'
folder = 'wykresy/'
wyniki = pd.read_csv(nazwa+roz, sep ='       ', header =None, engine = 'python')

wyniki_2 = pd.read_csv('wyniki_1s_v_grid_100.dta', sep ='       ', header =None, engine = 'python')
wyniki_2[0] = wyniki_2[0]*1000 # konwersja z m na mm 
wyniki_2[1] = wyniki_2[1]*1000 # konwersja z s na ms 

wyniki_3= pd.read_csv('wyniki_1s_v_grid-400.dta', sep ='       ', header =None, engine = 'python')
wyniki_3[0] = wyniki_3[0]*1000 # konwersja z m na mm 
wyniki_3[1] = wyniki_3[1]*1000 # konwersja z s na ms 


wyniki[0] = wyniki[0]*1000 # konwersja z m na mm 
wyniki[1] = wyniki[1]*1000 # konwersja z s na ms 

wyniki_wszystkie = wyniki
# ustawianie przerzedzania danych 
n_chciana = 50000      # pozadana liczba punktow 
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

# ----------------W Y K R E S Y  2 D ----------------------------

z1 = 0.2 # uwaga, trzeba wybrac wsp. z taka, ktora faktycznie jest w wynikach (dokladnie)
z2 = 4.2
z3 = 7.4 

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

wyniki_2_pkt_2 = wyniki_2[wyniki_2[0]==z2]
wyniki_3_pkt_2 = wyniki_3[wyniki_3[0]==4.2]


xmin = 0
xmax = 600
# p
plt.suptitle('Wartosci w punktach: ' + str(z1)+ ', ' + str(z2)+ ', ' + str(z3))
plt.subplot(2,2,1)
plt.xlim(xmin,xmax)
plt.plot(pkt_1[1],pkt_1[2], 'b', label = 'Inlet')     #pkt 1
plt.plot(pkt_2[1],pkt_2[2], 'g', label = 'Mid')       #pkt 2
plt.plot(pkt_3[1],pkt_3[2], 'r', label = 'Outlet')    #pkt 3
plt.xlabel('Czas [ms]')
plt.ylabel('Cisnienie [bar]')

#V
plt.subplot(2,2,2)
plt.xlim(xmin,xmax)
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
plt.plot(pkt_1[1], pkt_1[3], 'b')
plt.plot(pkt_2[1], pkt_2[3], 'g')
plt.plot(pkt_3[1], pkt_3[3], 'r')
plt.xlabel('Czas [ms]')
plt.ylabel('Energia [kJ/kg')

plt.figlegend(loc = 'lower center', ncol =3)
plt.show()


#---------------- wyniki dla roznych v grid
plt.suptitle('Wartosci w punktacie: ' + str(z2))
plt.subplot(2,2,1)
plt.xlim(xmin,xmax)
plt.ylim(9.999,10.002)
plt.plot(pkt_2[1],pkt_2[2], 'g', label = 'V_grid = 400*')       #pkt 2
plt.plot(wyniki_2_pkt_2[1],wyniki_2_pkt_2[2], 'r', label = 'V_grid = 100')    
plt.plot(wyniki_3_pkt_2[1],wyniki_3_pkt_2[2], 'b', label = 'V_grid = 400')    
plt.xlabel('Czas [ms]')
plt.ylabel('Cisnienie [bar]')

#V
plt.subplot(2,2,2)
plt.xlim(xmin,xmax)
plt.plot(pkt_2[1],pkt_2[4], 'g')
plt.plot(wyniki_2_pkt_2[1],wyniki_2_pkt_2[4], 'r')
plt.plot(wyniki_3_pkt_2[1],wyniki_3_pkt_2[4], 'b')
plt.xlabel('Czas [ms]')
plt.ylabel('Predkosc [m/s]')

# T
plt.subplot(2,2,3)
plt.xlim(xmin,xmax)
plt.plot(pkt_2[1], pkt_2[5], 'g')
plt.plot(wyniki_2_pkt_2[1], wyniki_2_pkt_2[5], 'r')
plt.plot(wyniki_3_pkt_2[1], wyniki_3_pkt_2[5], 'b')
plt.xlabel('Czas [ms]')
plt.ylabel('Temperatura [K]')

# energia wew
plt.subplot(2,2,4)
plt.xlim(xmin,xmax)
plt.plot(pkt_2[1], pkt_2[3], 'g')
plt.plot(wyniki_2_pkt_2[1], wyniki_2_pkt_2[3], 'r')
plt.plot(wyniki_3_pkt_2[1], wyniki_3_pkt_2[3], 'b')
plt.xlabel('Czas [ms]')
plt.ylabel('Energia [kJ/kg')

plt.figlegend(loc = 'lower center', ncol =3)
plt.show()



# --------------- W Y K R E S Y  3 D  MatPlotLib-------------------------


#surf = ax.plot3D(t,z,p)       # linie w 3D, wymaga danych 1D
#surf = plt.contour(x,y,p)     # standardowy wykres 3D, wymaga danych 2D i kwadratowej siatki 

# Wykres predkosci przeplywu (czas,polozenie)
fig = plt.figure()
ax = fig.gca(projection = '3d')

surf = ax.plot_trisurf(t,z,w)  # wykres 3D, powierzchnia z triangulacji punktow
#ax.scatter(t,z,w)             # punkty w 3D, wymaga danych 1D
ax.set_xlabel('Czas[ms]')
ax.set_ylabel('Odleglosc [mm]')
ax.set_zlabel('Predkosc [m/s]')
plt.title('Predkosc przeplywu')
plt.tight_layout()
plt.savefig(folder+case+'predkosc'+ '.png')
plt.show()

# Wykres cisnienie(czas,polozenie)
fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_trisurf(t[0:300],z[0:300],p, cmap='viridis', linewidth = 0)  # wykres 3D, powierzchnia z triangulacji punktow
#ax.scatter(t,z,p)             # punkty w 3D, wymaga danych 1D
ax.set_xlabel('Czas[ms]')
ax.set_ylabel('Odleglosc [mm]')
ax.set_zlabel('Cisnienie [bar]')
plt.title('Cisnienie')
plt.tight_layout()
plt.savefig(folder+case+'cisnienie'+ '.png')
plt.show()   

if False:

     

    # Wykres temperatury (czas,polozenie)
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    surf = ax.plot_trisurf(t,z,T)  # wykres 3D, powierzchnia z triangulacji punktow
    #ax.scatter(t,z,T)             # punkty w 3D, wymaga danych 1D
    ax.set_xlabel('Czas[ms]')
    ax.set_ylabel('Odleglosc [mm]')
    ax.set_zlabel('Temperatura [K]')
    plt.title('Temperatura')
    plt.tight_layout()
    plt.savefig(folder+case+'Temperatura'+ '.png')
    plt.show()
    
    
    # Wykres gestosci (czas,polozenie)
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    
    surf = ax.plot_trisurf(t,z,rho)  # wykres 3D, powierzchnia z triangulacji punktow
    #ax.scatter(t,z,rho)             # punkty w 3D, wymaga danych 1D
    ax.set_xlabel('Czas[ms]')
    ax.set_ylabel('Odleglosc [mm]')
    ax.set_zlabel('Gestosc [kg/m3]')
    plt.title('Gestosc')
    plt.tight_layout()
    plt.savefig(folder+case+'Gestosc'+ '.png')
    plt.show()
    
# ---------------------------------------------------------------