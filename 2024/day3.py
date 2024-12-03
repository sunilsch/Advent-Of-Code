inp = open('day3.txt').read()
i, s, s2 = 0,0,0
en = True
while not i == -1:
    isave = i
    i = inp.find("mul(", i+1)
    j = inp.find(")", i)
    for x in range(i, isave,-1):
        if inp.find("do()", x, i) != -1:
            en = True
            break
        if inp.find("don't()", x, i) != -1:
            en = False
            break
    try:
        a,b = (int(x) for x in inp[i+4:j].split(","))
        s += a*b
        if en:
            s2 += a*b
    except:
        pass
print("First star: ", s)
print("Second star: ", s2)