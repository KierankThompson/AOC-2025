with open("problem2.txt", 'r') as f:
    lines = f.readlines()
invalidSum = 0
for line in lines:
    line = line.rstrip("\n")
    ids = line.split(',')
    for idRange in ids:
        idStart, idEnd = idRange.split("-")
        for num in range(int(idStart), int(idEnd) + 1):
            num = str(num)
            for repeatNum in range(1, (len(num) // 2 + 1)):
              temp = num[:repeatNum] * (len(num) // repeatNum)
              if num[:repeatNum] * (len(num) // repeatNum) == num:
                  invalidSum += int(num)
                  break
print(invalidSum)
