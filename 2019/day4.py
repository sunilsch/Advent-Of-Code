num,up = (int(x) for x in open('day4.txt').readline().split("-"))
c,c2 = 0,0
while num <= up:
    num = list(str(num))
    for i in range(0,len(num)-1):
        if num[i] > num[i+1]:
            for j in range(i,len(num)):
                num[j] = num[i]
            break
    if int("".join(x for x in num)) <= up:
        if any(num[i] == num[i+1] for i in range(0,len(num)-1)):
            c+=1
        if any(num.count(str(i)) == 2 for i in range(0,10)):
            c2+=1
    num = int("".join(x for x in num))+1
print("First star: ", c)
print("Second star: ", c2)