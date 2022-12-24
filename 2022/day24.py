from math import gcd
from queue import Queue
with open('day24.txt') as f:
    grid = [[x for x in line.strip()[1:-1]] for line in f.readlines()[1:-1]]
h = len(grid)
w = len(grid[0])
lcm = (h*w) // gcd(h,w)
wm = {}
for i in range(h):
    for j in range(w):
        times = set()
        for jt in range(w):
            b = grid[i][jt]
            for k in range(lcm//w):
                if b == '>' or b == '<':
                    times.add(k*w+((j-jt) if b == '>' else (jt-j))%w)
        for it in range(h):
            b = grid[it][j]
            for k in range(lcm//h):
                if b == 'v' or b == '^':
                    times.add(k*h+((i-it) if b == 'v' else (it-i))%h)
        wm[(i,j)] = set(range(lcm)) - times
def getNbrs(node):
    p, t = node
    nt = (t+1) % lcm
    if p == (-1,0):
        nbrs = [p, (0,0)]
    elif p == (h,w-1):
        nbrs = [p, (h-1,w-1)]
    else:
        nbrs = [p]
        for (dx,dy) in [(0,1),(1,0),(0,-1),(-1,0)]:
            nbr = (p[0]+dx, p[1]+dy)
            if 0 <= nbr[0] < h and 0 <= nbr[1] < w:
                nbrs.append(nbr)
        if p == (0,0):
            nbrs.append((-1,0))
        elif p == (h-1,w-1):
            nbrs.append((h,w-1))
    r = []
    for nbr in nbrs:
        if nbr in [(-1,0), (h,w-1)]:
            r.append((nbr,nt))
        elif nt in wm[nbr]:
            r.append((nbr,nt))
    return r
def bfs(start, goal, time):
    q = Queue()
    sn = (start,time)
    q.put(sn)
    dist = {sn:0}
    while q:
        c = q.get()
        if c[0] == goal:
            return dist[c]
        for nbr in getNbrs(c):
            if nbr in dist:
                continue
            dist[nbr] = dist[c]+1
            q.put(nbr)
t = 0
s = (-1,0)
e = (h,w-1)
t += bfs(s,e,t)
print("First star: ", t)
t += bfs(e,s,t)
t += bfs(s,e,t)
print("Second star: ", t)