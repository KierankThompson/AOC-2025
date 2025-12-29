with open("problem3.txt", 'r') as f:
    lines = f.readlines()
totalJoltage = 0
for line in lines:
    line = line.rstrip("\n")
    banks = list(map(lambda x: int(x), line))
    left = 0
    digits = []
    for digitsLeft in range(12,0,-1):
        curDigit = banks[left]
        right = left + 1
        
        while right < len(banks) - digitsLeft + 1:
            if curDigit < banks[right]:
                left = right
                curDigit = banks[left]
            right += 1
        digits.append(curDigit)
        left += 1
    totalJoltage += int(''.join([str(i) for i in digits]))
        
print(totalJoltage)
