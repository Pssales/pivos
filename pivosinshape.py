import geopandas as gpd
import matplotlib.pyplot as plt

ana = gpd.read_file("matopibashape.shp", encoding="utf-8")
# detectados = gpd.read_file("output_v2pivosmatopibaok.shp", encoding="utf-8")
# detectados = gpd.read_file("output_dpv2ok_017.shp", encoding="utf-8")
# detectados = gpd.read_file("output_dpv2ok_020.shp", encoding="utf-8")
detectados = gpd.read_file("output_dpv2ok_022.shp", encoding="utf-8")
# detectados = gpd.read_file("output_amp_v2ok_060.shp", encoding="utf-8")


import pandas as pd
import numpy as np
regiao_pvos = pd.Series(np.empty((len(detectados)), dtype=bool) )
i = 0

for f in detectados.geometry:
    achou = False
    for p in ana.geometry:
        if(p.contains(f)):
            achou = True 
    regiao_pvos[i] = achou

    i = i + 1
print(len(regiao_pvos))
print(len(regiao_pvos[regiao_pvos == True]))
print(len(regiao_pvos[regiao_pvos == True])/len(regiao_pvos))
# pivos_regiao_2017 = detectados[regiao_pvos]

# base = deimitacao.plot(edgecolor='black', figsize=(5, 5))

# pivos_regiao_2017.plot(ax=base, color='red',  markersize=0.5)
# pivos_regiao_2017.show()


# 3633
# 877
# 0.2413982934214148


# 1520
# 704
# 0.4631578947368421


# 1249
# 659
# 0.5276220976781425


# 1031
# 607
# 0.588748787584869