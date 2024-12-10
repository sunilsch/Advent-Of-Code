from collections import defaultdict
C = []
with open('day22.txt') as f:
    for line in f:
        parts = line.strip().split(" ")
        switch = parts[0] == "on"
        cube = []
        for axis in parts[1].split(','):
            axis = axis.split('..')
            cube.append((int(axis[0][2:]), int(axis[1])))
        C.append((switch, tuple(cube)))
def firstStar():
    generator = [[[False for _ in range(100)]for _ in range(100)]for _ in range(100)]
    for switch,((x1,x2),(y1,y2),(z1,z2)) in C:
        if max(x1,x2,y1,y2,z1,z2) <= 50 and min(x1,x2,y1,y2,z1,z2) >= -50:
            for xi in range(x1,x2+1):
                for yi in range(y1,y2+1):
                    for zi in range(z1,z2+1):
                        generator[xi-50][yi-50][zi-50] = switch
    c = 0
    for x in generator:
        for y in x:
            for z in y:
                if z:
                    c+=1
    return(c)
def volume(cube):
    p = 1
    for b in cube:
        p *= abs(b[1] - b[0]) + 1 
    return p
def overlap(cube1, cube2):
    ans = []
    for b1,b2 in zip(cube1,cube2):
        if b1[1] < b2[0] or b2[1] < b1[0]:
            return None
        cube = (max(b1[0], b2[0]), min(b1[1], b2[1]))
        ans.append(cube)
    return tuple(ans)
def secondStar():
    c = defaultdict(int)
    for switch,cube in C:
        new_c = defaultdict(int)
        keys = set(c.keys())
        for o_cube in keys:
            o = overlap(cube, o_cube)
            if o == None:
                continue
            new_c[o] -= c[o_cube]
        if switch:
            new_c[cube] += 1
        for i in new_c:
            c[i] += new_c[i]
    ans = 0
    for cube in c:
        ans += volume(cube) * c[cube]
    return ans
print(firstStar())
print(secondStar())