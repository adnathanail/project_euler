def fac(n):
  if n == 1 or n == 0:
    return 1
  return n * fac(n-1)

def choose(n, r):
  if n < r or n < 1 or r < 1:
    return None
  return int(fac(n)/(fac(r)*fac(n-r)))

k = 0
for i in range(1,101):
  for j in range(1,i):
    if choose(i, j) > 1000000:
      k += 1
print(k)