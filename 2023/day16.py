grid = [list(x) for x in open("day16.txt").read().split("\n")]
dic = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def getStart(x,y,d):
    if grid[y][x] == "/":
        if d == 0:
            return 1
        elif d == 1:
            return 0
        elif d == 2:
            return 3
        elif d == 3:
            return 2
    elif grid[y][x] == "\\":
        if d == 0:
            return 3
        elif d == 1:
            return 2
        elif d == 2:
            return 1
        elif d == 3:
            return 0
    elif grid[y][x] == "|":
        if d == 0 or d == 2:
            return d
        else:
            return (0,2)
    elif grid[y][x] == "-":
        if d == 1 or d == 3:
            return d
        else:
            return (1,3)
    return d

def perform(y,x,d):
    visited = set()
    visited2 = set()
    q = []
    newd = getStart(x,y,d)
    if newd.__class__ == tuple:
        for i in newd:
            q.append((x,y,i))
    else:
        q.append((x,y,newd))

    while q:
        x,y,d = q.pop()
        if (x,y,d) in visited:
            continue
        if not (x,y) in visited2:
            visited2.add((x,y))
        visited.add((x,y,d))
        dy,dx = dic[d]
        newx,newy = x+dx,y+dy
        if newx < 0 or newx >= len(grid[0]) or newy < 0 or newy >= len(grid):
            continue
        if grid[newy][newx] == ".":
            q.append((newx,newy,d))
        elif grid[newy][newx] == "/":
            if d == 0:
                q.append((newx,newy,1))
            elif d == 1:
                q.append((newx,newy,0))
            elif d == 2:
                q.append((newx,newy,3))
            elif d == 3:
                q.append((newx,newy,2))
        elif grid[newy][newx] == "\\":
            if d == 0:
                q.append((newx,newy,3))
            elif d == 1:
                q.append((newx,newy,2))
            elif d == 2:
                q.append((newx,newy,1))
            elif d == 3:
                q.append((newx,newy,0))
        elif grid[newy][newx] == "|":
            if d == 0 or d == 2:
                q.append((newx,newy,d))
            else:
                q.append((newx,newy,0))
                q.append((newx,newy,2))
        elif grid[newy][newx] == "-":
            if d == 1 or d == 3:
                q.append((newx,newy,d))
            else:
                q.append((newx,newy,1))
                q.append((newx,newy,3))
    return len(visited2)
best = 0
for y in range(len(grid)):
    res = perform(y,0,1)
    best = max(res, best)
    res = perform(y,len(grid[0])-1,3)
    best = max(res, best)
for x in range(len(grid[0])):
    res = perform(0,x,2)
    best = max(res, best)
    res = perform(len(grid)-1,x,0)
    best = max(res, best)
print("First star: ", perform(0,0,1))
print("Second star: ", best)