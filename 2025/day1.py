inp = open("day1.txt").read().splitlines()
ans1, ans2, cur = 0, 0, 50
for x in inp:
    d, y = x[0], int(x[1:])
    for _ in range(y):
        cur += 1 if d == 'R' else -1
        cur %= 100
        ans2 += cur == 0
    ans1 += cur == 0
print("First star: ", ans1)
print("Second star: ", ans2)