dial = 50

password = 0

password2 = 0

with open("problem1.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip("\n")
        modify = int(line[1:])
        prevDial = dial
        password2 += modify // 100
        modify %= 100
        if line[0] == 'L':
            if modify > dial:
                password2 += 1
                dial = 100 - (modify - dial)
            else:
                dial -= modify
        else:
            if modify + dial >= 100:
                password2 += 1
            dial = (modify + dial) % 100
            
        
        if dial == 0:
            password += 1
            
        if dial >= 100:
            print(f"error: {prevDial=} {line=}")
print(password)
print(password2)


