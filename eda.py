import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import glob, os
from pandas.plotting import parallel_coordinates
import statistics
import pandas as pd


data = pd.read_csv('C:/Users/Camila/Desktop/pivos/amp_max.csv')
coordenadas = pd.read_csv('C:/Users/Camila/Desktop/pivos/amp_min.csv')

# data = data/10000
# coordenadas = coordenadas/10000
desvio= []
amplitude= []

# for i in range(len(data['2017-11-01'])):
#     desvio.append(data.loc[i].std())
#     amplitude.append(data.loc[i].max() - data.loc[i].min())


# h=0
for i in range(len(data['2018-01-17'])):
    plt.xlabel('Time')
    plt.ylabel("NDVI")
    plt.plot(data.loc[i],color="green",label="Pivot")
    plt.plot(coordenadas.loc[i],color="red",label="Not Pivot")
    plt.legend(['Pivot', 'Not Pivot'])
    plt.show()

# print(h)


# h=0
# for i in range(len(data['2017-11-01'])):
#     if(amplitude[i] > 0.56):
#         plt.plot(data.loc[i])
#         h+=1
# plt.show()
# print(h)


# h=0
# for i in range(len(data['2017-11-01'])):
#     if(amplitude[i] > 0.56 and desvio[i] > 0.26):
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
# data['desvio'] = desvio
# data['amplitude'] = amplitude
# data['lat'] = coordenadas['Lat']
# data['long'] = coordenadas['Long']


# # print("Amplitde Minima")
# # print(data['amplitude'].min())

# # print("Amplitde Maxima")
# # print(data['amplitude'].max())


# data = data[(data['2017-11-01'] > 0.0 ) & (data['2017-11-17'] > 0.0 ) & (data['2017-12-03'] > 0.0 ) & (data['2017-12-19'] > 0.0 ) & (data['2018-01-01'] > 0.0 ) & (data['2018-01-17'] > 0.0 ) & (data['2018-02-02'] > 0.0 ) & (data['2018-02-18'] > 0.0 ) & (data['2018-03-06'] > 0.0 ) & (data['2018-03-22'] > 0.0 )]

# # print("Desvio:")
# # print(data['desvio'].mean())
# # print("Amplitude média:")
# # print(data['amplitude'].mean())

# # print(len(data['2017-11-01']))

# # teste = data[data['desvio']>0.15]
# # teste.to_csv('desvio_15.csv', index=False)

# teste = data[data['amplitude'] == 0.6322000000000001]
# teste.to_csv('amp_max.csv', index=False)

# teste = data[(data["desvio"] > 0.26)]
# teste.to_csv('des_26.csv', index=False)