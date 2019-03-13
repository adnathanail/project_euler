from math import gcd
# a = z(x^2-y^2)
# b = 2xyz
# c = z(x^2+y^2)
# a + b + c = 2zx^2 + 2xyz
# So most important term 2x^2 (because grows quickest)
# So for a + b + c < 1,500,000
# 2x^2 < 1,500,500 (To be 100% sure all triples found)

up_to = 1500000
lim = int(up_to/2)**0.5 # Originally had while 2*x**2 < up_to
                        # Much quicker to not have to do that operation on x every time
triangles = [0 for n in range(up_to+1)]
x = 1
while x < lim:
  for y in range(1,x):
    if (x+y)%2 == 1 and gcd(x,y) == 1: # First condition to remove 2 even numbers, much quicker than gcd
      a = x**2 - y**2
      b = 2*x*y
      c = x**2 + y**2
      bp = a + b + c # Base-perimiter, perimiter of base triangle
      p = bp # Perimiter tally
      while p <= up_to:
        triangles[p] += 1
        p += bp
  x += 1
print(sum([1 for v in range(len(triangles)) if triangles[v] == 1]))