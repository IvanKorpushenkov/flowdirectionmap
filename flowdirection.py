import os, math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

os.chdir('/home/roizmsu/FLOW')

def fileReading(name):

    dim = []
    file = open(name, 'r')
    for line in file:
        dim.append(float(line))

    return dim

def numToDegrees(types, file):

    if types == 'lon':
        Lon_deg = []
        i = 0
        while i < len(file):
            if file[i] == 1:
                lon_deg = -180
                Lon_deg.append(lon_deg)
                i += 1
                continue
            elif file[i] == 720:
                lon_deg = 180
                Lon_deg.append(lon_deg)
                i += 1
                continue
            lon_deg += 0.5
            Lon_deg.append(lon_deg)
            i += 1
        outFile = Lon_deg
    elif types == 'lat':
        Lat_deg = []
        i = 0
        while i < len(file):
            if file[i] == 1:
                lat_deg = -90
                lat_deg0 = lat_deg
                Lat_deg.append(lat_deg)
                i += 1
                continue
            elif file[i] == 360:
                lat_deg = 90
                Lat_deg.append(lat_deg)
                i += 1
                continue
            if i > 0:
                if file[i] != 1 or file[i] != 360:
                    lat_deg = lat_deg0 + 0.5
                    Lat_deg.append(lat_deg)
                    i += 1
                    if file[i] != file[i-1]:
                        lat_deg0 = lat_deg
                        lat_deg = lat_deg0 + 0.5
                        Lat_deg.append(lat_deg)
                        i += 1
                        continue
                    continue
        outFile = Lat_deg


    return outFile


#1.data_processing
Lon = fileReading('lon.txt')
Lat = fileReading('lat.txt')
nextx = fileReading('nextx.txt')
nexty = fileReading('nexty.txt')


Lon_deg = numToDegrees('lon', Lon)
Lat_deg = numToDegrees('lat', Lat)

lonGrids = {}
i = 0
while i < 720:
    lonGrids[Lon[i]] = Lon_deg[i]
    i += 1

latGrids = {}
i = 0
while i < len(Lat):
    if i % 720 == 0:
        latGrids[Lat[i]] = Lat_deg[i]
    i += 1

print(latGrids)


#2.Map vizualization

# General map information
#map = Basemap(lat_0=-90,
#              lon_0=0,
#              llcrnrlat=54, #lat of South-west
#              llcrnrlon=104, #lon of south-west
#              urcrnrlat=74, #lat of North-east
#              urcrnrlon=133, #lon of north-east
#              resolution='i')

#map.shadedrelief()
#map.drawcoastlines()
#map.drawcountries()
#map.drawrivers(color='red')


# Draw parallels
#parallels = np.arange(-90, 90, 0.5)
#map.drawparallels(parallels,
#                  linewidth=0.2,
#                  dashes=[0.1, 0],
#                  labels=[True, False, False, False])

# Draw meridinas
#meridians = np.arange(-180, 180, 0.5)
#map.drawmeridians(meridians,
#                  linewidth=0.2,
#                  dashes=[0.1, 0],
#                  labels=[False, False, False, True])
