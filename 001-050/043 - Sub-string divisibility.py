def gen_pans(ns):
  if len(ns) == 1:
    return ns
  o = []
  for i in range(1,len(ns)+1):
    for j in gen_pans(ns[:i-1] + ns[i:]):
      o.append(ns[i-1] + j)
  return o

def has_prop(n):
  primes = [2,3,5,7,11,13,17]
  k = 0
  for i in range(1,8):
    if not int(n[i:i+3]) % primes[i-1]:
      k += 1
  return k == len(primes)

pan_tot = 0
for pan in gen_pans(list('0123456789')):
  if has_prop(pan):
    pan_tot += int(pan)
print(pan_tot)
