from collections import defaultdict
inp = [int(x) for x in open('day11.txt').readline().split(" ")]
save = defaultdict(lambda: -1)
def helper(_num, _age):
    if _age == 0:
        return 1
    if save[(_num, _age)] != -1:
        return save[(_num, _age)]
    s = str(_num)
    if _num == 0:
        st = helper(1, _age - 1)
    elif len(s)%2 == 0:
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        st = helper(int(a), _age - 1) + helper(int(b), _age - 1)
    else:
        st = helper(_num * 2024, _age - 1)
    save[(_num, _age)] = int(st)
    return int(st)
def solve(n):
    return sum(helper(x,n) for x in inp)
print("First star: ", solve(25))
print("Second star: ", solve(75))