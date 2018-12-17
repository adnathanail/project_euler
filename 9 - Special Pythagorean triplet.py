from itertools import count
from math import sqrt
spt = 0
brk = False
for a in count(1):
    if brk:
        break
    for b in count(a+1):
        c = sqrt((a**2)+(b**2))
        #print("a: " + str(a) + " b: " + str(b) + " c: " + str(c))
        if c.is_integer():
            print("a: " + str(a) + " b: " + str(b) + " c: " + str(int(c)))
            if (a+b+c)==1000:
                spt = a * b * c
                brk = True
                break
        if (a+b+c) > 1000:
            break
print(spt)
