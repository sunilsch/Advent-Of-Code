inp = open('day12.txt').read().splitlines()
visited = [[False for _ in range(len(inp[0]))] for _ in range(len(inp))]
s = 0
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
def explore_region(x,y):
    if visited[x][y]:
        return 0,0
    res = [0,1]
    visited[x][y] = True
    for direction in directions:
        if 0 <= x + direction[0] < len(inp) and 0 <= y + direction[1] < len(inp[0]):
            if inp[x+direction[0]][y+direction[1]] == inp[x][y]:
                _res = explore_region(x + direction[0], y + direction[1])
                res[0] += _res[0]
                res[1] += _res[1]
                continue
        res[0] += 1
    return res
print("First star: ", sum(res[0] * res[1]
                          for i in range(len(inp))
                          for j in range(len(inp[0]))
                          for res in [explore_region(i, j)]))