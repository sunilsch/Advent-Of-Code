with open('day6.txt') as f:
    fishes = [int(x) for x in f.readline().split(',')]
fishNumbers = [0 for _ in range(9)]
for fish in fishes:
    fishNumbers[fish]+=1
for x in range(256):
    fishNumberCopy = [0 for _ in range(9)]
    for i,y in enumerate(fishNumbers):
        if i>=1:
            fishNumberCopy[i-1] = fishNumbers[i]
    fishNumberCopy[8] += fishNumbers[0]
    fishNumberCopy[6] += fishNumbers[0]
    fishNumbers = fishNumberCopy.copy()
print(sum(fishNumbers))