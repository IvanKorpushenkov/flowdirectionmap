'''
flowToD8.py

Ivan Korpushenkov, Lomonosov MSU, land hydrology

12.10.2019 11:04

'''


import os
import math

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
                lon_deg = 179.5
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
                lat_deg = 89.5
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

#some_dictionaries
direction_u = {0: 0.5, 45: 0.5, 90: 0,
               135: -0.5, 180: -0.5, 225: -0.5,
               270: 0, 315: 0.5, 360: 0.5}

direction_v = {0: 0, 45: 0.5, 90: 0.5,
               135: -0.5, 180: 0, 225: -0.5,
               270: -0.5, 315: -0.5, 360: 0}

degrees = [0, 45, 90,
           135, 180, 225,
           270, 315, 360]

degrees_D8 = {0: 4, 45: 3, 90: 2,
              135: 1, 180: 8, 225: 7,
              270: 6, 315: 5, 360: 4}


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


#D8_plus_to_D8
for i in range(len(Lon_deg)):
    if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
        X = Lon_deg[i]
        Y = Lat_deg[i]
        U = nextx_deg[i] - Lon_deg[i]
        V = nexty_deg[i] - Lat_deg[i]
        if U != 0 and V != 0:
            if abs(U) > 0.5 and abs(V) > 0.5:
                if (abs(U) + abs(V)) % U == 0 or \
                        (abs(U) + abs(V)) % V == 0:
                    if X < nextx_deg[i] and Y < nexty_deg[i]:
                        numU = abs(int(U / 0.5))
                        numV = abs(int(V / 0.5))
                        maxNum = max(numU, numV)
                        j = 0
                        while j < maxNum:
                            nextx_deg[i + j] = X + 0.5
                            nexty_deg[i + j] = Y + 0.5
                            X = nextx_deg[i + j]
                            Y = nexty_deg[i + j]
                            j += 1
                            continue
                    elif X > nextx_deg[i] and Y < nexty_deg[i]:
                        numU = abs(int(U / 0.5))
                        numV = abs(int(V / 0.5))
                        maxNum = max(numU, numV)
                        j = 0
                        while j < maxNum:
                            nextx_deg[i + j] = X - 0.5
                            nexty_deg[i + j] = Y + 0.5
                            X = nextx_deg[i + j]
                            Y = nexty_deg[i + j]
                            j += 1
                            continue
                    elif X > nextx_deg[i] and Y > nexty_deg[i]:
                        numU = abs(int(U / 0.5))
                        numV = abs(int(V / 0.5))
                        maxNum = max(numU, numV)
                        j = 0
                        while j < maxNum:
                            nextx_deg[i + j] = X - 0.5
                            nexty_deg[i + j] = Y - 0.5
                            X = nextx_deg[i + j]
                            Y = nexty_deg[i + j]
                            j += 1
                            continue
                    elif X < nextx_deg[i] and Y > nexty_deg[i]:
                        numU = abs(int(U / 0.5))
                        numV = abs(int(V / 0.5))
                        maxNum = max(numU, numV)
                        j = 0
                        while j < maxNum:
                            nextx_deg[i + j] = X + 0.5
                            nexty_deg[i + j] = Y - 0.5
                            X = nextx_deg[i + j]
                            Y = nexty_deg[i + j]
                            j += 1
                            continue
        if int(V) == 0:
            if nextx_deg[i] > X:
                length = int(abs(V) / 0.5)
                j = 0
                while j <= length:
                    nextx_deg[i + j] = X + 0.5
                    X = nextx_deg[i + j]
                    j += 1
                    continue
            if nextx_deg[i] < X:
                length = int(abs(V) / 0.5)
                j = 0
                while j <= length:
                    nextx_deg[i + j] = X - 0.5
                    X = nextx_deg[i + j]
                    j += 1
                    continue
        elif int(U) == 0:
            if nexty_deg[i] > Y:
                length = int(abs(U) / 0.5)
                j = 0
                while j <= length:
                    nexty_deg[i + j] = Y + 0.5
                    Y = nexty_deg[i + j]
                    j += 1
                    continue
            if nexty_deg[i] < Y:
                length = int(abs(U) / 0.5)
                j = 0
                while j <= length:
                    nexty_deg[i + j] = Y - 0.5
                    Y = nexty_deg[i + j]
                    j += 1
                    continue

