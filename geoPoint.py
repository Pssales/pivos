import fiona
import geopandas as gpd
import numpy as np
from scipy.spatial import distance
from shapely.geometry import shape, mapping, Point, Polygon


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

gdf = gpd.read_file('PivosWhitinMatopiba.shp')
polygons = gdf.geometry

coords = [list(poly.exterior.coords) for poly in polygons]

with fiona.open('PivosWhitinMatopiba.shp') as src:
    meta = src.meta
    meta['schema']['geometry'] = 'Point'
    with fiona.open('outputlatlong.shp', 'w', **meta) as dst:
        i=0
        for f in src:
            pm = pontoMedio(coords[i][0],polygons[i].centroid)
            print(pm)
            f['geometry'] = mapping(pm)
            dst.write(f)
            i += 1
            print(i)


