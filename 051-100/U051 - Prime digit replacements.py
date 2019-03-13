# import time
# start = time.time()

primes = [2]
i = 3
done = False
while not done:
  prime = True
  for prime in primes:
    if prime > i/2:
      break
    else:
      if i % prime == 0:
        prime = False
        break
  if prime:
    primes.append(i)
    done = len(primes) >= 100
  i += 1

def isPrime(n):
  if n > primes[-1]:
    return None
  else:
    return n in primes


import itertools
import re

def permutate(n):
  o = []
  for i in itertools.product([0,1],repeat=len(str(n))):
    # print(i)
    s = str(n)
    for j in range(len(i)):
      if i[j] == 1:
        s = s[:j] + "x" + s[j+1:]
    if s == str(n):
      continue
    # print(s)
    l = []
    for k in range(9):
      z = int(re.sub("x",str(k),s))
      if isPrime(z) and len(str(z)) == len(str(n)):
        l.append(z)
    o.append(len(l))
    # print(l)
    # print([int(re.sub("x",str(k),s)) for k in range(9) if isPrime(int(re.sub("x",str(k),s)))])
  return max(o)

# print(permutate(13))
# print([[permutate(q),q] for q in range(100)])
l = [[permutate(q),q] for q in range(100)]
print(l)
print(max(l))


# end = time.time()
# print(end - start)
