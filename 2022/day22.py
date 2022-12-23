m = {"." : 0, "#" : 1}
with open('day22.txt') as f:
    grid = []
    n = False
    for line in f.readlines():
        if n:
            instructionsLine = line.strip()
            i = 0
            a = ""
            cur = "n"
            instructions = []
            while i < len(instructionsLine):
                if cur == "n":
                    if line[i].isdigit():
                        a += line[i]
                        i+=1
                    else:
                        cur = "a"
                        instructions.append(int(a))
                        a = ""
                else:
                    if not line[i].isdigit():
                        a += line[i]
                        i+=1
                    else:
                        cur = "n"
                        instructions.append(a)
                        a = ""
            if cur == "n":
                instructions.append(int(a))
            else:
                instructions.append(a)
            continue
        if line == "\n":
            n = True
            continue
        c = 0
        for x in line:
            if x == " ":
                c += 1
        line = line[c:]
        grid.append((c,[m[x] for x in line.strip("\n")]))

def lenOfRow(row):
    return grid[row][0] + len(grid[row][1])

def lenOfColumn(x):
    l = 0
    l2 = 0
    started = False
    for row in range(len(grid)):
        if not started:
            l2 += 1
        if grid[row][0] <= x and lenOfRow(row) > x:
            started = True
            l += 1
    return l+l2-1
def firstOfColumn(x):
    for row in range(len(grid)):
        if grid[row][0] <= x:
            return row
def solve(part):
    x = grid[0][0]
    y = 0
    orientation = 0
    for ins in instructions:
        if type(ins) == int:
            for _ in range(ins):
                newX = x
                newY = y
                newOrientation = orientation
                if orientation == 0:
                    newX += 1
                    if newX >= lenOfRow(y):
                        if part == 1:
                            newX = grid[y][0]
                        else:
                            if newY >= 150:
                                newOrientation = 3
                                newX = newY-150+50
                                newY = 149
                            elif newY >= 100:
                                newOrientation = 2
                                newY = 49-(newY-100)
                                newX = lenOfRow(newY)-1
                            elif newY >= 50:
                                newOrientation = 3
                                newX += newY-50
                                newY = 49
                            else:
                                newOrientation = 2
                                newY = 149-newY
                                newX = lenOfRow(newY)-1
                    if grid[newY][1][newX-grid[newY][0]] == 0:
                        x = newX
                        y = newY
                        orientation = newOrientation
                elif orientation == 1:
                    newY += 1
                    if newY >= lenOfColumn(x):
                        if part == 1:
                            newY = firstOfColumn(x)
                        else:
                            if newX >= 100:
                                newOrientation = 2
                                newY += newX-100
                                newX = lenOfRow(newY)-1
                            elif newX >= 50:
                                newOrientation = 2
                                newY += newX-50
                                newX = lenOfRow(newY)-1
                            else:
                                assert newX < 50
                                newX += 100
                                newY = 0
                    if grid[newY][1][newX-grid[newY][0]] == 0:
                        y = newY
                        x = newX
                        orientation = newOrientation
                elif orientation == 2:
                    newX -= 1
                    if newX < grid[y][0]:
                        if part == 1:
                            newX = lenOfRow(y)-1
                        else:
                            if newY >= 150:
                                newOrientation = 1
                                newX += newY-99
                                newY = 0
                            elif newY >= 100:
                                newOrientation = 0
                                newY = 49-(newY-100)
                                newX = 50
                            elif newY >= 50:
                                newOrientation = 1
                                newX = newY-50
                                newY = 100
                            else:
                                newOrientation = 0
                                newY = 99+(50-newY)
                                newX = 0
                    if grid[newY][1][newX-grid[newY][0]] == 0:
                        x = newX
                        y = newY
                        orientation = newOrientation
                else:
                    assert orientation == 3
                    newY -= 1
                    if newY < firstOfColumn(x):
                        if part == 1:
                            newY = lenOfColumn(x)-1
                        else:
                            if newX >= 100:
                                newX -= 100
                                newY = 199
                            elif newX >= 50:
                                newOrientation = 0
                                newY = 150+(newX-50)
                                newX = 0
                            else:
                                newOrientation = 0
                                newY = 50+newX
                                newX = 50
                    if grid[newY][1][newX-grid[newY][0]] == 0:
                        x = newX
                        y = newY
                        orientation = newOrientation
        else:
            if ins == "R":
                orientation += 1
                if orientation == 4:
                    orientation = 0
            else:
                orientation -= 1
                if orientation == -1:
                    orientation = 3
    return ((y+1)*1000)+((x+1)*4)+orientation
print("First star: ", solve(1))
print("Second star: ", solve(2))