liste = []
with open('day3.txt') as f:
    liste = [line.strip() for line in f.readlines()]
def check(dx,dy):
    x,ans = 0,0
    for y in range(0, len(liste), dy):
        if liste[y][x%len(liste[0])] == "#":
            ans+=1
        x+=dx
    return ans
print("First star: ", check(3,1))
print("Second star: ", check(1,1)*check(3,1)*check(5,1)*check(7,1)*check(1,2))