# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 16:22:21 2023

@author: Kuba
"""
import numpy as np 
import pandas as pd

path = 'dane/'
names = ['diff_100krokow', 'diff_v0_maly2', 'rownowagowy_100krokow', 'ziemniak']
ext = '.txt'
cols = ['t', 'j', 'p', 'u', 'x', 'v', 'rho', 'xr', 'Mach']
names = [name + ext for name in names]
""" robi to samo co wyzej
for name in range(len(names)):
    names[name] = names[name] + ext
"""    
print(names)

class Results():
    def __init__(self, filename, columns):
        self.filename = filename
        self.columns = columns
        
        filepath = path + self.filename
        try:
            self.data = np.loadtxt(filepath)
            self.data = pd.DataFrame(self.data, columns = self.columns, dtype = 'float')
        except FileNotFoundError:
            print(f" \n {self.filename} not found \n")
            pass

    def rescale(self, var, factor_a,factor_b):
        # rescale given var by multiplying by factor_a / factor_b 
        self.data[var] = self.data[var]*factor_a/factor_b
    
    def dropNans(self):
        self.data.dropna(inplace = True)
        

diff_100 = Results(names[0], cols)
diff_v0_maly = Results(names[1], cols)
rownowagowy_100= Results(names[2], cols)
ziemniak = Results(names[3], cols)

print('dupa')
print(diff_100.data['t'].max())

diff_100.rescale('t', 1000, 1)
print(diff_100.data['t'].max())


print(diff_100.data['p'].max())
diff_100.rescale('p', 1,1e5)
print(diff_100.data['p'].max())

diff_100.rescale('u', 1,1e3)

diff_100.dropNans()

przypadki = (diff_100,diff_v0_maly, rownowagowy_100)
for case in przypadki: 
    case.dropNans()
    case.data.rescale('t', 1000,1)
    case.data.rescale('p', 1,1e5)
    case.data.rescale('u', 1,1e3)



"""
case="testy_stabilnosci/dane/ciecz/3modele/"

path_diff = "diff_1000krokow"
diff = np.loadtxt(case+path_diff + '.txt')   
diff = pd.DataFrame(diff, columns = ['t','j', 'p','u' ,'x','V','rho','xr', 'Mach' ], dtype ='float')

path_nodiff = "rownowagowy_1000krokow"
nodiff = np.loadtxt(case+path_nodiff + '.txt')   
nodiff = pd.DataFrame(nodiff, columns = ['t','j', 'p','u' ,'x','V','rho','xr', 'Mach' ], dtype ='float')



creating mulitple dataframes:
d = {}
for name in companies:
    d[name] = pd.DataFrame()

from: https://python-forum.io/thread-26450-page-2.html
class PythonTraining():    
    def read_data(self, filepath):
        base_path = "D:\Data" 
        full_filepath = os.path.join(base_path, filepath, "outsummary2.csv")      
        self.data = pd.read_csv(full_filepath)
 
    def cal_rowmean(self, v1):         
        self.xmean = self.data['s3'].mean() + v1
        print(self.xmean)
"""