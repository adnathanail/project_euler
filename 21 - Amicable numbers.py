from functools import reduce

def factors(n):
    return list(set(reduce(list.__add__,([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0))))
def d(n):
    x = factors(n)
    try:
        x.remove(n)
    except ValueError:
        pass
    return sum(x)

ams = 0
for i in range(2,10000):
    di = d(i)
    if d(di) == i and di != i:
        ams += i
        print(i)
print(ams)
