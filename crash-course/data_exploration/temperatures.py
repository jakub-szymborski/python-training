# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 15:10:40 2024

@author: Kuba
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

file_alaska = 'temperatures\sitka_weather_2018_full.csv'
alaska = pd.read_csv(file_alaska, usecols=(2,3,5, 8, 9), header =0,
                      names =['Date', 'Wind_speed', 'Rainfall', 'Tmax', 'Tmin'] )

file_arizona = 'temperatures\death_valley_2018_full.csv'
arizona = pd.read_csv(file_arizona, usecols=(2,3,6, 7), header =0,
                      names =['Date', 'Rainfall', 'Tmax', 'Tmin'] )
# temperatures: F, rainfall: in

# Alaska
alaska['Date'] = pd.to_datetime(alaska['Date']).dt.date
a_day = pd.DateOffset(2)

fig = plt.figure()
plt.plot(alaska['Date'], alaska['Tmax'], label ='Max temp.', color ='r')
plt.plot(alaska['Date'], alaska['Tmin'], label ='Min temp.', color = 'b')
plt.fill_between(alaska['Date'], alaska['Tmax'],alaska['Tmin'], alpha = 0.2)

plt.title('Daily temperatures at Sitka Airport, Alaska, 2018')
plt.xlabel('Day')
plt.xlim(alaska['Date'].min()-a_day, alaska['Date'].max()+a_day)

plt.ylabel('Temperature [F]')
plt.tick_params(axis ='x', which = 'major')

plt.tight_layout()
fig.legend(ncol = 2, loc = 'lower center')
plt.show()

# Arizona 

arizona['Date'] = pd.to_datetime(arizona['Date']).dt.date

fig2 = plt.figure()
plt.plot(arizona['Date'], arizona['Tmax'], label ='Max temp.', color ='r')
plt.plot(arizona['Date'], arizona['Tmin'], label ='Min temp.', color = 'b')
plt.fill_between(arizona['Date'], arizona['Tmax'],arizona['Tmin'], alpha = 0.2)

plt.title('Daily temperatures at Death Valley, Arizona, 2018')
plt.xlabel('Day')
plt.xlim(arizona['Date'].min()-a_day, arizona['Date'].max()+a_day)

plt.ylabel('Temperature [F]')
plt.tick_params(axis ='x', which = 'major')

plt.tight_layout()
fig2.legend(ncol = 2, loc = 'lower center')
plt.show()


# on a single plot:  
fig3 = plt.figure()
plt.plot(arizona['Date'], arizona['Tmax'], label ='Max temp. Arizona', color ='r')
plt.plot(arizona['Date'], arizona['Tmin'], label ='Min temp. Arizona', color = 'b')
plt.plot(alaska['Date'], alaska['Tmax'], label ='Max temp. Alaska', color ='orange')
plt.plot(alaska['Date'], alaska['Tmin'], label ='Min temp. Alaska', color = 'green')

plt.fill_between(arizona['Date'], arizona['Tmax'],arizona['Tmin'], alpha = 0.2)
plt.fill_between(alaska['Date'], alaska['Tmax'],alaska['Tmin'], alpha = 0.2)

plt.title('Daily temperatures at Death Valley, Arizona, 2018')
plt.xlabel('Day')
plt.xlim(arizona['Date'].min()-a_day, arizona['Date'].max()+a_day)

plt.ylabel('Temperature [F]')
plt.tick_params(axis ='x', which = 'major')

plt.tight_layout()
fig3.legend(ncol = 2, loc = 'lower center')
plt.show()



# cols: date, wind speed, rainfall, Tmax, Tmin  
# awnd - avg. daily wind speed 
# prcp - precipitation 
"""
import csv 

filename = "temperatures\sitka_weather_2018_full.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        
 """