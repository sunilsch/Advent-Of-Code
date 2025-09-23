s = 0
for line in open("day4.txt"):
    parts = line.strip().rsplit("-", 1)
    name = parts[0]
    sector = int(parts[1].split("[")[0])
    checksum = parts[1].split("[")[1][:-1]
    counts = {}
    for c in name:
        if c != "-":
            counts[c] = counts.get(c, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    calc_checksum = "".join(x[0] for x in items[:5])
    dec_name = "".join(chr((ord(c) - ord("a") + sector) % 26 + ord("a")) if c != "-" else " " for c in parts[0])
    if dec_name == "northpole object storage":
        print("Second star:", sector)
    if calc_checksum == checksum:
        s += sector
print("First star:", s)