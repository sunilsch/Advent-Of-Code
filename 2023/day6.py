times = (48,98,90,83)
dist = (390,1103,1112,1360)
s1 = 1
for time, dist in zip(times, dist):
    a = 0
    for speed in range(time):
        if dist - time*speed < 0:
            a += 1
        time -= 1
    s1 *= a
print(s1)
time = 48989083
dist = 390110311121360
a = 0
for speed in range(time):
    if dist - time*speed < 0:
        a += 1
    time -= 1
print(a)