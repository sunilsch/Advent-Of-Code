inp = [[[int(z[2:]) for z in y.split(": ")[1].split(", ")] for y in x.split("\n") ]for x in open('day13.txt').read().split("\n\n")]
def solve(data):
    (a1, a2), (b1, b2), (c1, c2) = data
    min_value = float('inf')
    best_k1, best_n1 = -1, -1
    for n1 in range(101):
        numerator = c1 - n1 * b1
        if not numerator % a1 == 0:
            continue
        k1 = numerator // a1
        if not k1 * a2 + n1 * b2 == c2:
            continue
        value = 3 * k1 + n1
        if value < min_value:
            min_value = value
            best_k1, best_n1 = k1, n1
    if best_k1 == -1 or best_n1 == -1:
        return 0
    return min_value
print("First star: ", sum(solve(x,) for x in inp))