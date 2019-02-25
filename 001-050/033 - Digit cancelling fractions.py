from math import gcd

def cancels(f):
  n = f[0]/f[1] # Get value of fraction compare at end
  a = str(f[0])
  b = str(f[1])
  # Remove trivial cases
  if a[1] == '0' and b[1] == '0':
    return False
  # Remove out of scope cases
  if n >= 1:
    return False
  cancelled = False
  for i in range(len(a)):
    for j in range(len(b)):
      # Perform cancelling
      if a[i] == b[j]:
        a = a[:i] + a[i + 1:]
        b = b[:j] + b[j + 1:]
        cancelled = True
        break
    if cancelled:
      break
  try:
    if int(a)/int(b) == n and cancelled:
      return True
    else:
      return False
  except ZeroDivisionError:
    return False

numerators = 1 # Keeping track of the top half of our final fraction
denominators = 1 # Same for bottom
for i in range(10,99+1):
  for j in range(10,99+1):
    if i == j:
      continue
    if cancels([i,j]):
      # print(i,j)
      numerators *= i
      denominators *= j
# To get fraction in fully simple form
x = gcd(numerators,denominators)
print(denominators/x)