import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import glob, os
from pandas.plotting import parallel_coordinates
import statistics
import pandas as pd


data = pd.read_csv('seriesv2.csv')
coordenadas = pd.read_csv('output_coordenadas.csv')
data = data/10000
desvio= []

for i in range(len(data['2017-12-03'])):
    desvio.append(np.sqrt(data.loc[i].var()))

data['desvio'] = desvio
data['lat'] = coordenadas[' Lat']
data['long'] = coordenadas['Long ']

print(data['desvio'].mean())

# f,ax = plt.subplots(figsize = (10, 10))
# sns.heatmap(data.corr(), annot = True, linewidths = .2, fmt = '.2f')
# plt.show()

# for i in range(len(data['2017-02-02'])):
#     if(desvio[i]<0.20):
#         plt.plot(data.loc[i])
print(len(data['desvio']))

# teste = data[data['desvio']<0.33]
# teste.to_csv('dpv2_033.csv', index=False)
# print(len(teste))

# teste = data[data['desvio']>0.16]
# teste = teste[teste['desvio']<0.33]
# print(len(teste))
# teste.to_csv('dpv2_016_33.csv', index=False)

teste = data[data['desvio']>0.25]
teste.to_csv('dpv2_025.csv', index=False)
print(len(teste))
