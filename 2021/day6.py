fishes = []
with open('day6.txt') as f:
    fishes = [int(x) for x in f.readline().split(',')]
for x in range(256):
    for i, fish in enumerate(fishes[:]):
        if(fish == 0):
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i]-=1
print(len(fishes))