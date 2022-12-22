m = {" ": -1, "." : 0, "#" : 1}
o = {"r": 0, "d": 1, "l": 2, "u": 3}
# part 2 -> to adjust condition in 76
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

x = grid[0][0]
y = 0
orientation = 0

def lenOfRow(row):
    return row[0] + len(row[1])

def lenOfColumn(x):
    l = 0
    l2 = 0
    started = False
    for row in range(len(grid)):
        if not started:
            l2 += 1
        if grid[row][0] <= x and lenOfRow(grid[row]) > x: # not save
            started = True
            l += 1
    return l+l2-1
def firstOfColumn(x):
    for row in range(len(grid)):
        if grid[row][0] <= x:
            return row
for ins in instructions:
    print(ins)
    if type(ins) == int:
        print("move from: x = ", x, " y = ", y," in diretion: ", orientation, end=" ")
        for i in range(ins):
            if orientation == 0:
                newX = x
                newX += 1
                if newX >= lenOfRow(grid[y]): # PART 2
                    newX = grid[y][0]
                if grid[y][1][newX-grid[y][0]] == 0:
                    x = newX
                else:
                    #print("No move possible!")
                    pass
            elif orientation == 1:
                newY = y
                newY += 1
                if newY >= lenOfColumn(x):
                    newY = firstOfColumn(x)
                if grid[newY][1][x-grid[newY][0]] == 0:
                    y = newY
                else:
                    #print("No move possible!")
                    #print(grid[newY][1])
                    #print("newY", newY)
                    #print("len of column", lenOfColumn(x))
                    pass
            elif orientation == 2:
                newX = x
                newX -= 1
                if newX < grid[y][0]:
                    newX = lenOfRow(grid[y])-1
                if grid[y][1][newX-grid[y][0]] == 0:
                    x = newX
                else:
                    #print("No move possible!")
                    pass

            else:
                assert orientation == 3
                newY = y
                newY -= 1
                if newY < firstOfColumn(x):
                    newY = lenOfColumn(x)-1
                    
                if grid[newY][1][x-grid[newY][0]] == 0:
                    y = newY
                else:
                    #print("No move possible!")
                    pass
        print("to x = ", x, " y = ", y)

    else:
        if ins == "R":
            orientation += 1
            if orientation == 4:
                orientation = 0
        else:
            orientation -= 1
            if orientation == -1:
                orientation = 3

        #print(orientation)
#print(lenOfRow(grid[0]))
print(((y+1)*1000)+((x+1)*4)+orientation)