import heapq
caves = []
directionsX = [1,-1,0,0]
directionsY = [0,0,1,-1]
with open('day15.txt') as f:
    input = f.read().strip()
caves = [[int(i) for i in line] for line in input.split('\n')]
lenR = len(caves)
lenC = len(caves[0])
def get(r,c):
    x = (caves[r % lenR][c % lenC] + (r // lenR) + (c // lenC))
    return (x-1) % 9 + 1
pq = [(0,0,0)]
cost = {}
heapq.heapify(pq)
visited = set()
while len(pq) > 0:
    c, row, col = heapq.heappop(pq)
    if(row,col) in visited:
        continue
    visited.add((row,col))
    cost[(row, col)] = c
    if row == (lenR*5)-1 and col == (lenC*5)-1:
        break
    for x,y in zip(directionsX, directionsY):
        newRow = row + y
        newCol = col + x
        if (0 <= newRow < (lenR*5) and 0 <= newCol < (lenC*5)):
            heapq.heappush(pq, (c+ get(newRow, newCol), newRow, newCol))
print(cost[(lenR*5)-1, (lenC*5)-1])