with open('day4.txt') as f:
    ans = 0
    ans2 = 0
    for line in f.read().splitlines():
        line = line.strip()
        first, second = line.split(',')
        firstRange = [int(x) for x in first.split('-')]
        secondRange = [int(x) for x in second.split('-')]
        if ((firstRange[0] <= secondRange[0]) and (firstRange[1] >= secondRange[1])) or ((secondRange[0] <= firstRange[0]) and (secondRange[1] >= firstRange[1])):
            ans+=1
        if firstRange[0] <= secondRange[1] and firstRange[1] >= secondRange[0]:
            ans2+=1
    print("First star: ", ans)
    print("Second star: ", ans2)