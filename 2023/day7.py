hands = [line.split() for line in open('day7.txt').read().split('\n')]
def get_score(cards, withJoker=False):
    j = 0
    if withJoker:
        j = cards.count("J")
        cards = [x for x in cards if x != "J"]
    c = {}
    for card in cards:
        c[card] = cards.count(card)
    if 5 in c.values() or j == 5:
        return 50
    if 4 in c.values():
        return 10*(4+j)
    if 3 in c.values() and 2 in c.values():
        return 32
    if 3 in c.values():
        return 10*(3+j)
    if 2 in c.values() and list(c.values()).count(2) == 2:
        return 22 + 10*j
    if 2 in c.values():
        return 10*(2+j)
    return 10*(1+j)
def part1(h):
    h = [([int({"T": 10,"J": 11,"Q": 12,"K": 13,"A": 14}.get(i, i)) for i in hand[0]], int(hand[1]), get_score(hand[0])) for hand in h]
    h = sorted(h, key=lambda x: (x[2], x[0]))
    print("First star: ", sum(i * x[1] for i,x in enumerate(h, 1)))
def part2(h):
    h = [([int({"T": 10,"J": 1,"Q": 12,"K": 13,"A": 14}.get(i, i)) for i in hand[0]], int(hand[1]), get_score(hand[0], withJoker=True)) for hand in h]
    h = sorted(h, key=lambda x: (x[2], x[0]))
    print("Second star: ", sum(i * x[1] for i,x in enumerate(h, 1)))
part1(hands.copy())
part2(hands.copy())