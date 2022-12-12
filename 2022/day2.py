points = {
    ('A', 'X') : 3,
    ('B', 'X') : 0,
    ('C', 'X') : 6,
    ('A', 'Y') : 6,
    ('B', 'Y') : 3,
    ('C', 'Y') : 0,
    ('A', 'Z') : 0,
    ('B', 'Z') : 6,
    ('C', 'Z') : 3
}
part2 = {
    ('A', 'X') : 'Z',
    ('B', 'X') : 'X',
    ('C', 'X') : 'Y',
    ('A', 'Y') : 'X',
    ('B', 'Y') : 'Y',
    ('C', 'Y') : 'Z',
    ('A', 'Z') : 'Y',
    ('B', 'Z') : 'Z',
    ('C', 'Z') : 'X'
}
point2 = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}
ans1 = 0
ans2 = 0
with open('day2.txt') as f:
    for line in f.readlines():
        first, second = (line.strip()).split(" ")
        ans1 += points[(first, second)]
        ans1 += point2[second]
        needed = part2[(first, second)]
        ans2 += points[(first, needed)]
        ans2 += point2[needed]
print("First star: ", ans1)
print("Second star: ", ans2)