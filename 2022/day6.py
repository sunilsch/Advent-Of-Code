def solve(i):
    ans = 0
    last = []
    for c in line:
        if len(last) == i:
            if len(last) == len(set(last)):
                return ans
            last.pop(0)
        last.append(c)
        ans += 1
with open('day6.txt') as f:
    line = f.readline().strip()
print("First star: ", solve(4))
print("Second star: ", solve(14))