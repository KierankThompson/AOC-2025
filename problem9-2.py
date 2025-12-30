
with open("problem9.txt", 'r') as f:
    lines = f.read().splitlines()

redTiles = set()

xCoords = set()
yCoords = set()

for line in lines:
    x, y = line.split(",")
    redTiles.add((int(x),int(y)))
    xCoords.add(int(x))
    yCoords.add(int(y))



xCoords = sorted(list(xCoords))
yCoords = sorted(list(yCoords))

xMap = {}
yMap = {}

for i, x in enumerate(xCoords):
    xMap[x] = i
    xMap[i] = x

for i, y in enumerate(yCoords):
    yMap[y] = i
    yMap[i] = y



compressRedTiles = set()


for x,y in redTiles:
    compressRedTiles.add((xMap[x], yMap[y]))

coordsX = (sorted(compressRedTiles))
coordsY = sorted(compressRedTiles, key=lambda x: (x[1],x[0]))



greenTiles = set()

for i in range(len(coordsX) - 1):
    if coordsX[i][0] == coordsX[i+1][0]:
        x = coordsX[i][0]
        for y in range(coordsX[i][1]+1, coordsX[i+1][1]):
            greenTiles.add((x,y))

for i in range(len(coordsY) - 1):
    if coordsY[i][1] == coordsY[i+1][1]:
        y = coordsY[i][1]
        for x in range(coordsY[i][0]+1, coordsY[i+1][0]):
            greenTiles.add((x,y))

allTiles = greenTiles | compressRedTiles

def checkInside(x, y):
    count = 0
    if (x, y) in allTiles:
        return False
    for t in allTiles:
        if t[1] == y and t[0] > x:
            count += 1
    if count % 2 == 1:
        return True
    return False

import random

randX = -1
randY = -1

while not checkInside(randX, randY):
    randX = random.randint(xMap[min(xCoords)], xMap[max(xCoords)])
    randY = random.randint(yMap[min(yCoords)], yMap[max(yCoords)])

toFill = [(randX, randY)]

while toFill:
    curX, curY = toFill.pop(0)
    if (curX, curY) in allTiles:
        continue
    allTiles.add((curX, curY))
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        newX = curX + dx
        newY = curY + dy
        if (newX, newY) in allTiles:
            continue
        toFill.append((newX,newY))

redTileList = list(compressRedTiles)
distances = []

for i in range(len(redTileList)):
    for j in range(i+1, len(redTileList)):
        coord1 = redTileList[i]
        coord2 = redTileList[j]

        maxX = max(coord1[0], coord2[0])
        minX = min(coord1[0], coord2[0])
        maxY = max(coord1[1], coord2[1])
        minY = min(coord1[1], coord2[1])

        isValid = True
        
        for checkX in range(minX, maxX+1):
            for point in [(checkX, minY), (checkX, maxY)]:
                if point in allTiles:
                    continue
                else:
                    isValid = False
        for checkY in range(minY, maxY+1):
            for point in [(minX, checkY), (maxX, checkY)]:
                if point in allTiles:
                    continue
                else:
                    isValid = False
        if isValid:
            distances.append((abs(xMap[coord1[0]] - xMap[coord2[0]]) + 1) * (abs(yMap[coord1[1]] - yMap[coord2[1]])+ 1))
            
print(max(distances))
    