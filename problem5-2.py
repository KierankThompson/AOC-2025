with open("problem5.txt", 'r') as f:
    lines = f.read().splitlines()
addRange = True
ranges = []

for line in lines:
    if line == "":
        break
    left, right = line.split("-")
    ranges.append((int(left), int(right)))

ranges.sort()

i = 0
while i < len(ranges) - 1:
    if ranges[i][1] >= ranges[i+1][0]:
        ranges[i] = (ranges[i][0], max(ranges[i][1],ranges[i+1][1]))
        ranges.pop(i+1)
    else:
        i += 1
freshIngredients = 0

for lower,upper in ranges:
    freshIngredients += upper + 1 - lower
print(freshIngredients)


