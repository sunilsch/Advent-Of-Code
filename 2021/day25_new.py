south = []
east = []
with open('2021/day25.txt') as f:
    southLen = len(f.readlines())
    f.seek(0)
    for y,line in enumerate(f):
        line = line[:-1]
        print(line)
        eastLen = len(line)
        for x,C in enumerate(line):
            if C == 'v':
                south.append((y,x))
            elif C == '>':
                east.append((y,x))
moving = True
c = 0
print(eastLen)
print(southLen)
while moving:
    moving = False
    c+=1
    print(c)
    newEast = []
    for C in east:
        y,x = C[0],C[1]
        if x+1 < eastLen:
            if ((y,x+1) not in east) and ((y,x+1) not in south):
                moving = True
                newEast.append((y,x+1))
            else:
                newEast.append((y,x))
        else:
            if ((y,0) not in east) and ((y,0) not in south):
                moving = True
                newEast.append((y,0))
            else:
                newEast.append((y,x))
    east = newEast.copy()
    newSouth = []
    for C in south:
        y,x = C[0],C[1]
        if y+1 < southLen:
            if ((y+1,x) not in east) and ((y+1,x) not in south):
                moving = True
                newSouth.append((y+1,x))
            else:
                newSouth.append((y,x))
        else:
            if ((0,x) not in east) and ((0,x) not in south):
                moving = True
                newSouth.append((0,x))
            else:
                newSouth.append((y,x))
    south = newSouth.copy()
print(c)