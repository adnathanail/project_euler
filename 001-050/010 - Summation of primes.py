primes = []
for i in range(2,2000000):
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
  if i%250000 == 0:
    print(i)
print(sum(primes))
