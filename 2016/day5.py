inp = 'ojvtpuvg'
from hashlib import md5
from itertools import count
def hash_generator(s):
    for i in count():
        m = md5((s + str(i)).encode()).hexdigest()
        if m.startswith('00000'):
            yield m[5], m[6]
g, g2 = hash_generator(inp), hash_generator(inp)
print("First star:", ''.join(next(g)[0] for _ in range(8)))
p = ['_'] * 8
for a, b in g2:
    if a in '01234567':
        idx = int(a)
        if p[idx] == '_':
            p[idx] = b
            if '_' not in p:
                break
print("Second star:", ''.join(p))