# TAKES AGES
def npandigital(n):
  k = ""
  for i in range(1,len(str(n))+1):
    k += str(i)
  return sorted(str(n)) == sorted(k)

primes = []
nps = [] # n-pandigitals
i = 2
while i < 9999999: # Because all pandigitals above 7-digits are divisible by 3
  prime = True
  for j in range(2,int(i**0.5)+1):
    if not i%j:
      prime = False
      break
  if prime:
    primes.append(i)
    if npandigital(i):
      print(i)
      nps.append(i)
  i += 1
print(max(nps))