#- (D8 + D8_plus)_to D8
for i in range(len(Lon_deg)):
    if Lon_deg[i] > -180 and Lon_deg[i] < 180:
        if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
            X = Lon_deg[i]
            Y = Lat_deg[i]
            U = float(nextx_deg[i]) - float(Lon_deg[i])
            V = float(nexty_deg[i]) - float(Lat_deg[i])
            numU = abs(int(U / 0.5))
            numV = abs(int(V / 0.5))
            numMax = max(numU, numV)
            if U != 0 and V != 0:
                if abs(U) > 0.5 and abs(V) > 0.5:
                    if (abs(U) + abs(V)) % U == 0 or \
                            (abs(U) + abs(V)) % V == 0:
                        pass
                    else:
                        if X - nextx_deg[i] != 0:
                            linConst_a = (Y - nexty_deg[i]) / (X - nextx_deg[i])
                            linearPhi = (math.atan(linConst_a) * 180) / math.pi
                            k = 0
                            while k < numMax:
                                j = 0
                                mini = linearPhi - degrees[0]
                                while j < len(degrees):
                                    diff = linearPhi - degrees[j]
                                    if diff <= mini:
                                        mini = diff
                                        min_deg = degrees[j]
                                        j += 1
                                        continue
                                    else:
                                        j += 1
                                        continue
                                U = direction_u.get(min_deg)
                                V = direction_v.get(min_deg)
                                nextx_deg[i + k] = X + U
                                nexty_deg[i + k] = Y + V
                                X = nextx_deg[i + k]
                                Y = nexty_deg[i + k]
                                k += 1
                                continue
                elif abs(U) < 0.5 and abs(V) < 0.5:
                    pass
            elif U == 0:
                if abs(V) >= 0.5:
                    if abs(U + V) % V == 0:
                        pass
            elif V == 0:
                if abs(U) >= 0.5:
                    if abs(U + V) % U == 0:
                        pass
        elif nextx_deg[i] == -9999 and nexty_deg[i] == -9999:
            pass


#reverse_latitude_coordinates
Lat_deg.reverse()
nexty_deg.reverse()


#grid_shifting
for i in range(len(Lon_deg)):
    if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
        Lon_deg[i] = Lon_deg[i] + 0.25
        Lat_deg[i] = Lat_deg[i] + 0.25
        nextx_deg[i] = nextx_deg[i] + 0.25
        nexty_deg[i] = nexty_deg[i] + 0.25
        continue
    elif nextx_deg[i] == -9999 and nexty_deg[i] == -9999:
        Lon_deg[i] = Lon_deg[i] + 0.25
        Lat_deg[i] = Lat_deg[i] + 0.25


#reverse_latitude_coordinates
Lat_deg.reverse()
nexty_deg.reverse()


#degree_to_D8
#flow_directions
#1 2 3
#8 9 4
#7 6 5
flowDirectionsD8 = []
for i in range(len(Lon_deg)):
    if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
        if nextx_deg[i] - Lon_deg[i] == -0.5 \
                and nexty_deg[i] - Lat_deg[i] == 0.5:
            flowDirectionsD8.append(1)
            continue
        elif nextx_deg[i] - Lon_deg[i] == 0 \
                and nexty_deg[i] - Lat_deg[i] == 0.5:
            flowDirectionsD8.append(2)
            continue
        elif nextx_deg[i] - Lon_deg[i] == 0.5 \
                and nexty_deg[i] - Lat_deg[i] == 0.5:
            flowDirectionsD8.append(3)
            continue
        elif nextx_deg[i] - Lon_deg[i] == 0.5 \
                and nexty_deg[i] - Lat_deg[i] == 0:
            flowDirectionsD8.append(4)
            continue
        elif nextx_deg[i] - Lon_deg[i] == 0.5 \
                and nexty_deg[i] - Lat_deg[i] == -0.5:
            flowDirectionsD8.append(5)
            continue
        elif nextx_deg[i] - Lon_deg[i] == 0 \
                and nexty_deg[i] - Lat_deg[i] == -0.5:
            flowDirectionsD8.append(6)
            continue
        elif nextx_deg[i] - Lon_deg[i] == -0.5 \
                and nexty_deg[i] - Lat_deg[i] == -0.5:
            flowDirectionsD8.append(7)
            continue
        elif nextx_deg[i] - Lon_deg[i] == -0.5 \
                and nexty_deg[i] - Lat_deg[i] == 0:
            flowDirectionsD8.append(8)
            continue
        elif nextx_deg[i] - Lon_deg[i] == 0 \
                and nexty_deg[i] - Lat_deg[i] == 0:
            flowDirectionsD8.append(9)
            continue
    else:
        flowDirectionsD8.append(-9999)
        continue
