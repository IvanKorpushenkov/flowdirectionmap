import os
import matplotlib.pyplot as plt
import geopandas as gpd

os.chdir('/home/roizmsu/FLOW/OUT')
#os.chdir('/home/roizmsu/FLOW/DAT')

def fileReading(name):

    dim = []
    file = open(name, 'r')
    for line in file:
        dim.append(float(line))

    return dim

#1.data_processing

#Lon_deg = fileReading('LonD8.txt')
#Lat_deg = fileReading('LatD8.txt')

'''
nextx_deg = fileReading('nxD8.txt')
nexty_deg = fileReading('nyD8.txt')
'''

Lon_deg1 = fileReading('LonD8.txt')
Lat_deg1 = fileReading('LatD8.txt')
nextx_deg1 = fileReading('nxD8.txt')
nexty_deg1 = fileReading('nyD8.txt')


Lon_deg2 = fileReading('coord_x.txt')
Lat_deg2 = fileReading('coord_y.txt')
nextx_deg2 = fileReading('coord_nx.txt')
nexty_deg2 = fileReading('coord_ny.txt')


#2.Map vizualization

#world_basemap
worldMap = gpd.read_file('/home/roizmsu/FLOW/GSHHS_f_L1/GSHHS_f_L1.shp')

#world waterbodies
waterBodies = gpd.read_file('/home/roizmsu/FLOW/GSHHS_f_L2/GSHHS_f_L2.shp')
waterBodies.to_crs(worldMap.crs)

#multilayer plotting
world = worldMap.plot(color='white', edgecolor='black')
waterBodies.plot(ax=world)


'''
#D8
for i in range(len(Lon_deg)):
    if Lon_deg[i] > 0 and Lon_deg[i] < 60:
        if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
            X = Lon_deg[i]
            Y = Lat_deg[i]
            U = float(nextx_deg[i]) - float(Lon_deg[i])
            V = float(nexty_deg[i]) - float(Lat_deg[i])
            if abs(U) <= 0.5 and abs(V) <= 0.5:
                plt.quiver(X + 0.25, Y + 0.25, U, V,
                           angles='xy', scale_units='xy', scale=1, width=0.001, color='red')
'''

'''
Ldeg = []
Ladeg = []
nxxdeg = []
nyydeg = []
for i in range(len(mix)):
    Ldeg.append(Lon_deg[int(mix[i])])
    Ladeg.append(Lat_deg[int(mix[i])])
    nxxdeg.append(nextx_deg[int(mix[i])])
    nyydeg.append(nexty_deg[int(mix[i])])
'''


#print(Ldeg)
#print(Ladeg)
#print(nxxdeg)
#print(nyydeg)


#D8
for i in range(len(Lon_deg1)):
    if Lon_deg1[i] > -180 and Lon_deg1[i] < -60:
        if nextx_deg1[i] != -9999 and nexty_deg1[i] != -9999:
            X = Lon_deg1[i]
            Y = Lat_deg1[i]
            U = float(nextx_deg1[i]) - float(Lon_deg1[i])
            V = float(nexty_deg1[i]) - float(Lat_deg1[i])
            plt.quiver(X, Y, U, V, angles='xy', scale_units='xy',
                       scale=1, width=0.008, color='red')



#D8_intersections
for i in range(len(Lon_deg2)):
    if Lon_deg2[i] > -180 and Lon_deg2[i] < -60:
        if nextx_deg2[i] != -9999 and nexty_deg2[i] != -9999:
            X = Lon_deg2[i]
            Y = Lat_deg2[i]
            U = float(nextx_deg2[i]) - float(Lon_deg2[i])
            V = float(nexty_deg2[i]) - float(Lat_deg2[i])
            plt.quiver(X, Y, U, V, angles='xy', scale_units='xy',
                       scale=1, width=0.008, color='blue')



'''
#intersections
for i in range(len(Ldeg)):
#    if Lon_deg[i] > 35 and Lon_deg[i] < 62:
        if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
            X = Ldeg[i]
            Y = Ladeg[i]
            U = float(nxxdeg[i]) - float(Ldeg[i])
            V = float(nyydeg[i]) - float(Ladeg[i])
            plt.quiver(X, Y, U, V, angles='xy', scale_units='xy',
                       scale=1, width=0.008, color='red')
'''


plt.grid()
plt.title("Src".format(1))
plt.show()


'''
for i in range(len(Ldeg)):
    if Ldeg == 34.75 and Ladeg == 62.75:
        print('ok')
'''
'''
#intersections
for i in range(len(Ldeg)):
    X = Ldeg[i]
    Y = Ladeg[i]
    U = float(nxxdeg[i]) - float(Ldeg[i])
    V = float(nyydeg[i]) - float(Ladeg[i])
    plt.quiver(X, Y, U, V, angles='xy', scale_units='xy',
               scale=1, width=0.008, color='red')

plt.grid()
plt.title("Src".format(1))
plt.show()
'''

