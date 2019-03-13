from math import gcd

# For all primes p
# n/ψ(n) is maximised when n = Πp
# Max Πp where Πp < 1,000,000 is 2*3*5*7*11*13*17 = 510,510

def prime_factors(n):
  '''PRIME FACTORS: generates a list of prime factors for the number given
  RETURNS: number(being factored), list(prime factors), count(how many loops to find factors, for optimization)
  '''
  num = n                         #number at the end
  count = 0                       #optimization (to count iterations)
  index = 0                       #index (to test)
  t = [2, 3, 5, 7]                #list (to test)
  f = set()                          #prime factors list
  while t[index] ** 2 <= n:
    count += 1                  #increment (how many loops to find factors)
    if len(t) == (index + 1):
      t.append(t[-2] + 6)     #extend test list (as much as needed) [2, 3, 5, 7, 11, 13...]
    if n % t[index]:            #if 0 does else (otherwise increments, or try next t[index])
      index += 1              #increment index
    else:
      n = n // t[index]       #drop max number we are testing... (this should drastically shorten the loops)
      f.add(t[index])      #append factor to list
  if n > 1:
    f.add(n)                 #add last factor...
  return f

def nop(n):
  num = den = 1
  for f in prime_factors(n):
    num *= f-1
    den *= f
  return den/num # den/num to do 1/

maxnop = 0 # Max n over phi
maxn = 0 # N which gives maxnop
for n in range(2, 1000000+1):
  if not n%100000:
    print(n)
  cnop = nop(n) # Current nop
  if cnop > maxnop:
    maxnop = cnop
    maxn = n
print(maxn, maxnop)
