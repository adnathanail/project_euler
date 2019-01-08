def fac(n):
  k = 1
  for i in range(1,n+1):
    k *= i
  return k

# Run this to see why the numbers can't go above 7 figures
for k in range(1,10):
  n = k*fac(9)
  print("largest %i digit sum is %i which is %i digits" % (k, n, len(str(n))))

# Cache factorial results
facs = {}
for i in range(10):
  facs[i] = fac(i)
fac = lambda n : facs[n]

i = 10
ns = []
while i < 9999999:
  t = 0
  for j in str(i):
    t += fac(int(j))
  if i == t:
    ns.append(i)
    print(i, t)
  i += 1
print(sum(ns), ns)