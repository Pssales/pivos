import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

arquivos = ["bahia", "piaui","tocantins", "maranhao"]
for arquivo in arquivos:
    print(arquivo)
    ana = gpd.read_file("C:/Users/Camila/Desktop/pivos/ana/matopiba_"+arquivo+".shp", encoding="utf-8")
    detectados = gpd.read_file("C:/Users/Camila/Desktop/pivos/output_amp_v2ok_"+arquivo+".shp", encoding="utf-8")

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
    print("\n\n")
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





# # média
# bahia
# 678
# 590
# 0.8702064896755162



# piaui
# 30
# 4
# 0.13333333333333333



# tocantins
# 502
# 9
# 0.017928286852589643



# maranhao
# 719
# 22
# 0.030598052851182198

# média -0.1


# bahia
# 775
# 679
# 0.8761290322580645



# piaui
# 60
# 4
# 0.06666666666666667



# tocantins
# 715
# 12
# 0.016783216783216783



# maranhao
# 1201
# 22
# 0.018318068276436304
