from itertools import product
d = [x for x in product((-1,0,1),repeat=2)]
marked = set()
def count_neighbors(x,y):
    cnt = 0
    for dx,dy in d:
        if (x+dx,y+dy) in marked:
            cnt+=1
    return cnt
def get_rolls(r):
    res = 0
    for x,y in marked.copy():
        if count_neighbors(x,y) <= 4:
            res+=1
            if r:
                marked.discard((x,y))
    return res
for x,line in enumerate(open('day4.txt').read().splitlines()):
    for y,a in enumerate(line):
        if a=='@':
            marked.add((x,y))
ans, ans2 = 0, -1
print("First star: ", get_rolls(False))
while not ans == ans2:
    ans2 = ans
    ans += get_rolls(True)
print("Second star: ", ans)