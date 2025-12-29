with open("problem4.txt", 'r') as f:
    lines = f.read().splitlines()
floorMap = set()
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '@':
            floorMap.add((i,j))

accessibleRolls = 0
directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
while True:
    previousState = len(floorMap)
    toRemove = set()
    for i,j in floorMap:
            rollCount = 0
            for v,h in directions:
                if (i+v,j+h) in floorMap:
                    rollCount += 1
            if rollCount >= 4:
                continue
            accessibleRolls += 1
            toRemove.add((i,j))
    for i,j in toRemove:
        floorMap.remove((i,j))
    if previousState == len(floorMap):
        break
print(accessibleRolls)

