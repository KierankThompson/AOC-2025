with open("problem3.txt", 'r') as f:
    lines = f.readlines()
totalJoltage = 0
for line in lines:
    line = line.rstrip("\n")
    banks = list(map(lambda x: int(x), line))
    left = 0
    pointer = 1
    maxJoltage = banks[left] * 10 + banks[pointer]
    while pointer < len(banks):
        maxJoltage = max(maxJoltage, banks[left] * 10 + banks[pointer])
        if banks[pointer] > banks[left]:
            left = pointer
        pointer += 1
    totalJoltage += maxJoltage
print(totalJoltage)
