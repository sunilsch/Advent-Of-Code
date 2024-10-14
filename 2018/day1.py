inp = [int(x) for x in open('day1.txt').read().splitlines()]
print("First star: ", sum(inp))
d = set()
s, i = 0,0
while True:
    s += inp[i]
    i = (i+1) % len(inp)
    if s in d:
        print("Second star: ", s)
        break
    d.add(s)