dial = 50

password = 0

with open("problem1.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip("\n")
        modify = int(line[1:])
        prevDial = dial
        if line[0] == 'L':
            if modify > dial:
                dial = 100 - ((modify - dial) % 100)
            else:
                dial -= modify
        else:
            dial = (modify + dial) % 100
        
        if dial == 0:
            password += 1
        if dial >= 100:
            print(f"error: {prevDial=} {line=}")
print(password)
