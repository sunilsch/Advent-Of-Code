c = 400
dic = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
dic2 = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
def solve(part2):
    pos = [0,0]
    points = [(0,0)]
    p = 0
    for ins, num, color in [x.split() for x in open('day18.txt').readlines()]:
        if part2:
            color = color[2:-1]
            ins = dic2[int(color[5])]
            num = int(color[:-1], 16)
        p += int(num)
        d = dic[ins]
        pos[0] += d[0]*int(num)
        pos[1] += d[1]*int(num)
        points.append(tuple(pos))
    s = 0
    for (x1,y1), (x2,y2) in zip(points[1:], points[:-1]): # Gaußsche Trapezformel
        s += (x2-x1)*(y2+y1)
    return abs(s)//2 + p//2 + 1 # add p//2 + 1 because of the included edges
print(solve(False))
print(solve(True))