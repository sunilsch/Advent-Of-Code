import sys
sys.setrecursionlimit(100000)
moves = ((-1,0),(1,0),(0,-1),(0,1))
starts = []
with open('day12.txt') as f:
    grid = []
    for i,line in enumerate(f.readlines()):
        grid.append([])
        for j,x in enumerate(line.strip()):
            grid[-1].append(x)
            if x == 'a' or x == 'S':
                starts.append((i,j))
def visit(y,x,d): # dijkstra, slow -> Floyd would be faster
    if dist[y][x] <= d:
        return
    dist[y][x] = d
    for (dy,dx) in moves:
        newX = x + dx
        newY = y + dy
        if newX >= 0 and newY >= 0 and newY < len(grid) and newX < len(grid[0]):
            if ord(grid[newY][newX]) <= ord(grid[y][x])+1:
                visit(newY, newX, d+1)
grid[20][0] = 'a' # set start to a
grid[20][43] = 'z' # set end to z
ans2 = 99999999
for (y,x) in starts:
    dist = [[99999 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visit(y, x, 0)
    if x == 0 and y == 20:
        print("First star: ", dist[20][43])
    ans2 = min(ans2, dist[20][43])
print("Second star: ", ans2)