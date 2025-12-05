inp = [[int(y) for y in x] for x in open('day3.txt').read().splitlines()]
ans = 0
for x in inp:
    lim = len(x)
    while True:
        max_index = x.index(max(x[:lim]))
        if max_index != len(x)-1:
            max_index2 = x.index(max(x[max_index+1:]))
            ans += int(str(x[max_index]) + str(x[max_index2]))
            break
        else:
            lim-=1
print("First star: ", ans)