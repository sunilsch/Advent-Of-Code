n = 312051
l = 0
while (2 * l + 1) ** 2 < n:
    l += 1
m = (2*l+1)**2
s= 2*l+1
d_f_c = abs(n -(m - l))
print(l + abs(d_f_c % s - l))