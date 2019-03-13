from math import gcd

def add_frac(a, b):
  num = a[0] * b[1] + b[0] * a[1]
  den = a[1] * b[1]
  d = gcd(den, num)
  num, den = num//d, den//d
  return [num, den]

x = [2]
for i in range(1,33+1):
  x = x + [1, 2*i, 1]

k = 100
frac = [1,x[k-1]]
for i in range(k-2, -1, -1):
  frac = add_frac(frac, [x[i], 1])
  frac[0], frac[1] = frac[1], frac[0]
frac[0], frac[1] = frac[1], frac[0]
num = frac[0]
print(sum(list(map(int, str(num)))))