x = {'R': 1, 'L' : -1, 'U' : 0, 'D' : 0};
y = {'R': 0, 'L' : 0, 'U' : -1, 'D' : 1}; 
with open('day9.txt') as f:
    realHeadX = 0
    realHeadY = 0
    tails = [[0,0] for _ in range(9)]
    s = set()
    s2 = set()
    for line in f.readlines():
        line = line.strip()
        c, d =  line.split(" ")
        d = int(d)
        for _ in range(d):
            realHeadX += x[c]
            realHeadY += y[c]
            for i in range(9):
                if i == 0:
                    headX = realHeadX;
                    headY = realHeadY;
                else:
                    headX = tails[i-1][0]
                    headY = tails[i-1][1]
                tailX = tails[i][0]
                tailY = tails[i][1]
                if(headX == tailX and abs(headY-tailY) > 1):
                    tailY += headY-tailY-1 if headY > tailY else -(tailY-headY-1)
                elif (headY == tailY and abs(headX-tailX) > 1):
                    tailX += headX-tailX-1 if headX > tailX else -(tailX-headX-1)
                else:
                    if abs(headX-tailX) > 1:
                        if headX > tailX:
                            if headY > tailY:
                                tailX += 1
                                tailY += 1
                            else:
                                tailX += 1
                                tailY -= 1
                        else:
                            if headY > tailY:
                                tailX -= 1
                                tailY += 1
                            else:
                                tailX -= 1
                                tailY -= 1
                    elif abs(headY-tailY) > 1:
                        if headY > tailY:
                            if headX > tailX:
                                tailX += 1
                                tailY += 1
                            else:
                                tailX -= 1
                                tailY += 1
                        else:
                            if headX > tailX:
                                tailX += 1
                                tailY -= 1
                            else:
                                tailX -= 1
                                tailY -= 1
                tails[i][0] = tailX;
                tails[i][1] = tailY;   
            s.add((tails[0][0], tails[0][1]))
            s2.add((tails[-1][0], tails[-1][1]))
print("First star: ", len(s))
print("Second star: ", len(s2))