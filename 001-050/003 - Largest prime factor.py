import math
import itertools

#Not technically complete because doesn't check 1 or 2
def isprime(n):
  for i in range(3,int(n/2)+1,2):
    if n%i == 0:
      return False
  return True

def p3a(x):
  f = 0
  while x%2 == 0:
    f = 2
    x = int(x/2)
  #Starts at 3 because 1 is not prime and 2 is handled above
  for i in range(3,int(math.sqrt(x))+1,2):
    if x%i == 0 and isprime(i):
      f = i
      while x%i == 0:
        x = int(x/i)
    if x == 1:
      break
  return f
print(p3a(600851475143))