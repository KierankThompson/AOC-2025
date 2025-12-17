dial = 50

password1 = 0

password2 = 0

with open("problem1.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip("\n")
        modify = int(line[1:])
        password2 += modify // 100
        modify %= 100
        if line[0] == 'L':
            if modify > dial:
                dial = 100 - (modify - dial)
                if modify + dial > 100:
                    password2 += 1
            else:
                dial -= modify
            
        else:
            if dial + modify > 100:
                    password2 += 1
            dial = (modify + dial) % 100
            
        
        if dial == 0:
            password1 += 1

print(f"part 1: {password1}")
print(f"part2: {password2 + password1}")


