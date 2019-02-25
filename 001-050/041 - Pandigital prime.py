from itertools import permutations
# Only possible prime pandigitals are 1, 4 and 7 digits
# 1 digit ones will not be biggest
def is_prime(n):
  for j in range(2,int(n**0.5)+1):
    if not n%j:
      return False
  return True

nps = [] # n-pandigitals
for i in list([int(''.join(p)) for p in permutations('1234')]):
  if is_prime(i):
    nps.append(i)

nps = [] # n-pandigitals
for i in list([int(''.join(p)) for p in permutations('1234567')]):
  if is_prime(i):
    nps.append(i)

print(max(nps))