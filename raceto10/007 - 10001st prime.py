primes = []
n = 0
i = 2
while n < 10001:
  prime = True
  for p in primes:
    if i % p == 0:  # If i is divisble by a prime it cannot be prime
      prime = False
      break
    if p >= i**0.5:  # No need to test any primes past the square root of i as we would already have tested their hypothetical pairs
      break
  if prime:
    primes.append(i)
    n += 1
  i += 1
print(primes[-1])