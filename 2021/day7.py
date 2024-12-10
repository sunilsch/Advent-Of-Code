with open('day7.txt') as f:
    positions = [int(x) for x in f.readline().split(',')]
positions.sort()
best = positions[len(positions)//2]
fuel = 0
for x in positions:
    fuel+=abs(x-best)
print("Star 1: "+str(fuel))
best = 1e9
for x in range(2000):
    score = 0
    for y in positions:
        d = abs(y-x)
        score+=d*(d+1)//2
    if score < best:
        best = score
print("Star 2: "+str(best))