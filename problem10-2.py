from scipy.optimize import linprog

with open("problem10.txt", 'r') as f:
    lines = f.read().splitlines()


voltages = []
buttonArr = []

for line in lines:
    _, *buttons = line.split()
    
    curButtons = [eval(x) if len(x) > 3 else (int(x[1]),) for x in buttons[:-1] ]
    buttonArr.append(curButtons)
    curVoltage = buttons[-1][1:][:-1]
    voltages.append([int(voltage) for voltage in curVoltage.split(",")])

totalPresses = 0

for voltage, buttons in zip(voltages, buttonArr):
    
    a = [[0 for _ in range(len(buttons))] for _ in range(len(voltage))]
    b = voltage
    
    for i, button in enumerate(buttons):
        for light in button:
            a[light][i] = 1
    
    bound = [(0, None) for _ in range(len(buttons))]
    integrality = [1 for _ in range(len(buttons))]
    x0 = [1 for _ in range(len(buttons))]

    res = linprog(x0, A_eq=a, b_eq=b, bounds=bound, integrality=integrality)
    
    totalPresses += sum(res.x)
    

print(totalPresses)