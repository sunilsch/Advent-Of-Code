from collections import defaultdict
inp = [z.split(")") for z in open('day6.txt').read().splitlines()]
d = defaultdict(list)
for elem in inp:
    if elem[0] in d:
        d[elem[0]].append(elem[1])
    else:
        d[elem[0]] = [elem[1]]
curr = "COM"
su = 0
p1,p2 = [],[]
def explore(curr, s, p):
    global su, p1, p2
    su += s 
    if curr == "YOU":
        p1 = p
    elif curr == "SAN":
        p2 = p
    if d[curr]:
        p.append(curr)
        for nex in d[curr]:
            explore(nex, s+1, p.copy())
explore("COM", 0, [])
print("First star: ", su)
for i,(x,y) in enumerate(zip(p1,p2)):
    if not x == y:
        print("Second star: ", len(p1)-i + len(p2)-i)
        break