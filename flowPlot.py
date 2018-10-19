import os
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

os.chdir('/home/roizmsu/FLOW')

def fileReading(name):

    dim = []
    file = open(name, 'r')
    for line in file:
        dim.append(float(line))

    return dim

#1.data_processing
Lon_deg = fileReading('LonD8.txt')
Lat_deg = fileReading('LatD8.txt')

nextx_deg = fileReading('nxD8.txt')
nexty_deg = fileReading('nyD8.txt')

#2.Map vizualization

#world_basemap
worldMap = gpd.read_file('/home/roizmsu/FLOW/GSHHS_f_L1/GSHHS_f_L1.shp')

#world waterbodies
waterBodies = gpd.read_file('/home/roizmsu/FLOW/GSHHS_f_L2/GSHHS_f_L2.shp')
waterBodies.to_crs(worldMap.crs)

#multilayer plotting
world = worldMap.plot(color='white', edgecolor='black')
waterBodies.plot(ax=world)

#D8
for i in range(len(Lon_deg)):
    if Lon_deg[i] > 29 and Lon_deg[i] < 40:
        if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
            X = Lon_deg[i]
            Y = Lat_deg[i]
            U = float(nextx_deg[i]) - float(Lon_deg[i])
            V = float(nexty_deg[i]) - float(Lat_deg[i])
            if abs(U) <= 0.5 and abs(V) <= 0.5:
                plt.quiver(X + 0.25, Y + 0.25, U, V,
                           angles='xy', scale_units='xy', scale=1, width=0.001, color='red')


plt.grid()
plt.title("D8_plus".format(1))
plt.show()
