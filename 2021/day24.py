from itertools import product
steps = [15, 5, 6, None, 9, None, 14, 3, 1, None, None, None, None, None]
required = [None, None, None, 14, None, 7, None, None, None, 7, 8, 7, 5, 10]
input_space_first = product(range(1,10), repeat=7)
input_space_second = product(range(9,0,-1), repeat=7)
def works(digits):
    z = 0
    res = [0] * 14
    digits_idx = 0
    for i in range(14):
        increment, mod_req = steps[i], required[i]
        if increment == None:
            assert mod_req != None
            res[i] = ((z % 26) - mod_req)
            z //= 26
            if not (1 <= res[i] <= 9):
                return False
        else:
            assert increment != None
            z = z * 26 + digits[digits_idx] + increment
            res[i] = digits[digits_idx]
            digits_idx += 1
    return res
for digits in input_space_first:
    res = works(digits)
    if res:
        print("".join([str(i) for i in res]))
        break
for digits in input_space_second:
    res = works(digits)
    if res:
        print("".join([str(i) for i in res]))
        break