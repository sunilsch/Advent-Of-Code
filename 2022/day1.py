sums = []
with open('day1.txt') as f:
    summe = 0
    for line in f.readlines():
        if(line == '\n'):
            sums.append(summe)
            summe = 0
        else:
            summe += int(line.strip())
sums.sort(reverse=True)
print("First Star: ", sums[0])
print("Second Star: " ,sums[0]+sums[1]+sums[2])
