grid = []
elfs = set()
rounds = 1
with open('day23.txt') as f:
    for i,line in enumerate(f.readlines()):
        grid.append([])
        for j,x in enumerate(line.strip()):
            grid[-1].append(x)
            if x == '#':
                elfs.add((i,j))
print(grid)
def move():
    pass

def getArea(): # works
    ans = 0
    maxY = max(elf[0] for elf in elfs)
    maxX = max(elf[1] for elf in elfs)
    minY = min(elf[0] for elf in elfs)
    minX = min(elf[1] for elf in elfs)
    print(minX, maxX, minY, maxY)
    for i in range(minY,maxY+1):
        for j in range(minX, maxX+1):
            if not ((i,j) in elfs):
                ans += 1
    return ans

for _ in range(rounds):
    move()
print(getArea())