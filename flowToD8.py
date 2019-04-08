import os
import math

os.chdir('/home/roizmsu/FLOW/DAT')

def printing(name, var):

    os.chdir('/home/roizmsu/FLOW/OUT')

    f = open(name, 'w')
    for i in range(len(var)):
        f.write(str(var[i]) + '\n')
    f.close()

    return

def fileReading(name):

    dim = []
    file = open(name, 'r')
    for line in file:
        dim.append(float(line))

    return dim

def degComparison(X, Y, nextx_deg, nexty_deg):

    degrees = [0, 45, 90,
               135, 180, 225,
               270, 315, 360]

    fin_nx = nextx_deg
    fin_ny = nexty_deg

    if Y < nexty_deg and X < nextx_deg:
        tan_phi = (Y - fin_ny) / (X - fin_nx)
        linearPhi = math.degrees(math.atan(tan_phi))
    elif X > nextx_deg and Y < nexty_deg:
        tan_phi = (Y - fin_ny) / (X - fin_nx)
        linearPhi = 90 + math.degrees(math.atan(tan_phi))
    elif X > nextx_deg and Y > nexty_deg:
        tan_phi = (Y - fin_ny) / (X - fin_nx)
        linearPhi = 180 + math.degrees(math.atan(tan_phi))
    elif X < nextx_deg and Y > nexty_deg:
        tan_phi = (Y - fin_ny) / (X - fin_nx)
        linearPhi = 360 - abs(math.degrees(math.atan(tan_phi)))

    mins = []
    for i in range(len(degrees)):
        mins.append(abs(linearPhi - degrees[i]))

    for i in range(len(degrees)):
        if mins[i] == min(mins):
            linearPhi = degrees[i]


    return linearPhi


def dictEmulator(par, deg_x, deg_y, next_x, next_y, Lon_deg, Lat_deg):

    res = 0
    if par == 'x':
        listLengt = range(len(next_x))
        for i in listLengt:
            if deg_x == Lon_deg[i] and deg_y == Lat_deg[i]:
                res = nextx_deg[i]
    if par == 'y':
        listLengt = range(len(next_y))
        for i in listLengt:
            if deg_x == Lon_deg[i] and deg_y == Lat_deg[i]:
                res = nexty_deg[i]

    return res


#1.data_processing
Lon = fileReading('lon.txt')
Lat = fileReading('lat.txt')
lenParams = range(len(Lon))

nextx = fileReading('nextx.txt')
nexty = fileReading('nexty.txt')

riverWidth = fileReading('rivwth.txt')
#indexesForDelete = fileReading('iies.txt')


lon_c = fileReading('lon_c.txt')
lat_c = fileReading('lat_c.txt')
nx_new = fileReading('nx_new.txt')
ny_new = fileReading('ny_new.txt')
cParams = range(len(lon_c))


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
i = 1
lon_t = -180.0
while i <= 720:
    lonGrids[i] = lon_t
    lon_t += 0.5
    i += 1
    continue

latGrids = {}
i = 1
lat_t = 89.5
while i <= 360:
    latGrids[i] = lat_t
    lat_t -= 0.5
    i += 1
    continue

Lon_deg = []
i = 0
while i < len(Lon):
    Lon_deg.append(lonGrids.get(Lon[i]))
    i += 1

Lat_deg = []
i = 0
while i < len(Lon):
    Lat_deg.append(latGrids.get(Lat[i]))
    i += 1

nextx_deg = []
for i in lenParams:
    if nextx[i] != -9:
        if nextx[i] != -9999:
            nextx_deg.append(float(lonGrids.get(nextx[i])))
            continue
        elif nextx[i] == -9999:
            nextx_deg.append(-9999)
            continue
    elif nextx[i] == -9:
        nextx_deg.append(Lon_deg[i])

