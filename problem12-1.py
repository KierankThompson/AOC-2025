with open("problem12.txt", 'r') as f:
    lines = f.read().splitlines()


i = 1
shapes = {}
for k in range(6):
    areaCount = 0
    for j in range(3):
        areaCount += lines[i+j].count('#')
    shapes[k] = areaCount
    i += 5

i -= 1

canFit = 0

for requirements in lines[i:]:
    
    area, *requirement = requirements.split()
    x, y = area[:-1].split('x')
    requiredArea = int(x) * int(y)
    shapeArea = 0
    for i, r in enumerate(requirement):
        shapeArea += shapes[i] * int(r)
    if shapeArea <= requiredArea:
        canFit += 1
print(canFit)