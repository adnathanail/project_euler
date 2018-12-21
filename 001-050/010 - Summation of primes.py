primes = []
lp = 0
for i in range(2,2000000):
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
  if len(primes)%1000 == 0 and len(primes) != lp:
    lp = len(primes)
    print(len(primes))
print(sum(primes))
