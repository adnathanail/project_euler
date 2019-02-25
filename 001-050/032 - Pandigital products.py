from random import randint
from itertools import permutations
def find_products(n):
  products = []
  for i in range(1,7+1):
    for j in range(i+1,9):
      a = int(n[:i])
      b = int(n[i:j])
      c = int(n[j:])
      ab = a*b
      if ab == c:
        products.append(c)
  return products

perms = list([''.join(p) for p in permutations('123456789')])
all_prods = set()
for p in perms:
  prods = find_products(p)
  if len(prods) > 0:
    for p in prods:
      all_prods.add(p)
print(sum(all_prods))