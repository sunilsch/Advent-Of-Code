elfs = []
rounds = 100000000
directions = ["north", "south", "west", "east"]


with open('day23.txt') as f:
    for i,line in enumerate(f.readlines()):
        line = line.strip()
        for j,x in enumerate(line):
            if x == '#':
                elfs.append((i,j))
def printE():
    maxY = max(elf[0] for elf in elfs)
    maxX = max(elf[1] for elf in elfs)
    minY = min(elf[0] for elf in elfs)
    minX = min(elf[1] for elf in elfs)
    for i in range(minY,maxY+1):
        for j in range(minX, maxX+1):
            if (i,j) in elfs:
                print("#",end="")
            else:
                print(".", end ="")
        print("")
#printE()
def checkDirection(direction, elf): # return tuple of new pos and bool
    y = elf[0]
    x = elf[1]
    if direction == "north" or direction == "south":
        newY = y + (1 if direction == "south" else -1)
        for dx in range(-1,2):
            newX = x+dx
            if (newY,newX) in elfs:
                return False, tuple()
        return True, (newY,x)
    elif direction == "west" or direction == "east":
        newX = x + (1 if direction == "east" else -1)
        for dy in range(-1,2):
            newY = y+dy
            if (newY,newX) in elfs:
                return False, tuple()
        return True, (y,newX)
    else:
        raise("ERROR")
def isEmpty(elf):
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if (elf[0]+i,elf[1]+j) in elfs:
                return False
    return True
def move(r):
    #print(directions)
    newPostions = []
    inx = []
    notallowed = set()
    for i,elf in enumerate(elfs):
        if isEmpty(elf):
            continue
        for direction in directions:
            result = checkDirection(direction,elf)
            isValid, newPos = result
            if isValid:
                if newPos in notallowed:
                    pass
                elif not(newPos in newPostions):
                    #print("added")
                    newPostions.append(newPos)
                    inx.append(i)
                else:
                    #print("remove", newPos)
                    #print(inx)
                    #print(newPostions)
                    index = newPostions.index(newPos)
                    newPostions.pop(index)
                    inx.pop(index)
                    notallowed.add(newPos)
                    #print(inx)
                    #print(newPostions)
                break
    #print("new: ", newPostions)
    #print(notallowed)
    #print(elfs)
    #print(newPostions)
    if len(newPostions) == 0:
        print("Second star", r)
        exit()
    for (index, newPostion) in zip(inx, newPostions):
        #print("Change from  ",elfs[index], "to  ",newPostion)
        elfs[index] = newPostion

    #print(elfs)
    directions.append(directions.pop(0)) # cycle directions, works
    #printE()
    if r == 9:
        print("First star: ", getArea())

def getArea(): # works
    ans = 0
    maxY = max(elf[0] for elf in elfs)
    maxX = max(elf[1] for elf in elfs)
    minY = min(elf[0] for elf in elfs)
    minX = min(elf[1] for elf in elfs)
    #print(minX, maxX, minY, maxY)
    for i in range(minY,maxY+1):
        for j in range(minX, maxX+1):
            if not ((i,j) in elfs):
                ans += 1
    return ans

for r in range(rounds):
    move(r)
print("First star: ", getArea())