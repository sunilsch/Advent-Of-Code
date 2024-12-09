from collections import defaultdict
from itertools import permutations
inp = [[x for x in y] for y in open('day8.txt').read().splitlines()]
points, points2 = set(),set()
v = defaultdict(list)
for i,x in enumerate(inp):
    for j,y in enumerate(x):
        v[y].append((i,j))
del v["."]
for key,value in v.items():
    for x in permutations(value, 2):
        dx, dy = x[1][0] - x[0][0], x[1][1] - x[0][1]
        points2.add((x[1][0],x[1][1]))
        for i in range(1,1000):
            newx,newy = x[0][0]-(dx*i), x[0][1]-(dy*i)
            if newx >= 0 and newx < len(inp) and newy >= 0 and newy < len(inp[0]):
                if i == 1:
                    points.add((newx,newy))
                points2.add((newx,newy))
            else:
                break
print("First star: ", len(points))
print("Second star: ", len(points2))