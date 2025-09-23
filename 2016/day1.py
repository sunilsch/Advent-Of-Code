directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
inp = open("day1.txt").read().strip().split(", ")
d, x, y, sec = 0, 0, 0, 0
visited = set()
for i in inp:
    turn, dist = i[0], int(i[1:])
    d = (d + (1 if turn == "R" else -1)) % 4
    dx, dy = directions[d]
    for _ in range(dist):
        x, y = x + dx, y + dy
        if not sec and (x, y) in visited:
            sec = abs(x) + abs(y)
        visited.add((x, y))
print("First star: ", abs(x) + abs(y))
print("Second star:", sec)