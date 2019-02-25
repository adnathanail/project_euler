pen = lambda n: int(0.5*n*(3*n-1))

def is_pentagonal(n):
  r = (1+24*n)**0.5
  return r % 6 == 5

found = False
j = 1
while not found:
  pj = pen(j)
  for k in range(1,j):
    pk = pen(k)
    if is_pentagonal(pj+pk) and is_pentagonal(pj-pk):
      print(pj-pk)
      found = True
  j += 1