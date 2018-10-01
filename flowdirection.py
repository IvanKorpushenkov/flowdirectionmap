import os
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
        Lon_deg[259199] = 179.5
        outFile = Lon_deg
    elif types == 'lat':
        Lat_deg = []
        i = 0
        while i < len(file):
            if file[i] == 1:
                lat_deg = 90
                lat_deg0 = lat_deg
                Lat_deg.append(lat_deg)
                i += 1
                continue
            elif file[i] == 360:
                lat_deg = -90
                Lat_deg.append(lat_deg)
                i += 1
                continue
            if i > 0:
                if file[i] != 1 or file[i] != 360:
                    lat_deg = lat_deg0 - 0.5
                    Lat_deg.append(lat_deg)
                    i += 1
                    if file[i] != file[i-1]:
                        lat_deg0 = lat_deg
                        lat_deg = lat_deg0 - 0.5
                        Lat_deg.append(lat_deg)
                        i += 1
                        continue
                    continue
        outFile = Lat_deg


    return outFile


def toGrid(arr1, arr2, Lon, Lat):

    lonGrids = {}
    i = 0
    while i < 720:
        if i == 719:
            lonGrids[Lon[i]] = 179.5
            i += 1
            continue
        lonGrids[Lon[i]] = Lon_deg[i]
        i += 1

    latGrids = {}
    i = 0
    while i < len(Lat):
        if i % 720 == 0:
            latGrids[Lat[i]] = Lat_deg[i]
        i += 1

    deg = []
    for i in range(len(arr1)):
        if arr2[i] != -9:
            if arr2[i] != -9999:
                deg.append(float(lonGrids.get(arr2[i])))
            elif arr2[i] == -9999:
                deg.append(-9999)
        elif arr2[i] == -9:
            deg.append(float(arr1[i]))

    return deg

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
    if i == 719:
        lonGrids[Lon[i]] = 179.5
        i += 1
        continue
    lonGrids[Lon[i]] = Lon_deg[i]
    i += 1

latGrids = {}
i = 0
while i < len(Lat):
    if i % 720 == 0:
        latGrids[Lat[i]] = Lat_deg[i]
    i += 1

nextx_deg = []
for i in range(len(Lon_deg)):
    if nextx[i] != -9:
        if nextx[i] != -9999:
            nextx_deg.append(float(lonGrids.get(nextx[i])))
        elif nextx[i] == -9999:
            nextx_deg.append(-9999)
    elif nextx[i] == -9:
        nextx_deg.append(float(Lon_deg[i]))

nexty_deg = []
for i in range(len(Lat_deg)):
    if nexty[i] != -9:
        if nexty[i] != -9999:
            nexty_deg.append(float(latGrids.get(nexty[i])))
        elif nexty[i] == -9999:
            nexty_deg.append(-9999)
    elif nexty[i] == -9:
        nexty_deg.append(float(Lat_deg[i]))


#2.Map vizualization

# Map metadata
map = Basemap(lat_0=-90,
              lon_0=0,
              llcrnrlat=54, #lat of South-west
              llcrnrlon=110, #lon of south-west
              urcrnrlat=74, #lat of North-east
              urcrnrlon=133, #lon of north-east
              resolution='h')

#map.shadedrelief()
map.drawcoastlines()
map.drawcountries()
map.drawrivers(color='blue')
#map.etopo()

# Draw parallels
parallels = np.arange(-90, 90, 0.5)
map.drawparallels(parallels,
                  linewidth=0.2,
                  dashes=[0.1, 0],
                  labels=[True, False, False, False])

# Draw meridinas
meridians = np.arange(-180, 180, 0.5)
map.drawmeridians(meridians,
                  linewidth=0.2,
                  dashes=[0.1, 0],
                  labels=[False, False, False, True])


