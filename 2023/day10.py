dic = {
    "|":{0:(-1,0,0),2:(1,0,2)}, 
    "-":{1:(0,1,1),3: (0,-1,3)},
    "L":{2:(0,1,1),3:(-1,0,0)},
    "J":{2:(0,-1,3),1:(-1,0,0)},
    "7":{1:(1,0,2),0:(0,-1,3)},
    "F":{3:(1,0,2),0:(0,1,1)}
}
sToPipe = {
    (0,2): "|", (2,0): "|",
    (1,3): "-", (3,1): "-",
    (0,1): "L", (1,0): "L",
    (0,3): "J", (3,0): "J",
    (2,3): "7", (3,2): "7",
    (2,1): "F", (1,2): "F"
}
grid = [[x for x in line.strip()] for line in open("day10.txt").readlines()]
startD = []
startXY = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)
for neighbor in [(-1, 0, 0), (0, 1, 1), (0, -1, 3), (1, 0, 2)]:
    y = start[0] + neighbor[0]
    x = start[1] + neighbor[1]
    d = neighbor[2]
    if grid[y][x] in dic.keys() and d in dic[grid[y][x]].keys():
        startD.append((d))
        startXY.append((y,x))

dist = 0
y = startXY[0][0]
x = startXY[0][1]
d = startD[0]
while grid[y][x] != "S":
    oy = y
    ox = x
    y += dic[grid[oy][ox]][d][0]
    x += dic[grid[oy][ox]][d][1]
    d = dic[grid[oy][ox]][d][2]
    dist += 1
    grid[oy][ox] = "X"+str(grid[oy][ox])
print("First star: ", dist//2+1)

grid[start[0]][start[1]] = "X"+sToPipe[tuple(startD)]
grid2 = [["." for _ in range(len(grid[0])*3)] for _ in range(len(grid)*3)]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]=='X|':
            grid2[3*i+0][3*j+1] = 'x'
            grid2[3*i+1][3*j+1] = 'x'
            grid2[3*i+2][3*j+1] = 'x'
        elif grid[i][j]=='X-':
            grid2[3*i+1][3*j+0] = 'x'
            grid2[3*i+1][3*j+1] = 'x'
            grid2[3*i+1][3*j+2] = 'x'
        elif grid[i][j]=='X7':
            grid2[3*i+1][3*j+0] = 'x'
            grid2[3*i+1][3*j+1] = 'x'
            grid2[3*i+2][3*j+1] = 'x'
        elif grid[i][j]=='XF':
            grid2[3*i+2][3*j+1] = 'x'
            grid2[3*i+1][3*j+1] = 'x'
            grid2[3*i+1][3*j+2] = 'x'
        elif grid[i][j]=='XJ':
            grid2[3*i+1][3*j+0] = 'x'
            grid2[3*i+1][3*j+1] = 'x'
            grid2[3*i+0][3*j+1] = 'x'
        elif grid[i][j]=='XL':
            grid2[3*i+0][3*j+1] = 'x'
            grid2[3*i+1][3*j+1] = 'x'
            grid2[3*i+1][3*j+2] = 'x'

vis = set()
q = [(0,0)]
while len(q) > 0:
    y,x = q.pop()
    vis.add((y,x))
    for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny = y + neighbor[0]
        nx = x + neighbor[1]
        if nx >= len(grid2[0]) or nx < 0 or ny >= len(grid2) or ny < 0 or (ny,nx) in vis or grid2[ny][nx] == "x":
            continue
        q.append((ny,nx))
second = 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    seen = False
    for ii in [0,1,2]:
      for jj in [0,1,2]:
        if (3*i+ii,3*j+jj) in vis:
          seen = True
    if not seen:
      second += 1
print("Second star: ", second)