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

def is_circular(n):
  s = str(n)
  for i in range(len(s)):
    s = s[-1] + s[:-1]
    if int(s) not in primes:
      return False
  return True

print(len([i for i in primes if is_circular(i)]))