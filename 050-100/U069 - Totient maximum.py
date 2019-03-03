from math import gcd

def arp(a, b): # Are relatively prime
  return gcd(a,b) == 1

def frp(n): # Find relative primes
  ps = []
  for i in range(1,n):
    if arp(n,i):
      ps.append(i)
  return ps

def phi(n):
  return len(frp(n))

def nop(n): # n over phi
  return n/phi(n)

maxnop = 0
maxn = 0
for n in range(2, 10000+1):
  if not n%1000:
    print(n)
  # print(n)
  cnop = nop(n)
  if cnop > maxnop:
    maxnop = cnop
    maxn = n
print(maxn, maxnop)