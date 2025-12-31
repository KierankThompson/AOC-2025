import numpy as np
from numpy.linalg import matrix_power

with open("problem11.txt", 'r') as f:
    lines = f.read().splitlines()

paths = {}

for line in lines:
    a, *b = line.split()
    paths[a[:-1]] = b

rankings = {}

queue = ['svr']
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

fftRank = rankings['fft']
dacRank = rankings['dac']

def computePowerSum(matrix, n):
    if n == 1:
        return matrix
    
    i = np.identity(len(matrix))
    b = computePowerSum(matrix, n//2)
    a = matrix_power(matrix, n//2)

    result = b @ (i + a)
    if n % 2 == 1:
        result += a @ a @ matrix
    return result


finalMatrix = computePowerSum(adjMatrix, nextRank-1)

numPaths = finalMatrix[0][fftRank] * finalMatrix[fftRank][dacRank] * finalMatrix[dacRank][-1]

print(numPaths)