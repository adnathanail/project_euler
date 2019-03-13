from math import gcd

def reduce(a,b):
  g = gcd(a,b)
  return [int(a/g),int(b/g)]

def genfracs(maxd):
  fracs = []
  for d in range(1,maxd+1):
    for n in range(1, d):
      r = reduce(n,d)
      if r not in fracs:
        fracs.append(r)
  return fracs
    # print("%i/%i" % (n, d))

for i in range(1,20):
  print(i, len(genfracs(i)))

# fracs = sorted(genfracs(10), key=lambda x: x[0]/x[1])

# print(fracs[fracs.index([3,7]) - 1])