'''
#D8
for i in range(len(Lon_deg)):
    if Lon_deg[i] > 104 and Lon_deg[i] < 135:
        if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
            X = Lon_deg[i]
            Y = Lat_deg[i]
            U = float(nextx_deg[i]) - float(Lon_deg[i])
            V = float(nexty_deg[i]) - float(Lat_deg[i])
            if abs(U) <= 0.5 and abs(V) <= 0.5:
                map.quiver(X + 0.25, Y + 0.25, U, V,
                           angles='xy', scale_units='xy', scale=1, width=0.001, color='red')
'''

'''
#D8_plus
for i in range(len(Lon_deg)):
    if Lon_deg[i] > 104 and Lon_deg[i] < 135:
        if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
            X = Lon_deg[i]
            Y = Lat_deg[i]
            U = float(nextx_deg[i]) - float(Lon_deg[i])
            V = float(nexty_deg[i]) - float(Lat_deg[i])
            if U != 0 and V != 0:
                if abs(U) > 0.5 and abs(V) > 0.5:
                    if (abs(U) + abs(V)) % U == 0 or \
                            (abs(U) + abs(V)) % V == 0:
                        map.quiver(X + 0.25, Y + 0.25, U, V,
                                   angles='xy', scale_units='xy', scale=1, width=0.001, color='red')

                elif abs(U) <= 0.5 and abs(V) <= 0.5:
                    pass
            elif U == 0:
                if abs(V) > 0.5:
                    if abs(U + V) % V == 0:
                        map.quiver(X + 0.25, Y + 0.25, U, V,
                                   angles='xy', scale_units='xy', scale=1, width=0.001, color='red')

            elif V == 0:
                if abs(U) > 0.5:
                    if abs(U + V) % U == 0:
                        map.quiver(X + 0.25, Y + 0.25, U, V,
                                   angles='xy', scale_units='xy', scale=1, width=0.001, color='red')
'''


'''
#- (D8 + D8_plus)
for i in range(len(Lon_deg)):
    if Lon_deg[i] > 104 and Lon_deg[i] < 135:
        if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
            X = Lon_deg[i]
            Y = Lat_deg[i]
            U = float(nextx_deg[i]) - float(Lon_deg[i])
            V = float(nexty_deg[i]) - float(Lat_deg[i])
            if U != 0 and V != 0:
                if abs(U) > 0.5 and abs(V) > 0.5:
                    if (abs(U) + abs(V)) % U == 0 or \
                            (abs(U) + abs(V)) % V == 0:
                        pass
                elif abs(U) <= 0.5 and abs(V) <= 0.5:
                    pass
                else:
                    map.quiver(X + 0.25, Y + 0.25, U, V,
                               angles='xy', scale_units='xy', scale=1, width=0.001, color='black')
            elif U == 0:
                if abs(V) > 0.5:
                    if abs(U + V) % V == 0:
                        pass
            elif V == 0:
                if abs(U) > 0.5:
                    if abs(U + V) % U == 0:
                        pass
'''

'''
for i in range(len(Lon_deg)):
    if Lon_deg[i] > 104 and Lon_deg[i] < 135:
        if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
            X = Lon_deg[i]
            Y = Lat_deg[i]
            U = float(nextx_deg[i]) - float(Lon_deg[i])
            V = float(nexty_deg[i]) - float(Lat_deg[i])
            if ((X + U) - X) == 0.5 and ((Y + V) - Y) == 0.5:
#                print(X, end=' ')
#                print(Y, end=' ')
#                print(X + U, end=' ')
#                print(Y + V)
                map.quiver(X + 0.25, Y + 0.25, U, V,
                           angles='xy', scale_units='xy', scale=1, width=0.001, color='green')
#            elif ((X + U) - X) != 0.5 and ((Y + V) - Y) != 0.5:
#                map.quiver(X + 0.25, Y + 0.25, U, V,
#                           angles='xy', scale_units='xy', scale=1, width=0.001, color='red')
'''

plt.title("D8_plus".format(1))
plt.show()
