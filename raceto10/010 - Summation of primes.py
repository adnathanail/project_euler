primes = [2]  # Start with 2 in list so we can increment i by 2 every loop
i = 3
while i < 2000000:
  prime = True
  for p in primes:
    if i % p == 0:
      prime = False
      break
    if p >= i**0.5:
      break
  if prime:
    primes.append(i)
  i += 2
print(sum(primes))