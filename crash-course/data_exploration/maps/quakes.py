# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:52:07 2024

@author: Kuba
"""

import json 
import pandas as pd

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import plotly.express as px
import plotly.io as pio

pio.renderers.default='browser' # render plotly plots in browser, in spyder plots dont work :( 

path = 'data/'
filename = 'eq_data_1_day_m1.json'

with open(path+ filename) as f:
    eq_data = json.load(f)
    
features = eq_data['features']

quakes =pd.DataFrame(columns = ['id', 'long','lat', 'depth', 'mag', 'time'])

for i in range(len(eq_data['features'])):
    id_     = features[i]['id']
    
    long_   = features[i]['geometry']['coordinates'][0]
    lat_    = features[i]['geometry']['coordinates'][1]
    depth_  = features[i]['geometry']['coordinates'][2]

    mag_    = features[i]['properties']['mag']
    time_   = features[i]['properties']['time']
   
    new_row = {'id':id_,'long':long_,'lat':lat_,'depth':depth_,'mag':mag_,'time':time_}
    quakes.loc[i] = new_row
 
# convert time from (ms since Epoch) into datetime 
quakes['time'] = pd.to_datetime(quakes['time'], unit='ms')

quakes['depth text'] = 'Depth = ' + quakes['depth'].astype(str) + 'km'


# # Map the earthquakes:  plot per crash course 
data = [{
    'type': 'scattergeo',
    'lon': quakes['long'],
    'lat': quakes['lat'],
    'text': quakes['depth text'],
    'marker': {
        'size': [5*mag for mag in quakes['mag']],
        'color': quakes['depth'],
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Quake depth [km]'},
    },
}]

my_layout = Layout(title='Global Earthquakes, dot size: magnitude, dot color: depth')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')


# plots with plotly express
fig2 = px.scatter_geo(lon = quakes['long'], lat = quakes['lat'], size = quakes['mag'], 
               color = quakes['depth'], color_continuous_scale='Viridis_r', 
               hover_name  = quakes['depth text'],
               title = 'Global Earthquakes, dot size: magnitude, dot color: depth')
fig2.update_geos(projection_type='natural earth')
#fig.update_geos(projection_type="orthographic") # a sphere 

fig2.show()

