inp = [[int(x) for x in y] for y in open('day10.txt').read().splitlines()]
dirc = [(1,0),(-1,0),(0,-1),(0,1)]
def performSearch(current, value, visited,part1):
    if part1:
        if current in visited:
            return 0
        visited.add(current)
    if value == 9:
        return 1
    s = 0
    for x in dirc:
        if current[0]+x[0] >= 0 and current[1]+x[1] >= 0 and current[0]+x[0] < len(inp) and current[1]+x[1] < len(inp[0]):
            if inp[current[0] + x[0]][current[1] + x[1]] == value+1:
                s += performSearch((current[0] + x[0], current[1] + x[1]), inp[current[0] + x[0]][current[1] + x[1]], visited,part1)
    return s
def calc(part1):
    ans = 0
    for head in heads:
        ans += performSearch(head, 0,set(),part1)
    return ans
heads = []
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == 0:
            heads.append((i,j))
print("First star: ", calc(True))
print("Second star: ", calc(False))
