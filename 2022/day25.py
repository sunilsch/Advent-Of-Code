rep = [('0',0), ('1',0), ('2',0), ('=',1), ('-',1), ('0',1)]
with open('day25.txt') as f:
        inp = [line.strip() for line in f.readlines()]
def encode(n:str): # input decimal
    r = 0
    l = pow(5,len(n)-1)
    for x in n:
        if(x.isdigit()):
            r += int(x)*l
        elif(x == '-'):
            r += l*(-1)
        else:
            r += l*(-2)
        l //= 5
    return r
def decode(n):
    r = ""
    rem = 0
    while n:
        c,rem = rep[n%5+rem]
        r = c + r
        n //= 5
    return r
print(decode(sum(encode(x) for x in inp)))