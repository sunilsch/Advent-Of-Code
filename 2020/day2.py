ans1 = 0
ans2 = 0
with open('day2.txt') as f:
    for line in f.readlines():
        line = line.strip()
        nums, char, string = line.split(" ")
        low, high = nums.split("-")
        low = int(low)
        high = int(high)
        char = char[:-1]
        a = 0
        if (string[low-1] == char and not string[high-1] == char) or (string[high-1] == char and not string[low-1] == char):
            ans2+=1
        for c in string:
            if c == char:
                a+=1
        if low <= a and high >= a:
            ans1+=1
print("First star: ", ans1)
print("Second star: ", ans2)