with open("problem10.txt", 'r') as f:
    lines = f.read().splitlines()


goals = []
buttonArr = []

for line in lines:
    requirement, *buttons = line.split()
    curGoal = 0
    for i in range(1, len(requirement)-1):
        if requirement[i] == '#':
            curGoal += 2**(i-1)
    goals.append(curGoal)

    curButtons = [eval(x) if len(x) > 3 else (int(x[1]),) for x in buttons[:-1] ]
    buttonArr.append(curButtons)

totalPresses = 0

for goal, buttons in zip(goals, buttonArr):
    queue = []
    
    for i, b in enumerate(buttons):
        queue.append((0, 0, b, i))
    while queue:
        curNum, curPresses, curButton, idx = queue.pop(0)

        for lightNum in curButton:
            curNum ^= (1 << lightNum)
        
        curPresses += 1
        
        if curNum == goal:
            totalPresses += curPresses
            break
        for i, b in enumerate(buttons):
            if i > idx:
                queue.append((curNum, curPresses, b, i))
print(totalPresses)

        


