import fiona
from shapely.geometry import shape, mapping

with fiona.open('pivos.shp') as src:
    meta = src.meta
    meta['schema']['geometry'] = 'Point'
    with fiona.open('output_shapefile.csv', 'w', **meta) as dst:
        for f in src:
            centroid = shape(f['geometry']).centroid
            dst.write(str(centroid.x) + " "+  str(centroid.y) )