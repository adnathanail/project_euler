from math import factorial

def fac_sum(n): # Sum of factorial of digits
  tot = 0
  while n:
    tot += factorial(n%10)
    n //= 10
  return tot

cache = {}

def chain(n):
  i = n
  c = []
  while n not in c:
    # print("  ",n)
    if n in cache:
      cache[i] = len(c) + cache[n]
      return cache[i]
    c.append(n)
    n = fac_sum(n)
  cache[i] = len(c)
  return cache[i]

k = 0
for i in range(1000000):
  l = chain(i)
  if l == 60:
    k += 1
print(k)