from math import sqrt
tot = 0
i = 1
found = False
while not found:
  tot += i
  i += 1
  pentagonal = ((1+sqrt(1+24*tot))/6).is_integer()
  hexagonal = ((1+sqrt(1+8*tot))/4).is_integer()
  if pentagonal and hexagonal and tot not in [1,40755]:
    print(tot)
    found = True
  
