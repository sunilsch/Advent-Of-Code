cur1, cur2 = 5, 5
ans1, ans2 = "", ""
dir = {'U': -3, 'D': 3, 'L': -1, 'R': 1}
dir2 = {'U': -4, 'D': 4, 'L': -1, 'R': 1}
disallowed_moves1 = {
    'L': [1, 4, 7],
    'R': [3, 6, 9],
    'U': [1, 2, 3],
    'D': [7, 8, 9]
}
disallowed_moves2 = {
    1: ['U', 'L', 'R'],
    2: ['U', 'L'],
    4: ['U', 'R'],
    5: ['U', 'L', 'D'],
    9: ['U', 'R', 'D'],
    10: ['D', 'L'],
    12: ['D', 'R'],
    13: ['D', 'L', 'R']
}
correction = {
    3: ('U',2),
    11: ('D',-2),
    1: ('D',-2),
    13: ('U',2)
}
def check_first_star():
    if cur1 in disallowed_moves1[x]: return 0
    return dir[x]
def check_second_star():
    if cur2 in disallowed_moves2 and x in disallowed_moves2[cur2]: return 0
    return dir2[x] + (correction[cur2][1] if cur2 in correction and x == correction[cur2][0] else 0)
for line in open("day2.txt").readlines():
    for x in line.strip():
        cur1 += check_first_star()
        cur2 += check_second_star()
    ans1 += str(cur1)
    ans2 += str(hex(cur2)).upper()[-1]
print("First star: ", ans1)
print("Second star: ", ans2)