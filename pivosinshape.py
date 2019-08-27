import geopandas as gpd
import matplotlib.pyplot as plt

deimitacao = gpd.read_file("outputdpv2_025.shp", encoding="utf-8")
pivos_ana = gpd.read_file("matopibashape.shp", encoding="utf-8")


import pandas as pd
import numpy as np
regiao_pvos = pd.Series(np.empty((len(pivos_ana)), dtype=bool) )
i = 0

for f in pivos_ana.geometry:
    regiao_pvos[i] = pivos_ana.contains(f).values[0]
    i = i + 1
print(len(regiao_pvos))
print(len(regiao_pvos[regiao_pvos == True]))
# pivos_regiao_2017 = pivos_ana[regiao_pvos]

# base = deimitacao.plot(edgecolor='black', figsize=(5, 5))

# pivos_regiao_2017.plot(ax=base, color='red',  markersize=0.5)
# pivos_regiao_2017.show()