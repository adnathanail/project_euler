def riffle(d):
  l = int(len(d)/2)
  newd = []
  for i in range(l):
    newd.append(d[i])
    newd.append(d[i + l])
  return newd

def rtc(d): # Riffle to completion
  newd = riffle(d)
  n = 1
  while newd != d:
    newd = riffle(newd)
    n += 1
  return n

def s(n):
  d = [i for i in range(1, n+1)]
  return rtc(d)


t = 0
for i in range(0, 1000, 2):
  if s(i) == 8:
    t += i
    print(i)
print(t)