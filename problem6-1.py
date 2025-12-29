import math

with open("problem6.txt", 'r') as f:
    lines = f.read().splitlines()
realLines = []
for line in lines:
    curLine = line.split()
    try:
        curLine = (list(map(lambda x: int(x), curLine)))
        
    except ValueError:
        pass
    realLines.append(curLine)

ans = 0
for i in range(len(realLines[0])):
    
    if realLines[-1][i] == "*":
        ans += math.prod([realLines[j][i] for j in range(len(realLines) - 1)])
    else:
        ans += sum([realLines[j][i] for j in range(len(realLines) - 1)])

print(ans)