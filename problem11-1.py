import numpy as np

with open("problem11.txt", 'r') as f:
    lines = f.read().splitlines()

paths = {}

for line in lines:
    a, *b = line.split()
    paths[a[:-1]] = b

rankings = {}

queue = ['you']
nextRank = 0

while queue:
    device = queue.pop(0)
    if device in rankings:
        continue
    rankings[device] = nextRank
    nextRank += 1
    if device not in paths:
        continue
    for output in paths[device]:
        queue.append(output)


rankings['out'] = nextRank
nextRank += 1

adjMatrix = [[0 for _ in range(nextRank)] for _ in range(nextRank)]

for device, rank in rankings.items():
    try:
        for output in paths[device]:
            adjMatrix[rank][rankings[output]] = 1
    except KeyError:
        continue

adjMatrix = np.array(adjMatrix)
numPaths = 0
tempArray = np.copy(adjMatrix)

for _ in range(nextRank):
    numPaths += tempArray[0][-1]
    tempArray = tempArray @ adjMatrix

print(numPaths)