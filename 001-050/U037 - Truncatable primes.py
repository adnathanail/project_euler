# Must be made of 1, 3, 7, 9
import itertools

primes = []
for i in range(2,1000000):
  prime = True
  for prime in primes:
    if prime > i ** 0.5:
      break
    else:
      if i % prime == 0:
        prime = False
        break
  if prime:
    primes.append(i)
print("Primes calculated")

def gpwnd(n): # Gen primes with n digits
  l = ["1","3","7","9"]
  for i in range(n-1):
    newl = []
    for r in itertools.product(l, ["1","3","7","9"]):
      newl.append(r[0] + r[1])
    l = newl
  return [int(q) for q in l]

def is_truncatable(n):
  if n not in primes:
    return False
  s = str(n)
  for _ in range(len(s)-1):
    s = s[:-1]
    if int(s) not in primes:
      return False
  return True

def is_reversible(n):
  return is_truncatable(n) and is_truncatable(int(str(n)[::-1]))

for prime in primes:
  if is_reversible(prime):
    print(prime)
