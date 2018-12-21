from functools import reduce
def factors(n):
  return set(reduce(list.__add__,
        ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
tot = 0
len_biggest = 0
biggest = 0
i = 1
while len_biggest < 500:
  tot += i
  if len(factors(tot)) > len_biggest:
    len_biggest = len(factors(tot))
    biggest = tot
    print(tot, len(factors(tot)))
  i += 1