nexty_deg = []
for i in lenParams:
    if nexty[i] != -9:
        if nexty[i] != -9999:
            nexty_deg.append(float(latGrids.get(nexty[i])))
        elif nexty[i] == -9999:
            nexty_deg.append(-9999)
    elif nexty[i] == -9:
        nexty_deg.append(Lat_deg[i])

#to cell centre (19.02 added)
for i in lenParams:
    if Lon_deg[i] != -9999 and Lat_deg[i] != -9999:
        Lon_deg[i] += 0.25
        Lat_deg[i] += 0.25
    else:
        pass

for i in lenParams:
    if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
        nextx_deg[i] += 0.25
        nexty_deg[i] += 0.25
    else:
        pass

'''
#indexesForDelete1 = []
lon_indexes = []
lat_indexes = []
nx_indexes = []
ny_indexes = []
len_indexes = range(len(indexesForDelete))
for i in len_indexes:
    lon_indexes.append(Lon_deg[int(indexesForDelete[i])])
    lat_indexes.append(Lat_deg[int(indexesForDelete[i])])
    nx_indexes.append(nextx_deg[int(indexesForDelete[i])])
    ny_indexes.append(nexty_deg[int(indexesForDelete[i])])

print(len(indexesForDelete))
print(len(lon_indexes))
print(len(lat_indexes))
print(len(nx_indexes))
print(len(ny_indexes))


#printing('indexesDelete.txt', indexesForDelete1)
printing('lonind.txt', lon_indexes)
printing('latind.txt', lat_indexes)
printing('nxind.txt', nx_indexes)
printing('nyind.txt', ny_indexes)
'''


'''
lon_i = []
lat_i = []
nx_i = []
ny_i = []
len_indexes = range(len(indexesForDelete))
for i in lenParams:
    for j in len_indexes:
        if i == int(indexesForDelete[j]):
            lon_i.append(Lon_deg[i])
            lat_i.append(Lat_deg[i])
            nx_i.append(nextx_deg[i])
            ny_i.append(nexty_deg[i])

printing('loni.txt', lon_i)
printing('lati.txt', lat_i)
printing('nxi.txt', nx_i)
printing('nyi.txt', ny_i)
'''


#D8_plus_to_D8 (modified 20.02)
for i in lenParams:
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
                            riverWidth[i + j] = riverWidth[i]
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
                            riverWidth[i + j] = riverWidth[i]
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
                            riverWidth[i + j] = riverWidth[i]
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
                            riverWidth[i + j] = riverWidth[i]
                            j += 1
                            continue
            else:
                numU = abs(int(U / 0.5))
                numV = abs(int(V / 0.5))
                numMax = max(numU, numV)
                linearPhi = degComparison(X, Y,
                                          nextx_deg[i], nexty_deg[i])
                UU = direction_u.get(linearPhi)
                VV = direction_v.get(linearPhi)
                nextx_deg[i] = X + UU
                nexty_deg[i] = Y + VV
                X = nextx_deg[i]
                Y = nexty_deg[i]
                continue
            if abs(U) > 0.5 or abs(V) > 0.5:
                numU = abs(int(U / 0.5))
                numV = abs(int(V / 0.5))
                numMax = max(numU, numV)
                linearPhi = degComparison(X, Y,
                                          nextx_deg[i], nexty_deg[i])
                UU = direction_u.get(linearPhi)
                VV = direction_v.get(linearPhi)
                nextx_deg[i] = X + UU
                nexty_deg[i] = Y + VV
                X = nextx_deg[i]
                Y = nexty_deg[i]
                continue
            else:
                numU = abs(int(U / 0.5))
                numV = abs(int(V / 0.5))
                numMax = max(numU, numV)
                linearPhi = degComparison(X, Y,
                                          nextx_deg[i], nexty_deg[i])
                UU = direction_u.get(linearPhi)
                VV = direction_v.get(linearPhi)
                nextx_deg[i] = X + UU
                nexty_deg[i] = Y + VV
                X = nextx_deg[i]
                Y = nexty_deg[i]
                continue
        if V == 0:
            if abs(U) > 0.5:
                if nextx_deg[i] > X:
                    length = int(abs(V) / 0.5)
                    j = 0
                    while j <= length:
                        nextx_deg[i + j] = X + 0.5
                        X = nextx_deg[i + j]
                        riverWidth[i + j] = riverWidth[i]
                        j += 1
                        continue
                if nextx_deg[i] < X:
                    length = int(abs(V) / 0.5)
                    j = 0
                    while j <= length:
                        nextx_deg[i + j] = X - 0.5
                        X = nextx_deg[i + j]
                        riverWidth[i + j] = riverWidth[i]
                        j += 1
                        continue
        elif U == 0:
            if abs(V) > 0.5:
                if nexty_deg[i] > Y:
                    length = int(abs(U) / 0.5)
                    j = 0
                    while j <= length:
                        nexty_deg[i + j] = Y + 0.5
                        Y = nexty_deg[i + j]
                        riverWidth[i + j] = riverWidth[i]
                        j += 1
                        continue
                if nexty_deg[i] < Y:
                    length = int(abs(U) / 0.5)
                    j = 0
                    while j <= length:
                        nexty_deg[i + j] = Y - 0.5
                        riverWidth[i + j] = riverWidth[i]
                        Y = nexty_deg[i + j]
                        j += 1

