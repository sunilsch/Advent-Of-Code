def calcDif(l):
    nl = []
    for i in range(len(l)-1):
        nl.append(l[i+1]-l[i])
    return nl
s = [0,0]
for line in open('day9.txt').readlines():
    l = [int(x) for x in line.strip().split()]
    nls = [l, calcDif(l)]
    while not all(x == 0 for x in nls[-1]):
        nls.append(calcDif(nls[-1]))
    n = [0,0]
    for i in reversed(range(len(nls))):
        n[0] = nls[i][-1] + n[0]
        n[1] = nls[i][0] - n[1]
    s[0] += n[0]
    s[1] += n[1]
print("First star: ", s[0])
print("Second star: ", s[1])