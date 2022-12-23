from collections import deque
with open('day20.txt') as f:
    numbersOrg = [(i,int(x.strip())) for i,x in enumerate(f.readlines())]
numbersPart1 = deque(numbersOrg.copy())
numbersPart2 = deque([(i,x*811589153) for i,x in numbersOrg])
def solve(numbers,part2):
    for (i,num) in numbersOrg:
        if part2:
            num *= 811589153
        idx = numbers.index((i,num))
        numbers.remove((i,num))
        numbers.rotate(-num)
        numbers.insert(idx,(i,num))
    numbersList = [x for (_,x) in numbers]
    zeroIdx = numbersList.index(0)
    return sum(numbersList[(zeroIdx+1000*i) % len(numbersOrg)] for i in [1, 2, 3]), numbers
print("First star: ", solve(numbersPart1,False)[0])
ans = 0
for _ in range(10):
    a, numbersPart2 = solve(numbersPart2,True)
    ans += a
print("Second star: ", a)