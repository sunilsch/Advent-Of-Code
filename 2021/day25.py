map = []
with open('day25.txt') as f:
    for line in f:
        map.append([x for x in line.strip()])
def checkMove(d,y,x):
    if d == 'v':
        if map[y][x] == '.':
            return True
    else:
        if map[y][x] == '.':
            return True
    return False
def move(y,x,newY,newX):
    map[y][x], map[newY][newX] = map[newY][newX], map[y][x]
moving = True
c = 0
while moving:
    moving = False
    moved = []
    c+=1
    print(c)
    for y,R in enumerate(map):
        for x,C in enumerate(R):
            if not (y,x) in moved:
                if C == '>':
                    if x+1 < len(map[0]):
                        if(checkMove(C,y,x+1)):
                            moving = True
                            move(y,x,y,x+1)
                            moved.append((y,x+1))
                    else:
                        if(checkMove(C,y,0)):
                            moving = True
                            move(y,x,y,0)
                            moved.append((y,0))
    for y,R in enumerate(map):
        for x,C in enumerate(R):
            if not (y,x) in moved:
                if C == 'v':
                    if y+1 < len(map):
                        if(checkMove(C,y+1,x)):
                            moving = True
                            move(y,x,y+1,x)
                            moved.append((y+1,x))
                    else:
                        if(checkMove(C,0,x)):
                            moving = True
                            move(y,x,0,x)
                            moved.append((0,x))
print(c)