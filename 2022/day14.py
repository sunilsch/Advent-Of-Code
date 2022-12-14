grid = [[0 for _ in range(700)] for _ in range(200)]
with open('day14.txt') as f:
    for line in f.readlines():
        line = line.strip().split(" -> ")
        for i in range(len(line)-1):
            pair = [[int(x) for x in line[i].split(",")], [int(x) for x in line[i+1].split(",")]]
            pair.sort()
            if pair[0][0] == pair[1][0]:
                for i in range(pair[0][1],pair[1][1]+1):
                    grid[i][pair[0][0]] = "#"
            else:
                for i in range(pair[0][0],pair[1][0]+1):
                    grid[pair[0][1]][i] = "#"
ans = 0
part1 = True
while(True):
    y = 0
    x = 500
    move = True
    while(move):
        if y == 172:
            if part1:
                print("First star: ", ans)
                part1 = False
            grid[y][x] = "#"
            move = False
        if grid[y+1][x] == 0:
            y+=1
        elif grid[y+1][x-1] == 0:
            x-=1
            y+=1
        elif grid[y+1][x+1] == 0:
            x+=1
            y+=1
        else:
            grid[y][x] = "#"
            move = False
            if y == 0 and x == 500:
                print("Second star: ", ans+1)
                exit()
    ans += 1
print(grid)