with open("problem2.txt", 'r') as f:
    lines = f.readlines()
for line in lines:
    line = line.rstrip("\n")
    ids = line.split(',')
    for idRange in ids:
        