import fiona
import geopandas as gpd
import csv
# arquivos = ["detectados_bahia", "detectados_piaui","detectados_tocantins", "detectados_maranhao"]
# for arquivo in arquivos:
gdf = gpd.read_file('C:/Users/Camila/Desktop/LC8_SRgreenest_pivots_merged_polygon/output_pivos_ok.shp')
polygons = gdf.geometry
# print(polygons)
newfile = open("C:/Users/Camila/Desktop/LC8_SRgreenest_pivots_merged_polygon/output_pivos_ok_coordenadas.csv", 'w+')
output = []
output.append("Long,Lat\n")
i = 0
count = 0
for polygon in polygons:
    output.append(str(polygon.centroid.x) + "," + str(polygon.centroid.y)+"\n")

newfile.writelines(output)
newfile.close()
