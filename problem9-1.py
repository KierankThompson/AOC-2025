
with open("problem9.txt", 'r') as f:
    lines = f.read().splitlines()

coordinates = []

for line in lines:
    x, y = line.split(",")
    coordinates.append((int(x),int(y)))


distances = []
for i in range(len(coordinates)):
    for j in range(i+1, len(coordinates)):
        distances.append((abs(coordinates[i][0] - coordinates[j][0]) + 1) * (abs(coordinates[i][1] - coordinates[j][1])+ 1))
print(max(distances))