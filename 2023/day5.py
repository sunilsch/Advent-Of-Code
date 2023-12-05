data = open('day5.txt', 'r').read()
data = data.split('\n\n')
seeds = [int(x) for x in data[0].split(": ")[1].split()]
maps = []
minseed = 1e25
for i in range(1, len(data)):
    maps.append([])
    d = data[i].split(":\n")[1].split("\n")
    for x in d:
        maps[i-1].append(tuple(int(y) for y in x.split()))
for seed in seeds:
    for i in range(len(maps)):
        for item in maps[i]:
            if seed >= item[1] and seed < item[1]+item[2]:
                seed = item[0] + seed - item[1]
                break
    minseed = min(minseed, seed)
print("First star: ", minseed)
seed_rngs = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
current = 0
t = 0
while True:
    for m in reversed(maps):
        for d, s, r in m:
            if d <= t < d + r:
                t = s + (t - d)
                break
    for s, r in seed_rngs:
        if s <= t < s + r:
            print("Second star: ", current)
            exit()
    current += 1
    t = current