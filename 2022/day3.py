with open('day3.txt') as f:
    lines = [line.strip() for line in f.readlines()]
def prio(c):
    if c.isupper():
        return ord(c)-38
    else:
        return ord(c)-96
def firstStar():
    ans = 0
    for line in lines:
        line = line.strip()
        first, second = line[0:len(line)//2], line[len(line)//2:len(line)]
        for c in first:
            if c in second:
                ans += prio(c)
                break
    return ans
def secondStar():
    ans = 0
    for i in range(0, len(lines), 3):
        line1 = lines[i]
        line2 = lines[i+1]
        line3 = lines[i+2]
        for c in line1:
            if c in line2 and c in line3:
                ans += prio(c)
                break
    return ans
print("First Star: ", firstStar())
print("Second Star: ", secondStar())