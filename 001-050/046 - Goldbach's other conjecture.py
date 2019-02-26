def is_prime(n):
  # if n < 2:
  #   return False
  for i in range(2,int(n**0.5)+1):
    if not n%i:
      return False
  return True

def is_square(n):
  return n**.5%1==0

primes = []
i = 2
disproved = False
while not disproved:
  if is_prime(i):
    primes.append(i)
  elif i%2:
    found = False
    for p in primes:
      s = 0.5*(i-p)
      if is_square(s):
        print("%i = %i + 2*%i^2" % (i,p,int(s**0.5)))
        found = True
        break
    if not found:
      print(i)
      disproved = True
  i += 1