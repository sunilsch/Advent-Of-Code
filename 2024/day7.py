from itertools import product
inp = [(int(x.split(": ")[0]), [int(y) for y in x.split(": ")[1].split(" ")]) for x in open('day7.txt').read().splitlines()]
def solve(pattern):
    ans = 0
    for eq in inp:
        for x in product(pattern,repeat=len(eq[1])-1):
            s = eq[1][0]
            for i in range(len(eq[1])-1):
                if x[i] == '0':
                    s += eq[1][i+1]
                if x[i] == '1':
                    s *= eq[1][i+1]
                if x[i] == '2':
                    s = int(str(s)+str(eq[1][i+1]))
            if s == eq[0]:
                ans += s
                break
    return ans
print("First star: ", solve('01'))
print("Second star: ", solve('012'))