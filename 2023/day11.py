from itertools import combinations
grid = [[x for x in line.strip()] for line in open("day11.txt").readlines()]
row = []
col = []
for i in range(len(grid)):
    if all(x == "." for x in grid[i]):
        row.append(i)
    if all(x == "." for x in [grid[j][i] for j in range(len(grid))]):
        col.append(i)
points = []
for i,x in enumerate(grid):
    for j,y in enumerate(x):
        if y == "#":
            points.append((i,j))
s = 0   
for comb in combinations(points, 2):
    y1, x1 = comb[0]
    y2, x2 = comb[1]
    betRow = sum([1 for i in range(min(y1,y2)+1, max(y1,y2)) if i in row])
    betCol = sum([1 for i in range(min(x1,x2)+1, max(x1,x2)) if i in col])
    s += (abs(y1-y2)+abs(x1-x2)+betRow*(1000000-1)+betCol*(1000000-1))
print(row)
print(col)
print(s)