import fiona
import geopandas as gpd
import numpy as np
from scipy.spatial import distance
from shapely.geometry import shape, mapping, Point, Polygon
import pandas as pd

def pontoMedio(borda,centroid):
    x = []
    y = []
    x.append(float(borda[0]))
    x.append(float(centroid.x))
    y.append(float(borda[1]))
    y.append(float(centroid.y))

    distancia = lambda x,y:float(((x[1]-x[0])**2)+((y[1]-y[0])**2))**0.5
    xm = lambda x:(x[0]+x[1])/2
    ym = lambda y:(y[0]+y[1])/2
    pm = Point(xm(x),ym(y))
    return pm

gdf = gpd.read_file('C:/Users/Camila/Desktop/pivos/v2/PivosMatopibaMergedV2.shp')
polygons = gdf.geometry

points = pd.read_csv('dpv2_025.csv')

print(points)
coords = [list(poly.exterior.coords) for poly in polygons]

with fiona.open('C:/Users/Camila/Desktop/pivos/v2/PivosMatopibaMergedV2.shp') as src:
    meta = src.meta
    meta['schema']['geometry'] = 'Point'
    with fiona.open('outputdpv2_025.shp', 'w', **meta) as dst:
        i=0
        for f in src:
            pm = Point(points["long"][i],points["lat"][i])
            f['geometry'] = mapping(pm)
            dst.write(f)
            i += 1
            print(i)