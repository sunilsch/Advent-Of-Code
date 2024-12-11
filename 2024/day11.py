from collections import defaultdict
inp = [int(x) for x in open('day11.txt').readline().split(" ")]
save = defaultdict(int)
def helper(_num, _age):
    if _age == 0:
        return 1
    if save[(_num, _age)]:
        return save[(_num, _age)]
    s = str(_num)
    if _num == 0:
        save[(_num, _age)] = helper(1, _age - 1)
    elif len(s) % 2 == 0:
        a = s[:len(s) // 2]
        b = s[len(s) // 2:]
        save[(_num, _age)] = helper(int(a), _age - 1) + helper(int(b), _age - 1)
    else:
        save[(_num, _age)] = helper(_num * 2024, _age - 1)
    return save[(_num, _age)]
solve = lambda n: sum(helper(x, n) for x in inp)
print("First star: ", solve(25))
print("Second star: ", solve(75))