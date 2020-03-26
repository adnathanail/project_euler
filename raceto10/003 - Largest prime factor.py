n = 600851475143
i = 1
while n > 1:
  i += 1
  while n % i == 0:
    n /= i
print(i)  # We try numbers in increasing order so by definition the last number to be tested will the be the largest factor