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

'''
def intersections(X, Y):

    for i in range(len()):
        X = Lon_deg[i]
        Y = Lat_deg[i]
        for j in range(len()):
            if nextx_deg[j] == X and nexty_deg[j] == Y:
                print(i)


    return
'''


#1.data_processing
Lon = fileReading('lon.txt')
Lat = fileReading('lat.txt')

nextx = fileReading('nextx.txt')
nexty = fileReading('nexty.txt')

riverWidth = fileReading('rivwth.txt')

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
for i in range(len(Lon_deg)):
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
for i in range(len(Lat_deg)):
    if nexty[i] != -9:
        if nexty[i] != -9999:
            nexty_deg.append(float(latGrids.get(nexty[i])))
        elif nexty[i] == -9999:
            nexty_deg.append(-9999)
    elif nexty[i] == -9:
        nexty_deg.append(Lat_deg[i])


#to cell centre (19.02 added)
for i in range(len(Lon_deg)):
    if Lon_deg[i] != -9999 and Lat_deg[i] != -9999:
        Lon_deg[i] += 0.25
        Lat_deg[i] += 0.25
    else:
        pass

for i in range(len(Lon_deg)):
    if nextx_deg[i] != -9999 and nexty_deg[i] != -9999:
        nextx_deg[i] += 0.25
        nexty_deg[i] += 0.25
    else:
        pass


'''
#intersections_finder (added 20.02)
#тут надо на два условия проверять, в т.ч or
#не только and

iies = []
jjes = []
#2.0 (22.02, 19:50) -- ok!
for i in range(len(Lon_deg)):
    for j in range(len(Lon_deg)):
        if Lon_deg[i] != -9999 and Lat_deg[i] != -9999 and \
                Lon_deg[j] != -9999 and Lat_deg[j] != -9999:
            if Lon_deg[i] == nextx_deg[j] and \
                    Lat_deg[i] == nexty_deg[j] and \
                    Lon_deg[j] == nextx_deg[i] and \
                    Lat_deg[j] == nexty_deg[i] and \
                    i != j:
                iies.append(i)
                jjes.append(j)
            elif Lon_deg[i] == nextx_deg[j] and \
                    Lat_deg[i] == nexty_deg[j] and \
                    i != j:
                iies.append(i)
                jjes.append(j)
'''

#printing('iies.txt', iies)
#printing('jjes.txt', jjes)


'''
#D8_plus_to_D8 (modified 20.02)
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
#                            riverWidth[i + j] = riverWidth[i]
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
#                            riverWidth[i + j] = riverWidth[i]
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
#                            riverWidth[i + j] = riverWidth[i]
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
#                            riverWidth[i + j] = riverWidth[i]
                            j += 1
                            continue
            elif abs(U) > 0.5 or abs(V) > 0.5:
                numU = abs(int(U / 0.5))
                numV = abs(int(V / 0.5))
                numMax = max(numU, numV)
                linearPhi = degComparison(X, Y,
                                          nextx_deg[i], nexty_deg[i])
                U = direction_u.get(linearPhi)
                V = direction_v.get(linearPhi)
                nextx_deg[i] = X + U
                nexty_deg[i] = Y + V
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
#                        riverWidth[i + j] = riverWidth[i]
                        j += 1
                        continue
                if nextx_deg[i] < X:
                    length = int(abs(V) / 0.5)
                    j = 0
                    while j <= length:
                        nextx_deg[i + j] = X - 0.5
                        X = nextx_deg[i + j]
#                        riverWidth[i + j] = riverWidth[i]
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
#                        riverWidth[i + j] = riverWidth[i]
                        j += 1
                        continue
                if nexty_deg[i] < Y:
                    length = int(abs(U) / 0.5)
                    j = 0
                    while j <= length:
                        nexty_deg[i + j] = Y - 0.5
#                        riverWidth[i + j] = riverWidth[i]
                        Y = nexty_deg[i + j]
                        j += 1
'''

'''
for i in range(len(Lon_deg)):
    if Lat_deg[i] == 64.75:
        print(Lon_deg[i], riverWidth[i])
#    if Lon_deg[i] == 41.75 and Lat_deg[i] == 64.25:
#        print(riverWidth[i])
#    if Lon_deg[i] == 40.75 and Lat_deg[i] == 64.75:
#        print(riverWidth[i])
'''




'''
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
            elif abs(U) > 0.5 or abs(V) > 0.5:
                numU = abs(int(U / 0.5))
                numV = abs(int(V / 0.5))
                numMax = max(numU, numV)
                fin_nx = nextx_deg[i]
                fin_ny = nexty_deg[i]
                tan_phi = (Y - fin_ny) / (X - fin_nx)
                linearPhi = math.degrees(math.atan(tan_phi))
                if Y < nexty_deg[i] and X < nextx_deg[i]:
                    tan_phi = (Y - fin_ny) / (X - fin_nx)
                    linearPhi = math.degrees(math.atan(tan_phi))
                elif X > nextx_deg[i] and Y < nexty_deg[i]:
                    tan_phi = (Y - fin_ny) / (X - fin_nx)
                    linearPhi = 90 + math.degrees(math.atan(tan_phi))
                elif X > nextx_deg[i] and Y > nexty_deg[i]:
                    tan_phi = (Y - fin_ny) / (X - fin_nx)
                    linearPhi = 180 + math.degrees(math.atan(tan_phi))
                elif X < nextx_deg[i] and Y > nexty_deg[i]:
                    tan_phi = (Y - fin_ny) / (X - fin_nx)
                    linearPhi = 360 - abs(math.degrees(math.atan(tan_phi)))
                Phi = linearPhi
                for j in range(len(degrees) - 1):
                    if Phi > degrees[j] \
                            and Phi < (degrees[j + 1]):
                        if Phi > degrees[j] \
                                and Phi < ((degrees[j + 1]) / 2):
                            linearPhi = degrees[j]
                        else:
                            linearPhi = degrees[j + 1]
                U = direction_u.get(linearPhi)
                V = direction_v.get(linearPhi)
                nextx_deg[i] = X + U
                nexty_deg[i] = Y + V
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
'''

'''
#intersections_test
i = 0
j = 0
while i < len(Lon_deg):
    x = Lon_deg[i]
    y = Lat_deg[i]
    while j < len(Lon_deg):
        if nextx_deg[j] == x and nexty_deg[j] == y:
            print(Lon_deg[i])
            j = 0
            continue
        else:
            j += 1
            i += 1
            continue
    i +=1
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


printing('LonD8.txt',Lon_deg)
printing('LatD8.txt',Lat_deg)
printing('nxD8.txt',nextx_deg)
printing('nyD8.txt',nexty_deg)
printing('FD.txt', flowDirectionsD8)
printing('rivw.txt', riverWidth)
'''
