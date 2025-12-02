inp = [(int(l.split('-')[0]),int(l.split('-')[1])) for l in open('day2.txt').readline().split(",")]
def check(y, n):
    if len(y)%n != 0: return False
    return all(y[(len(y) // n) * j:(len(y) // n) * (j + 1)] == y[:len(y) // n] for j in range(0, n))
a1 = sum(x for r in inp for x in range(r[0], r[1]+1) if check(str(x), 2))
a2 = sum(x for r in inp for x in range(r[0], r[1]+1) if any(check(str(x), i) for i in range(2, len(str(x))+1)))
print("First star: ", a1)
print("Second star: ", a2)