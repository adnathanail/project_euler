test_num = lambda n, m: all([not n%i for i in range(1, m+1)])  # Check if n is evenly divisible by all numbers from 1 to m

fac = lambda n: 1 if n == 1 else n * fac(n-1)

n = fac(20)
for i in range(2, 20+1):
  while test_num(n/i, 20):
    n /= i
print(n)