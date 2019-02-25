up_to = 1000000

def is_prime(n):
  for i in range(2,int(n**0.5)+1):
    if not n%i:
      return False
  return True
primes = []
for i in range(2,up_to):
  if is_prime(i):
    primes.append(i)
print("Primes generated")

lp = len(primes)
max_primes = []
max_len = 0
for i in range(1, lp):
  if not i%1000:
    print(i)
  for j in range(i+2+max_len,lp):
    p = primes[i:j]
    sp = sum(p)
    l = len(p)
    if sp > up_to:
      break
    if sp in primes:
      if l > max_len:
        max_primes = p
        max_len = l
# print(max_len, max_primes, sum(max_primes))
print(sum(max_primes))