def substr(n):
  out = []
  sn = str(n)
  for i in range(0, len(sn)):
    for j in range(len(sn) - i):
      out.append(int(sn[j:j+i+1]))
  return out

def f(n):
  return len([x for x in substr(n) if x % 3 == 0])

def F(n):
  return sum([1 for i in range(10**(n-1), 10**n) if f(i) % 3 == 0])

for i in range(1, 100+1):
  print(i, f(i))

# for i in range(1, 6+1):
#   print(i, F(i))
