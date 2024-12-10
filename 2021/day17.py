input = 'target area: x=244..303, y=-91..-54'
x,y = input[13:].split(', ')
xTarget = [int(xT) for xT in x[2:].split('..')]
yTarget = [int(yT) for yT in y[2:].split('..')]
maxmaxy = 0
c = 0
for DX in range(1, xTarget[1]+1):
    for DY in range(-150,100):
        ok = False
        max_y = 0
        x,y = 0,0
        dx, dy = DX, DY
        maxy = 0
        for t in range(xTarget[1]):
            x += dx
            y += dy
            dx = max(0, dx-1)
            dy -= 1
            maxy = max(maxy, y)
            if xTarget[0]<=x<=xTarget[1] and yTarget[0]<=y<=yTarget[1]:
                c+=1
                maxmaxy = max(maxy, maxmaxy)
                break
            if x > xTarget[1] or (dy < 0 and y < yTarget[0]):
                break
print(maxmaxy)
print(c)