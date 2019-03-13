from math import gcd

frac = [3,2]
t = 0
for i in range(1,1000+1):
  frac[0] += frac[1] # Add 1
  frac = frac[::-1] # 1/
  frac[0] += frac[1] # Add 1
  d = gcd(frac[0],frac[1])
  frac[0], frac[1] = frac[0]//d, frac[1]//d # Simplify
  if len(str(frac[0])) > len(str(frac[1])):
    t += 1
print(t)