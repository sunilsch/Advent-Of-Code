times = (48,98,90,83)
dist = (390,1103,1112,1360)
s1 = 1
for time, dist in zip(times, dist):
    s1 *= round(int((time/2)+pow(pow(time/2, 2) - dist, 1/2))-int((time/2)-pow(pow(time/2, 2) - dist, 1/2)))
print("First star: ", s1)
time = 48989083
dist = 390110311121360
print("Second star: ", round(int((time/2)+pow(pow(time/2, 2) - dist, 1/2))-int((time/2)-pow(pow(time/2, 2) - dist, 1/2))))