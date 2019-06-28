from math import gcd

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def bc(n, b): # baseconvert(number, base)
  i = 0 # Max power of base
  while b**i < n:
    i += 1
  o = ""
  for j in range(i,-1,-1):
    x = n//(b**j)
    n -= x*(b**j)
    o += chars[x]
  if o[0] == "0":
    o = o[1:]
  return o

sortedbases = {base:sorted(chars[:base]) for base in range(2,20)}

def is_base_pandigital(n1, n2, n3, b):
  s = bc(n1, b) + bc(n2, b) + bc(n3, b)
  return sorted(s) == sortedbases[b]

# Algorithm to generate integer-sided triangle with 1 angle of 120 degress
# From "Integer-sided triangles with an angle of 120°" by Keith Selkerk
# 3 sides d, e, f: d > e > f
# d = k(x^2 - xy + y^2)
# e = k(2xy - x^2)
# f = k(y^2 - 2xy)
# where k is a positive rational number
# x and y are positive integers
# 4xy > x^2 + y^2
# y > 2x

triples = set()
for y in range(1,2000+1):
  if not y%500:
    print(y)
  x = 1
  while x < y:
    if gcd(x, y) == 1:
      d = y**2 + x**2 + y*x
      e = 2*y*x + x**2
      f = y**2 - x**2
      g = gcd(gcd(d, e), f)
      triples.add(tuple(sorted((f//g, e//g, d//g))))
    x += 1
triples = sorted(list(triples))
print("Sorted")
print(len(triples))

for a, b, c in triples:
  
  for base in range(9,18+1):
    if is_base_pandigital(a, b, c, base):
      print(a, b, c, base)