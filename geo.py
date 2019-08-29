import fiona
import geopandas as gpd
import csv

gdf = gpd.read_file('output_ana_matopiba.shp')
polygons = gdf.geometry
# print(polygons)
newfile = open("output_ana_matopiba_coordenadas.csv", 'w+')
output = []
output.append("Long,Lat"+"\n")
for polygon in polygons:
    output.append(str(polygon.centroid.x) + "," + str(polygon.centroid.y) + "\n")

newfile.writelines(output)
newfile.close()
