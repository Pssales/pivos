import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import glob, os
from pandas.plotting import parallel_coordinates
import statistics
import pandas as pd


data = pd.read_csv('serie_output_ana_matopiba_coordenadas.csv')
coordenadas = pd.read_csv('output_ana_matopiba_coordenadas.csv')
data = data/10000
desvio= []
amplitude= []

for i in range(len(data['2017-12-03'])):
    desvio.append(data.loc[i].std())
    amplitude.append(data.loc[i].max() - data.loc[i].min())

# f,ax = plt.subplots(figsize = (10, 10))
# sns.heatmap(data.corr(), annot = True, linewidths = .2, fmt = '.2f')
# h=0
# for i in range(len(data['2018-01-17'])):
#     if(amplitude[i] > 0.50):
#         plt.plot(data.loc[i])
#         h+=1
# plt.show()

# print(h)


# h=0
# for i in range(len(data['2018-01-17'])):
#     if(amplitude[i] > 0.60):
#         plt.plot(data.loc[i])
#         h+=1
# plt.show()
# print(h)

# h=0
# for i in range(len(data['2018-01-17'])):
#     if(amplitude[i] > 0.70):
#         plt.plot(data.loc[i])
#         h+=1
# plt.show()
# print(h)


# for i in range(len(data['2018-01-17'])):
#     if(desvio[i] > 0.20):
#         plt.plot(data.loc[i])
# plt.show()

# for i in range(len(data['2018-01-17'])):
#     if(desvio[i] > 0.22):
#         plt.plot(data.loc[i])
# plt.show()

data['desvio'] = desvio
data['amplitude'] = amplitude
print("Desvio:")
print(data['desvio'].mean())
print("Amplitude:")
print(data['amplitude'].mean())

print("Amplitde Minima")
print(data['amplitude'].min())

print("Amplitde Maxma")
print(data['amplitude'].max())
plt.plot(data['amplitude'])
plt.show()
# data['lat'] = coordenadas['Lat']
# data['long'] = coordenadas['Long']

# teste = data[data['amplitude']>0.60]
# teste.to_csv('amp_v2ok_060.csv', index=False)

# teste = data[data['desvio']>0.20]
# teste.to_csv('dpv2ok_020.csv', index=False)

# teste = data[data['desvio']>0.22]
# teste.to_csv('dpv2ok_022.csv', index=False)
