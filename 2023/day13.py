from copy import deepcopy
inp = [[x for x in part.split("\n")] for part in open('day13.txt').read().split("\n\n")]
for i in range(len(inp)):
    for j in range(len(inp[i])):
        inp[i][j] = list(inp[i][j])
def check(i, x):
    j = 1
    while i-j >= 0 and i+j-1 < len(x):
        if x[i-j] == x[i+j-1]:
            j += 1
        else:
            return False
    if j == 1:
        return False
    return True
def check2(i,x):
    j = 1
    while i-j >= 0 and i+j-1 < len(x[0]):
        if all(x[k][i-j] == x[k][i+j-1] for k in range(len(x))):
            j += 1
        else:
            return False
    if j == 1:
        return False
    return True
ans1 = 0
ans2 = 0
for x in inp:
    s1 = 0
    a1 = ""
    for i in range(len(x)):
        if(check(i, x)):
            s1 += 100*i
            a1 = "0," + str(i)
            break
    if s1 == 0:
        for j in range(len(x[0])):
            if(check2(j, x)):
                s1 += j
                a1 = "1," + str(j)
                break
    finish = False
    s2 = 0
    for ii in range(len(x)):
        for jj in range(len(x[0])): 
            xCopy = deepcopy(x)
            s2 = 0
            a2 = ""
            if xCopy[ii][jj] == '#':
                xCopy[ii][jj] = '.'
            else:
                xCopy[ii][jj] = '#'
            for i in range(len(xCopy)):
                if(check(i, xCopy)):
                    s2 += 100*i
                    a2 = "0," + str(i)
                    if a2 != a1:
                        break
                    else:
                        s2 = 0
            if s2 == 0:
                for j in range(len(xCopy[0])):
                    if(check2(j, xCopy)):
                        s2 += j
                        a2 = "1," + str(j)
                        if a2 != a1:
                            break
                        else:
                            s2 = 0
            if not (a2 == "" or a2 == a1):
                finish = True
                break
        if finish:
            break
    ans1 += s1
    ans2 += s2
print(ans1)
print(ans2)