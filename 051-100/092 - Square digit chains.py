def ssd(n): # Sum of square of digits
  tot = 0
  while n:
    tot += (n%10)**2
    n //= 10
  return tot

cache = {1:1, 89:89}

def ssdtr(n): # Ssd to repetition
  i = n
  while i not in cache:
    i = ssd(i)
  v = cache[i]
  cache[n] = v
  return v

t = 0
for i in range(1,10000000):
  if ssdtr(i) == 89:
    t += 1
print(t)