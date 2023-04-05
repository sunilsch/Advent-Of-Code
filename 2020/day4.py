import re
ans1 = 0
ans2 = 0
l = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def valid(c, v : str):
    if c == "byr":
        return int(v) >= 1920 and int(v) <= 2002
    elif c == "iyr":
        return int(v) >= 2010 and int(v) <= 2020
    elif c == "eyr":
        return int(v) >= 2020 and int(v) <= 2030
    elif c == "hgt":
        if v[-2:] == "cm":
            return int(v[:-2]) >= 150 and int(v[:-2]) <= 193
        elif v[-2:] == "in":
            return int(v[:-2]) >= 59 and int(v[:-2]) <= 76
        return False
    elif c == "hcl":
        if len(v) == 7:
            return bool(re.match(r"#([a-f0-9]+)", v))
    elif c == "ecl":
        return v in l
    elif c == "pid":
        return len(v) == 9 and v.isnumeric()

with open('day4.txt') as f:
    a1 = 0
    a2 = 0
    for line in f.readlines():
        if line == "\n":
            if a1 == 7:
                ans1+=1
            if a2 == 7:
                ans2+=1
            a1 = 0
            a2 = 0
        else:
            line = line.strip()
            for x in line.split(" "):
                c,v = x.split(":")
                if c != "cid":
                    a1 += 1
                    if valid(c,v):
                        a2 += 1
print("First star: ", ans1)
print("Second star: ", ans2)