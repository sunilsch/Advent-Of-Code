from queue import PriorityQueue
grid = [[int(x) for x in list(line)] for line in open("day17.txt").read().split("\n")]
def calc(p):
    q = PriorityQueue()
    q.put((0,0,0,-1,-1))
    D = {}
    while not q.empty():
        steps,x,y,d,stepsWithD = q.get()
        if (x,y,d,stepsWithD) in D:
            continue
        D[(x,y,d,stepsWithD)] = steps
        for i,(dy,dx) in enumerate([[-1,0],[0,1],[1,0],[0,-1]]):
            newy = y+dy
            newx = x+dx
            newd = i
            newStepsWithD = (1 if newd!=d else stepsWithD+1)
            part1 = newStepsWithD<=3
            part2 = newStepsWithD<=10 and (newd == d or stepsWithD==-1 or stepsWithD>=4)
            if 0<=newy<len(grid) and 0<=newx<len(grid[0]) and (newd + 2)%4 != d and ((p == 1 and part1) or (p == 2 and part2)):
                q.put((steps+grid[newy][newx],newx,newy,newd,newStepsWithD))
    s = 1e9
    for (x,y,d,stepsWithD),steps in D.items():
        if x==len(grid[0])-1 and y==len(grid)-1:
            if p == 1 or (p==2 and 4<=stepsWithD<=10):
                s = min(s, steps)
    return s
print(calc(1))
print(calc(2))