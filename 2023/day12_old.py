import itertools
lines = open("day12.txt").readlines()
def check(c: str,n: list):
    b = 0
    i = 0
    while i < len(c):
        if c[i] == "#":
            if b >= len(n):
                return False
            j = 0
            while j < n[b]:
                if i+j >= len(c):
                    return False 
                if c[i+j] != "#":
                    return False
                j += 1
            if i+j < len(c):
                if c[i+j] == "#":
                    return False
            i += j
            b += 1
        i += 1
    if b != len(n):
        return False
    return True

s = 0
for i,line in enumerate(lines):
    print(i)
    chars, nums = line.strip().split()
    chars = list(chars)
    nums = [int(x) for x in nums.split(",")]
    print(chars, nums)
    n = 0
    for x in chars:
        if x == "?":
            n += 1
    a = 0
    for comb in list(itertools.product([0, 1], repeat=n)):
        comb = list(comb)
        charsCopy = chars.copy()
        for i in range(len(chars)):
            if charsCopy[i] == "?":
                charsCopy[i] = "#" if comb.pop() else "."
        if check(charsCopy, nums):
            a += 1
    s += a
print(s)