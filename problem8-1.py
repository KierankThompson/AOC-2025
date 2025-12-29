import math
with open("problem8.txt", 'r') as f:
    lines = f.read().splitlines()
ids = []
size = []
pos = {}
for i, line in enumerate(lines):
    ids.append(i)
    size.append(1)
    pos[i] = tuple(map(lambda x: int(x), line.split(',')))


def find(lookup):
    while lookup != ids[lookup]:
        ids[lookup] = ids[ids[lookup]] 
        lookup = ids[lookup]
    return lookup

def union(p, q):
    parent1 = find(p)
    parent2 = find(q)
    if (parent1 == parent2):
        return
    if size[parent1] < size[parent2]:
        ids[parent1] = parent2
        size[parent2] += size[parent1]
    else:
        ids[parent2] = parent1
        size[parent1] += size[parent2]

distances = []
for i in range(len(ids)):
    for j in range(i+1, len(ids)):
        distance = math.sqrt((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2 + (pos[i][2] - pos[j][2])**2)
        
        distances.append((distance, i, j))

distances.sort()




for e in range(1000):
    _, i, j = distances[e]
    
    union(i,j)


numCircuits = set()
for id in ids:
    lookup = find(id)
    numCircuits.add(lookup)

maxSize = []
for circuit in numCircuits:
    maxSize.append(size[circuit])
maxSize.sort(reverse=True)
print(maxSize[0] * maxSize[1] * maxSize[2])
