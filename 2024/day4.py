g, m = open('day4.txt').read(), 'SAMX'
print("First star: ", sum(sum(g[i-x::x][:4] in (m[:4], m[:4][::-1]) for x in (1,140,141,142)) for i in range(len(g))))
print("Second star: ", sum(all(g[i-x::x][:3] in (m[:3], m[:3][::-1]) for x in (140,142)) for i in range(len(g))))