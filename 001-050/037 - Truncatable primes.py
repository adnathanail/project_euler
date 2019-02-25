# This can rely on previously generated primes because any
# truncated number is smaller than the original so the only
# possible primes it could be have already been found
def is_truncatable(n):
  s = str(n)
  for i in range(len(s)-1, 0, -1):
    if int(s[:i]) not in primes:
      return False
  for i in range(1,len(s)):
    if int(s[i:]) not in primes:
      return False
  return True

primes = []
truncatables = []
i = 2
while len(truncatables) < 11:
  prime = True
  for j in range(2,int(i**0.5)+1):
    if not i%j:
      prime = False
      break
  if prime:
    primes.append(i)
    if i > 9 and is_truncatable(i):
      truncatables.append(i)
  i += 1
print(truncatables)
print(sum(truncatables))