for i in cParams:
    for j in lenParams:
        if Lon_deg[j] == lon_c[i] and Lat_deg[j] == lat_c[i] and i != j:
            nextx_deg[j] = nx_new[i]
            nexty_deg[j] = ny_new[i]
        else:
            pass

'''
#(17:53) -- it's work
iies = []
for i in lenParams:
    if i % 1000 == 0:
        print(i)
    if Lon_deg[i] != -9999 and Lat_deg[i] != -9999 and \
            nextx_deg[i] != -9999 and nexty_deg[i] != -9999 and \
            Lon_deg[i] > -176 and Lon_deg[i] < 176 and \
            Lat_deg[i] > -86 and Lat_deg[i] < 86:
        if Lon_deg[i] - nextx_deg[i] == 0 and Lat_deg[i] - nexty_deg[i] == 0:
            pass
        else:
            if Lon_deg[i] == dictEmulator('x', nextx_deg[i], nexty_deg[i], nextx_deg, nexty_deg, Lon_deg, Lat_deg) and \
                    Lat_deg[i] == dictEmulator('y', nextx_deg[i], nexty_deg[i], nextx_deg, nexty_deg, Lon_deg, Lat_deg) and \
                    nextx_deg[i] == dictEmulator('x', Lon_deg[i], Lat_deg[i], nextx_deg, nexty_deg, Lon_deg, Lat_deg) and \
                    nexty_deg[i] == dictEmulator('y', Lon_deg[i], Lat_deg[i], nextx_deg, nexty_deg, Lon_deg, Lat_deg):
                iies.append(i)
'''

#printing('iies.txt', iies)

#print(len(iies))


'''
coord_x = []
coord_y = []
coord_nx = []
coord_ny = []
iieslength = range(len(indexesForDelete))
for i in iieslength:
    coord_x.append(Lon_deg[int(indexesForDelete[i])])
    coord_y.append(Lat_deg[int(indexesForDelete[i])])
    coord_nx.append(nextx_deg[int(indexesForDelete[i])])
    coord_ny.append(nexty_deg[int(indexesForDelete[i])])


printing('coord_x.txt', coord_x)
printing('coord_y.txt', coord_y)
printing('coord_nx.txt', coord_nx)
printing('coord_ny.txt', coord_ny)
'''


'''
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
            flowDirectionsD8.append(9)
    else:
        flowDirectionsD8.append(-9999)
        continue
'''

'''
printing('LonD8.txt', Lon_deg)
printing('LatD8.txt', Lat_deg)
printing('nxD8.txt', nextx_deg)
printing('nyD8.txt', nexty_deg)
'''

'''
printing('FD.txt', flowDirectionsD8)
'''
