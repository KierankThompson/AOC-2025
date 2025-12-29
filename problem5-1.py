with open("problem5.txt", 'r') as f:
    lines = f.read().splitlines()
addRange = True
ranges = set()
freshIngredients = 0
for line in lines:
    if line == "":
        addRange = False
        continue
    if addRange:
        left, right = line.split("-")
        ranges.add((int(left), int(right)))
    else:
        num = int(line)
        for left, right in ranges:
            if left <= num <= right:
                freshIngredients += 1
                break
print(freshIngredients)