import re
def has_abba(s):
    for m in re.finditer(r'(.)(.)\2\1', s):
        if m.group(1) != m.group(2):
            return True
    return False
def get_aba(net, reverse=False):
    s = set()
    for part in net:
        for m in re.finditer(r'(?=(.)(.)\1)', part):
            if m.group(1) != m.group(2):
                s.add((m.group(2), m.group(1)) if reverse else (m.group(1), m.group(2)))
    return s
def solve():
    for line in open('day7.txt').read().splitlines():
        parts = re.split(r'\[|\]', line)
        supernet = parts[::2]
        hypernet = parts[1::2]
        abba = any(has_abba(part) for part in supernet)
        no_abba = all(not has_abba(part) for part in hypernet)
        aba = get_aba(supernet)
        bab = get_aba(hypernet, reverse=True)
        yield abba and no_abba, len(aba & bab) > 0
print("First star:", sum(1 for a, b in solve() if a))
print("Second star:", sum(1 for a, b in solve() if b))