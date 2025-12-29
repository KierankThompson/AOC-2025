with open("problem2.txt", 'r') as f:
    lines = f.readlines()
invalidSum = 0
for line in lines:
    line = line.rstrip("\n")
    ids = line.split(',')
    for idRange in ids:
        idStart, idEnd = idRange.split("-")
        
        if len(idStart) % 2 == 1:
            if len(idStart) == len(idEnd):
                continue
            idStart = '1' + '0' * len(idStart)
            if int(idStart) > int(idEnd):
                continue
        
        
        firstHalf = idStart[:len(idStart) // 2]
        secondHalf = idStart[len(idStart) // 2:]
        firstHalf = int(firstHalf)
        secondHalf = int(secondHalf)

        if secondHalf > firstHalf:
            firstHalf += 1
        secondHalf = firstHalf

        combined = int(str(firstHalf) + str(secondHalf))
        idEnd = int(idEnd)
        while combined <= idEnd:
            invalidSum += combined
            
            firstHalf += 1
            secondHalf += 1
            combined = int(str(firstHalf) + str(secondHalf))
    
