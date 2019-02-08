fac = lambda n: 1 if n in [0,1] else n * fac(n-1)
choose = lambda n, r: None if n < r or n < 1 or r < 1 else int(fac(n)/(fac(r)*fac(n-r)))
print(sum([sum([1 if choose(i, j) > 1000000 else 0 for j in range(1,i)]) for i in range(1,101)]))