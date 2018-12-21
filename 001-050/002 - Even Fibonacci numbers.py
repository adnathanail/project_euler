def p2a(n):
  fibs = [1,1]
  evens = []
  while fibs[-1] < n:
    fibs.append(fibs[-1] + fibs[-2])
    if not fibs[-1] % 2:
      evens.append(fibs[-1])
  return sum(evens)
print(p2a(4000000))