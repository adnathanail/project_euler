def is_prime(n):
  for i in range(2,int(n**0.5)+1):
    if not n%i:
      return False
  return True

def pf(n):
  facs = []
  for p in primes:
    if p > n:
      break
    if not n%p:
      facs.append(p)
      n /= p
  return facs

nfnc = 4 # both number of factors, and number of consecutives

primes = []
i = 2
consec = 0
nums = []
while consec < nfnc:
  if is_prime(i):
    primes.append(i)
    consec = 0
    nums = []
  else:
    facs = pf(i)
    if len(facs) == nfnc:
      consec += 1
      nums.append(i)
    else:
      consec = 0
      nums = []
  i += 1
print(nums[0])