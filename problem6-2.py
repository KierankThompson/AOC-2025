import math

with open("problem6.txt", 'r') as f:
    lines = f.read().splitlines()
realLines = []

grandTotal = 0
nums = []
prevInstruction = '*'
for i in range(len(lines[0])):
    if lines[-1][i] == '*' or lines[-1][i] == "+":
        if prevInstruction == "*":
            grandTotal += math.prod(nums)
        else:
            grandTotal += sum(nums)
        prevInstruction = lines[-1][i]
        
        nums = []
    curNum = ""
    for j in range(len(lines) - 1):
        if lines[j][i] != " ":
            curNum += lines[j][i]
    if curNum != "":
        nums.append(int(curNum))
        
if prevInstruction == "*":
    print(math.prod(nums))
    grandTotal += math.prod(nums)
else:
    grandTotal += sum(nums)

if lines[-1][0] == '*':
    grandTotal -= 1
print(grandTotal)

    