grid = []
with open('day8.txt') as f:
    for line in f.readlines():
        line = line.strip()
        grid.append(line)
def checkX(i,j,x,y,step):
    h = 0
    for z in range(x, y,step):
        h+=1
        if grid[z][j] >= grid[i][j]:
            return (h, False)
    return (h, True)
def checkY(i,j,x,y,step):
    h = 0
    for z in range(x, y,step):
        h+=1
        if grid[i][z] >= grid[i][j]:
            return (h, False)
    return (h, True)
def vis1(i,j):
    if checkX(i,j,i-1, -1, -1)[1]:
        return True
    if checkX(i,j,i+1,len(grid), 1)[1]:
        return True
    if checkY(i,j,j-1, -1, -1)[1]:
        return True
    if checkY(i,j,j+1,len(grid), 1)[1]:
        return True
    return False
def vis2(i,j):
    return checkX(i,j,i-1, -1, -1)[0]*checkX(i,j,i+1,len(grid), 1)[0]*checkY(i,j,j-1, -1, -1)[0]*checkY(i,j,j+1,len(grid), 1)[0]
ans1 = 0
ans2 = 0
for i in range(1, len(grid)-1):
    for j in range (1, len(grid)-1):
        ans1 += vis1(i,j)
        ans2 = max(ans2, vis2(i,j))
print("First star: ", ans1+4*len(grid)-4)
print("Second star: ", ans2)