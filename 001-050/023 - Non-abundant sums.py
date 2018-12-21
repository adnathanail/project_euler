from functools import reduce
def factors(n):
  x = list(set(reduce(list.__add__,([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0))))
  try:
    x.remove(n)
  except ValueError:
    pass
  return x
def isAbundant(n):
  if sum(factors(n)) > n:
    return True
  else:
    return False
