import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import glob, os
from pandas.plotting import parallel_coordinates
import statistics
import pandas as pd


data = pd.read_csv('series.csv')
coordenadas = pd.read_csv('output_coordenadas.csv')
data = data/10000
desvio= []

for i in range(len(data['2017-02-02'])):
    desvio.append(np.sqrt(data.loc[i].var()))

data['desvio'] = desvio
# data['lat'] = coordenadas['Lat ']
# data['long'] = coordenadas[' Long']

for i in range(len(data['2017-02-02'])):
    if(desvio[i]>0.28):
        plt.plot(data.loc[i])

f,ax = plt.subplots(figsize = (10, 10))
sns.heatmap(data.corr(), annot = True, linewidths = .2, fmt = '.2f')
plt.show()

# for i in range(len(data['2017-02-02'])):
#     if(desvio[i]<0.20):
#         plt.plot(data.loc[i])

teste = data[data['desvio']>0.28]
print(len(teste))

for i in teste:
    print(i)

