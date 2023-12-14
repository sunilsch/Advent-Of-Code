grid = [list(y) for y in open('day14.txt').read().split("\n")]
ans = 0
part1 = True
def perform():
    global ans
    ans = 0
    for i,line in enumerate(grid):
        for j, el in enumerate(line):
            if el == "O":
                a = i
                for k in reversed(range(i)):
                    if grid[k][j] == ".":
                        a = k
                    if grid[k][j] == "#":
                        break
                grid[i][j] = "."
                grid[a][j] = "O"
                ans += len(grid) - a
for i in range(1000000000):
    for _ in range(4):
        perform()
        if part1:
            print("First star:", ans)
            part1 = False
        grid = [list(reversed(col)) for col in zip(*grid)]
    ans = 0
    for k, line in enumerate(grid):
        for x in line:
            if x == "O":
                ans += len(grid) - k
    print(i+1, ans) # analyse the pattern per hand and find the answer
for line in grid:
    print("".join(line))